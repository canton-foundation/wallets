<!--
  GENERATED FILE -- do not edit by hand.
  Source of truth: wallets/*.yaml + wallets/_feature_registry.yaml
  Regenerate with: python3 scripts/generate_table.py
-->

# Wallet Directory

Source of truth for Canton Network wallet providers' supported features and
assets, per the Wallet Directory Program (see [CONTRIBUTING.md](./CONTRIBUTING.md)).

**Legend:** ✅ self-attested -- click through to the evidence · 🛡️ *name* verified by an
independent third party -- click the name for their evidence · ❌ *name* found this claim to
be unsupported, contradicting the wallet -- click the name for their evidence · a linked
"Not supported" means the wallet has said no with a reason ·
— no claim made either way.

## Wallet Overview & Primary Canton Network Features

| Feature | [Dummy Wallet](wallets/dummy-wallet.yaml) | [Walley](wallets/walley.yaml) |
|---|---|---|
| **Wallet Overview** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Website | [https://example.com/dummy-wallet](https://example.com/dummy-wallet) | [https://walley.cc](https://walley.cc) |
| &nbsp;&nbsp;&nbsp;&nbsp;Added | 2026-06-10 | 2026-07-27 |
| **Wallet Type** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Retail / Enterprise | retail, enterprise | retail |
| &nbsp;&nbsp;&nbsp;&nbsp;Custody Type | self-custodial | self-custodial |
| &nbsp;&nbsp;&nbsp;&nbsp;Form factor (Mobile / Browser / Desktop / Browser Extension / Hardware) | browser, mobile | browser |
| &nbsp;&nbsp;&nbsp;&nbsp;Deployment Model (Self-hosted / SaaS / Hybrid) | saas, hybrid | saas |
| **Canton Coin** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;CC support (transfers and holding) | [✅](proofs/dummy-wallet/dummy-wallet-self-attestation.md#cc-support-transfers-and-holding-cc_support) 🛡️[ThirdParty](proofs/dummy-wallet/dummy-wallet-third-party-attestation.md#cc-support-transfers-and-holding-cc_support-verified-by-thirdparty) | [✅](proofs/walley/walley-self-attestation.md#cc-support-transfers-and-holding-cc_support) |
| &nbsp;&nbsp;&nbsp;&nbsp;Pre-approvals for CC | [✅](proofs/dummy-wallet/dummy-wallet-self-attestation.md#pre-approvals-for-cc-preapprovals) | [✅](proofs/walley/walley-self-attestation.md#pre-approvals-for-cc-preapprovals) |
| **Token Standard** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;CIP-0056 token standard transfer support | [✅](proofs/dummy-wallet/dummy-wallet-self-attestation.md#cip-0056-token-standard-transfer-support-cip_0056_transfer) | [✅](proofs/walley/walley-self-attestation.md#cip-0056-token-standard-transfer-support-cip_0056_transfer) |
| &nbsp;&nbsp;&nbsp;&nbsp;CIP-0056 token standard allocation support | — | [✅](proofs/walley/walley-self-attestation.md#cip-0056-token-standard-allocation-support-cip_0056_allocation) |
| &nbsp;&nbsp;&nbsp;&nbsp;CIP-112 token standard v2 support | ✅ | [Not supported](wallets/walley.yaml) |
| **Interoperability** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;CIP-0103 dApp API support | [✅](proofs/dummy-wallet/dummy-wallet-self-attestation.md#cip-0103-dapp-api-support-cip_0103_dapp_api) | [✅](proofs/walley/walley-self-attestation.md#cip-0103-dapp-api-support-cip_0103_dapp_api) |
| &nbsp;&nbsp;&nbsp;&nbsp;Wallet Connect support | [Not supported](wallets/dummy-wallet.yaml) | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Memo tag support for transfers to exchanges | [✅](proofs/dummy-wallet/dummy-wallet-self-attestation.md#memo-tag-support-for-transfers-to-exchanges-memo_tag_support) | [✅](proofs/walley/walley-self-attestation.md#memo-tag-support-for-transfers-to-exchanges-memo_tag_support) |

## Other Features

| Feature | [Dummy Wallet](wallets/dummy-wallet.yaml) | [Walley](wallets/walley.yaml) |
|---|---|---|
| **App Specific** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Pre-approvals for DA Registry issued assets | — | [✅](proofs/walley/walley-self-attestation.md#pre-approvals-for-da-registry-issued-assets-registry_preapprovals) |
| &nbsp;&nbsp;&nbsp;&nbsp;Wallet Gateway signing driver | — | [Not supported](wallets/walley.yaml) |
| **Party Specific** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Key generation method | — | WebAuthn passkey PRF secret, expanded with HKDF-SHA512 into an Ed25519 signing key that is generated and held in the browser. A 24-word BIP-39 phrase backs up the same secret. |
| &nbsp;&nbsp;&nbsp;&nbsp;Key recovery | ✅ | ✅ |
| &nbsp;&nbsp;&nbsp;&nbsp;Social recovery | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Multi-address / account | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Distributed parties | — | [Not supported](wallets/walley.yaml) |
| **Network relevant features** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;UTXO merge delegation contract enabled | — | [✅](proofs/walley/walley-self-attestation.md#utxo-merge-delegation-contract-enabled-utxo_merge_delegation) |
| **Transaction Signing** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Policy workflows | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Threshold Signature Scheme | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Hardware wallet support | ✅ | [Not supported](wallets/walley.yaml) |
| **Wallet Capabilities** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Compliance | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Validator hosting (self-hosted / BYOV) | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Tokenization | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Reward minting | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Transfer object / proof of transfer support | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Clear signing | ✅ | [✅](proofs/walley/walley-self-attestation.md#clear-signing-clear_signing) |
| &nbsp;&nbsp;&nbsp;&nbsp;Integrated swaps | — | [✅](proofs/walley/walley-self-attestation.md#integrated-swaps-integrated_swaps) |
| &nbsp;&nbsp;&nbsp;&nbsp;Assets supported | CC, USDC (CIP-0056), Example Token (CIP-0056) | CC, USDCx, CBTC, cETH, SBC, raUSD, HANDL, EDELx, USDM1, TRKX index tokens, Tradecraft LP tokens, any CIP-0056 token in the Walley registry (79 live at api.walley.cc/v1/tokens) |
| &nbsp;&nbsp;&nbsp;&nbsp;Languages supported | English, German | English |
