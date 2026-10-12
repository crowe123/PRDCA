# Pool Removal California

A static referral-directory site built from the *Pool Removal California: Site Structure* plan (10 Oct 2026):
a state hub, 20 city pages, a cost guide, an FAQ and an About This Site page, plus a separate contact page for referral requests.

## Build

```
python3 build.py        # writes the site to public/
python3 -m http.server -d public 8000
```

No dependencies beyond the Python standard library. `netlify.toml` builds and publishes `public/`, and the contact form uses Netlify Forms.

## Where things live

| File | What it holds |
|---|---|
| `site_data.py` | Cities, permit facts, published prices, official source links, `SITE_URL`, `LINK_CONTRACTOR_SITES` |
| `build.py` | Page templates and copy for the homepage, city pages, cost guide, FAQ, about and contact pages |
| `data/businesses.csv` | Contractor listings (empty until filled from the workbook, see below) |
| `data/image_prompts.json` | Prompts for the kie.ai image generator |
| `scripts/generate_images.py` | Generates photos with kie.ai Nano Banana into `static/img/` |
| `static/` | CSS, images and the partial vs full removal SVG diagram |

## Contractor listings

Export the workbook's Businesses and By city tabs to `data/businesses.csv` with these columns:

`business, phone, website, base_city, licence_number, licence_status, licence_checked, status, site_says, cities`

- `status`: only rows marked `listed` are published. Hold back lead-gen, inactive-licence and unverified rows.
- `licence_status`: a value starting with `Current` counts as active, and those listings sort first.
- `cities`: city slugs separated by semicolons, for example `san-jose;fremont;oakland`.

City pages render contractor cards from this file. The page gets one ItemList JSON-LD block when it has listings, and no other schema, as the plan requires.

## Images

```
cp .env.example .env    # then add KIE_API_KEY
set -a; . ./.env; set +a
python3 scripts/generate_images.py              # missing images only
python3 scripts/generate_images.py home-hero    # regenerate one image
```

`.env` is gitignored, so the API key is never committed.

## Rules applied from the plan

- Titles, H1s, URLs (`/cost/`, `/faq/`, `/{city}/`) and meta descriptions follow the plan exactly.
- Each page has one bold opening answer line, with no call to action in the opening or fact sections.
- Only one H2 per page carries the full search phrase (on city pages, `{City} Pool Removal Permit Rules`).
- Outbound links sit inside the sentences that use them. No page has a sources section.
- Every page shows an About This Site referral disclosure, and the footer links every other page.
- No byline and no visible dates on the cost guide.
- Each page has 1 to 10 images, and city pages also embed a Google map.
- City-page FAQs use question subheadings only when the page reaches 1,500 words or more.
