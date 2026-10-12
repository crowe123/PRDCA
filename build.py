#!/usr/bin/env python3
"""Build the Pool Removal California static site into public/.

    python3 build.py

No dependencies beyond the Python standard library. Page plan, titles, H1s and
rules come from the site structure document (10 October 2026).
"""
import csv
import datetime
import html
import json
import re
import shutil
from pathlib import Path

from site_data import (CITIES, LINK_CONTRACTOR_SITES, PRICES, REGION_COST,
                       REGIONS, SITE_NAME, SITE_URL, SRC,
                       BUSINESS_ADDRESS, BUSINESS_PHONE, BUSINESS_PHONE_TEL)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "public"
REGION_NAME = dict(REGIONS)
ALT = {k: v.get("alt", "") for k, v in json.loads((ROOT / "data" / "image_prompts.json").read_text()).items()}
CITY_BY_SLUG = {c["slug"]: c for c in CITIES}
N = len(CITIES)
NO_RULE_COUNT = sum(c["rules"] == "none" for c in CITIES)
HANDOUT_COUNT = sum(c["rules"] == "published" for c in CITIES)
FEE_ONLY_COUNT = sum(c["rules"] == "fee-only" for c in CITIES)
TOTAL_FOUND = 103  # businesses confirmed as offering in-ground pool removal (workbook)
FORMSPREE_URL = "https://formspree.io/f/mwlvnaqn"  # referral form endpoint


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
    alt = html.escape(ALT.get(name, ""))
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

CONTENT_PAGES = ["/"] + [f'/{c["slug"]}/' for c in CITIES] + ["/cost/", "/faq/", "/about/"]


def menu_link(href, text, current):
    if href == current:
        return f'<span aria-current="page">{text}</span>'
    return f'<a href="{href}">{text}</a>'


def header_nav(current):
    """Header menu linking every content page: 32 cities, cost guide, FAQ and About (the logo links home)."""
    regions = ""
    for key, label in REGIONS:
        links = "".join(f'<li>{menu_link("/" + c["slug"] + "/", c["name"], current)}</li>'
                        for c in CITIES if c["region"] == key)
        regions += f'<div class="mega-region"><p>{label}</p><ul>{links}</ul></div>'
    guides = "".join(menu_link(u, t, current) for u, t in
                     [("/cost/", "Costs"), ("/faq/", "Fill-in questions"), ("/about/", "About")])
    cta = "" if current == "/contact/" else '<a class="btn" href="/contact/">Get referrals</a>'
    return (
        '<nav class="nav" aria-label="Main">'
        '<details class="menu"><summary>Cities</summary>'
        f'<div class="mega"><div class="mega-grid">{regions}</div></div></details>'
        f'{guides}{cta}'
        f'<a class="btn phone-btn" href="tel:{BUSINESS_PHONE_TEL}" data-track-call="{SITE_NAME}">{BUSINESS_PHONE}</a>'
        '</nav>')


FOOTER = (
    '<footer class="site-footer"><div class="wrap">'
    f'<p class="foot-contact"><strong>{SITE_NAME}</strong><br>{BUSINESS_ADDRESS}<br>'
    f'<a href="tel:{BUSINESS_PHONE_TEL}" data-track-call="{SITE_NAME}">{BUSINESS_PHONE}</a></p>'
    '<p class="foot-note">Permit facts come from official city documents '
    f'read on 10 October 2026, and licence statuses from the <a href="{SRC["cslb_lookup"]}">Contractors State License '
    f'Board</a> check of 11 October 2026. {SITE_NAME} is a referral directory, not a contractor. '
    '<a href="/about/">Referral disclosure</a>.</p></div></footer>')


def page(path, title, description, body, crumbs=None, schema=None, index=True, city=""):
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
{"" if index else '<meta name="robots" content="noindex">'}
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
<body data-city="{html.escape(city)}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="logo" href="/">Pool Removal <span>California</span></a>
{header_nav(path)}
</div></header>
{crumb_html}
<main id="main" class="wrap">
{body}
</main>
{FOOTER}
<script>document.addEventListener("click",e=>{{const m=document.querySelector(".menu");if(m&&m.open&&!m.contains(e.target))m.open=false}});document.addEventListener("keydown",e=>{{if(e.key==="Escape")document.querySelector(".menu")?.removeAttribute("open")}});</script>
<script src="/track.js" defer></script>
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

BASIS = {
    "City named on its site": "its own website names {city}",
    "Region named on its site": "its website names the region {city} sits in",
    "Google Maps result for this city": "Google Maps lists it for pool removal in {city}",
}
BASIS_ORDER = list(BASIS)


def load_listings():
    """Rows from data/listings.csv (scripts/import_workbook.py), grouped by city slug.

    Only businesses whose licence was current and active at the state board are
    published. Sites sharing one licence number in the same city merge into one card.
    """
    slug_by_name = {c["name"]: c["slug"] for c in CITIES}
    by_city, held = {}, {}
    with (ROOT / "data" / "listings.csv").open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            slug = slug_by_name.get(r["city"])
            if not slug:
                continue
            if r["status"] != "Licence active":
                if r["status"] in ("No licence number on site", "Maps listing only, no website"):
                    held[slug] = held.get(slug, 0) + 1
                continue
            cards = by_city.setdefault(slug, {})
            key = r["licence_number"] or r["business"]
            if key in cards:
                card = cards[key]
                card["aliases"].append(r["business"])
                if BASIS_ORDER.index(r["basis"]) < BASIS_ORDER.index(card["basis"]):
                    card["basis"] = r["basis"]
            else:
                cards[key] = dict(r, aliases=[])
    listed = {slug: sorted(cards.values(), key=lambda b: (BASIS_ORDER.index(b["basis"]), b["business"].lower()))
              for slug, cards in by_city.items()}
    return listed, held


def contractor_card(b, city):
    name = html.escape(b["business"])
    if LINK_CONTRACTOR_SITES and b.get("website"):
        name = a(html.escape(b["website"]), name)
    aka = ""
    if b["aliases"]:
        aka = f'<p>Also trades as {html.escape(", ".join(b["aliases"]))}, under the same licence.</p>'
    classes = f' ({html.escape(b["classifications"])})' if b["classifications"] else ""
    lic = (f'<p>Licence {html.escape(b["licence_number"])}{classes}, held by {html.escape(b["licence_name"])}: '
           f'<span class="licence-ok">{html.escape(b["licence_status"].lower())}</span> at the state board, '
           'checked 11 October 2026.</p>')
    offer = ("Its website has a dedicated pool removal page or section."
             if b["clarity"].startswith("Dedicated") else "Its website lists pool removal among its services.")
    says = b["site_says"].strip()
    quote = ""
    if len(says) > 60 and says[0].isupper() and " " in says and "|" not in says:
        quote = f' The site says: &ldquo;{html.escape(says.rstrip(". "))}.&rdquo;'
    basis = BASIS.get(b["basis"], "").format(city=city)
    return (f'<article class="card"><h3>{name}</h3>'
            f'<p>Based in {html.escape(re.sub(r"\s*\(.*\)$", "", b["base_city"]))}</p>{lic}{aka}'
            f'<p>{offer}{quote} Listed for {city} because {basis}.</p></article>')


# ---------------------------------------------------------------- city pages

def city_page(c, listings, held):
    name, slug = c["name"], c["slug"]
    listed = listings.get(slug, [])
    held_n = held.get(slug, 0)
    region = REGION_NAME[c["region"]]
    published = c["rules"] == "published"

    if published:
        opening = (f'<p class="lead"><strong>Pool removal in {name} needs a {c["permit"].lower()} from the city\'s '
                   f'{c["dept"]}, and {SITE_NAME} found {c["found"]} businesses offering in-ground '
                   f'pool removal there, {c["active"]} with an active state licence.{c.get("opening_extra", "")}</strong></p>')
    else:
        opening = (f'<p class="lead"><strong>Pool removal in {name} has no city handout of its own, so the '
                   f'{c["dept"]} confirms the permit, and {SITE_NAME} found {c["found"]} businesses '
                   f'offering in-ground pool removal there, {c["active"]} with an active state licence.{c.get("opening_extra", "")}</strong></p>')

    if c.get("lead"):
        opening = ('<p class="lead"><strong>'
                   + fill(c["lead"], c).replace("{found}", str(c["found"])).replace("{active}", str(c["active"]))
                   + '</strong></p>')

    facts = (
        '<div class="facts">'
        f'<div class="fact"><b>{c["found"]}</b><span>businesses found for {name}</span></div>'
        f'<div class="fact"><b>{c["active"]}</b><span>with an active state licence</span></div>'
        f'<div class="fact"><b>{c.get("fee_short") or (c["fee"].split(" (")[0] if c["fee"][0] == "$" else ("Not published" if c["fee"].startswith("Not published") else "See below"))}</b>'
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
        cards = "<div class=\"cards\">" + "".join(contractor_card(b, name) for b in listed) + "</div>"
        if held_n:
            cards += (f'<p>Another {held_n} {"business shows" if held_n == 1 else "businesses show"} no licence '
                      f'number or only a Google Maps listing for {name}. '
                      f'{"It is" if held_n == 1 else "They are"} being checked by phone before being listed.</p>')
    else:
        cards = (
            f'<div class="notice"><p>The {c["found"]} businesses found for {name} are being confirmed before their '
            'cards are published here. Every listing shows the business name, phone number, base city, licence number '
            'with its state board status and the date checked, and what its own site says about pool removal. '
            'Lead-generation sites are left off, and Google Maps-only firms appear only after a phone check.</p>'
            '<p>Homeowners can request referrals now through the contact page.</p></div>')
    note = f'<p>{c["note"]}</p>' if c.get("note") else ""
    licence_para = (
        f'<p>A contractor\'s licence classes matter on a pool job. {name} permits are generally issued to holders of '
        f'the A (general engineering), C-12 (earthwork and paving), C-21 (building moving and demolition) or C-53 '
        f'(swimming pool) classes described in the <a href="{SRC["cslb_classes"]}">state licence board\'s '
        'classification guide</a>, and the accepted classes differ from city to city. '
        f'<a href="{SRC["cslb_2407"]}">Industry Bulletin 24-07</a> confirms that the $1,000 unlicensed-work exemption '
        'does not cover work that needs a permit, so a pool removal always needs a licensed contractor or an '
        'owner-builder permit.</p>')
    if c.get("compact"):
        licence_para = (
            f'<p>A pool removal in {name} needs a licensed contractor or an owner-builder permit, because '
            f'<a href="{SRC["cslb_2407"]}">Industry Bulletin 24-07</a> keeps permitted work outside the $1,000 '
            f'unlicensed-work exemption. The <a href="{SRC["cslb_classes"]}">state classification guide</a> explains '
            'the A, C-12, C-21 and C-53 classes most pool jobs use.</p>')
    contractors = f'<h2>Contractors serving {name}</h2>{cards}{note}' + licence_para

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
           f'<p>The {c["dept"]} is the office to call before any work starts. {name} is one of {NO_RULE_COUNT} cities among the '
           f'{len(CITIES)} in this directory that publish nothing specific to pools, so the department\'s answer on the phone '
           'decides the permit type, the fee and the fill standard.</p>')
        + ('' if c.get("compact") else
           '<p>Fees and requirements change at the start of each fiscal year, usually in July. The city document '
           'linked above is the record a contractor or inspector will work from.</p>'))

    cost_key = c["cost"]
    if c.get("cost_html"):
        cost = (f'<h2>{c.get("cost_heading", "What a " + name + " job costs")}</h2>'
                + "".join(f'<p>{fill(x, c)}</p>' for x in c["cost_html"])
                + '<p>The <a href="/cost/">California pool removal cost guide</a> covers what moves a quote, from '
                  'side-yard access to fill dirt and the compaction report.</p>')
    else:
      cost = (
        f'<h2>Published prices for {region}</h2><p>{REGION_COST[cost_key]}</p>'
        '<p>Four things move a quote more than anything else: equipment access (about $2,000 more where the side yard '
        'is under 6 ft wide), deck removal ($500 to $1,700), fill dirt (80 to 150 cubic yards for a full removal) and '
        'the engineer\'s compaction report ($1,500 to $4,000). The <a href="/cost/">California pool removal cost '
        'guide</a> sets out every published price by region and pool type.</p>'
        + (f'<p>{fill(c["cost_extra"], c)}</p>' if c.get("cost_extra") else ''))

    methods = (
        f'<h2>Partial fill-in or full removal in {name}</h2><p>{fill(c["method_html"], c)}</p>{diagram()}'
        + ('<p>The <a href="/faq/">fill-in questions page</a> sets the two methods side by side, with typical '
           'timelines of one to four days for a partial fill-in and three to seven for a full removal.</p>'
           if c.get("compact") else
        '<p>A partial fill-in breaks drainage holes through the floor, removes the top of the wall and fills the shell '
        'with soil. The method costs less and finishes faster, usually in one to four days, but most cities limit the '
        'area to landscaping afterwards. A full removal hauls away every piece of the shell and replaces it with fill '
        'compacted in layers to 90%, which takes three to seven days and is the route for anyone planning a structure '
        'over the old pool.</p>')
        + figure(f"city-{slug}-work", ALT.get(f"city-{slug}-work", "") + "."))

    if c["region"] == "la":
        drain_src = (f'<a href="{SRC["la_storm"]}">LA Stormwater</a> allows the storm drain only for dechlorinated '
                     'water within a set pH range')
    elif c["region"] == "sd":
        drain_src = (f'The <a href="{SRC["sd_pools"]}">San Diego pools and spas fact sheet</a> allows the storm drain '
                     'only for dechlorinated water within a set pH range')
    else:
        drain_src = (f'The <a href="{SRC["sd_pools"]}">San Diego pools and spas fact sheet</a> and '
                     f'<a href="{SRC["la_storm"]}">LA Stormwater</a> both allow the storm drain only for dechlorinated '
                     'water within a set pH range')
    if c.get("drain_html"):
        draining = f'<p>{fill(c["drain_html"], c)}</p>'
    else:
      draining = (
        '<p>Pool water has to go somewhere before demolition starts. '
        + ('Stockton and Riverside allow pool water to the sewer clean-out only, ' if c["slug"] in ("stockton", "riverside") else '')
        + (drain_src[0].lower() + drain_src[1:] if c["slug"] in ("stockton", "riverside") else drain_src)
        + f', and {name} contractors generally follow the same practice. The '
          f'{c["dept"]} is the office to ask about the local rule.</p>')

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

    if c.get("compact"):
        after = (f'<p>Sellers in {name} should keep the finaled permit, because the state\'s '
                 f'<a href="{SRC["dre_re6"]}">seller disclosure form</a> asks about fill on the property and about '
                 'unpermitted work.</p>')
    else:
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

    hero = img_tag(f"city-{slug}-hero", "hero-img", eager=True)

    def extra(key):
        return "".join(f'<h2>{h}</h2>' + "".join(fill(par, c) if par.startswith("<") else f'<p>{fill(par, c)}</p>'
                                               for par in pars)
                       for h, pars in c.get(key, []))

    def assemble(faq_html):
        return (
            '<div class="content">'
            f'<h1>Pool Removal Contractors Working in {name}</h1>{opening}{facts}{intro}{hero}'
            + contractors
            # One call to action per city page: USEOU scores two or more sales CTAs negatively.
            + cta(f'{name} referrals go to contractors with an active licence first.')
            + permit + extra("extra_after_permit") + methods
            + cost + extra("extra_after_cost") + draining + after + nearby + map_html + faq_html
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
                       "item": {"@type": "LocalBusiness", "name": b["business"],
                                "areaServed": f"{name}, CA"}}
                      for i, b in enumerate(listed)]}

    page(f"/{slug}/", f"Pool Removal {c.get('title_name', name)}: Local Contractors and Permit Rules",
         f"Pool removal contractors serving {name}, with the city's permit rules, published fees and the choice "
         f"between partial fill-in and full removal.",
         body, crumbs=[(None, name)], schema=schema, city=name)
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
<h1>Pool Removal Contractors Across California's 32 Largest Cities</h1>
<p class="lead"><strong>{SITE_NAME} lists {TOTAL_FOUND} businesses confirmed as offering in-ground pool removal across California's 32 largest cities, and the <a href="{SRC["cslb_lookup"]}">Contractors State License Board</a> check of 11 October 2026 found 51 of the licence numbers they show current and active.</strong></p>
<p>Each city page pairs the local contractor list with that city's own permit rules, taken from official building department documents. Coverage is uneven: Bay Area cities have about 30 businesses each, while Fresno has 2, Oxnard and Bakersfield 5 each, and Riverside 7. The {N} cities are ranked by the <a href="{SRC["dof_e1"]}">California Department of Finance population estimate for 1 January 2026</a>.</p>
{img_tag("home-hero", "hero-img", eager=True)}

<h2 id="cities">Contractor counts for {N} cities in {len(REGIONS)} regions</h2>
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

<h2>Permit names and fees by city</h2>
<p>Every city that publishes a rule requires a permit, but the permit's name, the fee and what may stay in the ground all differ. {HANDOUT_COUNT} of the {N} cities publish a pool-specific handout, {FEE_ONLY_COUNT} publish only a fee and {NO_RULE_COUNT} publish nothing specific. The table lists the {N - NO_RULE_COUNT} cities with a published rule or fee; the city pages cover the other {NO_RULE_COUNT}.</p>
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
{DISCLOSURE}
</div>"""
    page("/", "Pool Removal California: Contractors, Costs and Permits",
         "A directory of pool removal and demolition contractors across California's 32 largest cities, with local "
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
{img_tag("cost-hero", "hero-img", eager=True)}

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

<h2>Permit fees by city</h2>
<p>Permit fees are a small share of the total but vary widely between cities. Stockton charges $97.25 for fiscal year 2026-27 under <a href="https://www.stocktonca.gov/Documents/Business/Building%20%26%20Life%20Safety/Building%20Forms/BLDG-0014_SWIMMING%20POOL%20DEMOLITION%20REQUIREMENTS.pdf">form BLDG-0014</a>, while San Diego charges $360.36 for plan check plus $332.48 for inspection. San Bernardino bases its fee on the cubic yards of fill, since it treats pool removal as on-site grading. San Jose takes a refundable debris deposit instead of a set pool fee.</p>
<div class="table-wrap"><table><thead><tr><th>City</th><th>Permit</th><th>Published fee</th></tr></thead><tbody>{fee_rows}</tbody></table></div>
<p>Several cities, including Los Angeles, Long Beach, Irvine, Santa Clarita, Santa Ana and Garden Grove, publish rules but no pool fee, and {NO_RULE_COUNT} cities publish nothing specific to pools. The city pages link each city's own document. Fees for Fresno, Chula Vista, Fremont and Fontana come from older schedules and should be confirmed with the city before budgeting.</p>

<h2>Timeline from permit to finished grade</h2>
<p>A partial fill-in takes one to four days on site and a full removal three to seven, once the permit is in hand. Draining the pool adds a day or two, and must follow local discharge rules: the <a href="{SRC["sd_pools"]}">San Diego pools and spas fact sheet</a> and <a href="{SRC["la_storm"]}">LA Stormwater</a> allow the storm drain only for dechlorinated water within a set pH range, and Stockton and Modesto allow the sewer only.</p>
<p>Permits add one to three weeks in most cities. San Jose can issue in a single visit, and Fremont's express permit needs no plan review. San Jose also asks for a job number from the <a href="{SRC["baaqmd"]}">Bay Area Air Quality Management District</a> before demolition, and Oakland bars grading from 15 October to 15 April, so jobs there need to be booked for the dry season.</p>
{figure("cost-landscape", "Many owners keep part of the deck as a patio, which lowers both the price and the hauling volume.")}

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
{figure("draining", "Draining comes first, to the sewer clean-out or a storm drain where the city allows it.")}
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
{figure("faq-compaction", "Compaction to 90%, checked and certified, is the standard most California cities set for buildable fill.")}


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
<p>In San Jose, yes. San Jose's <a href="{SJ}">pool demolition page</a> requires a job number from the <a href="{SRC["baaqmd"]}">Bay Area Air Quality Management District</a> before demolition starts, and Lancaster requires an air district demolition notice as well. Elsewhere, the district's rules are written for load-bearing building demolition, so it confirms whether a pool-only job counts.</p>

<h2>Cost and timing</h2>

<h3>What does pool removal cost in California?</h3>
<p>California contractors publish $3,500 to $12,000 for a partial fill-in and $8,000 to $30,000 for a full removal in Northern California, and Los Angeles firms start at $10,500 and $17,500. The <a href="/cost/">pool removal cost guide</a> lists every published price with its source.</p>

<h3>What does above-ground pool removal cost?</h3>
<p>$300 to $3,500, depending on decking, according to <a href="{SRC["angi"]}">Angi</a>. Above-ground pools rarely need a demolition or grading permit.</p>

<h3>How long does pool removal take?</h3>
<p>One to four days for a partial fill-in and three to seven for a full removal. Permits add one to three weeks in most cities; San Jose's <a href="{SJ}">permit center</a> can issue in one visit. Oakland bars grading from 15 October to 15 April.</p>

<h2>Water, tax and selling</h2>

<h3>Where can the pool water be drained?</h3>
<p>The rule varies by city. Stockton allows the sewer clean-out only, and Modesto sends all pool water to the sewer, even when dechlorinated. Riverside prefers the sewer clean-out and allows the storm drain only below 0.1 mg/L of chlorine. San Diego and Los Angeles allow the storm drain if the water is dechlorinated and within a set pH range, as the <a href="{SRC["sd_pools"]}">San Diego pools and spas fact sheet</a> and <a href="{SRC["la_storm"]}">LA Stormwater's guidance for pool owners</a> explain.</p>
{figure("faq-draining", "Pool water must be drained to the sewer clean-out or, where allowed, dechlorinated before it reaches a storm drain.")}

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
<p class="lead"><strong>{SITE_NAME} is an independent referral directory of businesses that remove in-ground pools in California's 32 largest cities; it is not a contractor and does not perform any work.</strong></p>

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
<form class="quote" id="referral-form" method="POST" action="{FORMSPREE_URL}">
<input type="hidden" name="_subject" value="New pool removal referral request">
<input type="text" name="_gotcha" tabindex="-1" autocomplete="off" hidden>
<label>Name<input name="name" required autocomplete="name"></label>
<label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
<label>Email<input name="email" type="email" autocomplete="email"></label>
<label>City<select name="city" required><option value="">Choose a city</option>{options}<option value="other">Other California city</option></select></label>
<label>Pool type<select name="pool_type"><option>Concrete or gunite</option><option>Fiberglass</option><option>Vinyl liner</option><option>Above-ground</option><option>Not sure</option></select></label>
<label>Method<select name="method"><option>Not sure yet</option><option>Partial fill-in</option><option>Full removal</option></select></label>
<label>Anything else contractors should know<textarea name="notes" rows="4" placeholder="Access width, deck, plans for the area afterwards"></textarea></label>
<button class="btn" type="submit">Send referral request</button>
<p class="form-status" role="status" hidden></p>
</form>
{DISCLOSURE}
</div>"""
    page("/contact/", "Request Pool Removal Contractor Referrals in California",
         "Ask for referrals to licensed pool removal contractors in California's 32 largest cities.",
         body, crumbs=[(None, "Request referrals")], index=False)
    thanks = ('<div class="content"><h1>Referral Request Received</h1><p>Listed contractors serving the chosen city '
              'will be in touch by phone or email. The <a href="/cost/">cost guide</a> and '
              '<a href="/faq/">fill-in questions</a> help when comparing quotes.</p></div>')
    page("/thanks/", "Referral Request Received", "Referral request received.", thanks, index=False)


def not_found():
    body = ('<div class="content"><h1>Page Not Found</h1><p>The page may have moved. The '
            '<a href="/">California pool removal directory</a> links every city page.</p></div>')
    page("/404.html", "Page Not Found | Pool Removal California", "Page not found.", body, index=False)


def sitemap():
    urls = "".join(f"<url><loc>{SITE_URL}{p}</loc></url>" for p in CONTENT_PAGES)
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")


OPEN_ITEMS = [
    "Phone the firms on the workbook's To verify by phone tab, starting with the five in Fresno",
    "Decide whether the businesses with no licence number on their site are listed, listed lower, or held back",
    "Decide whether listings link out to each contractor's website (LINK_CONTRACTOR_SITES)",
    "Decide on limited-class licences: Bye Bye Pool / Bay Area Pool Demolition, Precision Excavation and Demolition, Beachfront Pools",
    "Confirm two licence name mismatches by phone: A-1 Septic (American Choice Enterprises) and Bye Bye Pool (PCR Demo)",
    "Re-check workers' compensation for Buendia Demolition and Optimal EarthWork",
    "Fill the thin cities: Fresno, Bakersfield and Riverside",
    "Call building departments in San Francisco, Sacramento, Oakland, Bakersfield, Anaheim and Modesto for pool rules",
    "Call building departments in Oxnard, Glendale, Lancaster, Oceanside, Palmdale and Garden Grove for pool rules",
    "Recheck permit fees from older schedules: Fresno, Chula Vista, Fremont and Fontana",
    "Confirm the three flagged FAQ answers: licence classes, sale disclosure and property tax",
    "Re-check each licence number at the state board before its page is updated",
    "Re-run the city ranking check before each wave",
    "Set SITE_URL in site_data.py to the live domain and connect it in Netlify",
]


def write_dashboard_data(counts, listings, held):
    """data/dashboard.json: static tracker data bundled into the dashboard API function."""
    pipeline = {}
    with (ROOT / "data" / "listings.csv").open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["status"] not in ("No licence number on site", "Maps listing only, no website"):
                continue
            b = pipeline.setdefault(r["business"], {
                "business": r["business"], "phone": r["phone"], "base_city": r["base_city"],
                "reason": r["status"], "website": r["website"], "cities": []})
            if r["city"] not in b["cities"]:
                b["cities"].append(r["city"])
    data = {
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "siteName": SITE_NAME,
        "pages": len(CONTENT_PAGES),
        "cities": [{
            "name": c["name"], "slug": c["slug"], "region": REGION_NAME[c["region"]], "wave": c["wave"],
            "confidence": c["confidence"], "listed": len(listings.get(c["slug"], [])), "held": held.get(c["slug"], 0),
            "words": counts[f'/{c["slug"]}/'],
        } for c in CITIES],
        "openItems": OPEN_ITEMS,
        "pipeline": sorted(pipeline.values(), key=lambda b: (b["reason"], b["business"].lower())),
    }
    (ROOT / "data" / "dashboard.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def dashboard_page():
    html_doc = """<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Referral Dashboard</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/styles.css">
<link rel="stylesheet" href="/dashboard.css">
</head>
<body class="dash">
<header class="site-header"><div class="wrap"><span class="logo">Pool Removal <span>California</span> · Dashboard</span>
<nav class="nav"><button id="refresh" class="link-btn" type="button">Refresh</button><button id="logout" class="link-btn" type="button">Sign out</button></nav></div></header>
<main class="wrap">
<section id="login" hidden>
<h1>Dashboard sign-in</h1>
<form id="login-form" class="quote"><label>Dashboard key<input id="key" type="password" autocomplete="current-password" required></label>
<button class="btn" type="submit">Open dashboard</button><p id="login-msg" class="muted"></p></form>
</section>
<p id="loading" class="muted" hidden>Loading…</p><p id="error" class="error"></p>
<div id="app" hidden>
<section><div class="dash-head"><h1>Referrals</h1>
<label>Period <select id="days"><option value="7">7 days</option><option value="30" selected>30 days</option><option value="90">90 days</option><option value="365">12 months</option></select></label></div>
<div id="kpis" class="kpis"></div>
<div class="dash-grid">
<div class="panel"><h2>Phone taps by page</h2><div id="calls-by-page"></div></div>
<div class="panel"><h2>Referrals by city</h2><div id="by-city"></div></div>
<div class="panel"><h2>Form requests by city</h2><div id="forms-by-city"></div></div>
</div>
<div class="panel"><h2>Recent referral events</h2><p class="muted">Phone counts are taps on the site's phone number; the call itself is not tracked. Form requests are copied to Formspree, which holds the visitor's contact details.</p>
<div class="table-wrap"><table><thead><tr><th>When</th><th>Type</th><th>City</th><th>Detail</th><th>Page</th></tr></thead><tbody id="recent"></tbody></table></div></div>
</section>
<section><h1>Site tracker</h1><p id="site-summary" class="muted"></p>
<div class="table-wrap"><table><thead><tr><th>City</th><th>Region</th><th>Wave</th><th>Listed</th><th>Held back</th><th>Permit confidence</th><th>Words</th><th>Referrals</th></tr></thead><tbody id="cities"></tbody></table></div>
<h2>Open items from the site plan</h2>
<div class="table-wrap"><table><tbody id="items"></tbody></table></div>
</section>
<section><div class="dash-head"><h1>Contractor pipeline</h1>
<label>Show <select id="pipe-filter"><option value="">All</option><option>To call</option><option>No answer</option><option>Verified</option><option>Not offering pool removal</option><option>Listed</option><option>Rejected</option></select></label></div>
<p class="muted">Businesses held back until a phone check. Mark a business Verified once confirmed, then set it to Licence active in the workbook and re-run the import to list it.</p>
<p id="pipe-count" class="muted"></p>
<div class="table-wrap"><table><thead><tr><th>Business</th><th>Phone</th><th>Base city</th><th>Cities</th><th>Status and note</th></tr></thead><tbody id="pipeline"></tbody></table></div>
</section>
</div>
</main>
<script src="/dashboard.js"></script>
</body>
</html>
"""
    (OUT / "dashboard").mkdir(parents=True, exist_ok=True)
    (OUT / "dashboard" / "index.html").write_text(html_doc, encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    for name in ("styles.css", "dashboard.css", "track.js", "dashboard.js"):
        shutil.copy(ROOT / "static" / name, OUT / name)
    shutil.copytree(ROOT / "static" / "img", OUT / "img")
    (OUT / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#12372a"/>'
        '<path d="M6 20c3 0 3 2 6 2s3-2 6-2 3 2 6 2 2-1 2-1" stroke="#8fe0b8" stroke-width="2.5" fill="none"/>'
        '<path d="M8 10h16" stroke="#fff" stroke-width="2.5"/></svg>')

    listings, held = load_listings()
    counts = {"/": home(), "/cost/": cost_page(), "/faq/": faq_page()}
    for c in CITIES:
        counts[f'/{c["slug"]}/'] = city_page(c, listings, held)
    about_page()
    contact_page()
    not_found()
    dashboard_page()
    write_dashboard_data(counts, listings, held)
    sitemap()
    for p, n in counts.items():
        print(f"{n:>5} words  {p}")
    print(f"Built {len(list(OUT.rglob('index.html')))} pages into {OUT}")


if __name__ == "__main__":
    main()
