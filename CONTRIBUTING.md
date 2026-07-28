# Contributing to the Wallet Directory Program

This repo is the source of truth for the Canton Foundation's Wallet
Directory Program: which wallet providers support which Canton Network
features, and the public evidence backing each claim. This file explains
how it all works -- for both wallet providers and third-party
verifiers.

## How the program works

1. A wallet provider self-attests to feature support by opening a PR that
   adds or edits `wallets/<wallet-name>.yaml`, with evidence in
   `proofs/<wallet-name>/<wallet-name>-self-attestation.md`.
2. Wallet providers must also join and stay active in
   `#ext-temp-party-scaling`, and be able to demonstrate sign-up
   rate-limiting / circuit-breaker controls (tracked in
   `slack_party_scaling_channel_joined`).
3. The Canton Foundation reviews and merges the PR.
4. Anyone -- individuals or organizations not affiliated with the wallet --
   can independently verify a claim by adding a heading with their evidence
   to `proofs/<wallet-name>/<wallet-name>-third-party-attestation.md` and a
   `verified_by` entry in the wallet's YAML.
5. `WALLET_DIRECTORY.md` is generated from all `wallets/*.yaml` files and is
   the public page people read. Never edit it by hand.

## The three places data lives

- **`WALLET_DIRECTORY.md`** -- the generated summary table everyone reads.
  Never edit it by hand; it's produced by `scripts/generate_table.py`.
- **`wallets/<wallet-name>.yaml`** -- one file per wallet provider, holding
  their name, website, and their claim (`supported: true/false`) on every
  feature. This is the only file a wallet provider edits to update their
  listing.
- **`proofs/<wallet-name>/`** -- one folder per wallet provider, holding the
  evidence behind those claims:
  ```
  proofs/
    <wallet-name>/
      <wallet-name>-self-attestation.md               <- the wallet's own evidence, one heading per feature
      <wallet-name>-self-attestation-images/          <- screenshots/recordings referenced from the self-attestation.md file
      <wallet-name>-third-party-attestation.md        <- independent verifiers' evidence, one heading per (feature, verifier)
      <wallet-name>-third-party-attestation-images/   <- screenshots/recordings referenced from the third-party-attestation.md file
  ```
  Self-attestation and third-party verification are kept in separate files
  because a verifier's evidence must be independently gathered, not copied
  from the wallet's own claims -- separate files make that easy to audit.
  Each heading covers one feature, formatted exactly as it appears in
  `wallets/_feature_registry.yaml`, e.g.:
  ```markdown
  ## CC support (transfers and holding) `cc_support`
  ```
  In the third-party attestation file, each heading also names the verifier 
  and the outcome (see "Third-party verification" below), and is unique per
  (feature, verifier) pair, so more than one verifier can check the same
  feature. The heading text matters: GitHub turns it into the page anchor
  that `WALLET_DIRECTORY.md` and the wallet's `proof:` /
  `verified_by[].proof` fields link to -- keep headings exactly as shown
  and don't reuse one for two different features. Free-text features
  (Wallet Type block, `key_generation_method`, `assets_supported`,
  `languages_supported`) never get a heading here as there's no link to 
  proof.

## Applying as a new wallet provider

1. Copy `wallets/TEMPLATE.yaml` to `wallets/<your-wallet-name>.yaml` and
   fill it in -- every feature is already listed there with a description
   and suggested test, in order. See `examples/dummy-wallet.yaml` for a 
   worked (fictional) example.
2. Copy `proofs/_TEMPLATE/TEMPLATE-self-attestation.md` to
   `proofs/<your-wallet-name>/<your-wallet-name>-self-attestation.md` and
   add a heading for every feature you mark `supported: true` and want to
   back with evidence -- only the ones you're claiming. Put screenshots/videos in
   `proofs/<your-wallet-name>/<your-wallet-name>-self-attestation-images/`
   (create that folder alongside the `.md` file) and reference them from
   your heading. Unproven claims are allowed, but evidence makes your
   listing more credible to readers. See
   `examples/dummy-wallet-self-attestation.md` for a worked
   example. Reference the resulting file + heading anchor in that
   feature's `proof:` field in your wallet YAML.

   A handful of boolean features are marked `self_attested_only: true` in
   `wallets/_feature_registry.yaml` -- generic wallet capabilities (e.g.
   key recovery, threshold signing, compliance certifications) that don't
   require proof. For those, just set `supported` (and `reason` if false) 
   in your wallet YAML and skip `proof`/`verified_by` and the evidence 
   heading entirely -- there's no mechanism to back or verify these claims.
3. Run `python3 scripts/generate_table.py` and include the regenerated
   `WALLET_DIRECTORY.md` in your PR. No install step -- it only uses the
   Python standard library, so any Python 3 works.
4. Open a PR using the pull request template. A maintainer will review
   and, once approved, merge your PR.

## Updating an existing listing

Same process, but scoped to the fields that changed. Because each wallet
has its own YAML file, your PR only touches your own file (plus the
generated `WALLET_DIRECTORY.md`) -- it won't conflict with other wallets'
submissions.

## Marking a feature as not supported

If you don't support a feature -- because it doesn't apply to your
product, it's not built yet, or any other reason -- you can leave the
feature out of your YAML entirely, and it'll render as "—" on
`WALLET_DIRECTORY.md`. If you'd rather give readers a reason instead of
silence, set `supported: false` and add `reason: "<short explanation>"`
under that feature. There's no approval or waiver involved -- it's just an
optional way to be upfront about a gap instead of leaving it blank. The
cell then reads "Not supported" and links to your wallet's YAML file where
the reason is written.

## Third-party verification

Anyone not affiliated with the wallet provider can verify a claim, for any
feature except one marked `self_attested_only: true` in
`wallets/_feature_registry.yaml` -- those are generic wallet capabilities
that aren't Canton Network specific, so there's nothing to independently
test; they're self-attested claims only, with no verification mechanism.
To verify a feature that does support it:

1. Independently reproduce the feature's test where one is defined (see
   `suggested_test` in `wallets/_feature_registry.yaml`) -- do not simply
   copy the wallet's self-attestation.
2. Copy `proofs/_TEMPLATE/TEMPLATE-third-party-attestation.md` to
   `proofs/<wallet-name>/<wallet-name>-third-party-attestation.md` (or add
   a heading to the existing file if one's already there), formatted as
   `## <Feature name> \`<feature_id>\` — Verified by <Your Name>`, and fill
   in your evidence underneath (screenshots/videos go in the matching
   `-images/` folder).
3. Add an entry to that feature's `verified_by` list in the wallet's YAML:
   ```yaml
   verified_by:
     - by: Your Name or Org
       date: "2026-07-01"
       result: verified
       proof: proofs/<wallet-name>/<wallet-name>-third-party-attestation.md#<anchor-for-your-heading>
   ```
4. Run `python3 scripts/generate_table.py` and include the regenerated
   `WALLET_DIRECTORY.md` in your PR, same as a wallet provider would.
5. Open a PR. Once merged, that feature's cell on `WALLET_DIRECTORY.md`
   links your name (with a 🛡️) to your evidence, alongside the wallet's
   own self-attestation link.

### Unverified features

If you can't verify a feature leave it blank. 

If instead you're able to show a feature isn't actually supported, despite
the wallet claiming `supported: true`, mark it as unsupported:

- Add a heading `## <Feature name> \`<feature_id>\` — Unsupported by <Your Name>`
  to the third-party attestation file, with your evidence that the feature
  doesn't work as claimed.
- Add a `verified_by` entry with `result: unsupported` (instead of
  `result: verified`), pointing at that heading.

That feature's cell on `WALLET_DIRECTORY.md` then shows a ❌ next to your
name, linked to your evidence, alongside the wallet's own claim -- so
readers see the dispute rather than a plain, unchallenged ✅.

## Regenerating the summary page

`WALLET_DIRECTORY.md` is generated, never hand-edited:

```
python3 scripts/generate_table.py
```

Run this locally after any change to a file under `wallets/` and commit
the result. It has no dependencies to install. A GitHub Action
(`.github/workflows/verify-wallet-directory.yml`) also regenerates and
diffs this file on every PR touching `wallets/` or `scripts/`, and fails
the check if it's out of sync, in case you forget.
