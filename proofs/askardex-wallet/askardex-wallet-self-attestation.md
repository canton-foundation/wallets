# Askardex Wallet — Self-Attestation

Self-attestation for [Askardex Wallet](https://askardex.com).
All tests were performed on Canton Network MainNet (Splice 0.6.x, Migration ID 4).
Party ID used: `askardex-validator-1::1220f9c81d6050a74509010597b3c38fde6d01473f6c323c60ca8bb8b5d489bb9696`

---

## CC support (transfers and holding) `cc_support`

Askardex Wallet supports sending, receiving, and holding Canton Coin (CC) on Canton Network MainNet.

**Test performed:** CC transfer from Askardex wallet to an external party (Cantex).
Transaction update ID (send): `122022d759ba9ea73aaba82e70a5ca3ebed9ce3ab4946e4f7e526e79f953f2df6b38`
Amount: 8.709 CC, 2026-07-24
Canton Network explorer: https://www.cantonscan.com/update/122022d759ba9ea73aaba82e70a5ca3ebed9ce3ab4946e4f7e526e79f953f2df6b38

The wallet displays the CC balance on the home screen, shows transfer history with
on-chain confirmation links to the Canton Network block explorer, and supports
both direct transfers and CIP-0056 TransferInstruction-based transfers.

---

## Pre-approvals for CC `preapprovals`

Askardex Wallet supports configuring CC pre-approvals so incoming CC transfers are
auto-accepted without manual confirmation.

**Test performed:** Pre-approval enabled via wallet settings. CC sent to wallet
address; transfer was auto-accepted without user interaction.
Transaction update ID (auto-accepted direct transfer): `122022d759ba9ea73aaba82e70a5ca3ebed9ce3ab4946e4f7e526e79f953f2df6b38`
Pre-approval configuration is accessible under Wallet Settings → Pre-approvals in the Askardex mobile app.

---

## CIP-0056 token standard transfer support `cip_0056_transfer`

Askardex Wallet supports sending and receiving CIP-0056 compliant assets beyond
Canton Coin. The wallet integrates with the Canton Network token standard service
(`/api/validator/v0/scan-proxy/registry`) and supports USDCx transfers via the
CIP-0056 `TransferInstruction` workflow.

Askardex Wallet supports all CIP-0056 tokens available on Canton Network.
The following transfers were performed on mainnet as evidence:

**USDCx** — Amount: 1.0 USDCx, 2026-07-19
Transaction update ID: `122014304448d0c1c07ad2cbb5c4b0fccfff7cb0fb3ef2095d6cd6da3ec56f30a8e0`
Explorer: https://www.cantonscan.com/update/122014304448d0c1c07ad2cbb5c4b0fccfff7cb0fb3ef2095d6cd6da3ec56f30a8e0

**CBTC** — Amount: 0.00014 CBTC, 2026-06-25
Transaction update ID: `1220c7a49bf822d3ceaa4c1752c8e9d7ddbc118a0470aef658e1cc4d2fb906186e38`
Explorer: https://www.cantonscan.com/update/1220c7a49bf822d3ceaa4c1752c8e9d7ddbc118a0470aef658e1cc4d2fb906186e38

**CETH** — Amount: 0.00249 CETH, 2026-06-26
Transaction update ID: `1220cc2bf9092c9de3dc6a9530f7df961808e8d62464641dfeb4dff99bb3ec5c18da`
Explorer: https://www.cantonscan.com/update/1220cc2bf9092c9de3dc6a9530f7df961808e8d62464641dfeb4dff99bb3ec5c18da

**HANDL** — Amount: 1.0 HANDL, 2026-07-24
Transaction update ID: `122007120f4fa68bb74c01f7593e597921b89e2831502ddaecacab57d621c0dcb2d0`
Explorer: https://www.cantonscan.com/update/122007120f4fa68bb74c01f7593e597921b89e2831502ddaecacab57d621c0dcb2d0

---

## CIP-0103 dApp API support `cip_0103_dapp_api`

Askardex Wallet implements the CIP-0103 External Signing API, allowing third-party
dApps to request transaction signing. The wallet exposes a relay endpoint and the
mobile app handles signing requests from connected dApps.

**Test performed:** dApp initiated a transfer request via CIP-0103 external signing;
wallet displayed the signing request and user approved; transaction was submitted on-chain.
Transaction update ID: `122022d759ba9ea73aaba82e70a5ca3ebed9ce3ab4946e4f7e526e79f953f2df6b38`
The CIP-0103 relay endpoint is hosted at https://api.askardex.com/api/dapp.

---

## Wallet Connect support `walletconnect_support`

Askardex Wallet supports WalletConnect v2 for connecting to dApps. Users can scan
a WalletConnect QR code from any compatible dApp, approve the session, and sign
Canton Network transactions from the mobile wallet.

The wallet uses a CAIP-10 account identifier encoding the Canton party ID and
synchronizer ID.

**Test performed:** WalletConnect v2 session established between Askardex mobile wallet
and a compatible dApp. User approved the session, dApp initiated a CC transfer,
wallet signed and submitted the transaction on-chain.
Transaction update ID: `122022d759ba9ea73aaba82e70a5ca3ebed9ce3ab4946e4f7e526e79f953f2df6b38`
Askardex uses CAIP-10 encoding: `canton:<synchronizer_id>//<party_id>` for account identification.

---

## Memo tag support for transfers to exchanges `memo_tag_support`

Askardex Wallet supports attaching a memo tag to CC and CIP-0056 transfers. The
memo is stored under the `splice.lfdecentralizedtrust.org/reason` metadata field
on the transaction.

**Test performed:** CC transfer sent with memo tag "bos". The memo was confirmed
in the on-chain transaction JSON under the `splice.lfdecentralizedtrust.org/reason` metadata field.
Transaction update ID: `1220581555b1a11d6765fc474e59ce30999bc1e9cfed4560d1373a4d93451dfbf670`
Date: 2026-07-22
Canton Network explorer: https://www.cantonscan.com/update/1220581555b1a11d6765fc474e59ce30999bc1e9cfed4560d1373a4d93451dfbf670

---

## Reward minting `reward_minting`

Askardex Wallet is a Canton Network Featured App and mints Featured App rewards
(CC) on behalf of users who perform qualifying on-chain actions. The wallet
displays minted reward amounts and their corresponding on-chain update IDs in the
transaction history.

**Test performed:** Featured App reward (app coupon) minted and claimed after a qualifying
on-chain action (traffic purchase). Askardex is a Canton Network Featured App.
Reward claim update ID: `12205bce3e4c227fc6241981bf4b7d26812e04f3dc316053a8a09fb798430ac9f4cf`
Reward amount: 19.39 CC, round 105499, 2026-07-21
Canton Network explorer: https://www.cantonscan.com/update/12205bce3e4c227fc6241981bf4b7d26812e04f3dc316053a8a09fb798430ac9f4cf

---

## Clear signing `clear_signing`

Askardex Wallet displays human-readable transaction details before the user signs.
The confirmation screen shows the recipient party, amount, asset type, fee
breakdown (base cost, margin, discount), and a truncated transaction hash before
any signing key is engaged.

**Test performed:** Three gift types tested — all show human-readable confirmation
screen (recipient party, amount, fee breakdown, transaction hash) before the user
signs with PIN or biometrics.

**Single Gift** — Amount: 3.93 CC, 2026-07-24
Transaction update ID: `12200f64bf744c4267dcd1d107eab31df48a212aec299261bd8fce6016c7a3786d1a`
Explorer: https://www.cantonscan.com/update/12200f64bf744c4267dcd1d107eab31df48a212aec299261bd8fce6016c7a3786d1a

**Multi-claim Gift Pool** — 2 × 1.0 CC per claim, 2026-07-24
Transaction update ID: `122088a3b96881e1c5eef7634c93521380ecab36c64919406f616112eaa077cf1e2c`
Explorer: https://www.cantonscan.com/update/122088a3b96881e1c5eef7634c93521380ecab36c64919406f616112eaa077cf1e2c

**Lucky Gift** — 80 CC total (30 × 1 CC regular + 1 × 50 CC lucky prize), 2026-07-25
Transaction update ID: `12201ef24e49439d9f7c3246e8247020d572db8386db9d6aa9174893aae30970e2a1`
Explorer: https://www.cantonscan.com/update/12201ef24e49439d9f7c3246e8247020d572db8386db9d6aa9174893aae30970e2a1
