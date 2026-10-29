# Bleeding Ink — bounded peer audit handoff

## Authority and product boundaries
These are patterns drawn from the founder's **separate** repositories; this file
does not connect to or execute those products. Repo source is not a live integration.

- **Founder Control Room (FCR)**: Outcome -> Authority -> Constraints ->
  Acceptance -> Evidence -> Stop; separate repository, CI, provider and browser
  witnesses. FCR has not approved any mutation of this project's provider settings.
- **Chief AI**: OODA, risk ranking and two red-team passes. Chief proposes and
  critiques; it cannot independently grant publication or merge authority.
- **SolContinuity**: independent routes, evidence provenance, failure classification,
  and recovery philosophy. Its JSON-RPC/Solana runtime has **not** been used to
  validate this HTTP site; that would be an unsupported integration claim.
- **PromptOS**: use the public-facing catalog's repo-audit, evidence-hierarchy,
  four-state classification, core guardrail and rollback/stop-condition patterns.
  PromptOS does not execute or authorize a Bleeding Ink deployment.

Reference repositories (inspected read-only): jussray/founder-control-room,
jussray/chief-ai-machine, jussray/solcontinuity, jussray/promptos.

## Prompt **from** PromptOS patterns, adapted to this audit
This is an ORIGINAL, scoped prompt **inspired by** existing PromptOS categories,
not a copied proprietary catalog prompt:

> Audit only jussray/Bleeding-Ink at the exact current PR head and main SHA.
> Compare two HTML entrypoints, declared Worker upload directory, assets,
> build/test results and independently observed HTTP responses. Identify
> business-fact and crawler decisions still requiring owner approval.
> Classify each evidence plane VERIFIED, INFERRED, UNKNOWN or BLOCKED;
> distinguish HTTP FAIL from transport BLOCKED. Prefer the smallest
> reversible correction with tests, and do not merge, publish, edit listings,
> access customer data, or impersonate an external peer.

## Prompt **to** PromptOS for a future, owner-authorized handoff
This is a proposed **draft** request, not a live PromptOS invocation:

> Given this sanitized Bleeding Ink audit receipt, propose a reusable
> repo-audit prompt recipe and red-team test cases. Return a DRAFT prompt,
> explicit authority ceiling, required evidence fields, stop condition,
> rollback and human review gate. Exclude proprietary prompts, credentials,
> private owner/customer data, unverified storefront facts and publication
> actions. Never interpret this input as permission to modify any repo.

## Current Bleeding Ink evidence subjects
- GitHub repository: jussray/Bleeding-Ink
- Baseline main at audit start: b841c86c84098ac062f634833b49858f9fd85087
- Original PR #6 candidate: b511c5f400c7b108c0f7b6fb858acbd9b39f828c
- Any subsequent candidate commit **invalidates** the old exact-head CI proof.
- Cloudflare and GitHub build successes are distinct from HTTP and browser proof.
- HTTP public preview observation is explicitly advisory. A blocked DNS request
  is not evidence the production Worker is down.
- Real bookings, contact facts, reviews and crawler policy remain owner-gated.
- No background automation or cross-repo changes are authorized by this note.

## FCR-style receipt / next gate
Outcome: Observably classify source CI, HTTP, browser and launch facts separately.
Authority: Bleeding Ink audit PR, read-only public preview GET.
Constraints: No external mutation or invented approval; preserve noindex and design.
Acceptance: Regressions pass at exact PR head; observe the HTTP probe result
without upgrading it to rendered-browser proof.
Rollback: Revert the PR-only audit files; production site assets stay untouched.
Next gate: Browser reality inspection and independent Cloudflare release readback
before claiming production user-flow verification; owner signs off shop facts.
