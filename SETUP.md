# withai.nyc GitHub Pages Setup

## 1. Create GitHub Repository - DONE

Repository created: https://github.com/btfinch/withai-landing

## 2. Enable GitHub Pages

1. Go to https://github.com/btfinch/withai-landing/settings/pages
2. Source: "Deploy from a branch"
3. Branch: `master`, folder: `/ (root)`
4. Save

## 3. Configure withai.nyc DNS

At your DNS provider, add these records:

| Type | Name | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | btfinch.github.io |

## 4. Finish GitHub Setup

1. In GitHub repo Settings > Pages
2. Custom domain: enter `withai.nyc`
3. Check "Enforce HTTPS" (after DNS propagates, ~24-48 hours)

The CNAME file already tells GitHub to serve at withai.nyc.
