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

| Feature | [Askardex Wallet](wallets/askardex-wallet.yaml) | [Dfns](wallets/dfns.yaml) | [Send](wallets/send.yaml) | [Walley](wallets/walley.yaml) |
|---|---|---|---|---|
| **Wallet Overview** |  |  |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Website | [https://wallet.askardex.com](https://wallet.askardex.com) | [https://www.dfns.co](https://www.dfns.co) | [https://cantonwallet.com](https://cantonwallet.com) | [https://walley.cc](https://walley.cc) |
| &nbsp;&nbsp;&nbsp;&nbsp;Added | 2026-07-25 | 2026-07-24 | 2026-07-24 | 2026-07-27 |
| **Wallet Type** |  |  |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Retail / Enterprise | Retail | enterprise | retail | retail |
| &nbsp;&nbsp;&nbsp;&nbsp;Custody Type | Self-custodial | self-custodial | self-custodial | self-custodial |
| &nbsp;&nbsp;&nbsp;&nbsp;Form factor (Mobile / Browser / Desktop / Browser Extension / Hardware) | mobile | browser | browser, mobile, browser-extension | browser |
| &nbsp;&nbsp;&nbsp;&nbsp;Deployment Model (Self-hosted / SaaS / Hybrid) | saas | self-hosted, saas, hybrid | saas | saas |
| **Canton Coin** |  |  |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;CC support (transfers and holding) | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#cc-support-transfers-and-holding-cc_support) | [✅](proofs/dfns/dfns-self-attestation.md#cc-support-transfers-and-holding-cc_support) | ✅ | [✅](proofs/walley/walley-self-attestation.md#cc-support-transfers-and-holding-cc_support) |
| &nbsp;&nbsp;&nbsp;&nbsp;Pre-approvals for CC | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#pre-approvals-for-cc-preapprovals) | [✅](proofs/dfns/dfns-self-attestation.md#pre-approvals-for-cc-preapprovals) | ✅ | [✅](proofs/walley/walley-self-attestation.md#pre-approvals-for-cc-preapprovals) |
| **Token Standard** |  |  |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;CIP-0056 token standard transfer support | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#cip-0056-token-standard-transfer-support-cip_0056_transfer) | [✅](proofs/dfns/dfns-self-attestation.md#cip-0056-token-standard-transfer-support-cip_0056_transfer) | ✅ | [✅](proofs/walley/walley-self-attestation.md#cip-0056-token-standard-transfer-support-cip_0056_transfer) |
| &nbsp;&nbsp;&nbsp;&nbsp;CIP-0056 token standard allocation support | — | — | ✅ | [✅](proofs/walley/walley-self-attestation.md#cip-0056-token-standard-allocation-support-cip_0056_allocation) |
| &nbsp;&nbsp;&nbsp;&nbsp;CIP-112 token standard v2 support | — | — | ✅ | [Not supported](wallets/walley.yaml) |
| **Interoperability** |  |  |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;CIP-0103 dApp API support | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#cip-0103-dapp-api-support-cip_0103_dapp_api) | — | ✅ | [✅](proofs/walley/walley-self-attestation.md#cip-0103-dapp-api-support-cip_0103_dapp_api) |
| &nbsp;&nbsp;&nbsp;&nbsp;Wallet Connect support | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#wallet-connect-support-walletconnect_support) | [✅](proofs/dfns/dfns-self-attestation.md#wallet-connect-support-walletconnect_support) | ✅ | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Memo tag support for transfers to exchanges | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#memo-tag-support-for-transfers-to-exchanges-memo_tag_support) | [✅](proofs/dfns/dfns-self-attestation.md#memo-tag-support-for-transfers-to-exchanges-memo_tag_support) | ✅ | [✅](proofs/walley/walley-self-attestation.md#memo-tag-support-for-transfers-to-exchanges-memo_tag_support) |

## Other Features

| Feature | [Askardex Wallet](wallets/askardex-wallet.yaml) | [Dfns](wallets/dfns.yaml) | [Send](wallets/send.yaml) | [Walley](wallets/walley.yaml) |
|---|---|---|---|---|
| **App Specific** |  |  |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Pre-approvals for DA Registry issued assets | — | [Not supported](wallets/dfns.yaml) | — | [✅](proofs/walley/walley-self-attestation.md#pre-approvals-for-da-registry-issued-assets-registry_preapprovals) |
| &nbsp;&nbsp;&nbsp;&nbsp;Wallet Gateway signing driver | — | [✅](proofs/dfns/dfns-self-attestation.md#wallet-gateway-signing-driver-wallet_gateway_signing_driver) | — | [Not supported](wallets/walley.yaml) |
| **Party Specific** |  |  |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Key generation method | Seed phrase (BIP-39 mnemonic, 24 words) | MPC/TSS -- keys generated as distributed shares across Dfns's signing network -- or HSM-based key generation; no seed phrases | — | WebAuthn passkey PRF secret, expanded with HKDF-SHA512 into an Ed25519 signing key that is generated and held in the browser. A 24-word BIP-39 phrase backs up the same secret. |
| &nbsp;&nbsp;&nbsp;&nbsp;Key recovery | ✅ | ✅ | ✅ | ✅ |
| &nbsp;&nbsp;&nbsp;&nbsp;Social recovery | — | — | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Multi-address / account | — | ✅ | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Distributed parties | — | — | — | [Not supported](wallets/walley.yaml) |
| **Network relevant features** |  |  |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;UTXO merge delegation contract enabled | — | — | — | [✅](proofs/walley/walley-self-attestation.md#utxo-merge-delegation-contract-enabled-utxo_merge_delegation) |
| **Transaction Signing** |  |  |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Policy workflows | — | ✅ | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Threshold Signature Scheme | — | ✅ | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Hardware wallet support | — | [✅](proofs/dfns/dfns-self-attestation.md#hardware-wallet-support-hardware_wallet_support) | ✅ | [Not supported](wallets/walley.yaml) |
| **Wallet Capabilities** |  |  |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Compliance | — | ✅ | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Validator hosting (self-hosted / BYOV) | ✅ | ✅ | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Tokenization | — | — | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Reward minting | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#reward-minting-reward_minting) | — | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Transfer object / proof of transfer support | — | — | — | [Not supported](wallets/walley.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Clear signing | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#clear-signing-clear_signing) | [✅](proofs/dfns/dfns-self-attestation.md#clear-signing-clear_signing) | — | [✅](proofs/walley/walley-self-attestation.md#clear-signing-clear_signing) |
| &nbsp;&nbsp;&nbsp;&nbsp;Integrated swaps | [Not supported](wallets/askardex-wallet.yaml) | — | ✅ | [✅](proofs/walley/walley-self-attestation.md#integrated-swaps-integrated_swaps) |
| &nbsp;&nbsp;&nbsp;&nbsp;Assets supported | CC, USDCx (CIP-0056), CBTC (CIP-0056), CETH (CIP-0056), HANDL (CIP-0056) | CC, Other CIP-0056 tokens on demand (token issuer provides an RPC node) | CC, CIP-0056 tokens | CC, USDCx, CBTC, cETH, SBC, raUSD, HANDL, EDELx, USDM1, TRKX index tokens, Tradecraft LP tokens, any CIP-0056 token in the Walley registry (79 live at api.walley.cc/v1/tokens) |
| &nbsp;&nbsp;&nbsp;&nbsp;Languages supported | English | English | English | English |
