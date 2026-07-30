# Walley — Self-Attestation Evidence

Wallet name: `walley`
Last updated: 2026-07-27

Walley is a self-custodial browser wallet for CIP-0056 tokens on Canton
MainNet, operated by K2F Labs. Signing keys are derived in the browser from a
WebAuthn passkey PRF secret and never leave the device.

The evidence below is drawn from publicly reachable sources: the product
documentation at [docs.walley.cc](https://docs.walley.cc), the public REST API
at `api.walley.cc` (including its Swagger UI at
<https://api.walley.cc/swagger-ui/>), and the published dApp SDK package on
npm. Every claim is reproducible by a verifier against MainNet using the
registry's suggested test. Joel Lovera at Digital Asset is familiar with
Walley's feature support and can attest to the claims below. Transaction
update IDs are not published in this submission and can be supplied on
request.

---

## CC support `cc_support`

> Send, receive, and hold Canton Coin.
>
> Suggested test: Send CC to and from the wallet. Record the transaction
> update IDs and optionally provide screenshots of the holding, transfer, and
> party ID.

- Transaction update ID(s): not published in this submission (see note above)
- Party ID(s): user parties take the form `walley-<hint>::<fingerprint>` and are hosted on the K2F validator `k2f-validator-1::1220a0a64bd45fee105f5c80474842a4337bb09323ca748d7ea6dacc07fc6237572c` (returned by <https://api.walley.cc/v1/traffic/config>)
- Explorer link(s): n/a
- Screenshot(s) / video: n/a
- Notes: Canton Coin is served as instrument `Amulet` (symbol `CC`, admin
  `DSO::1220b1431ef217342db44d516bb9befde802be7d8899637d290895fa58880f19accc`)
  from the public registry endpoint <https://api.walley.cc/v1/tokens>. Sending
  and receiving CC is documented at
  <https://docs.walley.cc/guides/sending-receiving>. The public API exposes
  `GET /v1/balances`, `GET /v1/holdings`, `GET /v1/transfers`, and the
  `POST /v1/transfers/prepare`, `/accept/prepare`, `/reject/prepare`, and
  `/withdraw/prepare` command builders.

## Pre-approvals for CC `preapprovals`

> Auto-accept incoming CC without manual confirmation. Distinct from
> registry_preapprovals (App Specific) below -- the two used to share an id
> but now have different suggested tests.
>
> Suggested test: Enable pre-approvals for CC. Send CC to the wallet address.
> Confirm the transfer was auto-accepted. Record the transaction update IDs
> and optionally provide screenshots of the holding, transfer, and party ID.

- Transaction update ID(s): not published in this submission (see note above)
- Party ID(s): as above
- Explorer link(s): n/a
- Screenshot(s) / video: n/a
- Notes: Transfer pre-approval is a user-enabled setting documented at
  <https://docs.walley.cc/guides/automation-approvals>. Enabling it is itself
  an on-ledger action the user reviews and signs, the status moves from
  Pending Approval to Enabled, and the pre-approval expires and can be renewed
  from the same Settings card. With it enabled, incoming transfers complete
  without a per-transfer acceptance. The API exposes
  `GET /v1/transfer-preapproval` and `POST /v1/transfer-preapproval/prepare`.

## CIP-0056 token standard transfer support `cip_0056_transfer`

> Send and receive any CIP-0056 token, not just Canton Coin.
>
> Suggested test: Send a CIP-0056-compatible token (not Canton Coin) to and
> from the wallet. Record the transaction update IDs and optionally provide
> screenshots of the holding, transfer, and party ID.

- Transaction update ID(s): not published in this submission (see note above)
- Party ID(s): as above
- Explorer link(s): n/a
- Screenshot(s) / video: n/a
- Notes: <https://api.walley.cc/v1/tokens> returns 79 live instruments as of
  2026-07-27, of which 78 are non-CC CIP-0056 tokens, including USDCx, CBTC,
  cETH, SBC, raUSD, HANDL, EDELx, USDM1, the TRKX index series, and Tradecraft
  LP tokens. Each carries its instrument id, admin party, and where applicable
  the registry operator party. Transfers use the token standard two-step offer
  and accept flow, described at
  <https://docs.walley.cc/guides/sending-receiving>, exercising
  `TransferFactory_Transfer` and then `TransferInstruction_Accept`,
  `_Reject`, or `_Withdraw`.

## CIP-0056 token standard allocation support `cip_0056_allocation`

> Support for the allocation half of the CIP-0056 standard, distinct from
> plain transfers.
>
> Suggested test: Create and settle a CIP-0056 allocation (distinct from a
> plain transfer). Record the transaction update ID(s) for the allocation and
> its settlement, and optionally provide screenshots of the allocation before
> and after settlement.

- Transaction update ID(s): not published in this submission (see note above)
- Party ID(s): as above
- Explorer link(s): n/a
- Screenshot(s) / video: n/a
- Notes: Walley funds trades on the Tradecraft AMM venue with token standard
  allocations rather than plain transfers. It exercises
  `AllocationFactory_Allocate` to create the `Allocation` contract, the venue
  executor settles it, and the sender-controlled `Allocation_Withdraw` choice
  reclaims an allocation that was never settled. The public API exposes
  `POST /v1/tradecraft/allocation/prepare` and
  `POST /v1/tradecraft/allocation/withdraw/prepare`, both listed in
  <https://api.walley.cc/swagger-ui/>.

## CIP-0103 dApp API support `cip_0103_dapp_api`

> Connect to and sign transactions from a third-party dApp via CIP-0103.
>
> Suggested test: Connect to a dApp using a CIP-0103 connection. Initiate a
> transaction from within the dApp and sign it from the wallet. Confirm the
> successful transaction. Optionally provide screenshots or a video
> recording.

- Transaction update ID(s): not published in this submission (see note above)
- Party ID(s): as above
- Explorer link(s): n/a
- Screenshot(s) / video: n/a
- Notes: Walley ships a published provider adapter,
  [`@k2flabs/walley-dapp-sdk`](https://www.npmjs.com/package/@k2flabs/walley-dapp-sdk)
  (v1.1.0), that registers with the `DiscoveryRegistry` from
  `@canton-network/dapp-sdk` and implements the standard `Provider` interface:
  `connect`, `disconnect`, `status`, `listAccounts`, `getPrimaryAccount`,
  `getActiveNetwork`, `signMessage`, `prepareExecute`, and
  `prepareExecuteAndWait`. Every method that signs opens a popup on walley.cc
  where the user reviews and approves. Full reference at
  <https://docs.walley.cc/build/provider-api>, quickstart at
  <https://docs.walley.cc/build/quickstart>, and the end-user view of
  connecting and revoking sessions at
  <https://docs.walley.cc/guides/dapp-connections>.

## Memo tag support for transfers to omnibus accounts `memo_tag_support`

> Attach a memo tag to a transfer, recorded under the
> splice.lfdecentralizedtrust.org/reason metadata.
>
> Suggested test: Include a memo tag in an asset transfer (this can be
> combined with the cc_support test). Record the transaction update ID
> showing the memo tag under the splice.lfdecentralizedtrust.org/reason
> metadata in the transaction JSON.

- Transaction update ID(s): not published in this submission (see note above)
- Party ID(s): as above
- Explorer link(s): n/a
- Screenshot(s) / video: n/a
- Notes: The send flow carries an optional "Reason / Memo" field, documented
  as step 4 of sending at
  <https://docs.walley.cc/guides/sending-receiving> ("optionally add a payment
  reason the recipient will see"). When set, Walley writes it into the
  transfer's `meta.values` under the key
  `splice.lfdecentralizedtrust.org/reason`, and reads it back out of the same
  key to display a Reason row on the signing confirmation screen.

## Pre-approvals for DA Registry issued assets `registry_preapprovals`

> Auto-accept incoming registry-issued (non-CC) assets. Distinct from
> preapprovals (Canton Coin) above -- see the note there.
>
> Suggested test: Register pre-approvals for a DA Registry issued asset. Send
> the asset to the wallet address. Confirm the asset was auto-accepted. Record
> the transaction update IDs and optionally provide screenshots of the
> holding, transfer, and party ID.

- Transaction update ID(s): not published in this submission (see note above)
- Party ID(s): as above
- Explorer link(s): n/a
- Screenshot(s) / video: n/a
- Notes: Separately from the Canton Coin pre-approval, Walley registers a
  blanket `TransferPreapproval` per registry instrument admin, covering every
  token that admin issues. Eligible registries are those exposing an operator
  party, which the public token registry reports as `operator_id` on each
  instrument at <https://api.walley.cc/v1/tokens>. The wallet's Settings
  screen groups preapprovable tokens by admin and shows which groups are
  already covered, so a verifier can enable a group and then confirm an
  incoming registry asset lands without a manual accept.

## UTXO merge delegation contract enabled `utxo_merge_delegation`

> The wallet enables the merge delegation contract so UTXOs can be
> consolidated on-chain, reducing UTXO bloat.
>
> Suggested test: Enable the merge delegation contract in the wallet. Witness
> a UTXO consolidation contract on-chain for CC (sender & receiver are the
> same party).

- Transaction update ID(s): not published in this submission (see note above)
- Party ID(s): as above
- Explorer link(s): n/a
- Screenshot(s) / video: n/a
- Notes: Merge delegation is an opt-in Settings toggle documented at
  <https://docs.walley.cc/guides/automation-approvals#merge-delegation>. The
  user signs a `MergeDelegationProposal` create, the status moves from Pending
  Approval to Enabled, and thereafter the network consolidates that party's
  holding contracts for an asset into fewer contracts. As the documentation
  states, the delegation authorizes consolidation only, does not authorize
  transfers to anyone else, and leaves the total balance unchanged. The API
  exposes `GET /v1/merge-delegation` and
  `POST /v1/merge-delegation/prepare`.

## Clear signing `clear_signing`

> The wallet displays human-readable transaction details (not raw hex/opaque
> data) before signing.
>
> Suggested test: Show the wallet displaying human-readable transaction
> details (not raw hex/opaque data) before signing. Provide a screenshot of
> the clear-signing confirmation screen for a real transaction, alongside its
> transaction update ID.

- Transaction update ID(s): not published in this submission (see note above)
- Party ID(s): as above
- Explorer link(s): n/a
- Screenshot(s) / video: n/a
- Notes: Every signature, whether started in the wallet or requested by a
  connected dApp, goes through a review screen first. Walley keeps a registry
  of known template and choice pairs and renders each command as a labelled
  action with named fields rather than raw payload. A token standard transfer,
  for example, renders as "Send Transfer" with Sender, Receiver, Amount,
  Token, and Reason rows, with the instrument id resolved to its symbol
  through the token registry. Merge delegation and the transfer instruction
  choices render as "Enable Merge Delegation", "Accept Transfer", "Reject
  Transfer", and "Withdraw Transfer". The mandatory review step is documented
  for end users at
  <https://docs.walley.cc/guides/sending-receiving#reviewing-transactions-before-signing>
  and for dApp integrators at <https://docs.walley.cc/build/transactions>.

## Integrated swaps `integrated_swaps`

> An in-wallet swap between two assets.
>
> Suggested test: Perform an in-wallet swap between two assets. Provide the
> transaction update ID(s) for the swap and a screenshot of balances before
> and after.

- Transaction update ID(s): not published in this submission (see note above)
- Party ID(s): as above
- Explorer link(s): n/a
- Screenshot(s) / video: n/a
- Notes: Walley has a built-in swap screen at <https://walley.cc/swap> that
  routes across three venues, all live on MainNet and all queryable without
  authentication:
  - Tradecraft, a constant-product AMM, at
    <https://api.walley.cc/v1/tradecraft/pools>, which returns pools such as
    CC/USDCx, CC/eXAU, SBC/USDCx, and CBTC/cETH with their per-pool LP and
    operator fees.
  - OneSwap pools at <https://api.walley.cc/v1/oneswap/pools>.
  - Silvana, a request-for-quote venue, at
    <https://api.walley.cc/v1/silvana/config>, which lists markets including
    CBTC/CC, CBTC/USDCx, and CC/USDCx. A Silvana fill is settled by the user's
    own signature on an `AtomicDVP_Settle` exercise, so the swap is atomic and
    the wallet never takes custody.

  Where more than one venue can route a pair, the wallet shows a venue
  selector and quotes each.
