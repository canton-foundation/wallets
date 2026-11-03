# Loop Wallet — Self-Attestation Evidence

Wallet: `loop` · [Website](https://wallet.looptech.io) · support@looptech.io  
Updated: **2026-10-28** · Network: **Mainnet only**

Evidence includes public transaction links, wallet screenshots, and provider-supplied database and console records. Provider confirmations are identified below.

Signup controls: the provider confirms that the signup-disable switch, topology queue capacity check, and configurable signup caps are deployed on mainnet (2026-10-28). Slack participation is confirmed in the wallet entry.

## CC support `cc_support`

Loop supports CC transfers. The example completes a **1 CC** transfer and creates the matching receiver holding.

[Transaction](https://data.looptech.io/transactions/122053355b418a285d33d7ab7b2a1e9ecf912f8d48c479e1341aa37b4109da06d1c0)

## Two-step CC transfers `two_step_cc_transfers`

Loop supports offers requiring recipient acceptance. These transactions create and accept the **same 5 CC offer**, producing the receiver holding.

[Offer](https://data.looptech.io/transactions/12208e9195542e5c2eaae050a89703a3a70104a8bf4520aea87cfd45682edeb92c66)  
[Acceptance](https://data.looptech.io/transactions/1220c8f6c4d55a542665bbff1e6386f42fdfe0e878552b26f20d85fba3492406c83b)

## Pre-approvals for CC `preapprovals`

Loop supports creating CC pre-approvals and receiving CC without manual acceptance. Setup and transfer examples use different pre-approval contracts.

[Setup](https://data.looptech.io/transactions/12202ea54f68c413776196ab8e97417adf2e92f68ebf02a748062a119ac48a5497d0)  
[Pre-approved transfer](https://data.looptech.io/transactions/122053355b418a285d33d7ab7b2a1e9ecf912f8d48c479e1341aa37b4109da06d1c0)

## CIP-0056 token standard transfer support `cip_0056_transfer`

Loop supports non-CC token transfers. Matching wallet screenshots show a completed **1 USDCx send and receipt**.

[Send](./loop-self-attestation-images/usdcx-send-completed.png) · [Receipt](./loop-self-attestation-images/usdcx-receive-completed.png) · [Transaction](https://data.looptech.io/transactions/1220579c896b4ff5cca3261de0932170693437a9e53671f11c14c000c8d6a8afdb0a)

## CIP-0056 token standard allocation support `cip_0056_allocation`

Loop supports allocation flows through connected dApps. The example creates and settles the **same 105 CC allocation**, producing a receiver holding (events `:11`, `:16`, `:17`, `:23`). The sender is provider-confirmed as a Loop party.

[Transaction](https://data.looptech.io/transactions/1220aabb40472b962d11eac0d349ce118a5916d937d4922066d09860e920c6ce4e60)

This uses V1 interfaces. Despite the transaction data’s `USDCx` label, the underlying instrument and holdings are `Amulet` (CC).

## CIP-112 token standard v2 support `cip_112_v2`

Loop holds V2-compatible assets. An active **1.0030448045 USDCx** holding in Loop’s mainnet database identifies the Loop owner, contract ID, and amount. Its instrument ID and registrar/source match registry metadata advertising `splice-api-token-holding-v2` and `splice-api-token-transfer-instruction-v2`.

[Registry info](./usdcx-registry-info.json) · [Instrument metadata](./usdcx-registry-instruments.json) · [Active holding database export](./loop-usdcx-holdings-db-export.json)

Registry metadata collected 2026-10-27; holding captured 2026-10-28 at 21:14:57 UTC. The provider-supplied database record demonstrates holding a V2-compatible asset.

## Memo tag support for transfers to omnibus accounts `memo_tag_support`

Loop preserves memos in `splice.lfdecentralizedtrust.org/reason`. The example includes the memo in both the transfer request and completed result. This example demonstrates memo placement.

[Transaction](https://data.looptech.io/transactions/122053355b418a285d33d7ab7b2a1e9ecf912f8d48c479e1341aa37b4109da06d1c0)

## Pre-approvals for DA Registry issued assets `registry_preapprovals`

Loop supports issuer-specific registry pre-approvals. Evidence shows USDCx enabled, an active approval for the recipient/admin, and a completed **0.1 USDCx receipt**. The provider confirms no manual acceptance was required.

[Settings](./loop-self-attestation-images/usdcx-preapproval-enabled.png) · [Approval database export](./usdcx-preapproval-db-export.json) · [Receipt](./loop-self-attestation-images/usdcx-preapproval-receipt.png) · [Transaction](https://data.looptech.io/transactions/122077b55156a3bce458ae952f1fef62ae2a23f24715e0a08dc66445a39101380a58)

The approval record comes from Loop’s active-contract database mirror.

## Distributed parties `distributed_parties`

New Loop parties support **2-of-3 participant confirmation**. The authorized example mapping lists CantonLoop, Digital Asset, and MPCH participants with `Confirmation` permission, threshold 2, and no recorded end of validity.

[Console query and output](./loop-party-topology-console.txt)

The threshold applies to participant confirmation. Users retain a single external signing key. Console identifiers are abbreviated.

## UTXO merge delegation contract enabled `utxo_merge_delegation`

Loop supports automatic UTXO management. Settings and a database record show delegation enabled. A separate automatic-worker example consumes **50 CC holdings**, leaving one owner holding of **24991.8336706069 CC** and a separate **13.5813712370 CC** fee holding.

[Settings](./loop-self-attestation-images/utxo-management-enabled.png) · [Delegation database export](./loop-merge-delegation-db-export.json) · [Worker log](./loop-cc-merge-log.json)  
[Consolidation](https://data.looptech.io/transactions/1220d5238697368599be15d3133d54234ab15ae5ebe2c4d3e8b428b1d9733f157b3b)

Setup and consolidation involve different Loop parties. The transaction demonstrates consolidation; the matching worker log identifies automatic execution.

## Transfer object / proof of transfer support `transfer_proof`

Loop History links to Loop Data, which provides structured transaction JSON. The CC example includes sender, receiver, asset, amount, completed result, and receiver holding.

[History link screenshot](./loop-self-attestation-images/usdcx-receive-completed.png) · [Transaction](https://data.looptech.io/transactions/122053355b418a285d33d7ab7b2a1e9ecf912f8d48c479e1341aa37b4109da06d1c0)

The evidence is a structured transfer record. Available event detail varies by transaction.

## Clear signing `clear_signing`

Loop shows readable details before confirmation for recognized transactions. The screenshot displays the requesting dApp, **5 CC** amount, recipient, estimated fee, origin, and expandable command details.

[Review screenshot](./loop-self-attestation-images/clear-signing-transfer-review.png) · [Completed transaction](https://data.looptech.io/transactions/1220354da1c31d0d437b3123b31bf8ea24ab5c1afa877e7fd16c707c2b7531fc0439)

The provider identifies this as the reviewed transaction. The mainnet transaction matches the screenshot’s 5 CC amount and shortened recipient; event `:0` reports completion and event `:4` creates the recipient holding.

## Integrated swaps `integrated_swaps`

Loop integrates swaps with quotes, provider selection, slippage controls, and fee review. The example swaps **10 CC for 1.0030448045 USDCx** through Tradecraft.

[Quote](./loop-self-attestation-images/swap-cc-usdcx-quote.png) · [Completed receipt](./loop-self-attestation-images/swap-usdcx-receipt.png)  
[CC offer](https://data.looptech.io/transactions/12202e12704692de32060154df6cf3269f4b6ca9fdfebc2af4ef7e34228a0a9b51ac)  
[CC acceptance](https://data.looptech.io/transactions/122098a0c7e29ef3f8fbe8bd3c85307bfc966a5a87d37d303c5004b7649b60876e49)

The linked transactions document the CC input. The wallet receipt documents the USDCx output and matches the acceptance update ID.
