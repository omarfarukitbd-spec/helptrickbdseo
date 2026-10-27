# schema/ — Schema.org JSON-LD starter templates

Minimal, opinionated starter blocks for the most common Schema.org types.
Copy the relevant `.json` file into your page as a `<script type="application/ld+json">` block, then adapt the placeholder values to your real entity.

| File | Type | Use on |
|---|---|---|
| `organization.json` | `Organization` | Every page (or just the homepage if you'd rather centralise) |
| `local-business.json` | `LocalBusiness` | Pages of a business with a physical location |
| `article.json` | `Article` | Blog posts / news / editorial content |
| `product.json` | `Product` | E-commerce product pages |
| `website.json` | `WebSite` (with SearchAction) | Homepage only |
| `person.json` | `Person` | Author bio / team-member pages |
| `breadcrumb.json` | `BreadcrumbList` | Every non-home page |

## Why these and not others

The audit pipeline (`scripts/checks/schema.py`) flags missing schemas per page kind. The seven templates here cover the core types it expects. For more exotic types (Event, Recipe, Course, etc.) refer to https://schema.org directly — these starters are a baseline, not an exhaustive catalogue.

## Reminder — visible-facts coverage

Per the Enhanced Entity Pages methodology (see `docs/STRUCTURED_DATA_BEST_PRACTICES.md`), the facts you declare in JSON-LD should **also appear in the visible body** of the page. Don't drop a `priceRange: "€€"` into JSON-LD if your page never says "€€" anywhere a human can read. The audit measures this overlap (`EE1` finding) and targets ≥ 70%.
