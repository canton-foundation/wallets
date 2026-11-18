# Wallets

Source of truth for the Canton Foundation's **Wallet Directory Program**:
which wallet providers support which Canton Network features, and the
public evidence backing each claim.

- **[WALLET_DIRECTORY.md](./WALLET_DIRECTORY.md)** -- the generated summary
  page. Start here.
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** -- how to add a wallet, update a
  listing, or verify someone else's claim.
- **`wallets/`** -- one YAML file per wallet provider (their
  self-attestation) plus `_feature_registry.yaml`, the single source of
  truth for feature IDs, names, and required-feature tests.
- **`proofs/`** -- evidence backing each claim, self-attested and
  independently verified, organized by wallet and feature.
- **`scripts/generate_table.py`** -- builds `WALLET_DIRECTORY.md` from
  the `wallets/` directory. A GitHub Action runs it on `main` after every
  merge, so contributors never commit `WALLET_DIRECTORY.md` themselves.