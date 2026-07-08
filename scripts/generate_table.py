#!/usr/bin/env python3
"""
Regenerates WALLET_DIRECTORY.md from wallets/_feature_registry.yaml and
wallets/*.yaml.

Usage:
    python3 scripts/generate_table.py
    python3 scripts/generate_table.py --wallets-dir examples --out /tmp/demo.md

No install step, no dependencies -- this file is everything you need to run
it. Just run it with plain python3. (It includes its own small YAML reader
below, scoped to exactly the handful of YAML shapes used by wallets/*.yaml,
so nothing needs to be pip installed.)

Run this after adding or editing a wallet YAML file and commit the
regenerated WALLET_DIRECTORY.md alongside your change.

Output is two tables, matching the split in Feature List.md: "Wallet
Overview & Primary Canton Network Features" (Wallet Type, Canton Coin,
Token Standard, Interoperability) and "Other Features" (everything else).
There is no "required vs. optional" distinction -- see the note at the top
of wallets/_feature_registry.yaml.
"""
import argparse
import glob
import os
import re

INDENT = "&nbsp;&nbsp;&nbsp;&nbsp;"

# Categories that make up table 1, "Wallet Overview & Primary Canton
# Network Features" -- everything else goes in table 2, "Other Features".
TABLE_1_CATEGORIES = {"Wallet Type", "Canton Coin", "Token Standard", "Interoperability"}


# --- Minimal YAML reader -----------------------------------------------
#
# This repo's wallets/*.yaml and wallets/_feature_registry.yaml files only
# ever use a small, fixed set of YAML shapes: nested mappings (2-space
# indented), block sequences ("- item"), flow sequences ("[a, b]"),
# quoted/unquoted scalars, null/true/false, and ">"-folded blocks (used
# only for suggested_test, which nothing here reads programmatically). This
# reader covers exactly that, so generate_table.py needs nothing beyond the
# Python standard library -- no pip install, no venv, no PEP 668 headaches
# for contributors. It is not a general-purpose YAML parser; don't reach
# for it outside this script.

def _strip_comment(text):
    # '#' starts a comment only at line-start or after whitespace, so it
    # doesn't clip unquoted proof URLs like ".../file.md#some-anchor".
    in_squote = in_dquote = False
    for i, c in enumerate(text):
        if c == "'" and not in_dquote:
            in_squote = not in_squote
        elif c == '"' and not in_squote:
            in_dquote = not in_dquote
        elif c == "#" and not in_squote and not in_dquote:
            if i == 0 or text[i - 1].isspace():
                return text[:i].rstrip()
    return text.rstrip()


def _parse_scalar(s):
    s = s.strip()
    if s in ("", "~", "null"):
        return None
    if s == "true":
        return True
    if s == "false":
        return False
    if len(s) >= 2 and s[0] == s[-1] == '"':
        return s[1:-1]
    if len(s) >= 2 and s[0] == s[-1] == "'":
        return s[1:-1]
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    return s


def _parse_flow_list(s):
    inner = s.strip()[1:-1].strip()
    if not inner:
        return []
    items, buf, in_quote = [], "", None
    for c in inner:
        if in_quote:
            buf += c
            if c == in_quote:
                in_quote = None
        elif c in "\"'":
            in_quote = c
            buf += c
        elif c == ",":
            items.append(_parse_scalar(buf))
            buf = ""
        else:
            buf += c
    if buf.strip() != "":
        items.append(_parse_scalar(buf))
    return items


def _parse_value(val):
    val = val.strip()
    if val.startswith("[") and val.endswith("]"):
        return _parse_flow_list(val)
    if re.match(r"^[|>][+-]?$", val):
        return None  # block-scalar body, discarded during preprocessing
    return _parse_scalar(val)


def _split_kv(content):
    key, _, val = content.partition(":")
    return key.strip(), val.strip()


def _preprocess(raw_text):
    """Flattens the file into [indent, content] entries, one per
    meaningful line, with ">"/"|" block-scalar bodies swallowed whole
    (their content is never needed by this script)."""
    lines = raw_text.split("\n")
    entries = []
    i, n = 0, len(lines)
    while i < n:
        raw = lines[i]
        if raw.strip() == "" or raw.lstrip(" ").startswith("#"):
            i += 1
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        content = _strip_comment(raw).strip()
        if content == "":
            i += 1
            continue
        entries.append([indent, content])
        if re.match(r"^[^:]+:\s*[|>][+-]?\s*$", content):
            i += 1
            while i < n and (lines[i].strip() == "" or len(lines[i]) - len(lines[i].lstrip(" ")) > indent):
                i += 1
            continue
        i += 1
    return entries


def _parse_nodes(entries, pos, indent):
    """Parses sibling nodes at exactly `indent` starting at entries[pos]
    into a dict or list, based on whether the first sibling is a "- " item."""
    if pos >= len(entries) or entries[pos][0] != indent:
        return None, pos

    if entries[pos][1].startswith("- ") or entries[pos][1] == "-":
        result = []
        while pos < len(entries) and entries[pos][0] == indent and (
            entries[pos][1].startswith("- ") or entries[pos][1] == "-"
        ):
            content = entries[pos][1]
            rest = content[1:].lstrip() if content != "-" else ""
            if rest == "":
                pos += 1
                child, pos = _parse_nodes(entries, pos, indent + 2)
                result.append(child)
            elif ":" in rest and not rest.startswith(("[", '"', "'")):
                virtual_indent = indent + 2
                key, val = _split_kv(rest)
                item = {key: _parse_value(val)}
                pos += 1
                while pos < len(entries) and entries[pos][0] == virtual_indent:
                    k2, v2 = _split_kv(entries[pos][1])
                    if v2 == "":
                        pos += 1
                        child, pos = _parse_nodes(entries, pos, virtual_indent + 2)
                        item[k2] = child
                    else:
                        item[k2] = _parse_value(v2)
                        pos += 1
                result.append(item)
            else:
                result.append(_parse_value(rest))
                pos += 1
        return result, pos

    result = {}
    while pos < len(entries) and entries[pos][0] == indent:
        key, val = _split_kv(entries[pos][1])
        if val == "":
            pos += 1
            if pos < len(entries) and entries[pos][0] > indent:
                child, pos = _parse_nodes(entries, pos, entries[pos][0])
                result[key] = child
            else:
                result[key] = None
        else:
            result[key] = _parse_value(val)
            pos += 1
    return result, pos


def yaml_load(path):
    with open(path) as f:
        text = f.read()
    entries = _preprocess(text)
    if not entries:
        return None
    value, _ = _parse_nodes(entries, 0, entries[0][0])
    return value


# --- Table generation ----------------------------------------------------

def load_registry(path):
    return yaml_load(path)


def load_wallets(wallets_dir):
    wallets = []
    for path in sorted(glob.glob(os.path.join(wallets_dir, "*.yaml"))):
        base = os.path.basename(path)
        if base.startswith("_") or base.upper().startswith("TEMPLATE"):
            continue
        data = yaml_load(path)
        if not data:
            continue
        data["_source_file"] = os.path.relpath(path)
        wallets.append(data)
    return sorted(wallets, key=lambda w: w.get("name", "").lower())


def wallet_file_link(wallet):
    return f"wallets/{os.path.basename(wallet.get('_source_file', ''))}"


def wallet_column_header(wallet):
    return f"[{wallet.get('name', '?')}]({wallet_file_link(wallet)})"


def render_boolean_cell(feature_id, wallet, self_attested_only=False):
    val = (wallet.get("features") or {}).get(feature_id)
    if not isinstance(val, dict):
        return "—"

    if not val.get("supported"):
        reason = val.get("reason")
        if reason:
            return f"[Not supported]({wallet_file_link(wallet)})"
        return "—"

    # self_attested_only features have no proof/verification mechanism --
    # generic wallet capabilities that aren't Canton Network specific, so
    # there's nothing to test against the network. Render a plain claim,
    # ignoring any proof/verified_by even if present.
    if self_attested_only:
        return "✅"

    proof = val.get("proof")
    cell = f"[✅]({proof})" if proof else "✅"

    verified_by = val.get("verified_by") or []
    confirmed = [v for v in verified_by if v.get("result", "verified") != "unsupported"]
    disputed = [v for v in verified_by if v.get("result") == "unsupported"]

    def link_names(entries):
        names = []
        for v in entries:
            name = v.get("by", "unknown")
            vproof = v.get("proof")
            names.append(f"[{name}]({vproof})" if vproof else name)
        return ", ".join(names)

    if confirmed:
        cell += " 🛡️" + link_names(confirmed)
    if disputed:
        cell += " ❌" + link_names(disputed)

    return cell


def render_freetext_cell(feature_id, wallet):
    val = (wallet.get("features") or {}).get(feature_id)
    if val in (None, "", []):
        return "—"
    if isinstance(val, list):
        return ", ".join(str(v) for v in val) if val else "—"
    return str(val)


def render_feature_cell(feature, wallet):
    if feature["type"] == "freetext":
        return render_freetext_cell(feature["id"], wallet)
    return render_boolean_cell(feature["id"], wallet, feature.get("self_attested_only", False))


def render_wallet_overview_rows(wallets):
    n = len(wallets)
    lines = ["| **Wallet Overview** | " + " | ".join([""] * n) + " |"]

    row = [f"{INDENT}Website"]
    for w in wallets:
        site = w.get("website")
        row.append(f"[{site}]({site})" if site else "—")
    lines.append("| " + " | ".join(row) + " |")

    row = [f"{INDENT}Added"]
    for w in wallets:
        added = w.get("added")
        row.append(added if added else "—")
    lines.append("| " + " | ".join(row) + " |")

    return lines


def render_table(features, wallets, include_overview_block):
    header = ["Feature"] + [wallet_column_header(w) for w in wallets]
    lines = ["| " + " | ".join(header) + " |",
             "|" + "|".join(["---"] * len(header)) + "|"]

    if include_overview_block:
        lines.extend(render_wallet_overview_rows(wallets))

    current_category = None
    for feature in features:
        if feature["category"] != current_category:
            current_category = feature["category"]
            lines.append(f"| **{current_category}** | " + " | ".join([""] * len(wallets)) + " |")
        row = [f"{INDENT}{feature['name']}"]
        for w in wallets:
            row.append(render_feature_cell(feature, w))
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="wallets/_feature_registry.yaml")
    parser.add_argument("--wallets-dir", default="wallets")
    parser.add_argument("--out", default="WALLET_DIRECTORY.md")
    args = parser.parse_args()

    registry = load_registry(args.registry)
    all_features = registry.get("features", [])
    table_1_features = [f for f in all_features if f["category"] in TABLE_1_CATEGORIES]
    table_2_features = [f for f in all_features if f["category"] not in TABLE_1_CATEGORIES]
    wallets = load_wallets(args.wallets_dir)

    if wallets:
        table_1_md = render_table(table_1_features, wallets, include_overview_block=True)
        table_2_md = render_table(table_2_features, wallets, include_overview_block=False)
    else:
        placeholder = "_No wallets listed yet. See [CONTRIBUTING.md](./CONTRIBUTING.md) to apply._"
        table_1_md = placeholder
        table_2_md = "_No wallets listed yet._"

    body = f"""<!--
  GENERATED FILE -- do not edit by hand.
  Source of truth: wallets/*.yaml + wallets/_feature_registry.yaml
  Regenerate with: python3 scripts/generate_table.py
-->

# Wallet Directory

Source of truth for Canton Network wallet providers' supported features and
assets, per the Wallet Directory Program (see [CONTRIBUTING.md](./CONTRIBUTING.md)).

**Legend:** ✅ self-attested -- click through to the evidence · 🛡️ *name* verified by an
independent third party -- click the name for their evidence · ❌ *name* found this claim to
be unsupported, contradicting the wallet -- click the name for their evidence · a linked
"Not supported" means the wallet has said no with a reason ·
— no claim made either way.

## Wallet Overview & Primary Canton Network Features

{table_1_md}

## Other Features

{table_2_md}
"""

    with open(args.out, "w") as f:
        f.write(body)
    print(f"Wrote {args.out} ({len(wallets)} wallet(s) from {args.wallets_dir}/)")


if __name__ == "__main__":
    main()
