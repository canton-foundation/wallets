# Console Wallet — Self-Attestation Evidence

Wallet: `console-wallet` · [Website](https://consolewallet.io) · <support@consolewallet.io>\
Updated: **2026-11-13** · Network: **Devnet / Testnet/ Mainnet**

Evidence includes public transaction links on [CCView](https://ccview.io) and wallet screenshots. Console Wallet ships as a browser extension ([Chrome Web Store](https://chromewebstore.google.com/detail/console-wallet/lpnfhpbpmlobjlgkdmnjieeihjmihhjd)), an iOS app ([App Store](https://apps.apple.com/us/app/console-wallet/id6754840343)) and an Android app ([Google Play](https://play.google.com/store/apps/details?id=io.ccview.wallet)). Documentation: [User Guide](https://consolewallet.io/user) · [Developer docs](https://consolewallet.io/develop) · [dApp sandbox](https://consolewallet.io/sandbox).

Signup controls: new wallets require an invitation code issued through a waitlist, approvals are manual (about 100 per day) and suspicious accounts are reviewed or removed. Slack participation is confirmed in the wallet entry.

## CC support `cc_support`

Console Wallet sends, receives and holds CC. The examples show `consolewallet-maslach_3` receiving **2 CC** from `consolewallet-nick13-consolewallet` and sending **1 CC** back.

[Holding](./console-wallet-self-attestation-images/cc_support-holding.png) · [Receipt](./console-wallet-self-attestation-images/cc_support-transfer-to.png) · [Send](./console-wallet-self-attestation-images/cc_support-transfer-from.png)\
[Transaction 1](https://ccview.io/transfers/122099b7c9c05a6a27a4e899042f21c2542be7bcda49154f2029f73209e0eb30630b:1/) · [Transaction 2](https://ccview.io/transfers/1220d0bba884341c12841c5de60cd9b99dfa002429ceb26da68cf86a8034cefa8766:1/)

Send and Receive are on the main dashboard. Receive shows the party ID and a QR code.

## Two-step CC transfers `two_step_cc_transfers`

Console Wallet sends CC as offers that the recipient accepts. These transactions create and accept the **same 1 CC offer** from `consolewallet-cctag_mainnet` to `consolewallet-clear_mainnet`.

[Offer screenshot](./console-wallet-self-attestation-images/two_step_cc_transfers-offer.png) · [Acceptance screenshot](./console-wallet-self-attestation-images/two_step_cc_transfers-accepted.png)\
[Offer](https://ccview.io/updates/12204fc20bac936695ee06cc803a3039e34ccd679263f402654c49c279ab5d8289a3/)\
[Acceptance](https://ccview.io/updates/122007057f2f22bc8f17b588ccf6f6db30aa6e15759cb8dba7e31a93678ab3f1442c/)

Offers have an optional expiration and appear in the Offers tab. The receiver can accept or decline an offer, and the sender can withdraw it until it is accepted.

## Pre-approvals for CC `preapprovals`

Console Wallet receives CC without manual acceptance once pre-approvals are on. The example credits **20 CC** from `consolewallet-123456` to `consolewallet-maslach_3`, which has the setting enabled.

[Settings](./console-wallet-self-attestation-images/preapprovals-toggle.png) · [Receipt](./console-wallet-self-attestation-images/preapprovals-credited.png) · [Transaction](https://ccview.io/updates/122030cf3f402ec20500cd00ac592189decb63dcba74c97742178d1e076a2490965e/)

The "Approve incoming offers" setting (Canton Network Settings) applies to officially supported Canton tokens and can be switched on or off at any time.

## CIP-0056 token standard transfer support `cip_0056_transfer`

Console Wallet transfers non-CC tokens. The examples show `consolewallet-maslach_3` receiving **0.03 USDCx** and sending **0.1 USDCx**.

[Receipt](./console-wallet-self-attestation-images/cip_0056_transfer-in.png) · [Send](./console-wallet-self-attestation-images/cip_0056_transfer-from.png)\
[Receipt transaction](https://ccview.io/updates/1220f5fde60a64620f1b63fccc2818f06c267064ebd14447d4c06385323de5564d9d/)\
[Send transaction](https://ccview.io/updates/1220bee9509db32fc4425865609033f63cb3e5c0fe8edec18412b7983df160c3bed8/)

Other CIP-0056 tokens, such as CBTC, are also supported. Canton token balances are detected automatically.

## Memo tag support for transfers to omnibus accounts `memo_tag_support`

Console Wallet writes memos to `splice.lfdecentralizedtrust.org/reason`. The example sends **654.924107 CC** to the omnibus deposit account `unionchainpayin` with memo `6277749825087064`.

[Transaction JSON](./console-wallet-self-attestation-images/memo_tag_support-json.png) · [Wallet details](./console-wallet-self-attestation-images/memo_tag_support-memo.png) · [Transaction](https://ccview.io/transfers/1220b0b1d59a71cb28b17da782c45c5879d2b2887b465ac893bdbbfb2de8b53691c2:1/)

The memo appears under `transfer.meta.values` in the `TransferFactory_Transfer` choice argument. Users enter it in the "Memo" field on the Send screen. This is the same deposit as the integrated swap below.

## CIP-0103 dApp API support `cip_0103_dapp_api`

Console Wallet connects to dApps as a provider. The example transfer from `consolewallet-maslach_3` was initiated in a dApp and signed in the wallet.

[Third-party dApp connection](./console-wallet-self-attestation-images/cip_0103_dapp_api-connect.png) · [dApp SDK wallet picker](./console-wallet-self-attestation-images/cip_0103_dapp_api-connect-native.png) · [Transaction](https://ccview.io/transfers/1220fba1a37e0e5a3bd2259e8dc20ea3d3f89e47dca54275cf947aff5acf102de1d3:1/)

Connection tested with [PartyLayer](https://partylayer.xyz/). A public demo is available at the [Console Wallet sandbox](https://consolewallet.io/sandbox/digital-asset).

## UTXO merge delegation contract enabled `utxo_merge_delegation`

Console Wallet supports automatic UTXO merging. Enabling "Merge UTXOs" creates a `Splice.Util.Token.Wallet.MergeDelegation:MergeDelegation` contract for the party.

[Settings](./console-wallet-self-attestation-images/utxo_merge_delegation-setting.png) · [Party](https://ccview.io/party/consolewallet-maslach_3::122056469ab9bd7bbfa03758dfb7d879529c42176722e31f935f88749d2585e6fd7d/)

"Manual merge UTXOs" is also available for immediate consolidation.

## Clear signing `clear_signing`

Console Wallet shows readable details before confirmation: recipient, sender account, network, expiration date, traffic, amount, network fee, total and memo.

[Input screenshot](./console-wallet-self-attestation-images/clear_signing-input-steps.png) · [Review screenshot](./console-wallet-self-attestation-images/clear_signing-confirm.png) · [Transaction](https://ccview.io/transfers/1220fba1a37e0e5a3bd2259e8dc20ea3d3f89e47dca54275cf947aff5acf102de1d3:1/)

## Integrated swaps `integrated_swaps`

Console Wallet integrates swaps through Swap & Bridge, opened with the "Change" button. The backend selects the provider with the best rate automatically. The example swaps **654.924107 CC for 0.027353 ETH** (swap ID `46lu0nlp2t8surec`).

[Quote](./console-wallet-self-attestation-images/integrated_swaps-pair-example.png) · [Completed swap](./console-wallet-self-attestation-images/integrated_swaps-after.png) · [CC deposit](https://ccview.io/transfers/1220b0b1d59a71cb28b17da782c45c5879d2b2887b465ac893bdbbfb2de8b53691c2:1/)

The linked transaction documents the CC input. The wallet screenshot documents the ETH output.
