# Dummy Wallet — Self-Attestation Evidence

Wallet name: `dummy-wallet`
Last updated: 2026-06-10

<!-- This is a worked example referenced from CONTRIBUTING.md -- "Dummy
Wallet" is not a real wallet provider. Evidence below is illustrative
placeholder data, not a real transaction record. -->

---

## CC support `cc_support`

> Send, receive, and hold Canton Coin.
>
> Suggested test: Send CC to and from the wallet. Record the transaction
> update IDs and optionally provide screenshots of the holding, transfer, and
> party ID.

- Transaction update ID(s): `1220a1b2c3d4e5f6...dummy-cc-holding`, `1220f6e5d4c3b2a1...dummy-cc-transfer`
- Party ID(s): `dummy-wallet-party-1::1220...`
- Explorer link(s): https://scan.example.com/tx/1220a1b2c3d4e5f6...dummy-cc-holding
- Screenshot(s) / video: ![holding](./dummy-wallet-self-attestation-images/cc_support-holding.png)
- Notes: Round-trip transfer performed on Canton MainNet.

## Two-step CC transfers `two_step_cc_transfers`

> Perform a two-step CC transfer (propose/create followed by a separate
> accept/settle step, rather than a single atomic send).
>
> Suggested test: Perform a two-step CC transfer. Record the transaction
> update ID(s) for both steps and optionally provide screenshots of each.

- Transaction update ID(s): `1220a2b3c4d5e6f7...dummy-2step-propose`, `1220b3c4d5e6f7a8...dummy-2step-accept`
- Party ID(s): `dummy-wallet-party-1::1220...`
- Explorer link(s): https://scan.example.com/tx/1220a2b3c4d5e6f7...dummy-2step-propose
- Screenshot(s) / video: ![two-step](./dummy-wallet-self-attestation-images/two_step_cc_transfers-propose-accept.png)
- Notes: Proposed the transfer, then accepted it as a separate step, confirmed on Canton MainNet.

## Pre-approvals for CC `preapprovals`

> Auto-accept incoming CC without manual confirmation. Distinct from
> registry_preapprovals (App Specific) below -- the two used to share an id
> but now have different suggested tests.
>
> Suggested test: Enable pre-approvals for CC. Send CC to the wallet address.
> Confirm the transfer was auto-accepted. Record the transaction update IDs
> and optionally provide screenshots of the holding, transfer, and party ID.

- Transaction update ID(s): `1220b2c3d4e5f6a1...dummy-preapproval`
- Party ID(s): `dummy-wallet-party-1::1220...`
- Explorer link(s): https://scan.example.com/tx/1220b2c3d4e5f6a1...dummy-preapproval
- Screenshot(s) / video: ![auto-accept](./dummy-wallet-self-attestation-images/preapprovals-auto-accept.png)
- Notes: Pre-approval enabled, then an unsolicited CC transfer was auto-accepted with no manual step.

## CIP-0056 token standard transfer support `cip_0056_transfer`

> Send and receive any CIP-0056 token, not just CC.
>
> Suggested test: Send a CIP-0056-compatible token (not Canton Coin) to and
> from the wallet. Record the transaction update IDs and optionally provide
> screenshots of the holding, transfer, and party ID.

- Transaction update ID(s): `1220c3d4e5f6a1b2...dummy-cip0056-transfer`
- Party ID(s): `dummy-wallet-party-1::1220...`
- Explorer link(s): https://scan.example.com/tx/1220c3d4e5f6a1b2...dummy-cip0056-transfer
- Screenshot(s) / video: ![transfer](./dummy-wallet-self-attestation-images/cip_0056_transfer-holding.png)
- Notes: Transferred "Example Token (CIP-0056)" to and from the wallet.

## CIP-0103 dApp API support `cip_0103_dapp_api`

> Connect to and sign transactions from a third-party dApp via CIP-0103.
>
> Suggested test: Connect to a dApp using a CIP-0103 connection. Initiate a
> transaction from within the dApp and sign it from the wallet. Confirm the
> successful transaction. Optionally provide screenshots or a video
> recording.

- Transaction update ID(s): `1220d4e5f6a1b2c3...dummy-dapp-connect`
- Party ID(s): `dummy-wallet-party-1::1220...`
- Explorer link(s): https://scan.example.com/tx/1220d4e5f6a1b2c3...dummy-dapp-connect
- Screenshot(s) / video: ![dapp-connect](./dummy-wallet-self-attestation-images/cip_0103_dapp_api-session.png)
- Notes: Connected to a sample dApp via CIP-0103 and signed a transaction initiated from it.

## Memo tag support for transfers to omnibus accounts `memo_tag_support`

> Attach a memo tag to a transfer, recorded under the
> splice.lfdecentralizedtrust.org/reason metadata.
>
> Suggested test: Include a memo tag in an asset transfer (this can be
> combined with the cc_support test). Record the transaction update ID
> showing the memo tag under the splice.lfdecentralizedtrust.org/reason
> metadata in the transaction JSON.

- Transaction update ID(s): `1220e5f6a1b2c3d4...dummy-memo-tag`
- Party ID(s): `dummy-wallet-party-1::1220...`
- Explorer link(s): https://scan.example.com/tx/1220e5f6a1b2c3d4...dummy-memo-tag
- Screenshot(s) / video: ![memo-tag](./dummy-wallet-self-attestation-images/memo_tag_support-metadata.png)
- Notes: Transaction JSON shows the memo tag under `splice.lfdecentralizedtrust.org/reason`.
