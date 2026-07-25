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

| Feature | [Askardex Wallet](wallets/askardex-wallet.yaml) | [Dummy Wallet](wallets/dummy-wallet.yaml) |
|---|---|---|
| **Wallet Overview** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Website | [https://wallet.askardex.com](https://wallet.askardex.com) | [https://example.com/dummy-wallet](https://example.com/dummy-wallet) |
| &nbsp;&nbsp;&nbsp;&nbsp;Added | 2026-07-25 | 2026-06-10 |
| **Wallet Type** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Retail / Enterprise | Enterprise | retail, enterprise |
| &nbsp;&nbsp;&nbsp;&nbsp;Custody Type | Self-custodial | self-custodial |
| &nbsp;&nbsp;&nbsp;&nbsp;Form factor (Mobile / Browser / Desktop / Browser Extension / Hardware) | mobile | browser, mobile |
| &nbsp;&nbsp;&nbsp;&nbsp;Deployment Model (Self-hosted / SaaS / Hybrid) | saas | saas, hybrid |
| **Canton Coin** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;CC support (transfers and holding) | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#cc-support-transfers-and-holding-cc_support) | [✅](proofs/dummy-wallet/dummy-wallet-self-attestation.md#cc-support-transfers-and-holding-cc_support) 🛡️[ThirdParty](proofs/dummy-wallet/dummy-wallet-third-party-attestation.md#cc-support-transfers-and-holding-cc_support-verified-by-thirdparty) |
| &nbsp;&nbsp;&nbsp;&nbsp;Pre-approvals for CC | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#pre-approvals-for-cc-preapprovals) | [✅](proofs/dummy-wallet/dummy-wallet-self-attestation.md#pre-approvals-for-cc-preapprovals) |
| **Token Standard** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;CIP-0056 token standard transfer support | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#cip-0056-token-standard-transfer-support-cip_0056_transfer) | [✅](proofs/dummy-wallet/dummy-wallet-self-attestation.md#cip-0056-token-standard-transfer-support-cip_0056_transfer) |
| &nbsp;&nbsp;&nbsp;&nbsp;CIP-0056 token standard allocation support | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;CIP-112 token standard v2 support | — | ✅ |
| **Interoperability** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;CIP-0103 dApp API support | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#cip-0103-dapp-api-support-cip_0103_dapp_api) | [✅](proofs/dummy-wallet/dummy-wallet-self-attestation.md#cip-0103-dapp-api-support-cip_0103_dapp_api) |
| &nbsp;&nbsp;&nbsp;&nbsp;Wallet Connect support | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#wallet-connect-support-walletconnect_support) | [Not supported](wallets/dummy-wallet.yaml) |
| &nbsp;&nbsp;&nbsp;&nbsp;Memo tag support for transfers to exchanges | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#memo-tag-support-for-transfers-to-exchanges-memo_tag_support) | [✅](proofs/dummy-wallet/dummy-wallet-self-attestation.md#memo-tag-support-for-transfers-to-exchanges-memo_tag_support) |

## Other Features

| Feature | [Askardex Wallet](wallets/askardex-wallet.yaml) | [Dummy Wallet](wallets/dummy-wallet.yaml) |
|---|---|---|
| **App Specific** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Pre-approvals for DA Registry issued assets | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Wallet Gateway signing driver | — | — |
| **Party Specific** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Key generation method | Seed phrase (BIP-39 mnemonic, 24 words) | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Key recovery | ✅ | ✅ |
| &nbsp;&nbsp;&nbsp;&nbsp;Social recovery | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Multi-address / account | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Distributed parties | — | — |
| **Network relevant features** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;UTXO merge delegation contract enabled | — | — |
| **Transaction Signing** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Policy workflows | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Threshold Signature Scheme | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Hardware wallet support | — | ✅ |
| **Wallet Capabilities** |  |  |
| &nbsp;&nbsp;&nbsp;&nbsp;Compliance | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Validator hosting (self-hosted / BYOV) | ✅ | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Tokenization | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Reward minting | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#reward-minting-reward_minting) | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Transfer object / proof of transfer support | — | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Clear signing | [✅](proofs/askardex-wallet/askardex-wallet-self-attestation.md#clear-signing-clear_signing) | ✅ |
| &nbsp;&nbsp;&nbsp;&nbsp;Integrated swaps | [Not supported](wallets/askardex-wallet.yaml) | — |
| &nbsp;&nbsp;&nbsp;&nbsp;Assets supported | CC, USDCx (CIP-0056), CBTC (CIP-0056), CETH (CIP-0056), HANDL (CIP-0056) | CC, USDC (CIP-0056), Example Token (CIP-0056) |
| &nbsp;&nbsp;&nbsp;&nbsp;Languages supported | English | English, German |
