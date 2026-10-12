#!/usr/bin/env python3
"""Build the Pool Removal California static site into public/.

    python3 build.py

No dependencies beyond the Python standard library. Page plan, titles, H1s and
rules come from the site structure document (10 October 2026).
"""
import csv
import html
import json
import re
import shutil
from pathlib import Path

from site_data import (CITIES, IMAGES, LINK_CONTRACTOR_SITES, PRICES, REGION_COST,
                       REGIONS, SITE_NAME, SITE_URL, SRC)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "public"
REGION_NAME = dict(REGIONS)
CITY_BY_SLUG = {c["slug"]: c for c in CITIES}
TOTAL_FOUND = 103  # businesses confirmed as offering in-ground pool removal (workbook)


def a(href, text):
    return f'<a href="{href}">{text}</a>'


def doc_link(c, text=None):
    return a(c["doc_url"], text or c["doc"])


def fill(s, c):
    return s.replace("{doc}", doc_link(c))


def img_tag(name, cls="", eager=False):
    path = ROOT / "static" / "img" / f"{name}.jpg"
    if not path.exists():
        return ""
    alt = html.escape(IMAGES[name])
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img src="/img/{name}.jpg" alt="{alt}" width="1600" height="900" '
            f'{load} decoding="async"{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}>')


def figure(name, caption):
    tag = img_tag(name)
    return f"<figure>{tag}<figcaption>{caption}</figcaption></figure>" if tag else ""


def diagram():
    return ('<figure><img src="/img/methods-diagram.svg" width="960" height="380" loading="lazy" '
            'alt="Diagram comparing a partial fill-in, where the shell stays with drainage holes and is limited to '
            'landscaping, with a full removal, where the shell is hauled away and compacted fill can be built on.">'
            '<figcaption>Partial fill-in against full removal. Hole sizes, spacing and how much wall comes off vary by '
            'city.</figcaption></figure>')


def cta(text, label="Request contractor referrals"):
    return f'<aside class="cta"><p>{text}</p><a class="btn" href="/contact/">{label}</a></aside>'


DISCLOSURE = (
    '<section class="disclosure" aria-labelledby="about-site"><h2 id="about-site">About This Site</h2>'
    f'<p>{SITE_NAME} is an independent referral directory. The site is not a contractor and does not remove pools. '
    'Listed businesses may pay a referral fee when a homeowner is put in touch with them through the site, and that '
    'fee never changes the listing order: contractors with an active state licence appear first. The '
    '<a href="/about/">full referral disclosure and listing criteria</a> explain how each business was checked.</p>'
    '</section>')


# ---------------------------------------------------------------- shell

def footer_links(current):
    cities = "".join(
        f'<li><a href="/{c["slug"]}/">{c["name"]}</a></li>' for c in CITIES if f'/{c["slug"]}/' != current)
    guides = [("/", "California pool removal directory"), ("/cost/", "Pool removal cost"),
              ("/faq/", "Pool fill-in questions"), ("/about/", "About This Site"),
              ("/contact/", "Request contractor referrals")]
    guide_items = "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in guides if u != current)
    return (
        '<footer class="site-footer"><div class="wrap"><div class="foot-grid">'
        f'<div><h2>Pool removal by city</h2><ul>{cities}</ul></div>'
        f'<div><h2>Guides</h2><ul style="columns:1">{guide_items}</ul></div>'
        '</div><p class="foot-note">Permit facts come from official city documents read on 10 October 2026, and '
        f'licence statuses from the <a href="{SRC["cslb_lookup"]}">Contractors State License Board</a> check of '
        f'11 October 2026. {SITE_NAME} is a referral directory, not a contractor.</p></div></footer>')


def page(path, title, description, body, crumbs=None, schema=None):
    crumb_html = ""
    if crumbs:
        parts = ['<a href="/">California</a>'] + [
            (a(u, t) if u else f'<span aria-current="page">{t}</span>') for u, t in crumbs]
        crumb_html = f'<nav class="crumbs wrap" aria-label="Breadcrumb">{" › ".join(parts)}</nav>'
    schema_html = (f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>'
                   if schema else "")
    doc = f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{SITE_URL}{path}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/styles.css">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE_URL}{path}">
<meta property="og:image" content="{SITE_URL}/img/home-hero.jpg">
{schema_html}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="logo" href="/">Pool Removal <span>California</span></a>
<nav class="nav" aria-label="Main">
<a href="/#cities">Cities</a><a href="/cost/">Costs</a><a href="/faq/">Fill-in questions</a><a href="/about/">About</a>
<a class="btn" href="/contact/">Get referrals</a>
</nav></div></header>
{crumb_html}
<main id="main" class="wrap">
{body}
</main>
{footer_links(path)}
</body>
</html>
"""
    dest = OUT / path.strip("/") / "index.html" if path != "/404.html" else OUT / "404.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(doc, encoding="utf-8")
    return doc


def word_count(fragment):
    text = re.sub(r"<[^>]+>", " ", fragment)
    return len(re.findall(r"[A-Za-z0-9$%][\w$%,.'-]*", text))


# ---------------------------------------------------------------- data

def load_businesses():
    path = ROOT / "data" / "businesses.csv"
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("business") or r.get("status", "").strip().lower() != "listed":
                continue
            r["city_slugs"] = [s.strip() for s in r.get("cities", "").split(";") if s.strip()]
            r["active"] = r.get("licence_status", "").strip().lower().startswith("current")
            rows.append(r)
    return rows


def contractor_card(b):
    name = html.escape(b["business"])
    if LINK_CONTRACTOR_SITES and b.get("website"):
        name = a(html.escape(b["website"]), name)
    lic = ""
    if b.get("licence_number"):
        lic = (f'<p>Licence {html.escape(b["licence_number"])}: <span class="{"licence-ok" if b["active"] else ""}">'
               f'{html.escape(b.get("licence_status", ""))}</span> at the state board, checked '
               f'{html.escape(b.get("licence_checked", ""))}.</p>')
    says = f'<p>{html.escape(b["site_says"])}</p>' if b.get("site_says") else ""
    return (f'<article class="card"><h3>{name}</h3><p>Based in {html.escape(b.get("base_city", ""))} · '
            f'{html.escape(b.get("phone", ""))}</p>{lic}{says}</article>')


# ---------------------------------------------------------------- city pages

def city_page(c, businesses):
    name, slug = c["name"], c["slug"]
    listed = sorted([b for b in businesses if slug in b["city_slugs"]],
                    key=lambda b: (not b["active"], b["business"].lower()))
    region = REGION_NAME[c["region"]]
    published = c["rules"] == "published"

    if published:
        opening = (f'<p class="lead"><strong>Pool removal in {name} needs a {c["permit"].lower()} from the city\'s '
                   f'{c["dept"]}, and research for this directory found {c["found"]} businesses offering in-ground '
                   f'pool removal there, {c["active"]} with an active state licence.</strong></p>')
    else:
        opening = (f'<p class="lead"><strong>Pool removal in {name} has no city handout of its own, so the '
                   f'{c["dept"]} confirms the permit, and research for this directory found {c["found"]} businesses '
                   f'offering in-ground pool removal there, {c["active"]} with an active state licence.</strong></p>')

    facts = (
        '<div class="facts">'
        f'<div class="fact"><b>{c["found"]}</b><span>businesses found for {name}</span></div>'
        f'<div class="fact"><b>{c["active"]}</b><span>with an active state licence</span></div>'
        f'<div class="fact"><b>{c["fee"].split(" (")[0] if c["fee"][0] == "$" else "See below"}</b>'
        f'<span>published permit fee</span></div>'
        f'<div class="fact"><b>{c["confidence"]}</b><span>confidence in published city rules</span></div>'
        '</div>')

    intro = (
        f'<p>This directory groups {name} under {region}. Each listing below was matched to {name} because the '
        'business names the city on its own website, serves it through a named region, or appears for it on Google '
        f'Maps. Licence numbers were checked at the <a href="{SRC["cslb_lookup"]}">Contractors State License Board '
        'lookup</a> on 11 October 2026, and businesses with an active licence are listed first.</p>')

    # Contractors section
    if listed:
        cards = "<div class=\"cards\">" + "".join(contractor_card(b) for b in listed) + "</div>"
    else:
        cards = (
            f'<div class="notice"><p>The {c["found"]} businesses found for {name} are being confirmed before their '
            'cards are published here. Every listing shows the business name, phone number, base city, licence number '
            'with its state board status and the date checked, and what its own site says about pool removal. '
            'Lead-generation sites are left off, and Google Maps-only firms appear only after a phone check.</p>'
            '<p>Homeowners can request referrals now through the contact page.</p></div>')
    note = f'<p>{c["note"]}</p>' if c.get("note") else ""
    contractors = (
        f'<h2>Contractors serving {name}</h2>{cards}{note}'
        f'<p>A contractor\'s licence classes matter on a pool job. {name} permits are generally issued to holders of '
        f'the A (general engineering), C-12 (earthwork and paving), C-21 (building moving and demolition) or C-53 '
        f'(swimming pool) classes described in the <a href="{SRC["cslb_classes"]}">state licence board\'s '
        'classification guide</a>, and the accepted classes differ from city to city. '
        f'<a href="{SRC["cslb_2407"]}">Industry Bulletin 24-07</a> confirms that the $1,000 unlicensed-work exemption '
        'does not cover work that needs a permit, so a pool removal always needs a licensed contractor or an '
        'owner-builder permit.</p>')

    # Permit section — the only subheading carrying the full search phrase
    permit_rows = (
        '<div class="table-wrap"><table><tbody>'
        f'<tr><th scope="row">Permit</th><td>{c["permit"]}</td></tr>'
        f'<tr><th scope="row">Issued by</th><td>{name} {c["dept"]}</td></tr>'
        f'<tr><th scope="row">Published fee</th><td>{c["fee"]}</td></tr>'
        f'<tr><th scope="row">City document</th><td>{doc_link(c, c["doc"][0].upper() + c["doc"][1:])}</td></tr>'
        f'<tr><th scope="row">Confidence</th><td>{c["confidence"]}</td></tr>'
        '</tbody></table></div>')
    permit = (
        f'<h2>{name} Pool Removal Permit Rules</h2><p>{fill(c["permit_html"], c)}</p>{permit_rows}'
        + ('' if published else
           f'<p>The {c["dept"]} is the office to call before any work starts. {name} is one of six cities among the '
           '20 in this directory that publish nothing specific to pools, so the department\'s answer on the phone '
           'decides the permit type, the fee and the fill standard.</p>')
        + '<p>Fees and requirements change at the start of each fiscal year, usually in July. The city document '
          'linked above is the record a contractor or inspector will work from.</p>')

    cost_key = c["cost"]
    cost = (
        f'<h2>Published prices for {region}</h2><p>{REGION_COST[cost_key]}</p>'
        '<p>Four things move a quote more than anything else: equipment access (about $2,000 more where the side yard '
        'is under 6 ft wide), deck removal ($500 to $1,700), fill dirt (80 to 150 cubic yards for a full removal) and '
        'the engineer\'s compaction report ($1,500 to $4,000). The <a href="/cost/">California pool removal cost '
        'guide</a> sets out every published price by region and pool type.</p>')

    methods = (
        f'<h2>Partial fill-in or full removal in {name}</h2><p>{fill(c["method_html"], c)}</p>{diagram()}'
        '<p>A partial fill-in breaks drainage holes through the floor, removes the top of the wall and fills the shell '
        'with soil. The method costs less and finishes faster, usually in one to four days, but most cities limit the '
        'area to landscaping afterwards. A full removal hauls away every piece of the shell and replaces it with fill '
        'compacted in layers to 90%, which takes three to seven days and is the route for anyone planning a structure '
        'over the old pool.</p>'
        + figure("full-removal" if c["rank"] % 2 else "partial-fill",
                 "Full removal leaves an open excavation ready for compacted fill." if c["rank"] % 2 else
                 "A partial fill-in breaks drainage holes through the pool floor before backfill."))

    draining = (
        '<p>Pool water has to go somewhere before demolition starts. '
        + ('Stockton and Riverside allow pool water to the sewer clean-out only, ' if c["slug"] in ("stockton", "riverside") else '')
        + f'The <a href="{SRC["sd_pools"]}">San Diego pools and spas fact sheet</a> and '
          f'<a href="{SRC["la_storm"]}">LA Stormwater</a> both allow the storm drain only for dechlorinated water '
          f'within a set pH range, and {name} contractors generally follow the same practice. The '
          f'{c["dept"]} confirms the local rule.</p>')

    nearby = (
        '<h2>Nearby areas</h2>'
        f'<p>Contractors listed for {name} also work in neighbouring communities, including '
        f'{", ".join(c["nearby"][:-1])} and {c["nearby"][-1]}. Neighbouring cities set their own permit rules, so a '
        f'job outside {name} city limits follows that city\'s building department or, in unincorporated areas, the '
        'county.</p>')
    region_links = [x for x in CITIES if x["region"] == c["region"] and x["slug"] != slug]
    if region_links:
        nearby += ("<p>Other " + region + " pages in this directory: "
                   + ", ".join(a(f'/{x["slug"]}/', x["name"]) for x in region_links) + ".</p>")

    map_html = (f'<figure><iframe class="map" title="Map of {name}, California" loading="lazy" '
                f'referrerpolicy="no-referrer-when-downgrade" '
                f'src="https://maps.google.com/maps?q={name.replace(" ", "+")},+CA&amp;z=11&amp;output=embed"></iframe>'
                f'<figcaption>{name}, California. Listings cover the city and named neighbouring areas.</figcaption>'
                '</figure>')

    after = (
        f'<p>Removing a pool can lower the assessed value of a {name} property. The '
        f'<a href="{SRC["boe_8609"]}">Board of Equalization\'s letter 86/09</a> treats removal of an improvement as a '
        'reason to reduce assessed value, but the reduction is tied to the pool\'s own assessed value, so an older '
        'pool may bring only a small change. Sellers should also expect the question on the state\'s '
        f'<a href="{SRC["dre_re6"]}">seller disclosure form</a>, which asks about fill on the property and about '
        'unpermitted work.</p>')

    def faq_block(heading_tag):
        items = ""
        for q, ans in c["faqs"]:
            ans = fill(ans, c)
            if heading_tag:
                items += f"<h3>{q}</h3><p>{ans}</p>"
            else:
                items += f"<p><strong>{q}</strong><br>{ans}</p>"
        return f'<h2>Common {name} questions</h2>{items}'

    hero = img_tag("permit-plans" if c["rank"] % 3 == 0 else ("home-hero" if c["rank"] % 3 == 1 else "debris-haul"),
                   "hero-img", eager=True)

    def assemble(faq_html):
        return (
            '<div class="content">'
            f'<h1>Pool Removal Contractors Working in {name}</h1>{opening}{facts}{intro}{hero}'
            + cta(f'Homeowners in {name} can ask for referrals to listed contractors who take pool removal work.')
            + contractors + permit + methods
            + cta(f'{name} referrals go to contractors with an active licence first.')
            + cost + draining + after + nearby + map_html + faq_html
            + cta('Ready to compare quotes? Referral requests take a couple of minutes.')
            + DISCLOSURE + '</div>')

    body = assemble(faq_block(False))
    # Question subheadings only on pages of 1,500 words or more.
    if word_count(body) >= 1500:
        body = assemble(faq_block(True))

    schema = None
    if listed:
        schema = {"@context": "https://schema.org", "@type": "ItemList",
                  "name": f"Pool removal contractors serving {name}",
                  "itemListElement": [
                      {"@type": "ListItem", "position": i + 1,
                       "item": {"@type": "LocalBusiness", "name": b["business"], "telephone": b.get("phone", ""),
                                "areaServed": f"{name}, CA"}}
                      for i, b in enumerate(listed)]}

    page(f"/{slug}/", f"Pool Removal {name}: Local Contractors and Permit Rules",
         f"Pool removal contractors serving {name}, with the city's permit rules, published fees and the choice "
         f"between partial fill-in and full removal.",
         body, crumbs=[(None, name)], schema=schema)
    return word_count(body)


# ---------------------------------------------------------------- homepage

def home():
    regions_html = '<div class="regions">'
    for key, label in REGIONS:
        links = "".join(f'<a href="/{c["slug"]}/">{c["name"]} <span>{c["found"]} found</span></a>'
                        for c in CITIES if c["region"] == key)
        regions_html += f'<div class="region"><h3>{label}</h3>{links}</div>'
    regions_html += "</div>"

    permit_rows = "".join(
        f'<tr><td>{a("/" + c["slug"] + "/", c["name"])}</td><td>{c["permit"]}</td><td>{c["fee"]}</td>'
        f'<td>{doc_link(c, c["doc"][0].upper() + c["doc"][1:])}</td></tr>'
        for c in CITIES if c["rules"] != "none")

    body = f"""<div class="content">
<h1>Pool Removal Contractors Across California's 20 Largest Cities</h1>
<p class="lead"><strong>{SITE_NAME} lists {TOTAL_FOUND} businesses confirmed as offering in-ground pool removal across California's 20 largest cities, and the <a href="{SRC["cslb_lookup"]}">Contractors State License Board</a> check of 11 October 2026 found 51 of the licence numbers they show current and active.</strong></p>
<p>Each city page pairs the local contractor list with that city's own permit rules, taken from official building department documents. Coverage is uneven: Bay Area cities have about 30 businesses each, while Fresno has 2, Bakersfield 5 and Riverside 6. The 20 cities are ranked by the <a href="{SRC["dof_e1"]}">California Department of Finance population estimate for 1 January 2026</a>.</p>
{img_tag("home-hero", "hero-img", eager=True)}
{cta("Homeowners can ask for referrals to listed contractors in any of the 20 cities.")}

<h2 id="cities">Contractor counts for 20 cities in six regions</h2>
<p>Every city page sits one click from here. The count beside each city is the number of businesses research found offering in-ground pool removal there; a business that serves several cities is counted under each. San Jose has the deepest list at 34, and Oakland and Fremont follow at 32 each.</p>
{regions_html}
{cta("Each referral request is matched to contractors who name the city on their own site.")}

<h2>Partial fill-in or full removal</h2>
<p>California cities allow two methods, and the choice decides what can be built on the land afterwards. A partial fill-in breaks holes through the bottom of the shell, removes the top of the wall and fills the rest with soil. The <a href="https://dbs.lacity.gov/sites/default/files/efs/forms/pc17/p-bc-2020-111-backfill-of-swimming-pools.pdf">Los Angeles backfill bulletin P/BC 2026-111</a> allows that only for landscaping use on ground sloping 10% or less. Long Beach goes further: its <a href="https://www.longbeach.gov/globalassets/lbcd/media-library/documents/building--safety/information-bulletins/ib-008">bulletin IB-008</a> requires a recorded covenant on the property when a shell stays.</p>
<p>A full removal hauls away the whole shell and replaces it with fill compacted to 90% and certified by an engineer. Stockton's <a href="https://www.stocktonca.gov/Documents/Business/Building%20%26%20Life%20Safety/Building%20Forms/BLDG-0014_SWIMMING%20POOL%20DEMOLITION%20REQUIREMENTS.pdf">form BLDG-0014</a> sets the two routes side by side as Option A and Option B, the clearest statement of the choice in any city document.</p>
{diagram()}

<h2>What pool removal costs in California</h2>
<p>California contractors publish higher prices than the national cost guides. Northern California firms quote $3,500 to $12,000 for a partial fill-in and $8,000 to $30,000 for full removal, according to published price lists from <a href="{SRC["souza"]}">Souza &amp; Son's</a>, <a href="{SRC["byebye"]}">Bye Bye Pool</a> and <a href="{SRC["walberg"]}">Walberg, Inc.</a> Los Angeles and Orange County firms start higher: <a href="{SRC["lapdc"]}">Los Angeles Pool Demolition Contractors</a> lists prices from $10,500 for a partial and $17,500 for a full removal. The <a href="/cost/">pool removal cost guide</a> lists every published price with its source.</p>
{figure("debris-haul", "Hauling broken concrete is a large part of a full removal's cost.")}
{cta("Comparing written quotes from licensed contractors is the surest way to price a specific pool.")}

<h2>Permit names and fees by city</h2>
<p>Every city that publishes a rule requires a permit, but the permit's name, the fee and what may stay in the ground all differ. Twelve of the 20 cities publish a pool-specific handout, two publish only a fee and six publish nothing specific. The table lists the 14 cities with a published rule or fee; the city pages cover the other six.</p>
<div class="table-wrap"><table><thead><tr><th>City</th><th>Permit</th><th>Published fee</th><th>City document</th></tr></thead><tbody>{permit_rows}</tbody></table></div>
<p>Fees for Fresno, Chula Vista, Fremont and Fontana come from older schedules, so a call to the city confirms the current amount.</p>

<h2>Licence checks behind each listing</h2>
<p>Listings come from each firm's own website, or its Google Maps listing where it has no site. Of the {TOTAL_FOUND} businesses, 54 show a California licence number, and the state board check found 51 of those current and active and 3 not active. Businesses with an inactive licence are held back. Another 33 show no number and go on a page only after a phone check, as do the 6 that exist only as Google Maps listings. Ten lead-generation sites that pass enquiries to unnamed contractors are left off entirely.</p>
<p>An active licence means the <a href="{SRC["cslb_lookup"]}">Contractors State License Board lookup</a> shows the licence as current and active on the date checked. The board's record also lists the licence classes and the workers' compensation policy, both worth a look before signing a contract. The <a href="/about/">listing criteria</a> give the full method.</p>

<h2>Common questions from homeowners</h2>
<p><strong>Does pool removal need a permit in California?</strong><br>Yes in every city whose handout was read: a grading permit in Los Angeles and Long Beach, a demolition permit in San Diego, Riverside and Fontana, and a building permit in San Jose, Irvine and Stockton.</p>
<p><strong>Can a house or ADU be built over a filled pool?</strong><br>Only where the shell was removed and the fill compacted to 90% and certified by an engineer, as the <a href="https://www.fontanaca.gov/DocumentCenter/View/48412/Demolition-of-Swimming-Pool-or-Spa-PDF">Fontana handout</a> states directly.</p>
<p><strong>How long does pool removal take?</strong><br>One to four days for a partial fill-in and three to seven for a full removal, with permits adding one to three weeks in most cities.</p>
<p><strong>Is there a rebate for removing a pool?</strong><br>No statewide programme exists. <a href="{SRC["valley_water"]}">Valley Water in Santa Clara County</a> pays $2 a square foot, up to $3,000, when a pool becomes low-water landscape.</p>
<p>The <a href="/faq/">pool fill-in questions page</a> answers a dozen more from city and state sources.</p>
{figure("after-landscape", "A former pool area planted as low-water landscape, the use most cities allow after a partial fill-in.")}
{cta("Referral requests go to licensed contractors in the homeowner's city.")}
{DISCLOSURE}
</div>"""
    page("/", "Pool Removal California: Contractors, Costs and Permits",
         "A directory of pool removal and demolition contractors across California's 20 largest cities, with local "
         "permit rules and published price ranges.", body)
    return word_count(body)


# ---------------------------------------------------------------- cost guide

def cost_page():
    rows = "".join(
        f'<tr><td>{a(p["url"], p["source"])}</td><td>{p["area"]}</td><td>{p["partial"]}</td><td>{p["full"]}</td>'
        f'<td>{p["published"]}</td></tr>' for p in PRICES)
    fee_rows = "".join(
        f'<tr><td>{a("/" + c["slug"] + "/", c["name"])}</td><td>{c["permit"]}</td><td>{c["fee"]}</td></tr>'
        for c in CITIES if c["fee"][0] == "$")

    body = f"""<div class="content">
<h1>Published Pool Removal Prices From California Contractors</h1>
<p class="lead"><strong>California contractors publish $3,500 to $12,000 for a partial fill-in and $8,000 to $30,000 for a full removal in Northern California, while <a href="{SRC["lapdc"]}">Los Angeles Pool Demolition Contractors</a> starts at $10,500 and $17,500 and <a href="{SRC["frisch"]}">Frisch &amp; Sons</a> quotes up to $30,000 or more in Orange County.</strong></p>
<p>Those contractor figures run well above the national cost guides. <a href="{SRC["homeadvisor"]}">HomeAdvisor</a>, <a href="{SRC["fixr"]}">Fixr</a> and <a href="{SRC["homeguide"]}">HomeGuide</a> average prices across the whole country, where labour, dump fees and permit costs are lower, so their numbers work best as a floor for California budgets. Every price on this page is attributed to the contractor or guide that published it.</p>
{img_tag("debris-haul", "hero-img", eager=True)}

<h2>California prices run above the national guides</h2>
<p>Three things push California prices up. Labour and equipment rates in the state's metro areas are among the highest in the country. Most California cities require engineering for a full removal, and a compaction report from a soils engineer adds $1,500 to $4,000. Dump fees for concrete and the cost of clean fill dirt are higher near the coast, where most pools are.</p>
<p>Prices also vary sharply within a region. San Diego's two published price lists disagree by a factor of three or more: <a href="{SRC["demodiego"]}">Demo Diego</a> quotes $9,000 to $15,000 for a full removal, while <a href="{SRC["villa"]}">Villa Demolition</a> quotes $45,000 to $60,000. The gap reflects different pool sizes, access and finish standards, which is why written quotes from more than one licensed contractor are the only reliable guide for a specific pool.</p>

<div class="table-wrap"><table><thead><tr><th>Source</th><th>Area</th><th>Partial fill-in</th><th>Full removal</th><th>Published</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>No source with local prices was found for the Central Valley or the Inland Empire. Owners in Fresno, Bakersfield, Stockton, Modesto, Riverside, San Bernardino and Fontana should start from the Northern California ranges and expect quotes to reflect local labour rates.</p>
{cta("Comparing two or three written quotes is the fastest way to place a pool inside these ranges.")}

<h2>Pool removal cost for a partial fill-in against a full removal</h2>
<p>A partial fill-in is the cheaper route. A crew breaks drainage holes through the floor, removes the top 12 inches to 2 feet of wall, drops the broken concrete into the shell and fills it with soil. <a href="{SRC["byebye"]}">Bye Bye Pool in Concord</a> quotes $3,500 to $7,000 for that work, and <a href="{SRC["souza"]}">Souza &amp; Son's</a> quotes $4,500 to $10,000 across the Bay Area. Most cities limit the area to landscaping afterwards, and some record the shell against the property.</p>
<p>A full removal hauls away the whole shell, then replaces it with fill compacted in layers to 90%. <a href="{SRC["walberg"]}">Walberg, Inc.</a> prices that at $12,000 to $30,000 for Northern California, and <a href="{SRC["angi"]}">Angi's Los Angeles figures</a> put the average at $6,816 within a range of $4,550 to $18,200. Full removal costs more in hauling, fill dirt and engineering, but it is the only route that keeps the land buildable for an accessory dwelling unit, an addition or a slab.</p>
{diagram()}
<p>City rules can narrow the gap between the two. Fresno's <a href="https://www.fresno.gov/wp-content/uploads/2023/02/SwimmingPoolAbandonment.pdf">pool abandonment bulletin</a> requires the entire bottom broken out and all backfill engineered to 90% compaction even when the walls stay, so a Fresno partial job carries most of the cost of a full removal. Riverside's <a href="https://riversideca.gov/cedd/sites/riversideca.gov.cedd/files/pdf/building/forms_handouts/inspections/2019/SWIMMING-POOL-DEMOLITION.pdf">pool demolition handout</a> likewise asks for an engineer's 90% compaction report.</p>

<h2>Prices by pool type</h2>
<p>Concrete and gunite pools, the most common type in California, cost the most to remove because the shell is thick, reinforced with rebar and heavy to haul. Every contractor price in the table above is for a concrete pool unless it says otherwise.</p>
<p>Fiberglass pools come out in fewer pieces. <a href="{SRC["norcal"]}">NorCal Earthworks in Sacramento</a> prices full removal at $6,000 to $12,000 for fiberglass against $8,000 to $15,000 for concrete. Vinyl liner pools, with steel or polymer walls and a sand or grout floor, usually sit between fiberglass and concrete because the walls are lighter but the fill volume is the same.</p>
<p>Above-ground pools are the cheapest. <a href="{SRC["angi"]}">Angi</a> puts removal at $300 to $3,500, with the top of the range reached when a deck surrounds the pool. Above-ground removal rarely needs a demolition or grading permit, though an electrical permit may apply where a dedicated circuit is removed.</p>
{figure("full-removal", "A full removal leaves an excavation of 80 to 150 cubic yards to refill.")}

<h2>Access, decking, fill and engineering move the price</h2>
<p>Equipment access is the largest single variable. Contractors add about $2,000 where the side yard is under 6 ft wide, because a smaller excavator or hand labour takes longer and the debris must be carried out in smaller loads. Some jobs need a fence panel removed and replaced, or a crane over the house where no side access exists.</p>
<p>Deck removal adds $500 to $1,700, depending on whether the deck is concrete, pavers or wood and how far it extends past the coping. Many owners keep part of the deck as a patio, which lowers the price and the hauling volume.</p>
<p>Fill dirt is the next large cost. A full removal takes 80 to 150 cubic yards of clean fill, delivered and placed in layers. Clean fill prices vary by county, and a full truckload holds roughly 10 to 14 cubic yards, so a typical full removal needs eight or more truckloads in addition to the loads hauling concrete out.</p>
<p>The compaction report from a soils engineer adds $1,500 to $4,000. San Diego requires a soils compaction report for any pool deeper than five feet under <a href="https://www.sandiego.gov/development-services/forms-publications/information-bulletins/710">Information Bulletin 710</a>, and Irvine requires a soils engineer to supervise the backfill under its <a href="https://cityofirvine.gov/building-permits-and-inspections/removing-single-family-residential-swimming-pool-or-spa">pool removal page</a>. A full removal without that report is rarely accepted as buildable ground.</p>
<p>Utilities make up a smaller line. The pump, filter, heater, lighting and gas lines must be disconnected and capped, which is why Santa Ana requires building, electrical and plumbing permits under <a href="https://santa-ana.gov/documents/abandoned-pools-bld-16/">handout BLD-16</a>.</p>
{figure("compaction", "Fill placed in layers and compacted to 90%, with the engineer's density test recorded for the report.")}
{cta("Listed contractors include permits, fill and compaction in their written quotes on request.")}

<h2>Permit fees by city</h2>
<p>Permit fees are a small share of the total but vary widely between cities. Stockton charges $97.25 for fiscal year 2026-27 under <a href="https://www.stocktonca.gov/Documents/Business/Building%20%26%20Life%20Safety/Building%20Forms/BLDG-0014_SWIMMING%20POOL%20DEMOLITION%20REQUIREMENTS.pdf">form BLDG-0014</a>, while San Diego charges $360.36 for plan check plus $332.48 for inspection. San Bernardino bases its fee on the cubic yards of fill, since it treats pool removal as on-site grading. San Jose takes a refundable debris deposit instead of a set pool fee.</p>
<div class="table-wrap"><table><thead><tr><th>City</th><th>Permit</th><th>Published fee</th></tr></thead><tbody>{fee_rows}</tbody></table></div>
<p>Los Angeles, Long Beach, Irvine, Santa Clarita and Santa Ana publish rules but no pool fee, and six cities publish nothing specific. The city pages link each city's own document. Fees for Fresno, Chula Vista, Fremont and Fontana come from older schedules and should be confirmed with the city before budgeting.</p>

<h2>Timeline from permit to finished grade</h2>
<p>A partial fill-in takes one to four days on site and a full removal three to seven, once the permit is in hand. Draining the pool adds a day or two, and must follow local discharge rules: the <a href="{SRC["sd_pools"]}">San Diego pools and spas fact sheet</a> and <a href="{SRC["la_storm"]}">LA Stormwater</a> allow the storm drain only for dechlorinated water within a set pH range, and Stockton and Riverside allow the sewer clean-out only.</p>
<p>Permits add one to three weeks in most cities. San Jose can issue in a single visit, and Fremont's express permit needs no plan review. Bay Area jobs also need an air district notice from the <a href="{SRC["baaqmd"]}">Bay Area Air Quality Management District</a> before demolition, and Oakland bars grading from 15 October to 15 April, so jobs there need to be booked for the dry season.</p>
{figure("draining", "Draining comes first, to the sewer clean-out or a storm drain where the city allows it.")}

<h2>Property tax and rebates after removal</h2>
<p>Removing a pool can lower a property's assessed value. The <a href="{SRC["boe_8609"]}">Board of Equalization's letter 86/09</a> treats removal of an improvement as a reason to reduce assessed value, and the board's <a href="{SRC["boe_newcon"]}">new construction guidance</a> covers how improvements are added and removed. The reduction is tied to the pool's own assessed value, so for a pool built decades ago it may be small. The <a href="{SRC["sd_assessor"]}">San Diego County Assessor</a> handles such changes through its realty assessment division; no county publishes a step-by-step process for reporting a removal.</p>
<p>One rebate was confirmed in California. <a href="{SRC["valley_water"]}">Valley Water in Santa Clara County</a> pays $2 a square foot, up to $3,000, when a pool becomes low-water landscape, and requires approval before work starts. No statewide programme was found.</p>

<h2>Regional price notes</h2>
<p>Los Angeles County prices start highest among published lists. <a href="{SRC["lapdc"]}">Los Angeles Pool Demolition Contractors</a> lists $10,500 and $17,500 as starting points, and Angi's Los Angeles range runs from $2,850 for the simplest partial job. Hillside lots in the county often need engineered compaction even for landscaping, which pushes jobs towards the top of the range.</p>
<p>Orange County has the highest published ceiling. <a href="{SRC["frisch"]}">Frisch &amp; Sons</a> quotes $12,000 to $20,000 for a partial and $18,000 to $30,000 or more for full removal, and many Orange County homes add homeowners association approval to the timeline.</p>
<p>San Diego County shows the widest spread, from Demo Diego's $9,000 full removal floor to Villa Demolition's $60,000 ceiling. The Bay Area clusters between $3,500 and $12,000 for a partial and $8,000 to $30,000 for full removal across Souza &amp; Son's, Bye Bye Pool and Walberg. Sacramento's one published list, from NorCal Earthworks, sits at $8,000 to $15,000 for a concrete full removal.</p>

<h2>Items a written quote should cover</h2>
<p>A written quote that lists each item makes two contractors' prices comparable. The scope line should name the method, partial fill-in or full removal, and how much of the wall and floor comes out. The permit line should say who pulls the permit, which permit it is and whether the fee is included. The fill line should give the cubic yards, the source of the fill and the compaction standard, normally 90%.</p>
<p>The engineering line should say whether a soils engineer's compaction report is included, and at what price. Disposal, deck removal, utility disconnection, fence panel removal and final grading each belong on their own line. The quote should also carry the contractor's licence number, which the <a href="{SRC["cslb_lookup"]}">state licence board lookup</a> confirms, and the workers' compensation policy where the firm has employees.</p>
<p>Payment terms matter too. California limits the down payment on a home improvement contract to 10% of the price or $1,000, whichever is less, and the contract should tie later payments to completed stages such as demolition, fill and final inspection.</p>
{figure("after-landscape", "Low-water landscape on a former pool site, the use that qualifies for the Valley Water rebate.")}
{cta("Referrals are free to request and go to licensed contractors first.")}
{DISCLOSURE}
</div>"""
    page("/cost/", "Pool Removal Cost in California: Partial Fill-In and Full Removal",
         "Published pool removal prices from California contractors, by region and pool type, with permit fees, "
         "timelines and what moves the price.", body, crumbs=[(None, "Pool removal cost")])
    return word_count(body)


# ---------------------------------------------------------------- FAQ

def faq_page():
    LA = "https://dbs.lacity.gov/sites/default/files/efs/forms/pc17/p-bc-2020-111-backfill-of-swimming-pools.pdf"
    LB = "https://www.longbeach.gov/globalassets/lbcd/media-library/documents/building--safety/information-bulletins/ib-008"
    FONTANA = "https://www.fontanaca.gov/DocumentCenter/View/48412/Demolition-of-Swimming-Pool-or-Spa-PDF"
    STOCKTON = CITY_BY_SLUG["stockton"]["doc_url"]
    SJ = CITY_BY_SLUG["san-jose"]["doc_url"]
    body = f"""<div class="content">
<h1>Pool Fill-In and Removal Questions Answered From City Rules</h1>
<p class="lead"><strong>Filling in a pool in California needs a city permit, and the rules differ: the <a href="{LA}">Los Angeles backfill bulletin</a> allows a shell to stay only for landscaping on gentle ground, while Stockton's <a href="{STOCKTON}">form BLDG-0014</a> sets out a $97.25 permit with two methods.</strong></p>
<p>Every answer below comes from a California city, county or state source, linked in the sentence that uses it. Where no California source exists, the answer says so.</p>
{img_tag("partial-fill", "hero-img", eager=True)}

<h2>Filling in a pool under California permit rules</h2>

<h3>Is a permit needed to remove a pool in California?</h3>
<p>Yes, in every city whose handout was read. Los Angeles and Long Beach use a grading permit; San Diego, Riverside and Fontana a demolition permit; and San Jose, Irvine and Stockton a building permit. The Los Angeles Department of Building and Safety sets its backfill rules in <a href="{LA}">bulletin P/BC 2026-111</a>, and San Diego's Development Services Department in <a href="https://www.sandiego.gov/development-services/forms-publications/information-bulletins/710">Information Bulletin 710</a>. San Francisco publishes no pool rule, but its <a href="https://codelibrary.amlegal.com/codes/san_francisco/latest/sf_building/0-0-0-92027">Building Code section 106A</a> requires a permit to remove any regulated structure.</p>

<h3>Who is licensed to remove a pool?</h3>
<p>Cities differ on the licence classes they accept. San Diego names the A and C-21 classes, Stockton names A, C-12 or C-53, and Fresno names C-12 or A. The <a href="{SRC["cslb_classes"]}">state licence board's classification guide</a> describes each class. Because the work needs a permit, the state's $1,000 unlicensed-work exemption does not apply, as <a href="{SRC["cslb_2407"]}">Industry Bulletin 24-07</a> explains. The board's own <a href="{SRC["cslb_quiz"]}">2016 newsletter quiz</a> named C-53, the swimming pool class, which conflicts with what several cities accept, so a call to the city settles it for a given job.</p>

<h3>Can a homeowner pull the permit?</h3>
<p>Yes in San Diego, Fresno and Stockton, where an owner-builder may apply; in Stockton that covers Option A, the partial fill-in. An owner-builder takes on the contractor's responsibilities, including the inspections and, where required, hiring the soils engineer.</p>

<h3>How can a contractor's licence be checked?</h3>
<p>The <a href="{SRC["cslb_lookup"]}">Contractors State License Board lookup</a> shows whether a licence is current and active, which classes it carries and whether a workers' compensation policy is on file. Every licence number on this directory was checked there on 11 October 2026.</p>
{figure("permit-plans", "Most cities want a simple site plan showing the pool and what the area becomes afterwards.")}

<h2>Methods and building afterwards</h2>

<h3>What is the cheapest way to remove a pool?</h3>
<p>A partial fill-in. The trade-off is that the area is limited to landscaping, and some cities record that against the property. The <a href="{LA}">Los Angeles bulletin</a> allows a shell to stay only for landscaping use on ground sloping 10% or less, and Long Beach's <a href="{LB}">bulletin IB-008</a> requires two 24-inch holes and a recorded covenant.</p>

<h3>Should a pool be filled in or removed fully?</h3>
<p>The answer turns on whether anything will be built there later. Stockton's <a href="{STOCKTON}">form BLDG-0014</a> sets out the choice most clearly: Option A leaves the shell with four holes and the top two feet removed, and Option B removes it with engineered fill. Option A suits a garden; Option B suits a future accessory dwelling unit, addition or slab.</p>
{diagram()}

<h3>Can a house be built over a filled-in pool?</h3>
<p>Only where the shell was removed and the fill was compacted to 90% and certified by an engineer. Fontana's <a href="{FONTANA}">pool demolition handout</a> and the Los Angeles bulletin say so directly. San Jose's <a href="{SJ}">pool demolition page</a> marks the area non-buildable unless an engineer certifies the compaction.</p>

<h3>How many holes go in the bottom of a filled pool?</h3>
<p>Between two and six or more, depending on the city. Long Beach requires two 24-inch holes, Stockton four, Santa Ana five 3-ft holes, and Fontana six 1-ft openings. Los Angeles asks for 12-inch holes every 8 ft and San Bernardino 12-inch holes every 6 ft. Fresno requires the entire bottom broken out.</p>

<h3>What fill goes into a pool?</h3>
<p>Broken concrete from the walls usually goes in the bottom on a partial fill-in, with clean soil above it. Garden Grove's 2026 bulletin adds 12 inches of rock under the soil. A full removal takes 80 to 150 cubic yards of clean fill, placed in layers and compacted to 90%.</p>
{figure("compaction", "Compaction to 90% is the standard most California cities set for buildable fill.")}


<h3>Can a pool be filled in with dirt alone?</h3>
<p>Not under most city rules. Filling a shell with dirt without breaking drainage holes through the bottom traps water in the old basin, which leads to soggy ground and settling. Every city handout read requires holes or removal of the bottom, and most require the top of the wall removed too: the top two feet in Stockton, San Bernardino and Fontana, and 12 inches below grade in Riverside.</p>

<h3>Is partial pool removal allowed in every California city?</h3>
<p>No. Ontario's <a href="https://ontarioca.gov/sites/default/files/Ontario-Files/Building/IB%20111%20%28demolition%20of%20swimming%20pool%20%26%20spa%20Requirements%29-eff%2010-16-2024.docx">bulletin IB 111</a> requires the entire shell removed, and Fresno requires the whole bottom broken out. Where partial removal is allowed, cities such as Los Angeles, Long Beach and Moreno Valley limit the area to landscaping or open space.</p>

<h3>What happens to the pool equipment and lines?</h3>
<p>The pump, filter, heater and lights are removed, and the electrical circuit, gas line and water lines are disconnected and capped. Santa Ana requires separate building, electrical and plumbing permits for that reason under <a href="https://santa-ana.gov/documents/abandoned-pools-bld-16/">handout BLD-16</a>.</p>

<h3>What inspections does a pool removal need?</h3>
<p>Most cities inspect at least twice: once after the holes are broken or the shell is removed and before fill goes in, and once at final grade. Cities that require an engineer's compaction report, such as Riverside and Huntington Beach, also need that report before final sign-off. Fremont's express permit is inspection only, with no plan review.</p>

<h3>Do homeowners associations have a say?</h3>
<p>Often, yes. Many Orange County and Inland Empire subdivisions require association approval for changes to the yard, and Irvine's <a href="https://cityofirvine.gov/building-permits-and-inspections/removing-single-family-residential-swimming-pool-or-spa">pool removal page</a> asks the owner to state the area's new use on the plans. Association approval is separate from the city permit.</p>

<h3>Does the air district need notice?</h3>
<p>In the Bay Area, yes. San Jose's <a href="{SJ}">pool demolition page</a> requires a job number from the <a href="{SRC["baaqmd"]}">Bay Area Air Quality Management District</a> before demolition starts, and Lancaster requires an air district demolition notice as well.</p>

<h2>Cost and timing</h2>

<h3>What does pool removal cost in California?</h3>
<p>California contractors publish $3,500 to $12,000 for a partial fill-in and $8,000 to $30,000 for a full removal in Northern California, and Los Angeles firms start at $10,500 and $17,500. The <a href="/cost/">pool removal cost guide</a> lists every published price with its source.</p>

<h3>What does above-ground pool removal cost?</h3>
<p>$300 to $3,500, depending on decking, according to <a href="{SRC["angi"]}">Angi</a>. Above-ground pools rarely need a demolition or grading permit.</p>

<h3>How long does pool removal take?</h3>
<p>One to four days for a partial fill-in and three to seven for a full removal. Permits add one to three weeks in most cities; San Jose's <a href="{SJ}">permit center</a> can issue in one visit. Oakland bars grading from 15 October to 15 April.</p>
{cta("Listed contractors can quote both methods so the two can be compared side by side.")}

<h2>Water, tax and selling</h2>

<h3>Where can the pool water be drained?</h3>
<p>The rule varies by city. Stockton and Riverside allow the sewer clean-out only. San Diego and Los Angeles allow the storm drain if the water is dechlorinated and within a set pH range, as the <a href="{SRC["sd_pools"]}">San Diego pools and spas fact sheet</a> and <a href="{SRC["la_storm"]}">LA Stormwater's guidance for pool owners</a> explain.</p>
{figure("draining", "Pool water must be drained to the sewer clean-out or, where allowed, dechlorinated before it reaches a storm drain.")}

<h3>Does removing a pool lower property tax in California?</h3>
<p>Possibly, by a small amount. The <a href="{SRC["boe_8609"]}">Board of Equalization's letter 86/09</a> treats removal of an improvement as a reason to reduce assessed value, but the reduction is tied to the pool's own assessed value, so it may be small for an old pool. The <a href="{SRC["sd_assessor"]}">San Diego County Assessor</a> handles realty changes, though no county publishes how an owner reports a pool removal.</p>

<h3>Does a removed pool have to be disclosed on sale?</h3>
<p>The state's seller disclosure form asks about fill on the property and about unpermitted work, as the Department of Real Estate's <a href="{SRC["dre_re6"]}">disclosure booklet RE 6</a> shows. Long Beach and Santa Clarita also put a record on the property when the shell stays, so a permitted job with a final inspection is the cleanest history to hand a buyer.</p>

<h3>Are there rebates for removing a pool?</h3>
<p>No statewide programme was found. <a href="{SRC["valley_water"]}">Valley Water in Santa Clara County</a> pays $2 a square foot, up to $3,000, when a pool becomes low-water landscape, and requires approval before work starts.</p>

<h3>Does removing a pool decrease home value?</h3>
<p>No California source measures it. Buyers' preferences vary by area and by the age and condition of the pool, and a local real estate agent is the best guide for a specific property.</p>

<h3>Do unincorporated areas follow city rules?</h3>
<p>No. Homes outside city limits follow the county. <a href="{SRC["oc_pw"]}">Orange County Public Works</a>, for example, publishes its own pool demolition requirements for unincorporated Orange County.</p>
{cta("Referral requests go to licensed contractors who know the local permit rules.")}
{DISCLOSURE}
</div>"""
    page("/faq/", "Filling In a Pool in California: Permits, Methods and Questions",
         "Answers on filling in or removing a pool in California, from city permit rules, the state licence board "
         "and county sources.", body, crumbs=[(None, "Pool fill-in questions")])
    return word_count(body)


# ---------------------------------------------------------------- about / contact / 404

def about_page():
    body = f"""<div class="content">
<h1>About This Site: Referral Disclosure and Listing Criteria</h1>
<p class="lead"><strong>{SITE_NAME} is an independent referral directory of businesses that remove in-ground pools in California's 20 largest cities; it is not a contractor and does not perform any work.</strong></p>

<h2>Referral disclosure</h2>
<p>The site makes money through referrals. When a homeowner asks for referrals through the <a href="/contact/">contact page</a>, the request goes to one or more listed contractors, and a contractor may pay {SITE_NAME} a fee for that introduction. Homeowners pay nothing to the site. Referral fees never change the order of listings or which businesses appear; the order is set by licence status. {SITE_NAME} offers no free inspections, giveaways or discounts, and makes no promise about any contractor's price or work. Homeowners should check every contractor's licence and insurance and get the scope, price and permit responsibility in a written contract.</p>

<h2>How businesses are found</h2>
<p>Research for the directory started from Google Maps listings and organic search results for pool removal and pool demolition in each city, then read each business's own website. A business is listed under a city when its site names the city, serves it through a named region, or appears for it on Google Maps. A business that serves several cities is listed under each. Where at least four operators were found running two or three sites each, those sites are merged into a single listing.</p>

<h2>How listings are checked</h2>
<p>Every licence number found on a business's website was checked at the <a href="{SRC["cslb_lookup"]}">Contractors State License Board</a> on 11 October 2026, along with the name on the licence, its classes and its workers' compensation record. A listing shows the licence number, its status and the date checked.</p>
<p>Businesses with an active licence are listed first. Businesses whose licence is not active are held back. Businesses that show no licence number, and firms that exist only as Google Maps listings, are added only after a phone check. Lead-generation sites, which pass enquiries to unnamed contractors, are left off, and the evidence for each is kept on file.</p>

<h2>Permit and price facts</h2>
<p>Permit facts come only from official city documents, read on 10 October 2026 and linked on each city page. Where a city publishes no pool rule, the city page says so and names the department to call. Prices come only from contractors and cost guides that publish them, each linked in the sentence that uses it; the site does not invent local figures.</p>

<h2>Corrections</h2>
<p>Contractors and city staff can ask for a correction through the <a href="/contact/">contact page</a>. Licence statuses are re-checked before each page is updated.</p>
</div>"""
    page("/about/", "About This Site: Referral Disclosure and Listing Criteria",
         "How Pool Removal California finds and checks pool removal contractors, and how referrals work.",
         body, crumbs=[(None, "About This Site")])


def contact_page():
    options = "".join(f'<option value="{c["slug"]}">{c["name"]}</option>' for c in sorted(CITIES, key=lambda c: c["name"]))
    body = f"""<div class="content">
<h1>Request Pool Removal Contractor Referrals</h1>
<p class="lead">Referral requests go to listed contractors serving the city named below, with active-licence contractors first. Requests are free; contractors may pay {SITE_NAME} a referral fee, as the <a href="/about/">referral disclosure</a> explains.</p>
<form class="quote" name="referral" method="POST" action="/thanks/" data-netlify="true" netlify-honeypot="company">
<input type="hidden" name="form-name" value="referral">
<p hidden><label>Leave blank <input name="company"></label></p>
<label>Name<input name="name" required autocomplete="name"></label>
<label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
<label>Email<input name="email" type="email" autocomplete="email"></label>
<label>City<select name="city" required><option value="">Choose a city</option>{options}<option value="other">Other California city</option></select></label>
<label>Pool type<select name="pool_type"><option>Concrete or gunite</option><option>Fiberglass</option><option>Vinyl liner</option><option>Above-ground</option><option>Not sure</option></select></label>
<label>Method<select name="method"><option>Not sure yet</option><option>Partial fill-in</option><option>Full removal</option></select></label>
<label>Anything else contractors should know<textarea name="notes" rows="4" placeholder="Access width, deck, plans for the area afterwards"></textarea></label>
<button class="btn" type="submit">Send referral request</button>
</form>
{DISCLOSURE}
</div>"""
    page("/contact/", "Request Pool Removal Contractor Referrals in California",
         "Ask for referrals to licensed pool removal contractors in California's 20 largest cities.",
         body, crumbs=[(None, "Request referrals")])
    thanks = ('<div class="content"><h1>Referral Request Received</h1><p>Listed contractors serving the chosen city '
              'will be in touch by phone or email. The <a href="/cost/">cost guide</a> and '
              '<a href="/faq/">fill-in questions</a> help when comparing quotes.</p></div>')
    page("/thanks/", "Referral Request Received", "Referral request received.", thanks)


def not_found():
    body = ('<div class="content"><h1>Page Not Found</h1><p>The page may have moved. The '
            '<a href="/">California pool removal directory</a> links every city page.</p></div>')
    page("/404.html", "Page Not Found | Pool Removal California", "Page not found.", body)


def sitemap():
    paths = ["/"] + [f'/{c["slug"]}/' for c in CITIES] + ["/cost/", "/faq/", "/about/", "/contact/"]
    urls = "".join(f"<url><loc>{SITE_URL}{p}</loc></url>" for p in paths)
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (OUT / "robots.txt").write_text(f"User-agent: *\nDisallow: /thanks/\nSitemap: {SITE_URL}/sitemap.xml\n")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copy(ROOT / "static" / "styles.css", OUT / "styles.css")
    shutil.copytree(ROOT / "static" / "img", OUT / "img")
    (OUT / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#12372a"/>'
        '<path d="M6 20c3 0 3 2 6 2s3-2 6-2 3 2 6 2 2-1 2-1" stroke="#8fe0b8" stroke-width="2.5" fill="none"/>'
        '<path d="M8 10h16" stroke="#fff" stroke-width="2.5"/></svg>')

    businesses = load_businesses()
    counts = {"/": home(), "/cost/": cost_page(), "/faq/": faq_page()}
    for c in CITIES:
        counts[f'/{c["slug"]}/'] = city_page(c, businesses)
    about_page()
    contact_page()
    not_found()
    sitemap()
    for p, n in counts.items():
        print(f"{n:>5} words  {p}")
    print(f"Built {len(list(OUT.rglob('index.html')))} pages into {OUT}")


if __name__ == "__main__":
    main()
