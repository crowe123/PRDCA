# Pool Removal Directory CA

A static referral-directory site built from the *Pool Removal Directory CA: Site Structure* plan (10 Oct 2026):
a state hub, 32 city pages (the plan's 20 plus the fourth wave of cities 21 to 32), a cost guide, an FAQ and an About This Site page, plus a separate contact page for referral requests.

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

Listings come from the businesses workbook. After updating it, regenerate the CSV and rebuild:

```
pip install openpyxl
python3 scripts/import_workbook.py path/to/pool_removal_california_businesses.xlsx   # writes data/listings.csv
python3 build.py
```

`data/listings.csv` has one row per city and business (the By city tab), joined with licence details from the Businesses tab. The build publishes only rows marked **Licence active**:

- Rows marked *No licence number on site* or *Maps listing only* are held back until the phone check. Each city page shows how many are pending.
- Rows marked *Likely lead-gen site* or *Licence not active* never appear.
- Sites that share a licence number in the same city merge into one card ("Also trades as ...").
- Cards sort by listing basis: city named on the site, then region named, then Google Maps.

When you change a listing's status in the workbook (for example after a phone check), re-run the import. City pages get one ItemList JSON-LD block and no other schema, as the plan requires.

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
