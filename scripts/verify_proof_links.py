#!/usr/bin/env python3
"""
Checks that every wallets/*.yaml proof / verified_by.proof path that
points into proofs/ names a file that exists in the repo.

Usage:
    python3 scripts/verify_proof_links.py

Exit status 0 when every referenced proof file exists, 1 otherwise.
Shares the YAML reader with generate_table.py (stdlib only).
"""
import glob
import os
import sys

from generate_table import load_registry, yaml_load


def _proof_paths_from_feature(meta):
    """Yield proof path strings (file part only, no #anchor) from one feature."""
    if not isinstance(meta, dict):
        return
    proof = meta.get("proof")
    if isinstance(proof, str) and proof.startswith("proofs/"):
        yield proof.split("#", 1)[0]
    for entry in meta.get("verified_by") or []:
        if not isinstance(entry, dict):
            continue
        vproof = entry.get("proof")
        if isinstance(vproof, str) and vproof.startswith("proofs/"):
            yield vproof.split("#", 1)[0]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)

    registry = load_registry("wallets/_feature_registry.yaml") or {}
    self_attested_only = {
        f["id"]
        for f in registry.get("features", [])
        if f.get("self_attested_only")
    }

    missing = []
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
            for proof_path in _proof_paths_from_feature(meta):
                if not os.path.isfile(proof_path):
                    missing.append((path, feature_id, proof_path))

    if missing:
        print("Missing proof files referenced from wallet YAML:", file=sys.stderr)
        for wallet_path, feature_id, proof_path in missing:
            print(f"  {wallet_path} feature={feature_id} -> {proof_path}", file=sys.stderr)
        print(
            "\nFix the path, add the file, or clear the proof field.",
            file=sys.stderr,
        )
        return 1

    print("All referenced proof files exist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
