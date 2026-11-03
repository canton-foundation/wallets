# MahaWallet — Self-Attestation Evidence

Wallet name: `mahawallet`
Last updated: 2026-10-16

All evidence below is from mainnet. Transaction update IDs open in the Lighthouse explorer, and the `maha-*` party IDs belong to MahaWallet accounts. The explorer shows only the CC side of token transfers (it indexes Amulet events), so token movements are backed by its CIP-56 activity list and by the wallet's balances.

---

## CC support `cc_support`

- Transaction update ID(s):
  - `12205b1cd7e36dc1522709b3ccbc721298d2809cf72222ab58a7e4aa8f770a0149b1`: maha-awikwokk to maha-haland, 1.0 CC, 2026-10-15 13:16 UTC (explorer link confirmed by owner)
  - `1220a061f752a2c82afb00c421303d7c91574a65df4489214d1ae83f0aa680803b40`: maha-haland back to maha-awikwokk, 1.0 CC, 2026-10-15 13:19 UTC (explorer link confirmed by owner). Its input holding `00a492df…` is the holding created by the first transfer.
- Party ID(s):
  - sender: `maha-awikwokk::12202f941fbab22462c09463dc65166ff92eb4d274a7a9ada8e96f5659cf65eeb468`
  - receiver: `maha-haland::122029daf227013c8515bc9b45efaa3ac01dcd013b3f761c1471cc7814f502571d4e`
- Explorer link(s):
  - https://lighthouse.cantonloop.com/transactions/12205b1cd7e36dc1522709b3ccbc721298d2809cf72222ab58a7e4aa8f770a0149b1
  - https://lighthouse.cantonloop.com/transactions/1220a061f752a2c82afb00c421303d7c91574a65df4489214d1ae83f0aa680803b40
- Notes: Choice `TransferFactory_Transfer` (token standard, `ExternalPartyAmuletRules`) completed in one step (`TransferInstructionResult_Completed`). Network: mainnet. Both parties are MahaWallet accounts (owner-confirmed).

## Two-step CC transfers `two_step_cc_transfers`

- Transaction update ID(s) (both explorer links confirmed by owner):
  - Step 1, sender creates the offer (`TransferFactory_Transfer`, result `TransferInstructionResult_Pending`, 1.0 CC, 2026-10-15 13:23 UTC): `1220ef7ecbdbf3f588e156cf5dce448f845a390d0b15e2b4d06d60a43c0897de3ffc`
  - Step 2, receiver accepts (`TransferInstruction_Accept`, result `TransferInstructionResult_Completed`): `1220a5348a15ed006b596e2dbe288de744d32b53e45f60f6877337acd9b602e8f3b8`
- Party ID(s):
  - sender: `maha-awikwokk::12202f941fbab22462c09463dc65166ff92eb4d274a7a9ada8e96f5659cf65eeb468`
  - receiver: `maha-cepiritttttt::1220addef1e3730acd7eaa7fef6797285c37f78dca22d5a85a5168d60b1e09aadeab`
- Network: mainnet
- Explorer link(s):
  - https://lighthouse.cantonloop.com/transactions/1220ef7ecbdbf3f588e156cf5dce448f845a390d0b15e2b4d06d60a43c0897de3ffc
  - https://lighthouse.cantonloop.com/transactions/1220a5348a15ed006b596e2dbe288de744d32b53e45f60f6877337acd9b602e8f3b8
- Notes: The receiver had no preapproval, so step 1 returned a pending TransferInstruction (`00922e37…da8325f`). Step 2 exercises `TransferInstruction_Accept` on that same contract and creates the receiver's holding.

## Pre-approvals for CC `preapprovals`

- Transaction update ID(s):
  - Enable (`ExternalPartySetupProposal_Accept`, creates a `TransferPreapproval` and a `ValidatorRight`): `12205fedd29773e767e6a64d15a27c6f089db355a32500eb20df23d4e8e1f52f8ad4`
  - Auto-accepted transfer to this party after enabling (`TransferFactory_Transfer`, result `TransferInstructionResult_Completed`, 1.0 CC from maha-awikwokk, 2026-10-15 13:42 UTC; its `transfer-preapproval` context value equals the `transferPreapprovalCid` created above): `12208cca0b5b4ec7e33cf962ed9f05083d21d34968fc3836627ac42ef0e4425b9c4a`
- Party ID(s): `maha-cepiritttttt::1220addef1e3730acd7eaa7fef6797285c37f78dca22d5a85a5168d60b1e09aadeab`
- Network: mainnet
- Explorer link(s) (both confirmed by owner):
  - https://lighthouse.cantonloop.com/transactions/12205fedd29773e767e6a64d15a27c6f089db355a32500eb20df23d4e8e1f52f8ad4
  - https://lighthouse.cantonloop.com/transactions/12208cca0b5b4ec7e33cf962ed9f05083d21d34968fc3836627ac42ef0e4425b9c4a
- Notes: Settings has a CC preapproval switch and one per token. Turning it on creates a setup proposal and the wallet accepts it, which is two ledger transactions. The new `transferPreapprovalCid` is `00d43de3…2b7969ca…529030`; the auto-accepted transfer above carries exactly that value as `transfer-preapproval` in its context.

## Memo tag support for transfers to omnibus accounts `memo_tag_support`

- Transaction update ID(s): `12202ca6e1975a8aef7368454cb4a2316cf37a141863f43496fa78ad6fc9bfcf06c9` (1.0 CC, 2026-10-15 13:44 UTC, mainnet; explorer link confirmed by owner)
- Party ID(s):
  - sender: `maha-cepiritttttt::1220addef1e3730acd7eaa7fef6797285c37f78dca22d5a85a5168d60b1e09aadeab`
  - receiver: `maha-awikwokk::12202f941fbab22462c09463dc65166ff92eb4d274a7a9ada8e96f5659cf65eeb468`
- Explorer link(s): https://lighthouse.cantonloop.com/transactions/12202ca6e1975a8aef7368454cb4a2316cf37a141863f43496fa78ad6fc9bfcf06c9
- Memo in the transaction JSON: `choice_argument.transfer.meta.values["splice.lfdecentralizedtrust.org/reason"] = "test-memo-mahawallet"`, echoed in `exercise_result.meta.values` of the same key.
- Notes: The memo is on-ledger and visible to parties entitled to see the transfer.

## CIP-0056 token standard transfer support `cip_0056_transfer`

USDCx (a CIP-0056 token, not CC) sent and received by the wallet on mainnet. The first two rows appear in the explorer's CIP-56 activity list for the wallet; the third is the Cantex swap settlement. The explorer's event tree only shows the Amulet side of these updates, so token movements are read from that activity list and from the wallet.

- Transaction update ID(s):
  - Send, USDCx from `maha-awikwokk` to `maha-haland`, 2026-10-05 16:56 UTC: `12204723eca0907dfb50f35be15ed84351efd24f725e233dc501c9e6c449f89953c4`
  - Receive, USDCx from `maha-tip` to `maha-awikwokk`, 2026-10-06 14:03 UTC: `1220502976d173f66974dd55e073366e4ccaec14249e864e66680fd2a0ec0ac4dfa9`
  - Receive, USDCx from the Cantex swap into `maha-awikwokk`, 2026-10-15 15:19 UTC: `122052f0883977b306a9d312e26029fee27712e91299a13a75e788f6c33fe5e2b563` (see the swap section)
- Party ID(s): `maha-awikwokk::12202f941fbab22462c09463dc65166ff92eb4d274a7a9ada8e96f5659cf65eeb468`, `maha-haland::122029daf227013c8515bc9b45efaa3ac01dcd013b3f761c1471cc7814f502571d4e`, `maha-tip::122025cef1bec8edc8aa50108068aa065b63dc1336f0695448dc8d669ae029e08ff8`
- Network: mainnet
- Explorer link(s):
  - https://lighthouse.cantonloop.com/transactions/12204723eca0907dfb50f35be15ed84351efd24f725e233dc501c9e6c449f89953c4
  - https://lighthouse.cantonloop.com/transactions/1220502976d173f66974dd55e073366e4ccaec14249e864e66680fd2a0ec0ac4dfa9
- Notes: `maha-awikwokk`, `maha-haland` and `maha-tip` are MahaWallet-controlled accounts (owner-confirmed).

## Integrated swaps `integrated_swaps`

- Transaction update ID(s):
  - Swap input, 50 CC sent to Cantex with the output token named in the memo (`TransferFactory_Transfer`, memo `splice.lfdecentralizedtrust.org/reason` = `USDCx`, result `TransferInstructionResult_Pending`, 2026-10-15 15:18 UTC, mainnet): `122028dd9dbcad1db5167157ba29f7fdb31c66fd1c0a65ba43c59323659f9608155a` (explorer link confirmed by owner)
  - Cantex settlement update `122052f0883977b306a9d312e26029fee27712e91299a13a75e788f6c33fe5e2b563` (round 117507). One of its events is `TransferInstruction_Accept` by `cantex-swap` on the instruction `00f3a9cb…a94` created by the 50 CC send above, result `TransferInstructionResult_Completed`. Following events take a 2.1 CC fee to `Cantex-validator-1` and move the remaining 47.9 CC to `pool-custodian`.
  - Swap output (USDCx): the settlement update's transaction record contains a USDCx-side view whose informees are `Bridge-Operator` and `decentralized-usdc-interchain-rep` (the USDCx issuer-side parties), `cantex-swap` and `maha-awikwokk`, next to a view with only `cantex-swap` and `maha-awikwokk`. The explorer's event tree shows only the CC side (it lists Amulet events). The USDCx receipt is confirmed by the wallet balance below.
- Party ID(s):
  - wallet: `maha-awikwokk::12202f941fbab22462c09463dc65166ff92eb4d274a7a9ada8e96f5659cf65eeb468`
  - Cantex: `cantex-swap::122038c015864f106cfed48bb9106b7c89982368d27956ffcdfda6c38328f0909b8c`
- Balances: CC decreased by 50. USDCx balance after the swap: 5.5804 (owner-confirmed from the wallet). The USDCx balance before the swap was not recorded, so the exact amount received is not stated.
- Notes: Swaps run through Cantex Connect: the wallet sends the input to Cantex's party with the output token in the memo, and Cantex sends the output back.

## CIP-0103 dApp API support `cip_0103_dapp_api`

- Status: self-attested by the wallet owner. No run with a third-party dApp is on record, so no transaction update ID is given.
- Implementation: MahaWallet injects the Canton Network SDK provider (`@canton-network/core-provider-dapp` with the `core-rpc-transport` window transport, version 1.8.0) as `window.canton` and announces it with the `canton:announceProvider` event.
- Methods answered: `connect`, `disconnect`, `isConnected`, `status`, `listAccounts`, `getPrimaryAccount`, `signMessage`, `prepareExecute`, `prepareExecuteAndWait`. Events sent to the page: `accountsChanged`, `statusChanged`, `txChanged`.
- Not yet implemented: `getActiveNetwork`, `ledgerApi`.
- Testing so far: the flow has been exercised with MahaWallet's own test page only.
