# Bleeding Ink — crawler decision record (not deployed)

**Status: AWAITING AUTHORIZED OWNER DECISION.** No `robots.txt` file is created or deployed by this package, because the studio has not chosen a policy. `crawlerPolicyApproved` remains `false` in `studio.json`.

## Questions to settle before publishing

1. Should the public studio website be eligible for Google Search and Google AI Search features? If yes, make Googlebot access and snippet/indexing settings intentional. The V3 **preview** still uses `<meta name="robots" content="noindex,nofollow">`.
2. Should OpenAI and Anthropic's **search** crawlers access public studio pages? Their vendor documentation identifies these as search-oriented bots, separate from the training crawlers.
3. Should OpenAI's GPTBot and Anthropic's ClaudeBot be allowed to collect material for potential model training? This is a separate choice. Do not infer it from answer visibility preferences.
4. Is there an existing hosting platform/CDN robots policy? Inspect it before making changes; multiple rules and host configurations can interact.

| Vendor | Search / user-directed fetching | Training/other | Decision |
|---|---|---|---|
| Google | Googlebot | Google-Extended has separate Gemini-related controls, including grounding; **not simply training-only** | PENDING |
| OpenAI | OAI-SearchBot; ChatGPT-User is user-initiated | GPTBot | PENDING |
| Anthropic | Claude-SearchBot and Claude-User | ClaudeBot | PENDING |
| Perplexity | PerplexityBot; Perplexity-User | No training-bot decision asserted here | PENDING |

**Important:** For a preview you intend to keep out of Search, use `noindex` and, ideally, access protection. Google warns that `robots.txt Disallow` can stop a crawler from seeing `noindex` and does not guarantee a page URL won't appear in search. Do not use robots.txt as access security.

## Documentation references (Google, OpenAI and Anthropic checked October 28, 2026; Perplexity link carried from the supplied research, not independently rechecked)

- Google Search indexing rules: https://developers.google.com/search/docs/crawling-indexing/block-indexing
- Google Search/AI guidance: https://developers.google.com/search/docs/appearance/ai-features
- OpenAI crawler documentation: https://developers.openai.com/api/docs/bots
- Anthropic robots guide: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Perplexity crawler documentation: https://docs.perplexity.ai/docs/resources/perplexity-crawlers

These are documented crawler roles and stated outcomes, not measurements of rank, visibility lift, or traffic. Review them again before an actual live change.

**Not included:** `robots.txt`, sitemap, `llms.txt`, FAQPage markup or JSON-LD. Creating them now would imply choices or facts that have not been approved.