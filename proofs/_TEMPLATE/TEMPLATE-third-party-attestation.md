# <Wallet Name> — Third-Party Verification Evidence

Wallet name: `wallet-name`

<!-- See CONTRIBUTING.md -> "Third-party verification" for the full
walkthrough. Quick version: one heading per (feature, verifier) pair,
either "... — Verified by <Name>" or, if you can show the wallet's claim
doesn't hold up, "... — Unsupported by <Name>"; reproduce the test
independently, don't copy the wallet's own evidence; set result: verified
or result: unsupported on the matching verified_by entry in the wallet's
YAML to match; screenshots go in
./your-wallet-name-third-party-attestation-images/. If you tried and
genuinely can't tell either way, don't add anything -- see CONTRIBUTING.md
-> "Unverified features". -->

---

## CC support (transfers and holding) `cc_support` — Verified by <Verifier Name>

> Send, receive, and hold Canton Coin.
>
> Suggested test: Send CC to and from the wallet. Record the transaction
> update IDs and optionally provide screenshots of the holding, transfer, and
> party ID.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![holding](./your-wallet-name-third-party-attestation-images/cc_support-verifier-name-holding.png)
- Notes:

<!--
## CC support (transfers and holding) `cc_support` — Unsupported by <Verifier Name>

> Send, receive, and hold Canton Coin.
>
> Suggested test: Send CC to and from the wallet. Record the transaction
> update IDs and optionally provide screenshots of the holding, transfer, and
> party ID.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date attempted: YYYY-MM-DD

- What was attempted:
- Why the wallet's claim doesn't hold up (evidence, transaction ID(s), screenshots):
- Notes:
-->

<!--
Commented-out starter blocks for every remaining feature that can actually
be verified. Uncomment the block that you want to verify, rename 
<Verifier Name>, and fill in your evidence. Each follows the
"Verified by" pattern; swap the heading suffix and body for the
"Unsupported" pattern shown above if you're disputing the wallet's claim
instead of confirming it. If you tried and genuinely can't tell either
way, don't add a block at all -- see CONTRIBUTING.md -> "Unverified
features". self_attested_only boolean features (see
wallets/_feature_registry.yaml) have no verification mechanism at all --
there's nothing to independently test, so there's no block for them here.
-->

<!--
## Pre-approvals for CC `preapprovals` — Verified by <Verifier Name>

> Auto-accept incoming CC without manual confirmation. Distinct from
> registry_preapprovals (App Specific) below -- the two used to share an id
> but now have different suggested tests.
>
> Suggested test: Enable pre-approvals for CC. Send CC to the wallet address.
> Confirm the transfer was auto-accepted. Record the transaction update IDs
> and optionally provide screenshots of the holding, transfer, and party ID.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/preapprovals-verifier-name-description.png)
- Notes:
-->

<!--
## CIP-0056 token standard transfer support `cip_0056_transfer` — Verified by <Verifier Name>

> Send and receive any CIP-0056 token, not just CC.
>
> Suggested test: Send a CIP-0056-compatible token (not Canton Coin) to and
> from the wallet. Record the transaction update IDs and optionally provide
> screenshots of the holding, transfer, and party ID.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/cip_0056_transfer-verifier-name-description.png)
- Notes:
-->

<!--
## CIP-0056 token standard allocation support `cip_0056_allocation` — Verified by <Verifier Name>

> Support for the allocation half of the CIP-0056 standard, distinct from
> plain transfers.
>
> Suggested test: Create and settle a CIP-0056 allocation (distinct from a
> plain transfer). Record the transaction update ID(s) for the allocation and
> its settlement, and optionally provide screenshots of the allocation before
> and after settlement.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/cip_0056_allocation-verifier-name-description.png)
- Notes:
-->

<!--
## CIP-112 token standard v2 support `cip_112_v2` — Verified by <Verifier Name>

> Support for CIP-112 v2 tokens.
>
> Suggested test: Send or hold a CIP-112 v2 token in the wallet. Record the
> transaction update ID and optionally provide screenshots of the holding and
> transfer, noting the CIP-112 version in the token metadata.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/cip_112_v2-verifier-name-description.png)
- Notes:
-->

<!--
## CIP-0103 dApp API support `cip_0103_dapp_api` — Verified by <Verifier Name>

> Connect to and sign transactions from a third-party dApp via CIP-0103.
>
> Suggested test: Connect to a dApp using a CIP-0103 connection. Initiate a
> transaction from within the dApp and sign it from the wallet. Confirm the
> successful transaction. Optionally provide screenshots or a video
> recording.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/cip_0103_dapp_api-verifier-name-description.png)
- Notes:
-->

<!--
## Wallet Connect support `walletconnect_support` — Verified by <Verifier Name>

> Connect to and sign transactions from a third-party dApp via Wallet
> Connect.
>
> Suggested test: Connect to a dApp using Wallet Connect. Initiate a
> transaction from within the dApp and sign it from the wallet. Confirm the
> successful transaction. Optionally provide screenshots or a video
> recording.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/walletconnect_support-verifier-name-description.png)
- Notes:
-->

<!--
## Memo tag support for transfers to exchanges `memo_tag_support` — Verified by <Verifier Name>

> Attach a memo tag to a transfer, recorded under the
> splice.lfdecentralizedtrust.org/reason metadata.
>
> Suggested test: Include a memo tag in an asset transfer (this can be
> combined with the cc_support test). Record the transaction update ID showing
> the memo tag under the splice.lfdecentralizedtrust.org/reason metadata in
> the transaction JSON.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/memo_tag_support-verifier-name-description.png)
- Notes:
-->

<!--
## Pre-approvals for DA Registry issued assets `registry_preapprovals` — Verified by <Verifier Name>

> Auto-accept incoming registry-issued (non-CC) assets. Distinct from
> preapprovals (Canton Coin) above -- see the note there.
>
> Suggested test: Register pre-approvals for a DA Registry issued asset. Send
> the asset to the wallet address. Confirm the asset was auto-accepted. Record
> the transaction update IDs and optionally provide screenshots of the
> holding, transfer, and party ID.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/registry_preapprovals-verifier-name-description.png)
- Notes:
-->

<!--
## Wallet Gateway signing driver `wallet_gateway_signing_driver` — Verified by <Verifier Name>

> Integration with the Wallet Gateway signing driver.
>
> Suggested test: Integrate with the Wallet Gateway signing driver and
> demonstrate a signed transaction routed through it. Link to the signing
> driver. Optionally provide a screenshot or log excerpt
> showing the driver handling the signing request.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/wallet_gateway_signing_driver-verifier-name-description.png)
- Notes:
-->

<!--
## Distributed parties `distributed_parties` — Verified by <Verifier Name>

> Support for parties whose authority is distributed across multiple signers.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/distributed_parties-verifier-name-description.png)
- Notes:
-->

<!--
## UTXO merge delegation contract enabled `utxo_merge_delegation` — Verified by <Verifier Name>

> The wallet enables the merge delegation contract so UTXOs can be
> consolidated on-chain, reducing UTXO bloat.
>
> Suggested test: Enable the merge delegation contract in the wallet. Witness
> a UTXO consolidation contract on-chain for CC (sender & receiver are the
> same party).

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/utxo_merge_delegation-verifier-name-description.png)
- Notes:
-->

<!--
## Hardware wallet support `hardware_wallet_support` — Verified by <Verifier Name>

> Support for hardware signing devices (e.g. Ledger-class devices).

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/hardware_wallet_support-verifier-name-description.png)
- Notes:
-->

<!--
## Tokenization `tokenization` — Verified by <Verifier Name>

> Tokenization capabilities the wallet supports.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/tokenization-verifier-name-description.png)
- Notes:
-->

<!--
## Reward minting `reward_minting` — Verified by <Verifier Name>

> Claiming or minting a reward (e.g. a validator or app reward).
>
> Suggested test: Demonstrate the wallet claiming or minting a reward (e.g. a
> validator or app reward). Provide the transaction update ID of the
> reward-minting event and a screenshot of the resulting holding.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/reward_minting-verifier-name-description.png)
- Notes:
-->

<!--
## Transfer object / proof of transfer support `transfer_proof` — Verified by <Verifier Name>

> Generate a transfer / proof-of-transfer object for a completed transaction.
>
> Suggested test: Generate a transfer/proof-of-transfer object for a completed
> transaction. Provide the transaction update ID and a screenshot or export of
> the proof object.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/transfer_proof-verifier-name-description.png)
- Notes:
-->

<!--
## Clear signing `clear_signing` — Verified by <Verifier Name>

> The wallet displays human-readable transaction details (not raw hex/opaque
> data) before signing.
>
> Suggested test: Show the wallet displaying human-readable transaction
> details (not raw hex/opaque data) before signing. Provide a screenshot of
> the clear-signing confirmation screen for a real transaction, alongside its
> transaction update ID.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/clear_signing-verifier-name-description.png)
- Notes:
-->

<!--
## Integrated swaps `integrated_swaps` — Verified by <Verifier Name>

> An in-wallet swap between two assets.
>
> Suggested test: Perform an in-wallet swap between two assets. Provide the
> transaction update ID(s) for the swap and a screenshot of balances before
> and after.

Verifier: <Verifier name or org>
Contact: <email or Slack handle>
Date verified: YYYY-MM-DD

- Transaction update ID(s):
- Party ID(s):
- Explorer link(s):
- Screenshot(s) / video: ![description](./your-wallet-name-third-party-attestation-images/integrated_swaps-verifier-name-description.png)
- Notes:
-->
