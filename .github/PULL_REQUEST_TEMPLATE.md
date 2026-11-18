<!--
Thanks for contributing to the Wallet Directory Program. Fill in the
section(s) that apply and delete the rest. See CONTRIBUTING.md for the full
process.
-->

### Type of submission
<!-- check one -->
- [ ] New wallet application
- [ ] Update to an existing wallet's feature support
- [ ] Third-party verification (confirmed, or disputed as unsupported) of an existing claim
- [ ] Marking a feature as not supported, with a reason

### Summary

<!-- One or two sentences: what is this PR doing and why. -->

### Checklist

- [ ] `wallets/<wallet-name>.yaml` added or updated (self-attestation)
- [ ] A heading added to `proofs/<wallet-name>/<wallet-name>-self-attestation.md`
      for every feature newly claimed as `supported: true`
- [ ] `WALLET_DIRECTORY.md` is **not** changed in this PR. It is rebuilt
      automatically after merge (the CI check fails if it's included). To
      preview your change, download the `wallet-directory-preview` artifact
      from the PR's checks, or run
      `python3 scripts/generate_table.py --out WALLET_DIRECTORY.preview.md`
- [ ] If applying for the first time: confirmed membership in
      `#ext-temp-party-scaling` and set `slack_party_scaling_channel_joined: true`
- [ ] If marking a feature as not supported: reason filled in under that
      feature's `reason:` field, not just left blank
- [ ] If this is a verification: the heading added to
      `proofs/<wallet-name>/<wallet-name>-third-party-attestation.md`
      reflects evidence gathered independently, not copied from the
      wallet's self-attestation, and `result` on the matching
      `verified_by` entry is set to `verified` or `unsupported` to match

### Additional context

<!-- Anything reviewers should know: links, related Slack threads, etc. -->
