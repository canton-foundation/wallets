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
- [ ] `python scripts/generate_table.py` was run and the regenerated
      `WALLET_DIRECTORY.md` is included in this PR (a CI check will catch
      this if it's missed, but running it locally saves a round trip)
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
