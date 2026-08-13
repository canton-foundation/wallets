# Metatarz — Self-Attestation Evidence

Wallet name: `metatarz`
Last updated: 2026-08-13

<!-- See CONTRIBUTING.md for the full walkthrough. Quick version: one
heading per feature, exactly as shown below; only add headings for
features you're backing with evidence; screenshots go in
./your-wallet-name-self-attestation-images/. -->


---

## CC support `cc_support`

> Send, receive, and hold Canton Coin.
>
> Suggested test: Send CC to and from the wallet. Record the transaction
> update IDs and optionally provide screenshots of the holding, transfer, and
> party ID.

- Transaction update ID(s): 12204181c5b35b3067d73806819f167fe3f3eb649432a943183dbb981fde81bfadad
- Party ID(s): user_3A1A185E::12207cc1fffa811b0c31e388ac7e7f9e872fc3ae4b96c0ea9383d4d8b5624076d601
- Explorer link(s): https://ccview.io/updates/12204181c5b35b3067d73806819f167fe3f3eb649432a943183dbb981fde81bfadad/
- Notes: See docs link: https://wallet.metatarz.xyz/docs 

<!--
Commented-out starter blocks for every remaining feature that can actually
be backed by evidence. Copy the block for the feature you're claiming,
uncomment it, and fill in your evidence. Two kinds of feature never need a
heading here, because there's nothing to prove: free-text features
(Wallet Type block, key_generation_method, assets_supported,
languages_supported), and self_attested_only boolean features -- generic
wallet capabilities that aren't Canton Network specific (see
wallets/_feature_registry.yaml). Just set `supported` in your wallet YAML
for those; no proof, no heading, no verification.
-->

<!--
## Two-step CC transfers `two_step_cc_transfers`

> Perform a two-step CC transfer (propose/create followed by a separate
> accept/settle step, rather than a single atomic send).
>
> Suggested test: Perform a two-step CC transfer. Record the transaction
> update ID(s) for both steps and optionally provide screenshots of each.

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-self-attestation-images/two_step_cc_transfers-description.png)
- Notes:
-->


## Pre-approvals for CC `preapprovals`

> Auto-accept incoming CC without manual confirmation. Distinct from
> registry_preapprovals (App Specific) below -- the two used to share an id
> but now have different suggested tests.
>
> Suggested test: Enable pre-approvals for CC. Send CC to the wallet address.
> Confirm the transfer was auto-accepted. Record the transaction update IDs
> and optionally provide screenshots of the holding, transfer, and party ID.

- Transaction update ID(s): 122086a54579cf791840d88c7128bd6e536111096d2689844f542e13b5e13be49e4d
- Party ID(s): user_0f6a5647::122089c0e9ce925ed2f4654359a5e33474d565295d818a389d5f297dd297d086c3bc
- Explorer link(s): https://ccview.io/updates/122086a54579cf791840d88c7128bd6e536111096d2689844f542e13b5e13be49e4d/
- Notes: See docs link: https://wallet.metatarz.xyz/docs 



## CIP-0056 token standard transfer support `cip_0056_transfer`

> Send and receive any CIP-0056 token, not just CC.
>
> Suggested test: Send a CIP-0056-compatible token (not Canton Coin) to and
> from the wallet. Record the transaction update IDs and optionally provide
> screenshots of the holding, transfer, and party ID.

- Transaction update ID(s): 12209dd4db480b1a2b1a10d439d7f266b7e6848b5e1f7fa7867d2b1c00ea12245bbb
- Party ID(s): user_Baa3C4A9::12204a9ed631ac1b995c654f144be3f2e1f633777feced1bbc7a3ce9b22c550cdbff
- Explorer link(s): https://ccview.io/updates/12209dd4db480b1a2b1a10d439d7f266b7e6848b5e1f7fa7867d2b1c00ea12245bbb/
- Notes: See docs link: https://wallet.metatarz.xyz/docs 


<!--
## CIP-0056 token standard allocation support `cip_0056_allocation`

> Support for the allocation half of the CIP-0056 standard, distinct from
> plain transfers.
>
> Suggested test: Create and settle a CIP-0056 allocation (distinct from a
> plain transfer). Record the transaction update ID(s) for the allocation and
> its settlement, and optionally provide screenshots of the allocation before
> and after settlement.

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-self-attestation-images/cip_0056_allocation-description.png)
- Notes:
-->

<!--
## CIP-112 token standard v2 support `cip_112_v2`

> Support for CIP-112 v2 tokens.
>
> Suggested test: Send or hold a CIP-112 v2 token in the wallet. Record the
> transaction update ID and optionally provide screenshots of the holding and
> transfer, noting the CIP-112 version in the token metadata.

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-self-attestation-images/cip_112_v2-description.png)
- Notes:
-->


## Memo tag support for transfers to omnibus accounts `memo_tag_support`

> Attach a memo tag to a transfer, recorded under the
> splice.lfdecentralizedtrust.org/reason metadata.
>
> Suggested test: Include a memo tag in an asset transfer (this can be
> combined with the cc_support test). Record the transaction update ID showing
> the memo tag under the splice.lfdecentralizedtrust.org/reason metadata in
> the transaction JSON.

- Transaction update ID(s): 122040eefb3e50155e7abbbfe93f1b676fba8bc117d041aa4304979ce436cea48907
- Party ID(s): user_b87606b0::122062b9057e7913d2e499f5a4d10f7413ec60ed622b2df6b2cccbcdcbd0303a1966
- Explorer link(s): https://ccview.io/updates/122040eefb3e50155e7abbbfe93f1b676fba8bc117d041aa4304979ce436cea48907/
- Notes: See docs link: https://wallet.metatarz.xyz/docs 




## CIP-0103 dApp API support `cip_0103_dapp_api`

> Connect to and sign transactions from a third-party dApp via CIP-0103.
>
> Suggested test: Connect to a dApp using a CIP-0103 connection. Initiate a
> transaction from within the dApp and sign it from the wallet. Confirm the
> successful transaction. Optionally provide screenshots or a video
> recording.

- Transaction update ID(s): n/a
- Party ID(s): n/a
- Explorer link(s): n/a
- Notes: See docs link: https://wallet.metatarz.xyz/docs



<!--
## Wallet Connect support `walletconnect_support`

> Connect to and sign transactions from a third-party dApp via Wallet
> Connect.
>
> Suggested test: Connect to a dApp using Wallet Connect. Initiate a
> transaction from within the dApp and sign it from the wallet. Confirm the
> successful transaction. Optionally provide screenshots or a video
> recording.

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-self-attestation-images/walletconnect_support-description.png)
- Notes:
-->


## Pre-approvals for DA Registry issued assets `registry_preapprovals`

> Auto-accept incoming registry-issued (non-CC) assets. Distinct from
> preapprovals (Canton Coin) above -- see the note there.
>
> Suggested test: Register pre-approvals for a DA Registry issued asset. Send
> the asset to the wallet address. Confirm the asset was auto-accepted. Record
> the transaction update IDs and optionally provide screenshots of the
> holding, transfer, and party ID.

- Transaction update ID(s): 122052680be0e9fd0f4f15516325003d5ee5d163ab32c3cfd64d7e71d0f02deb350d
- Party ID(s): user_0f6a5647::122089c0e9ce925ed2f4654359a5e33474d565295d818a389d5f297dd297d086c3bc
- Explorer link(s): https://ccview.io/updates/122052680be0e9fd0f4f15516325003d5ee5d163ab32c3cfd64d7e71d0f02deb350d/
- Notes: See docs link: https://wallet.metatarz.xyz/docs 



<!--
## Wallet Gateway signing driver `wallet_gateway_signing_driver`

> Integration with the Wallet Gateway signing driver.
>
> Suggested test: Integrate with the Wallet Gateway signing driver and
> demonstrate a signed transaction routed through it. Link to the signing
> driver. Record the transaction update ID and the Wallet Gateway
> request/session ID, and optionally provide a screenshot or log excerpt
> showing the driver handling the signing request.

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-self-attestation-images/wallet_gateway_signing_driver-description.png)
- Notes:
-->

<!--
## Distributed parties `distributed_parties`

> Support for parties whose authority is distributed across multiple signers.

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-self-attestation-images/distributed_parties-description.png)
- Notes:
-->

<!--
## UTXO merge delegation contract enabled `utxo_merge_delegation`

> The wallet enables the merge delegation contract so UTXOs can be
> consolidated on-chain, reducing UTXO bloat.
>
> Suggested test: Enable the merge delegation contract in the wallet. Witness
> a UTXO consolidation contract on-chain for CC (sender & receiver are the
> same party).

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-self-attestation-images/utxo_merge_delegation-description.png)
- Notes:
-->

<!--
## Hardware wallet support `hardware_wallet_support`

> Support for hardware signing devices (e.g. Ledger-class devices).

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-self-attestation-images/hardware_wallet_support-description.png)
- Notes:
-->

<!--
## Tokenization `tokenization`

> Tokenization capabilities the wallet supports.

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-self-attestation-images/tokenization-description.png)
- Notes:
-->

<!--
## Reward minting `reward_minting`

> Claiming or minting a reward (e.g. a validator or app reward).
>
> Suggested test: Demonstrate the wallet claiming or minting a reward (e.g. a
> validator or app reward). Provide the transaction update ID of the
> reward-minting event and a screenshot of the resulting holding.

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-self-attestation-images/reward_minting-description.png)
- Notes:
-->

<!--
## Transfer object / proof of transfer support `transfer_proof`

> Generate a transfer / proof-of-transfer object for a completed transaction.
>
> Suggested test: Generate a transfer/proof-of-transfer object for a completed
> transaction. Provide the transaction update ID and a screenshot or export of
> the proof object.

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-self-attestation-images/transfer_proof-description.png)
- Notes:
-->


## Clear signing `clear_signing`

> The wallet displays human-readable transaction details (not raw hex/opaque
> data) before signing.
>
> Suggested test: Show the wallet displaying human-readable transaction
> details (not raw hex/opaque data) before signing. Provide a screenshot of
> the clear-signing confirmation screen for a real transaction, alongside its
> transaction update ID.

- Transaction update ID(s): n/a
- Party ID(s): n/a
- Explorer link(s): n/a
- Notes: See docs link: https://wallet.metatarz.xyz/docs 



<!--
## Integrated swaps `integrated_swaps`

> An in-wallet swap between two assets.
>
> Suggested test: Perform an in-wallet swap between two assets. Provide the
> transaction update ID(s) for the swap and a screenshot of balances before
> and after.

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-self-attestation-images/integrated_swaps-description.png)
- Notes:
-->
