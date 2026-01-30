---
name: deal-finder
description: Find the best online deals for any product in the USA. Searches deal aggregators, trusted retailers, and promo code sites to return top deals with prices, URLs, and applicable coupons. Use when users ask to find deals, compare prices, search for discounts, find the best price, or look for promo codes/coupons.
---

# Deal Finder

Find the best product deals across trusted US retailers with applicable promo codes.

## Workflow

### Phase 1: Deal Aggregator Search (Start Here)

Search deal aggregator sites FIRST - they consolidate pricing across retailers:

```
Search: "[product name] slickdeals"
Search: "[product name] deal reddit"
Search: "[product name] price tracker"
```

These often reveal the best current deals and price history context.

### Phase 2: Direct Retailer Search

Search for the product at major retailers:

```
Search: "[product name] site:amazon.com"
Search: "[product name] site:walmart.com price"
Search: "[product name] site:target.com"
Search: "[product name] site:bestbuy.com"
Search: "[product name] [retailer from category list] price"
```

Identify the **product category** and search category-specific retailers from [references/trusted-retailers.md](references/trusted-retailers.md).

### Phase 3: Promo Code Search

Search for active promo codes at deal sites (NOT per-retailer):

```
Search: "[retailer] promo code [current month year]"
Search: "site:retailmenot.com [retailer] coupon"
Search: "site:slickdeals.net [retailer] promo code"
```

Check the Trusted Promo Code Sources in references for valid codes.

### Phase 4: Compile Results

For each deal found, gather:
- **Exact price** (not "around $X")
- **Direct product URL** (not search results page)
- **Seller type**: Official retailer vs third-party/marketplace seller
- **Stock status**: In-stock, low stock, or backordered
- **Shipping**: Free shipping threshold or cost
- **Applicable promo codes**: Code, discount amount, expiration

## Output Format

```markdown
## Best Deals for [Product Name]

*Prices as of [current date/time]*

### 1. [Retailer] - $XX.XX ⭐ BEST PRICE
   **URL:** [direct product link]
   **Seller:** [Official / Third-party marketplace]
   **Promo Code:** [CODE] - saves $X (expires [date]) OR "None found"
   **Shipping:** [Free / $X / Free over $XX]
   **Stock:** [In stock / Limited / Check availability]

### 2. [Retailer] - $XX.XX
   [same format]

### 3. [Retailer] - $XX.XX
   [same format]

---

## 💡 Recommendation

[Brief recommendation on best overall value considering price, shipping, promo codes, and seller reliability]

## ⚠️ Warnings (if applicable)

- [Third-party seller warnings]
- [Price unusually low - verify legitimacy]
- [Model variations to watch for]

## 💰 Additional Savings Tips

- [Credit card offers: e.g., Target RedCard 5% off]
- [Cashback: e.g., Rakuten cashback at this retailer]
- [Loyalty programs: e.g., Kohl's Cash]
```

## Rules

1. **Trusted retailers only**: Use [references/trusted-retailers.md](references/trusted-retailers.md)
2. **Flag marketplace sellers**: Clearly distinguish "Sold by Amazon" vs "Third-party on Amazon"
3. **Exact prices only**: No approximations like "around $80" - get exact price
4. **Verify availability**: Note if item is out of stock or backordered
5. **Include all costs**: Note shipping costs or free shipping thresholds
6. **Promo code quality**: Only include codes from trusted sources, note expiration
7. **Category awareness**: Check category-specific retailers (kitchen → Bed Bath, Williams Sonoma, etc.)
8. **Price context**: If you find price history (CamelCamelCamel, Keepa), note if current price is good/bad vs historical

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Price seems too low | Flag as potential third-party/grey market seller |
| Can't find exact product | Note model number differences clearly |
| Promo codes expired | Search for "[retailer] working promo code [current month]" |
| Multiple variants | Clarify which variant (color, size, generation) is priced |
