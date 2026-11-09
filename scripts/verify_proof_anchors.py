#!/usr/bin/env python3
"""
Checks that every wallets/*.yaml proof / verified_by.proof URL that
points into proofs/ with a #fragment names a Markdown heading whose
GitHub-style slug matches that fragment.

Usage:
    python3 scripts/verify_proof_anchors.py

Exit status 0 when every fragment resolves, 1 otherwise.
Shares the YAML reader with generate_table.py (stdlib only).
"""
from __future__ import annotations

import glob
import os
import re
import sys

from generate_table import load_registry, yaml_load

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)


def github_slug(heading: str) -> str:
    """Approximate GitHub's heading anchor for Markdown headings."""
    text = heading.strip().lower().replace("`", "")
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-")


def heading_slugs(md_path: str) -> set[str]:
    with open(md_path, encoding="utf-8") as f:
        body = f.read()
    slugs = {github_slug(m.group(2)) for m in HEADING_RE.finditer(body)}
    slugs.update(re.findall(r'id=["\']([^"\']+)["\']', body))
    return slugs


def _proof_refs_from_feature(meta):
    """Yield full proof strings that start with proofs/ (may include #frag)."""
    if not isinstance(meta, dict):
        return
    proof = meta.get("proof")
    if isinstance(proof, str) and proof.startswith("proofs/"):
        yield proof
    for entry in meta.get("verified_by") or []:
        if not isinstance(entry, dict):
            continue
        vproof = entry.get("proof")
        if isinstance(vproof, str) and vproof.startswith("proofs/"):
            yield vproof


def main() -> int:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)

    registry = load_registry("wallets/_feature_registry.yaml") or {}
    self_attested_only = {
        f["id"]
        for f in registry.get("features", [])
        if f.get("self_attested_only")
    }

    broken = []
    for path in sorted(glob.glob(os.path.join("wallets", "*.yaml"))):
        base = os.path.basename(path)
        if base.startswith("_") or base.upper().startswith("TEMPLATE"):
            continue
        data = yaml_load(path)
        if not data:
            continue
        features = data.get("features") or {}
        for feature_id, meta in features.items():
            if feature_id in self_attested_only:
                continue
            for ref in _proof_refs_from_feature(meta):
                if "#" not in ref:
                    continue
                file_part, frag = ref.split("#", 1)
                if not frag:
                    continue
                if not os.path.isfile(file_part):
                    # File existence is covered by verify_proof_links.py.
                    continue
                slugs = heading_slugs(file_part)
                if frag not in slugs:
                    broken.append((path, feature_id, ref))

    if broken:
        print(
            "Proof fragments that do not match a heading anchor:",
            file=sys.stderr,
        )
        for wallet_path, feature_id, ref in broken:
            print(
                f"  {wallet_path} feature={feature_id} -> {ref}",
                file=sys.stderr,
            )
        print(
            "\nUse the GitHub slug for the attestation heading "
            "(punctuation dropped, spaces to single hyphens; "
            "a slash does not become '--').",
            file=sys.stderr,
        )
        return 1

    print("All proof URL fragments match a heading anchor.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
