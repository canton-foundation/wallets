# Dfns — Self-Attestation Evidence

Wallet name: `dfns`
Last updated: 2026-07-24

---

## CC support (transfers and holding) `cc_support`

> Send, receive, and hold Canton Coin.

- Notes: Dfns supports Canton Coin balance tracking, transfers, and
  transaction broadcasting via API and dashboard, with real-time indexing
  of incoming and outgoing transfers. Public announcements:
  [Dfns Canton Tier-1 support](https://dfns.co/article/canton-tier-1-support),
  [Introducing Dfns on Canton Network](https://www.canton.network/blog/introducing-dfns-institutional-grade-custody-and-wallet-infrastructure-on-canton-network).

## Pre-approvals for CC `preapprovals`

> Auto-accept incoming CC without manual confirmation. Distinct from
> registry_preapprovals (App Specific).

- Notes: Assets can be pre-approved (dashboard "Approve Assets" or API) so
  incoming transfers of that asset are accepted automatically. Public
  documentation: [Canton Network — Dfns docs](https://docs.dfns.co/networks/canton).

## CIP-0056 token standard transfer support `cip_0056_transfer`

> Send and receive any CIP-0056 token, not just CC.

- Notes: Dfns supports CIP-0056 (Canton token standard) transfers, including
  free-of-payment transfers that can be approved or rejected on-chain, for
  Canton Coin and other CIP-0056 tokens on demand. Public announcement:
  [Canton Token Standard Support (CIP-56)](https://www.dfns.co/article/canton-token-standard-support).

## Wallet Connect support `walletconnect_support`

> Connect to and sign transactions from a third-party dApp via Wallet
> Connect.

- Notes: Dfns wallets can be connected to external dApps via WalletConnect
  from the dashboard, with policy controls and signature review applied to
  transaction requests. Dfns is WalletConnect Institutional Certified.
  Public documentation:
  [Use WalletConnect — Dfns docs](https://docs.dfns.co/guides/walletconnect),
  [Institutional Certified by WalletConnect](https://www.dfns.co/article/institutional-certified-by-walletconnect).

## Memo tag support for transfers to exchanges `memo_tag_support`

> Attach a memo tag to a transfer, recorded under the
> splice.lfdecentralizedtrust.org/reason metadata.

- Notes: Memo tags can be attached to transfers via the `memo` field of the
  transfer endpoint, and are recorded under the
  `splice.lfdecentralizedtrust.org/reason` metadata. Public documentation:
  [Transfer Asset — Dfns docs](https://docs.dfns.co/api-reference/wallets/transfer-asset).

## Wallet Gateway signing driver `wallet_gateway_signing_driver`

> Integration with the Wallet Gateway signing driver.

- Notes: Dfns is an official signing provider for the Canton Wallet Gateway;
  the Dfns signing driver is merged into the Gateway codebase. The driver
  handles key resolution, signing (subject to configured Dfns policies:
  approval thresholds, amount limits, time locks, KYT checks, passkey
  authentication), and signature return to the Gateway for validator
  submission. Public announcement:
  [Canton Wallet Gateway Support](https://dfns.co/article/canton-wallet-gateway-support/).

## Hardware wallet support `hardware_wallet_support`

> Support for hardware signing devices.

- Notes: Signing can be backed by HSMs (hardware security modules) in
  addition to Dfns's MPC/TSS signing network.

## Clear signing `clear_signing`

> The wallet displays human-readable transaction details (not raw
> hex/opaque data) before signing.

- Notes: Human-readable transaction details are displayed before signing
  (passkey/WebAuthn confirmation flow shows the decoded transaction, not
  raw payload data).
