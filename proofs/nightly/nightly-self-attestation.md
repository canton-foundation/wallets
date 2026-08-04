# Nightly — Self-Attestation Evidence

Wallet name: `nightly`
Last updated: 2026-08-04

This submission uses Nightly's public product documentation and open-source
Canton integration as evidence. Transaction update IDs and screenshots are not
included in this initial submission.

---

## CC support `cc_support`

Nightly's [Canton wallet page](https://nightly.app/wallet/canton) documents
support for storing, sending, and receiving Canton assets. The
[Canton transaction command documentation](https://docs.nightly.app/docs/canton/canton/transaction_commands/)
also demonstrates constructing and submitting an Amulet transfer.

## Two-step CC transfers `two_step_cc_transfers`

Nightly's [Canton transaction command documentation](https://docs.nightly.app/docs/canton/canton/transaction_commands/)
documents separate commands for creating a transfer and accepting, rejecting,
or withdrawing a pending transfer.

## Memo tag support for transfers to omnibus accounts `memo_tag_support`

Nightly's [Canton transaction command documentation](https://docs.nightly.app/docs/canton/canton/transaction_commands/)
includes an optional `memo` field in the transfer command parameters and shows
it used in an example transfer.

## CIP-0103 dApp API support `cip_0103_dapp_api`

Nightly's open-source [Canton Web3 template](https://github.com/nightly-labs/canton-web3-template/blob/main/README.md)
declares CIP-0103 support. Its
[provider adapter](https://github.com/nightly-labs/canton-web3-template/blob/main/app/misc/adapter.ts)
uses the Canton Network dApp RPC client and exposes the CIP-0103 connection,
account, execution, Ledger API, signing, and event methods through
`window.canton`.
