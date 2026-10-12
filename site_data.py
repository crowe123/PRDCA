"""Content and facts for the Pool Removal California site.

Every fact here comes from the site structure document of 10 October 2026
(permit table, cost table, FAQ notes and city table). Contractor listings are
not stored here: they load from data/businesses.csv, exported from the
workbook's Businesses and By city tabs.
"""

SITE_NAME = "Pool Removal California"
# Set to the live domain before deploying; used for canonical URLs and the sitemap.
SITE_URL = "https://pool-removal-california.netlify.app"

# Business contact details shown in the footer of every page.
BUSINESS_ADDRESS = "1150 S Olive St, Los Angeles, CA 90015"
BUSINESS_PHONE = "(213) 325-3273"
BUSINESS_PHONE_TEL = "+12133253273"

# Open item in the plan: whether contractor cards link to each contractor's site.
LINK_CONTRACTOR_SITES = True

# Official and published sources, linked inside the sentences that use them.
SRC = {
    "cslb_lookup": "https://www.cslb.ca.gov/OnlineServices/CheckLicenseII/CheckLicense.aspx",
    "cslb_classes": "https://www.cslb.ca.gov/Resources/GuidesAndPublications/DescriptionOfClassifications.pdf",
    "cslb_2407": "https://www.cslb.ca.gov/Resources/IndustryBulletins/2024/AB%202622%20Implementation.FINAL.pdf",
    "cslb_quiz": "https://www2.cslb.ca.gov/Newsletter/2016-summer/quiz.asp",
    "boe_8609": "https://www.boe.ca.gov/proptaxes/pdf/86_09.pdf",
    "boe_newcon": "https://www.boe.ca.gov/proptaxes/newconstructionproperty.htm",
    "sd_assessor": "https://www.sdarcc.gov/content/arcc/home/divisions/assessor/realty-assessment.html",
    "dre_re6": "https://www.dre.ca.gov/files/pdf/re6.pdf",
    "sd_pools": "https://www.sandiego.gov/sites/default/files/pools_and_spas_fact_sheet.pdf",
    "la_storm": "https://www.lastormwater.org/take-action/practice-good-housekeeping/tips-for-pools-spas-and-fountain-owners/",
    "valley_water": "https://www.valleywater.org/saving-water/rebates-surveys/landscape-rebates",
    "oc_pw": "https://pwds.oc.gov/sites/ocpwocds/files/2021-06/Swimming%20Pool%20Demolition%20Requirements.pdf",
    "dof_e1": "https://dof.ca.gov/Forecasting/Demographics/estimates-e1/",
    "homeadvisor": "https://www.homeadvisor.com/cost/swimming-pools-hot-tubs-and-saunas/remove-and-fill-in-pool/",
    "fixr": "https://www.fixr.com/costs/fill-in-pool",
    "homeguide": "https://homeguide.com/costs/cost-to-fill-in-a-pool",
    "baaqmd": "https://www.baaqmd.gov/permits/asbestos",
    "angi": "https://www.angi.com/articles/pool-removal-cost/ca/los-angeles",
    "frisch": "https://www.frischandsons.com/pool-demolition-cost-orange-county",
    "lapdc": "https://losangelespooldemo.com/",
    "demodiego": "https://www.demodiego.com/demolition/pool-demolition",
    "villa": "https://villademolition.com/pool-removal-san-diego/",
    "souza": "https://souzasonsinc.com/services/pool-removal/",
    "byebye": "https://byebyepools.com/partial-vs-full-pool-removal-cost-may/",
    "norcal": "https://norcalearthworks.com/blog/pool-removal-before-adu-sacramento",
    "walberg": "https://www.walberginc.com/blog/swimming-pool-removal-cost-northern-california",
    "la_cd": "https://sanitation.lacity.gov/san/faces/home/portal/s-lsh-wwd/s-lsh-wwd-s/s-lsh-wwd-s-r/s-lsh-wwd-s-r-cdr",
}

# Published prices from the cost table. Dates stay: they are facts about the sources.
PRICES = [
    {"source": "Angi", "url": SRC["angi"], "area": "Los Angeles", "partial": "$2,850 to $11,350",
     "full": "$4,550 to $18,200, average $6,816", "published": "Jun 2026"},
    {"source": "Frisch &amp; Sons", "url": SRC["frisch"], "area": "Orange County", "partial": "$12,000 to $20,000",
     "full": "$18,000 to $30,000 or more", "published": "2025 guide"},
    {"source": "Los Angeles Pool Demolition Contractors", "url": SRC["lapdc"], "area": "Los Angeles",
     "partial": "From $10,500", "full": "From $17,500", "published": "Jun 2026"},
    {"source": "Demo Diego", "url": SRC["demodiego"], "area": "San Diego", "partial": "$5,000 to $9,000",
     "full": "$9,000 to $15,000", "published": "2026"},
    {"source": "Villa Demolition", "url": SRC["villa"], "area": "San Diego", "partial": "$12,000 to $30,000",
     "full": "$45,000 to $60,000", "published": "Jun 2026"},
    {"source": "Souza &amp; Son's", "url": SRC["souza"], "area": "Bay Area", "partial": "$4,500 to $10,000",
     "full": "$8,000 to $22,000 for a 15 by 30 ft pool", "published": "May 2026"},
    {"source": "Bye Bye Pool", "url": SRC["byebye"], "area": "Concord", "partial": "$3,500 to $7,000",
     "full": "$9,000 to $19,000", "published": "May 2026"},
    {"source": "NorCal Earthworks", "url": SRC["norcal"], "area": "Sacramento", "partial": "Not priced",
     "full": "$8,000 to $15,000 concrete, $6,000 to $12,000 fiberglass", "published": "May 2026"},
    {"source": "Walberg, Inc.", "url": SRC["walberg"], "area": "Northern California", "partial": "$5,000 to $12,000",
     "full": "$12,000 to $30,000", "published": "Aug 2026"},
]

REGIONS = [
    ("la", "Los Angeles County"),
    ("oc", "Orange County"),
    ("sd", "San Diego County"),
    ("ie", "Inland Empire"),
    ("bay", "Bay Area"),
    ("cv", "Sacramento and the Central Valley"),
    ("ven", "Ventura County"),
]

# Regional cost paragraphs: published ranges only, never invented local figures.
REGION_COST = {
    "la": (
        f'<a href="{SRC["lapdc"]}">Los Angeles Pool Demolition Contractors</a> publishes prices from $10,500 for a '
        f'partial fill-in and from $17,500 for a full removal. <a href="{SRC["angi"]}">Angi\'s Los Angeles cost page</a> '
        'reports a wider spread of $2,850 to $11,350 for a partial and $4,550 to $18,200 for a full removal, with an '
        'average of $6,816. Contractor quotes in Los Angeles County sit nearer the top of the Angi range than its average.'
    ),
    "oc": (
        f'<a href="{SRC["frisch"]}">Frisch &amp; Sons, an Orange County demolition contractor</a>, publishes $12,000 to '
        '$20,000 for a partial fill-in and $18,000 to $30,000 or more for a full removal. Los Angeles firms start at '
        f'$10,500 and $17,500 according to <a href="{SRC["lapdc"]}">Los Angeles Pool Demolition Contractors</a>, '
        'so Southern California prices begin well above the national cost guides.'
    ),
    "sd": (
        f'San Diego\'s two published price lists disagree by a factor of three or more. <a href="{SRC["demodiego"]}">Demo '
        'Diego</a> quotes $5,000 to $9,000 for a partial fill-in and $9,000 to $15,000 for a full removal, while '
        f'<a href="{SRC["villa"]}">Villa Demolition</a> quotes $12,000 to $30,000 and $45,000 to $60,000. A written '
        'quote from more than one contractor is the only reliable way to place a pool inside that spread.'
    ),
    "bay": (
        f'<a href="{SRC["souza"]}">Souza &amp; Son\'s</a> publishes $4,500 to $10,000 for a partial fill-in and $8,000 to '
        f'$22,000 for a full removal of a 15 by 30 ft pool. <a href="{SRC["byebye"]}">Bye Bye Pool in Concord</a> quotes '
        f'$3,500 to $7,000 and $9,000 to $19,000, and <a href="{SRC["walberg"]}">Walberg, Inc.</a> gives $5,000 to '
        '$12,000 and $12,000 to $30,000 for Northern California.'
    ),
    "sac": (
        f'<a href="{SRC["norcal"]}">NorCal Earthworks in Sacramento</a> prices full removal at $8,000 to $15,000 for a '
        f'concrete pool and $6,000 to $12,000 for fiberglass. <a href="{SRC["walberg"]}">Walberg, Inc.</a> publishes '
        '$5,000 to $12,000 for a partial fill-in and $12,000 to $30,000 for a full removal across Northern California.'
    ),
    "none": (
        'No contractor in this part of California publishes local prices, so the statewide figures apply. Northern '
        f'California firms such as <a href="{SRC["walberg"]}">Walberg, Inc.</a> quote $3,500 to $12,000 for a partial '
        f'fill-in and $8,000 to $30,000 for a full removal, and <a href="{SRC["lapdc"]}">Los Angeles firms</a> start at '
        '$10,500 and $17,500. National guides such as <a href="' + SRC["homeadvisor"] + '">HomeAdvisor</a> run lower and '
        'work best as a floor.'
    ),
}

# Cities 1 to 20, ranked by the 1 January 2026 population estimate.
# found = businesses found; active = active licence; searches = monthly searches.
CITIES = [
    {
        "rank": 1, "name": "Los Angeles", "slug": "los-angeles", "region": "la", "cost": "la",
        "searches": "50", "found": 20, "active": 9, "wave": 1,
        "dept": "Department of Building and Safety, Grading Division",
        "permit": "Grading permit", "fee": "Not published",
        "doc": "Bulletin P/BC 2026-111",
        "doc_url": "https://dbs.lacity.gov/sites/default/files/efs/forms/pc17/p-bc-2020-111-backfill-of-swimming-pools.pdf",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "The Los Angeles Department of Building and Safety treats pool removal as grading work, so the job runs on a "
            "grading permit. {doc} sets out how a pool may be backfilled. A shell may stay in the ground only when the "
            "area will be used for landscaping and the ground slopes 10% or less. The bottom must then be broken with "
            "12-inch drainage holes spaced every 8 ft so water does not collect in the old basin. The department "
            "publishes no separate fee for pool backfill; the grading fee depends on the scope the plans show."
        ),
        "method_html": (
            "Los Angeles allows a partial fill-in only for landscaping on gentle ground, which suits a garden or lawn. "
            "Anyone planning an accessory dwelling unit, an addition or a patio slab over the old pool needs the full "
            "removal route: the shell comes out and the fill is compacted and certified, as the "
            "{doc} describes. Hillside lots steeper than 10% fall outside the partial option altogether."
        ),
        "faqs": [
            ("Which permit covers pool removal in Los Angeles?",
             "A grading permit from the Department of Building and Safety. {doc} covers the backfill rules, and the fee follows the grading scope."),
            ("Can a pool shell stay in the ground in Los Angeles?",
             "Only for landscaping use on ground sloping 10% or less, with 12-inch drainage holes every 8 ft across the bottom."),
            ("Where can Los Angeles pool water be drained?",
             "Dechlorinated water within the set pH range may go to the storm drain under the LA Stormwater guidance; other water goes to the sewer clean-out."),
            ("How much does pool removal cost in Los Angeles?",
             "Los Angeles Pool Demolition Contractors publishes prices from $10,500 for a partial fill-in and $17,500 for a full removal. Angi's Los Angeles figures run from $2,850 to $11,350 for a partial and $4,550 to $18,200 for a full removal."),
            ("How long does a Los Angeles pool removal take?",
             "The work takes one to four days for a partial fill-in and three to seven days for a full removal. The three city inspections, and on a full removal the approval of the compaction report, add time on top of that."),
            ("Can an ADU be built over a filled pool in Los Angeles?",
             "Only after a full removal. {doc} limits a shell left in place to landscaping, and no foundation work may start until the Grading Division approves the compaction report."),
            ("Does removing a pool affect a Los Angeles home sale?",
             "The state's seller disclosure form asks about fill on the property and about unpermitted work. Sellers should keep the finaled grading permit and, on a full removal, the approved compaction report to answer both questions."),
        ],
        "nearby": ["Burbank", "Glendale", "Pasadena", "Culver City", "Santa Monica", "Inglewood"],
        "note": "One contractor in the research trades under three different websites, so the listing merges them.",
        "opening_extra": (" The one Los Angeles contractor that publishes prices starts at $10,500 for a partial "
                          "fill-in and $17,500 for a full removal."),
        "extra_after_permit": [
            ("Inspections and paperwork on a Los Angeles job", [
                "The Department of Building and Safety sets out two versions of the same grading permit in {doc}, "
                "revised in June 2026, and each version comes with the same three inspections, called for as the "
                "grading work reaches each stage:",
                "<ol><li>Initial meeting and inspection.</li>"
                "<li>Bottom inspection: on a partial fill-in, after the drainage holes are broken and before any soil "
                "goes in; on a full removal, after the shell is out and before compacted fill is placed.</li>"
                "<li>Final inspection, once the fill is complete.</li></ol>",
                "On a partial fill-in, the bulletin requires at least one drainage hole at the deepest point of the "
                "shell, and the backfill must be clean soil or gravel, moistened and compacted by tractor rolling or a "
                "mechanical tamper.",
                "A partial fill-in also needs a plot plan showing where the pool sits, its distance to every building "
                "and property line, and a note that the fill is uncertified. That label matters later. Uncertified "
                "fill cannot support a footing, so the area stays limited to planting.",
                "A full removal asks for more paperwork. The grading permit states the total cubic yards of fill, the "
                "shell leaves the site, and the excavation bottom is inspected before compacted fill goes in. All fill "
                "must reach 90% relative compaction under the ASTM D1557 test, checked by a soil testing agency the "
                "department approves, and the compaction report with its Certificate of Compliance goes to the Grading "
                "Division for approval. No foundation work may start until that report is approved, which is the step "
                "that clears the way for an accessory dwelling unit or an addition.",
                "Two further documents apply to some full removals. A site inside a Hillside Grading Area needs a "
                "Grading Pre-Inspection report, and the department can ask for a soil report from a licensed soils "
                "engineer covering temporary excavation, grading specifications and allowable bearing pressures. Each "
                "adds an engineer's fee and time to the schedule, so a quote for a Los Angeles hillside job should say "
                "whether it includes them.",
            ]),
        ],
        "cost_extra": (
            "In Los Angeles, the city's own steps sit on top of those four. Compaction testing and the Certificate of "
            "Compliance fall inside the engineer's report cost above, but a hillside lot can add a Grading "
            "Pre-Inspection report and a soils engineer's report, and the grading permit fee depends on the cubic yards "
            "shown on the plans. A quote that leaves out the permit, the testing or the engineering cannot be compared "
            "fairly with one that includes them."
        ),
        "extra_after_cost": [
            ("Hauling the old shell out of Los Angeles", [
                "Concrete and gunite from a full removal count as construction and demolition waste. The city's "
                f'<a href="{SRC["la_cd"]}">'
                "Citywide Construction and Demolition Waste Recycling Ordinance</a>, approved in 2010, sends all mixed "
                "construction and demolition waste generated inside city limits to a city-certified processor, and "
                "anyone hauling it needs a Private Waste Hauler Permit from LA Sanitation. The city can fine up to "
                "$5,000 for each load taken elsewhere. A contractor that hauls its own debris should hold that permit, "
                "and a homeowner hiring a separate hauler can ask for the permit number before the first load leaves.",
            ]),
        ],
    },
    {
        "rank": 2, "name": "San Diego", "slug": "san-diego", "region": "sd", "cost": "sd",
        "searches": "30", "found": 16, "active": 10, "wave": 1,
        "dept": "Development Services Department",
        "permit": "Demolition/Removal Permit", "fee": "$360.36 plan check plus $332.48 inspection (Sept 2026)",
        "doc": "Information Bulletin 710",
        "doc_url": "https://www.sandiego.gov/development-services/forms-publications/information-bulletins/710",
        "confidence": "Medium-high", "rules": "published",
        "permit_html": (
            "San Diego's Development Services Department issues a Demolition/Removal Permit for pools, described in "
            "{doc}. The published fees in September 2026 were $360.36 for plan check and $332.48 for inspection, "
            "about $693 in total before any other charges. A soils compaction report is required for any pool deeper "
            "than five feet. Owner-builders may pull the permit themselves, and the bulletin names the A and C-21 "
            "licence classes for contractors."
        ),
        "method_html": (
            "San Diego permits both routes under the same Demolition/Removal Permit. Deep pools, which most older "
            "family pools are at the deep end, trigger the soils compaction report either way, so the engineering "
            "cost sits in most San Diego jobs. A full removal with compacted fill is the route that keeps the yard "
            "buildable for a later structure."
        ),
        "faqs": [
            ("What does a San Diego pool removal permit cost?",
             "$360.36 for plan check plus $332.48 for inspection, about $693 in total at the September 2026 fee schedule."),
            ("Does San Diego require a soils report?",
             "Yes for pools deeper than five feet: {doc} requires a soils compaction report for those."),
            ("Can a San Diego homeowner pull the permit?",
             "Yes. San Diego accepts an owner-builder application, and contractors need an A or C-21 licence."),
        ],
        "nearby": ["Chula Vista", "La Mesa", "El Cajon", "Poway", "National City", "Santee"],
        "note": "Searches for pool demolition in San Diego add about 40 a month to the pool removal figure.",
    },
    {
        "rank": 3, "name": "San Jose", "slug": "san-jose", "region": "bay", "cost": "bay",
        "searches": "30", "found": 34, "active": 19, "wave": 1,
        "dept": "Building Division, Development Services Permit Center",
        "permit": "Building permit", "fee": "Not published; refundable debris deposit",
        "doc": "swimming pool demolition page (Bulletin #289)",
        "doc_url": "https://www.sanjoseca.gov/businesses/development-services-permit-center/start-your-project/swimming-pool-demolition",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "San Jose's Development Services Permit Center handles pool demolition on a building permit, and the city's "
            "{doc} lists the requirements. The city takes a refundable debris deposit rather than publishing a flat pool "
            f'fee. The filled area is marked non-buildable unless an engineer certifies the compaction, and the job needs '
            f'a job number from the <a href="{SRC["baaqmd"]}">Bay Area Air Quality Management District</a> before '
            "demolition starts. San Jose can issue the permit in a single visit, which shortens the usual wait."
        ),
        "method_html": (
            "San Jose's choice turns on the non-buildable marking. A partial fill-in without an engineer's compaction "
            "certificate leaves the area recorded as non-buildable, which limits later plans for an accessory dwelling "
            "unit. A full removal with certified compaction clears that marking. Santa Clara County owners turning the "
            f'pool into low-water landscape may also qualify for the <a href="{SRC["valley_water"]}">Valley Water landscape '
            "rebate</a> of $2 a square foot, up to $3,000, with approval before work starts."
        ),
        "faqs": [
            ("Is a filled pool area buildable in San Jose?",
             "Only when an engineer certifies the compaction; otherwise the city marks the area non-buildable."),
            ("Does San Jose pool removal need an air district number?",
             "Yes. The job needs a Bay Area Air Quality Management District job number before demolition starts."),
            ("Is there a rebate for removing a pool in San Jose?",
             "Valley Water pays $2 a square foot, up to $3,000, when a pool becomes low-water landscape, with approval before work begins."),
        ],
        "nearby": ["Santa Clara", "Campbell", "Milpitas", "Cupertino", "Los Gatos", "Saratoga"],
        "note": "San Jose has the deepest contractor pool of the 32 cities.",
    },
    {
        "rank": 4, "name": "San Francisco", "slug": "san-francisco", "region": "bay", "cost": "bay",
        "searches": "10", "found": 31, "active": 19, "wave": 2,
        "dept": "Department of Building Inspection",
        "permit": "None specific to pools", "fee": "Not found",
        "doc": "Building Code section 106A",
        "doc_url": "https://codelibrary.amlegal.com/codes/san_francisco/latest/sf_building/0-0-0-92027",
        "confidence": "Low", "rules": "none",
        "permit_html": (
            "San Francisco publishes no rule specific to pool removal. The general requirement in {doc} applies: a permit "
            "is needed to remove any regulated structure, and a swimming pool is one. The Department of Building "
            "Inspection is the office to call for the permit type, the fee and any engineering it expects for the fill. "
            f'The <a href="{SRC["baaqmd"]}">Bay Area Air Quality Management District</a> asks for notice before demolitions '
            "and confirms whether a pool-only job counts."
        ),
        "method_html": (
            "With no published pool rule, San Francisco owners should confirm with the Department of Building Inspection "
            "whether a partial fill-in is accepted on their lot. Many San Francisco pools sit on tight lots with limited "
            "equipment access, and contractors add about $2,000 where clearance is under 6 ft. A full removal with "
            "compacted, engineer-certified fill is the safest route where anything will be built later."
        ),
        "faqs": [
            ("Does San Francisco have a pool removal handout?",
             "No. The general rule in {doc} requires a permit to remove any regulated structure; the Department of Building Inspection confirms the details."),
            ("Does narrow access raise the price in San Francisco?",
             "Contractors add about $2,000 where equipment access is under 6 ft wide, which is common on city lots."),
            ("Which licence should a San Francisco contractor hold?",
             "Cities name A, C-12, C-21 or C-53 classes; the state licence board lookup shows each contractor's classes."),
        ],
        "nearby": ["Daly City", "South San Francisco", "Brisbane", "San Bruno", "Sausalito", "Pacifica"],
        "note": "",
    },
    {
        "rank": 5, "name": "Fresno", "slug": "fresno", "region": "cv", "cost": "none",
        "searches": "10", "found": 2, "active": 2, "wave": 3,
        "dept": "Building and Safety Services Division",
        "permit": "Swimming Pool Abandonment Permit", "fee": "$321 (2013 figure)",
        "doc": "Bulletin 13-02",
        "doc_url": "https://www.fresno.gov/wp-content/uploads/2023/02/SwimmingPoolAbandonment.pdf",
        "confidence": "Medium-high", "rules": "published",
        "permit_html": (
            "Fresno issues a Swimming Pool Abandonment Permit through its Building and Safety Services Division, set out "
            "in {doc}. The bulletin's fee of $321 dates from 2013 and should be confirmed with the city before a job is "
            "priced. Fresno's rule is strict: the entire bottom must be broken out, and all backfill must be engineered "
            "to 90% compaction. Owner-builders may apply, and the bulletin names the C-12 and A licence classes."
        ),
        "method_html": (
            "Fresno's abandonment rules leave less difference between the two routes than most cities. Breaking out the "
            "whole bottom and compacting every layer to 90% means even a partial job carries engineering and fill costs "
            "close to a full removal. Owners who expect to build later usually choose full removal for the cleaner record."
        ),
        "faqs": [
            ("What is the Fresno pool abandonment fee?",
             "$321 in {doc}, a 2013 figure that needs a recheck with the city before budgeting."),
            ("Does Fresno require the pool bottom removed?",
             "Yes. The entire bottom must be broken out and all backfill engineered to 90% compaction."),
            ("Can a Fresno homeowner pull the abandonment permit?",
             "Yes. Fresno accepts owner-builders, and contractors need a C-12 or A licence."),
        ],
        "nearby": ["Clovis", "Sanger", "Selma", "Kerman", "Madera", "Fowler"],
        "note": "Only two confirmed contractors, so more are being checked by phone.",
    },
    {
        "rank": 6, "name": "Sacramento", "slug": "sacramento", "region": "cv", "cost": "sac",
        "searches": "20", "found": 11, "active": 5, "wave": 1,
        "dept": "Community Development Department, Building Division",
        "permit": "Unclear; demolition uses a wrecking permit", "fee": "Not found",
        "doc": "building forms page",
        "doc_url": "https://www.cityofsacramento.gov/community-development/building/building-forms",
        "confidence": "Low", "rules": "none",
        "permit_html": (
            "Sacramento publishes no rule specific to pool removal. Demolition in the city runs on a wrecking permit, and "
            "the Community Development Department's {doc} carries the general applications. The department is the "
            "office to call to confirm which permit a pool takes, the fee and whether an engineer's compaction report "
            "is required."
        ),
        "method_html": (
            "Without a published pool rule, the Sacramento choice depends on later plans. "
            f'<a href="{SRC["norcal"]}">NorCal Earthworks</a> writes about full removal ahead of an accessory dwelling '
            "unit, which is the common reason for taking the whole shell out. A partial fill-in suits a yard staying as "
            "lawn or garden, subject to what the department accepts."
        ),
        "faqs": [
            ("Which permit does Sacramento use for pool removal?",
             "No pool rule is published; demolition generally uses a wrecking permit, and the Community Development Department confirms the type."),
            ("Is full removal needed before building an ADU in Sacramento?",
             "Building over the area needs the shell removed and compacted, engineer-certified fill."),
            ("What does pool removal cost in Sacramento?",
             "NorCal Earthworks publishes $8,000 to $15,000 for a concrete pool and $6,000 to $12,000 for fiberglass."),
        ],
        "nearby": ["Elk Grove", "Rancho Cordova", "Citrus Heights", "West Sacramento", "Roseville", "Folsom"],
        "note": "A national referral directory currently ranks first for this city.",
    },
    {
        "rank": 7, "name": "Long Beach", "slug": "long-beach", "region": "la", "cost": "la",
        "searches": "10", "found": 20, "active": 6, "wave": 2,
        "dept": "Community Development Department, Building and Safety Bureau",
        "permit": "Grading permit", "fee": "Not published",
        "doc": "Information Bulletin IB-008",
        "doc_url": "https://www.longbeach.gov/globalassets/lbcd/media-library/documents/building--safety/information-bulletins/ib-008",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Long Beach's Building and Safety Bureau handles pool removal on a grading permit, and {doc} sets the rules. "
            "Leaving the shell in place needs two 24-inch holes through the bottom and a recorded covenant against the "
            "property, and the area is limited to landscaping. The bulletin publishes no pool fee; the grading fee "
            "follows the scope of work."
        ),
        "method_html": (
            "The recorded covenant is the main difference between the two Long Beach routes. A partial fill-in stays on "
            "the property record and limits the area to landscaping, which buyers and lenders will see. A full removal "
            "with compacted fill avoids the covenant and keeps the area open for a later structure."
        ),
        "faqs": [
            ("Does Long Beach record a partial pool fill-in?",
             "Yes. Leaving the shell needs a recorded covenant on the property and two 24-inch holes in the bottom."),
            ("Which permit covers pool removal in Long Beach?",
             "A grading permit, under {doc}."),
            ("Can a Long Beach filled pool area be built on?",
             "Not after a partial fill-in, which is limited to landscaping; full removal with compacted fill is needed."),
        ],
        "nearby": ["Lakewood", "Signal Hill", "Seal Beach", "Carson", "Bellflower", "Paramount"],
        "note": "",
    },
    {
        "rank": 8, "name": "Oakland", "slug": "oakland", "region": "bay", "cost": "bay",
        "searches": "10", "found": 32, "active": 18, "wave": 1,
        "dept": "Planning and Building Department",
        "permit": "Unclear", "fee": "Not found",
        "doc": "grading permits page",
        "doc_url": "https://www.oaklandca.gov/My-Household/Building-and-Remodeling/Homeowner-Projects-Permits/Grading-Permits",
        "confidence": "Low", "rules": "none",
        "permit_html": (
            "Oakland publishes no rule specific to pool removal. The city's {doc} sets one firm limit: no grading from "
            "15 October to 15 April, the rainy season. The Planning and Building Department is the office to call for the "
            f'permit type and fee, and Bay Area demolition also needs a <a href="{SRC["baaqmd"]}">Bay Area Air Quality '
            "Management District</a> notice."
        ),
        "method_html": (
            "Oakland's grading season shapes the schedule more than the method. Hillside lots in the Oakland hills often "
            "make full removal the safer route because fill on a slope needs engineered compaction. Either route should "
            "be booked to finish before 15 October."
        ),
        "faqs": [
            ("When can pool removal grading happen in Oakland?",
             "Between 15 April and 15 October; the city's grading page bars grading from 15 October to 15 April."),
            ("Does Oakland publish pool removal rules?",
             "No. The Planning and Building Department confirms the permit type and any engineering required."),
            ("What do Bay Area contractors charge?",
             "Published Bay Area prices run $3,500 to $12,000 for a partial fill-in and $8,000 to $30,000 for full removal."),
        ],
        "nearby": ["Berkeley", "Alameda", "Emeryville", "Piedmont", "San Leandro", "Orinda"],
        "note": "",
    },
    {
        "rank": 9, "name": "Bakersfield", "slug": "bakersfield", "region": "cv", "cost": "none",
        "searches": "10", "found": 5, "active": 2, "wave": 3,
        "dept": "Development Services Department, Building Division",
        "permit": "Unclear", "fee": "Not found",
        "doc": "building forms page",
        "doc_url": "https://www.bakersfieldcity.us/forms",
        "confidence": "Low", "rules": "none",
        "permit_html": (
            "Bakersfield publishes no rule specific to pool removal. The city's {doc} carries the general building "
            "applications, and the Development Services Building Division is the office to call for the permit type, "
            "the fee and the compaction standard it expects."
        ),
        "method_html": (
            "Without a published rule, Bakersfield owners should ask the Building Division whether a partial fill-in is "
            "accepted and whether the area is then limited to landscaping, as most California cities require. Full "
            "removal with compacted, certified fill keeps the yard buildable."
        ),
        "faqs": [
            ("Does Bakersfield publish pool removal rules?",
             "No. The Development Services Building Division confirms the permit and any engineering required."),
            ("What does pool removal cost in Bakersfield?",
             "No local prices are published; statewide contractor ranges run $3,500 to $12,000 partial and $8,000 to $30,000 full."),
            ("How many contractors serve Bakersfield?",
             "Five businesses were found, two with an active state licence; more are being checked by phone."),
        ],
        "nearby": ["Oildale", "Shafter", "Lamont", "Arvin", "Tehachapi", "Delano"],
        "note": "",
    },
    {
        "rank": 10, "name": "Anaheim", "slug": "anaheim", "region": "oc", "cost": "oc",
        "searches": "Under 10", "found": 20, "active": 10, "wave": 2,
        "dept": "Planning and Building Department, Building Division",
        "permit": "Building permit (general rule)", "fee": "Not found",
        "doc": "Handout B 804",
        "doc_url": "https://www.anaheim.net/DocumentCenter/View/41215",
        "confidence": "Low-medium", "rules": "none",
        "permit_html": (
            "Anaheim's {doc} states that a permit is required before any pool is removed, under the general building "
            "permit rule, but publishes no pool procedure or fee. The Planning and Building Department confirms the "
            f'requirements. For unincorporated Orange County, <a href="{SRC["oc_pw"]}">Orange County Public Works</a> '
            "publishes its own pool demolition requirements, which do not apply inside Anaheim city limits."
        ),
        "method_html": (
            "Anaheim publishes no rule on what may stay in the ground, so the Planning and Building Department decides "
            "whether a partial fill-in is accepted. Neighbouring Santa Ana requires five 3-ft holes and removal of the "
            "bond beam, which gives a sense of what Orange County cities expect."
        ),
        "faqs": [
            ("Does Anaheim require a permit to remove a pool?",
             "Yes. {doc} requires a permit before any pool is removed, though no procedure is published."),
            ("What do Orange County contractors charge?",
             "Frisch &amp; Sons publishes $12,000 to $20,000 for a partial fill-in and $18,000 to $30,000 or more for full removal."),
            ("Are all Anaheim listings real contractors?",
             "Two lead-generation sites appeared in the Anaheim research; both are left off the directory."),
        ],
        "nearby": ["Fullerton", "Orange", "Garden Grove", "Placentia", "Yorba Linda", "Buena Park"],
        "note": "",
    },
    {
        "rank": 11, "name": "Stockton", "slug": "stockton", "region": "cv", "cost": "none",
        "searches": "10", "found": 12, "active": 10, "wave": 2,
        "dept": "Community Development Department, Building and Life Safety Division",
        "permit": "Building permit", "fee": "$97.25 (FY 2026-27)",
        "doc": "Form BLDG-0014",
        "doc_url": "https://www.stocktonca.gov/Documents/Business/Building%20%26%20Life%20Safety/Building%20Forms/BLDG-0014_SWIMMING%20POOL%20DEMOLITION%20REQUIREMENTS.pdf",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Stockton has one of the best-documented pool permits in this directory. The Community Development Department issues "
            "a building permit priced at $97.25 for fiscal year 2026-27, and {doc} sets out two options. Option A leaves "
            "the shell with four holes in the bottom and the top two feet of wall removed. Option B removes the pool and "
            "replaces it with engineered fill. The form names the A, C-12 and C-53 licence classes, and owner-builders "
            "may pull Option A."
        ),
        "method_html": (
            "Stockton's Option A and Option B set out the choice more clearly than any other city. Option A is the "
            "cheaper partial fill-in for a yard staying as landscape. Option B, full removal with engineered fill, is "
            "the route for anyone planning to build there. Stockton allows pool water to the sewer clean-out only."
        ),
        "faqs": [
            ("What does a Stockton pool removal permit cost?",
             "$97.25 for fiscal year 2026-27, a lower fee than any city except Elk Grove, which charges $85."),
            ("What is the difference between Stockton's Option A and Option B?",
             "Option A leaves the shell with four holes and the top two feet removed; Option B removes it with engineered fill."),
            ("Where does Stockton pool water go?",
             "To the sewer clean-out only; Stockton does not allow it in the storm drain."),
        ],
        "nearby": ["Lodi", "Manteca", "Lathrop", "Tracy", "French Camp", "Morada"],
        "note": "",
    },
    {
        "rank": 12, "name": "Riverside", "slug": "riverside", "region": "ie", "cost": "none",
        "searches": "10", "found": 7, "active": 2, "wave": 2,
        "dept": "Building and Safety Division",
        "permit": "Demolition permit", "fee": "$125 plus $41 issuance (FY 2026-27, general line)",
        "doc": "pool demolition handout (2015)",
        "doc_url": "https://riversideca.gov/cedd/sites/riversideca.gov.cedd/files/pdf/building/forms_handouts/inspections/2019/SWIMMING-POOL-DEMOLITION.pdf",
        "confidence": "Medium", "rules": "published",
        "permit_html": (
            "Riverside's Building and Safety Division issues a demolition permit, with a general fee line of $125 plus "
            "$41 issuance for fiscal year 2026-27. The city's {doc} requires the shell to be cut 12 inches below grade "
            "and an engineer's report showing 90% compaction. Riverside allows pool water to the sewer clean-out only."
        ),
        "method_html": (
            "Riverside's handout requires an engineer's compaction report, so a compaction engineer's fee of $1,500 to "
            "$4,000 belongs in most Riverside budgets. With the engineering already paid for, the gap between a partial "
            "fill-in and full removal narrows, and full removal keeps the yard open for later building."
        ),
        "faqs": [
            ("What does a Riverside pool demolition permit cost?",
             "The general demolition line is $125 plus $41 issuance for 2026-27."),
            ("How far down must a Riverside pool shell be cut?",
             "12 inches below grade, with an engineer's report showing 90% compaction."),
            ("Where can Riverside pool water be drained?",
             "To the sewer clean-out only."),
        ],
        "nearby": ["Moreno Valley", "Corona", "Jurupa Valley", "Norco", "Grand Terrace", "Perris"],
        "note": "",
    },
    {
        "rank": 13, "name": "Irvine", "slug": "irvine", "region": "oc", "cost": "oc",
        "searches": "50", "found": 17, "active": 8, "wave": 1,
        "dept": "Community Development Department, Building and Safety",
        "permit": "Building permit", "fee": "Minimum fees; amount not published",
        "doc": "pool removal page (Bulletin 217)",
        "doc_url": "https://cityofirvine.gov/building-permits-and-inspections/removing-single-family-residential-swimming-pool-or-spa",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Irvine's Building and Safety division issues a building permit at minimum fees, though the amount is not "
            "published. The city's {doc} requires the plans to state whether the fill is non-structural (landscaping) or "
            "structural (a building pad). Holes of at least 12 inches go through the bottom at six feet on centre, and a "
            "soils engineer supervises the backfill to 90% and supplies a final compaction report."
        ),
        "method_html": (
            "Irvine asks the owner to choose at the plan stage: landscaping or building pad. A building pad needs full "
            "removal and engineer-supervised fill; landscaping allows a partial fill-in. Many Irvine homes sit under "
            "homeowners association rules, which may add their own approval step."
        ),
        "faqs": [
            ("What must Irvine pool removal plans show?",
             "Whether the area becomes landscaping or a building pad; a soils engineer supervises the backfill."),
            ("What does an Irvine pool removal permit cost?",
             "Minimum building permit fees apply; the city does not publish the amount."),
            ("What do Orange County contractors charge?",
             "Published Orange County prices run $12,000 to $20,000 partial and $18,000 to $30,000 or more for full removal."),
        ],
        "nearby": ["Tustin", "Lake Forest", "Costa Mesa", "Newport Beach", "Laguna Hills", "Santa Ana"],
        "note": "",
    },
    {
        "rank": 14, "name": "Santa Ana", "slug": "santa-ana", "region": "oc", "cost": "oc",
        "searches": "Under 10", "found": 16, "active": 8, "wave": 2,
        "dept": "Planning and Building Agency, Building Safety Division",
        "permit": "Building, electrical and plumbing permits", "fee": "No pool line published",
        "doc": "Handout BLD-16",
        "doc_url": "https://santa-ana.gov/documents/abandoned-pools-bld-16/",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Santa Ana's Planning and Building Agency requires building, electrical and plumbing permits for pool "
            "removal, since the pump, lighting and lines are disconnected along with the shell. {doc} requires five "
            "3-ft holes in the bottom and removal of the bond beam when a shell stays. The fee schedule has no pool line."
        ),
        "method_html": (
            "Santa Ana's partial route is demanding: five 3-ft openings and the bond beam removed. Owners planning any "
            "future structure on the area should budget for full removal with compacted fill instead."
        ),
        "faqs": [
            ("How many permits does Santa Ana pool removal need?",
             "Three: building, electrical and plumbing permits, under {doc}."),
            ("What does Santa Ana require for a shell left in place?",
             "Five 3-ft holes in the bottom and removal of the bond beam."),
            ("What do Orange County contractors charge?",
             "Frisch &amp; Sons publishes $12,000 to $20,000 partial and $18,000 to $30,000 or more full."),
        ],
        "nearby": ["Tustin", "Orange", "Garden Grove", "Costa Mesa", "Fountain Valley", "Irvine"],
        "note": "",
    },
    {
        "rank": 15, "name": "Chula Vista", "slug": "chula-vista", "region": "sd", "cost": "sd",
        "searches": "Under 10", "found": 15, "active": 9, "wave": 2,
        "dept": "Development Services Department",
        "permit": "Demolition permit", "fee": "$404 (Sept 2024)",
        "doc": "demolition permit page",
        "doc_url": "https://www.chulavistaca.gov/departments/development-services/do-you-need-a-permit/city-permits/demolitionpermit",
        "confidence": "Medium", "rules": "fee-only",
        "permit_html": (
            "Chula Vista's Development Services Department issues a demolition permit, with a fee of $404 on the "
            "September 2024 schedule that needs a recheck. The city's {doc} requires a waste management report before the "
            "permit is issued but publishes no technical rules for pools."
        ),
        "method_html": (
            "Chula Vista publishes no rule on what may stay in the ground, so the Development Services Department "
            "confirms whether a partial fill-in is accepted. The San Diego bulletin, which most contractors working "
            "both cities follow, requires a soils compaction report for pools deeper than five feet."
        ),
        "faqs": [
            ("What does a Chula Vista pool demolition permit cost?",
             "$404 on the September 2024 schedule; confirm the current fee with the city."),
            ("What does Chula Vista require before the permit?",
             "A waste management report for the demolition debris."),
            ("Do San Diego contractors work in Chula Vista?",
             "Yes. Most Chula Vista listings also serve San Diego."),
        ],
        "nearby": ["National City", "Bonita", "Imperial Beach", "San Diego", "Otay Mesa", "Spring Valley"],
        "note": "",
    },
    {
        "rank": 16, "name": "Fremont", "slug": "fremont", "region": "bay", "cost": "bay",
        "searches": "10", "found": 32, "active": 19, "wave": 2,
        "dept": "Community Development Department, Building and Safety",
        "permit": "Express building permit", "fee": "$252 flat (Nov 2024)",
        "doc": "permit types page",
        "doc_url": "https://www.fremont.gov/government/departments/community-development/planning-building-permit-services/planning-building-permits/permit-types",
        "confidence": "Medium", "rules": "fee-only",
        "permit_html": (
            "Fremont's Building Division handles pool removal as an express building permit with a flat fee of $252 on "
            "the November 2024 schedule, which needs a recheck. The city's {doc} lists the work as inspection only, "
            "with no plan review, and publishes no technical rules for the fill."
        ),
        "method_html": (
            "Fremont's express permit makes either route quick to start. Because no technical rules are published, the "
            "inspector's expectations decide the partial option, and engineered compaction is the safe choice for any "
            f'area that may hold a structure later. Bay Area jobs also need a <a href="{SRC["baaqmd"]}">Bay Area Air '
            "Quality Management District</a> notice."
        ),
        "faqs": [
            ("What does a Fremont pool removal permit cost?",
             "$252 flat for an express permit on the November 2024 schedule; confirm the current amount."),
            ("Does Fremont require plan review?",
             "No. The express permit is inspection only, with no plan review."),
            ("What do Bay Area contractors charge?",
             "Souza &amp; Son's publishes $4,500 to $10,000 partial and $8,000 to $22,000 full for a 15 by 30 ft pool."),
        ],
        "nearby": ["Newark", "Union City", "Milpitas", "Hayward", "Pleasanton", "Sunol"],
        "note": "",
    },
    {
        "rank": 17, "name": "Santa Clarita", "slug": "santa-clarita", "region": "la", "cost": "la",
        "searches": "Under 10", "found": 14, "active": 5, "wave": 3,
        "dept": "Building and Safety Division",
        "permit": "Building permit (abandonment)", "fee": "Not published",
        "doc": "information bulletins",
        "doc_url": "https://santaclarita.gov/building-safety/info-bulletins-details/",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Santa Clarita's Building and Safety Division issues a building permit for pool abandonment, described in "
            "the city's {doc}. A pool left in place is permanently recorded as an abandoned structure on the property. "
            "The city publishes no fee for the permit."
        ),
        "method_html": (
            "The permanent record is the deciding factor in Santa Clarita. A partial fill-in leaves an abandoned "
            "structure on file for every later buyer, while full removal with compacted fill clears it. Hillside lots "
            "common in the valley also favour engineered compaction."
        ),
        "faqs": [
            ("Does Santa Clarita record a filled-in pool?",
             "Yes. A pool left in place is permanently recorded as an abandoned structure."),
            ("Which permit covers pool removal in Santa Clarita?",
             "A building permit for abandonment, described in the city's {doc}."),
            ("Must a recorded pool be disclosed on sale?",
             "The state seller disclosure form asks about fill on the property, and the city record is public."),
        ],
        "nearby": ["Valencia", "Newhall", "Saugus", "Canyon Country", "Castaic", "Stevenson Ranch"],
        "note": "",
    },
    {
        "rank": 18, "name": "San Bernardino", "slug": "san-bernardino", "region": "ie", "cost": "none",
        "searches": "Under 10", "found": 9, "active": 3, "wave": 3,
        "dept": "Community and Economic Development Department",
        "permit": "Treated as on-site grading", "fee": "Based on cubic yards of fill",
        "doc": "pool demolition handout (2017)",
        "doc_url": "https://www.sanbernardino.gov/DocumentCenter/View/518/Swimming-Pool-Demo-Req-PDF",
        "confidence": "Medium", "rules": "published",
        "permit_html": (
            "San Bernardino treats pool removal as on-site grading, so the fee is based on the cubic yards of fill. The "
            "city's {doc} requires 12-inch holes every 6 ft across the bottom and the top two feet of wall cut down "
            "when the shell stays."
        ),
        "method_html": (
            "San Bernardino's fill-based fee means a full removal, which takes 80 to 150 cubic yards of fill, costs more "
            "in permit fees as well as dirt. A partial fill-in uses less fill and suits a yard staying as landscape."
        ),
        "faqs": [
            ("How is the San Bernardino pool permit fee set?",
             "By the cubic yards of fill, since the city treats pool removal as on-site grading."),
            ("What does San Bernardino require for a shell left in place?",
             "12-inch holes every 6 ft across the bottom and the top two feet of wall removed."),
            ("What does pool removal cost in San Bernardino?",
             "No local prices are published; statewide contractor ranges apply."),
        ],
        "nearby": ["Highland", "Rialto", "Colton", "Loma Linda", "Redlands", "Fontana"],
        "note": "",
    },
    {
        "rank": 19, "name": "Modesto", "slug": "modesto", "region": "cv", "cost": "none",
        "searches": "10", "found": 10, "active": 8, "wave": 2,
        "dept": "Community and Economic Development Department, Building Safety Division",
        "permit": "Demolition permit (inferred)", "fee": "$301 (FY 2026-27, general line)",
        "doc": "building fee schedule",
        "doc_url": "https://www.modestogov.com/3308/Building-Safety-Fees",
        "confidence": "Low", "rules": "none",
        "permit_html": (
            "Modesto publishes no rule specific to pool removal. The city's {doc} shows a general demolition line of "
            "$301 for fiscal year 2026-27, which is the likely permit, and Building Safety confirms the type and any "
            "engineering it expects for the fill."
        ),
        "method_html": (
            "Without a published pool rule, Modesto owners should ask Building Safety whether a partial fill-in is "
            "accepted. Nearby Stockton's Option A and Option B are a useful guide to what a Central Valley inspector "
            "is likely to expect."
        ),
        "faqs": [
            ("Does Modesto publish pool removal rules?",
             "No. The general demolition line of $301 for 2026-27 is the likely permit; Building Safety confirms it."),
            ("What does pool removal cost in Modesto?",
             "No local prices are published; statewide contractor ranges apply."),
            ("Do Stockton contractors work in Modesto?",
             "Several do; one named in the research serves Sacramento, Stockton and Modesto."),
        ],
        "nearby": ["Ceres", "Riverbank", "Salida", "Turlock", "Oakdale", "Empire"],
        "note": "",
    },
    {
        "rank": 20, "name": "Fontana", "slug": "fontana", "region": "ie", "cost": "none",
        "searches": "Under 10", "found": 9, "active": 3, "wave": 3,
        "dept": "Department of Building and Safety",
        "permit": "Demolition permit", "fee": "$120 (2023 schedule)",
        "doc": "pool demolition handout (2026)",
        "doc_url": "https://www.fontanaca.gov/DocumentCenter/View/48412/Demolition-of-Swimming-Pool-or-Spa-PDF",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Fontana's Department of Building and Safety issues a demolition permit, priced at $120 on the 2023 schedule, "
            "which needs a recheck. The city's {doc} requires six 1-ft openings in the bottom and the top two feet of "
            "wall removed when the shell stays. The handout also states directly that building over the area needs "
            "the shell removed and the fill compacted and certified."
        ),
        "method_html": (
            "Fontana's handout says plainly what most cities imply: a structure may go over a former pool only where "
            "the shell was removed and the fill compacted to 90% and certified by an engineer. A partial fill-in with "
            "six openings suits a yard that stays as landscape."
        ),
        "faqs": [
            ("What does a Fontana pool demolition permit cost?",
             "$120 on the 2023 schedule; confirm the current fee with the city."),
            ("Can a Fontana homeowner build over a filled pool?",
             "Only where the shell was removed and the fill compacted and certified, as the {doc} states."),
            ("What does Fontana require for a shell left in place?",
             "Six 1-ft openings in the bottom and the top two feet of wall removed."),
        ],
        "nearby": ["Rialto", "Rancho Cucamonga", "Ontario", "San Bernardino", "Bloomington", "Eastvale"],
        "note": "",
    },
]


# Cities 21 to 32 (fourth wave), from the workbook's Cities tab, checked 11 October 2026.
# title_name adds "CA" where searches return other places with the same name.
CITIES += [
    {
        "rank": 21, "name": "Moreno Valley", "slug": "moreno-valley", "region": "ie", "cost": "none",
        "searches": "Under 10", "found": 8, "active": 2, "wave": 4,
        "dept": "Community Development Department, Building and Safety Division",
        "permit": "Demolition permit",
        "fee": "$153 plan check plus $347 inspection (2026-27, general demolition line)", "fee_short": "$500",
        "doc": "pool and spa demolition handout (2022)",
        "doc_url": "https://moval.gov/city_hall/forms/building-safety/SwimmingPools-Spa-DemoRequirements.pdf",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Moreno Valley's Building and Safety Division issues a demolition permit for pools and spas, and the city's "
            "{doc} sets out two options. The general demolition fee line for 2026-27 is $153 for plan check and $347 for "
            "inspection; the schedule has no pool-specific line. Option A leaves the shell: three holes of at least 2 ft "
            "go through the bottom, at least 12 inches of #4 rock is placed, the coping and bond beam come off to at "
            "least 18 inches below grade, and the fill is compacted to 90% under a geotechnical consultant. Option B "
            "removes the whole shell and backfills with engineered fill in lifts of no more than 8 inches, with a "
            "stamped geotechnical report. Every job has at least two inspections."
        ),
        "method_html": (
            "Moreno Valley ties Option A to a signed acknowledgement: the owner agrees to keep the area as open space, "
            "landscape or garden, and to disclose it on sale. Option B is required if anything will be built on the "
            "area. Both options need a geotechnical consultant, so the engineering cost sits in every Moreno Valley job."
        ),
        "faqs": [
            ("What does Moreno Valley require to leave a pool shell in place?",
             "Three holes of at least 2 ft in the bottom, 12 inches of #4 rock, the bond beam removed to 18 inches below grade and 90% compaction."),
            ("Does Moreno Valley record a filled-in pool?",
             "The owner signs an acknowledgement limiting the area to open space, landscape or garden use and disclosing it on sale."),
            ("What does the Moreno Valley demolition permit cost?",
             "The general demolition line for 2026-27 is $153 for plan check plus $347 for inspection."),
        ],
        "nearby": ["Riverside", "Perris", "Beaumont", "Banning", "March Air Reserve Base area", "Lake Perris"],
        "note": "Six of the listings found for Moreno Valley come only from a named region, so the city list is thin.",
    },
    {
        "rank": 22, "name": "Oxnard", "slug": "oxnard", "region": "ven", "cost": "none",
        "searches": "Under 10", "found": 5, "active": 4, "wave": 4,
        "dept": "Community Development Department, Building and Engineering Division",
        "permit": "General demolition permit (no pool rule)",
        "fee": "$147 or $88.20 general demolition lines (July 2026)", "fee_short": "$88.20–$147",
        "doc": "B100 development fee schedule",
        "doc_url": "https://www.oxnard.gov/wp-content/uploads/b100-fees-charged-to-dev-7-18-2026.pdf",
        "confidence": "Low", "rules": "none",
        "permit_html": (
            "Oxnard publishes no pool demolition or abandonment handout. Demolition work in the city needs a demolition "
            "permit from the Building and Engineering Division, and the city's {doc}, effective 18 July 2026, lists a "
            "$147 fee for building demolition inspections and $88.20 for accessory structures and similar items. Which "
            "line applies to a pool is not stated, and no city document sets drainage holes, shell depth or compaction "
            "rules."
        ),
        "method_html": (
            "With no published rule, the Building and Engineering Division decides whether a partial fill-in is "
            "accepted in Oxnard. Most California cities that allow one limit the area to landscaping, and Moreno "
            "Valley and Santa Rosa both require a signed acknowledgement of that limit. Full removal with compacted, "
            "engineer-certified fill is the safe choice where anything may be built later."
        ),
        "faqs": [
            ("Does Oxnard publish pool removal rules?",
             "No. Oxnard has no pool demolition handout; the Building and Engineering Division confirms the permit and fill standard."),
            ("What does an Oxnard demolition permit cost?",
             "The July 2026 schedule lists $147 for building demolition and $88.20 for accessory structures; the pool line is not stated."),
            ("What does pool removal cost in Oxnard?",
             "No Ventura County contractor publishes prices; statewide contractor ranges apply."),
        ],
        "nearby": ["Ventura", "Camarillo", "Port Hueneme", "El Rio", "Santa Paula", "Thousand Oaks"],
        "note": "",
    },
    {
        "rank": 23, "name": "Glendale", "title_name": "Glendale CA", "slug": "glendale", "region": "la", "cost": "la",
        "searches": "Under 10", "found": 15, "active": 6, "wave": 4,
        "dept": "Community Development Department, Building and Safety Section",
        "permit": "Building demolition permit", "fee": "Not published",
        "doc": "permit application guidance page",
        "doc_url": "https://www.glendaleca.gov/government/departments/community-development/development-services/permit-guidance",
        "confidence": "Low", "rules": "none",
        "permit_html": (
            "Glendale publishes no pool-specific permit. The city's {doc} says demolition permits are applied for as "
            "\"Building Demo\" in the GlendalePermits portal, with a site plan, a renovation-demolition acknowledgement "
            "form and a lead abatement acknowledgement. Pool backfill projects also need Design Review from Planning, "
            "and the backfilled area must stay as landscaping under the city's water efficient landscape rules or meet "
            "all zoning development standards. No fee line for pool demolition was found."
        ),
        "method_html": (
            "Glendale's Design Review step applies to any pool backfill, so the Planning review sits on the schedule "
            "whichever method is chosen. Glendale publishes no rules on holes, shell removal or compaction, so the "
            "Building and Safety Section confirms what it expects. A backfilled area kept as landscaping must meet the "
            "water efficient landscape rules."
        ),
        "faqs": [
            ("Does Glendale require Design Review to fill in a pool?",
             "Yes. Pool backfill projects need Design Review from Planning, and the area must stay landscaping or meet zoning standards."),
            ("How is a Glendale pool demolition permit applied for?",
             "As \"Building Demo\" in the GlendalePermits portal, with a site plan and the demolition and lead abatement acknowledgements."),
            ("Is this Glendale, California or Glendale, Arizona?",
             "Glendale, California, in Los Angeles County; searches often mix in Glendale, Arizona."),
        ],
        "nearby": ["Burbank", "Pasadena", "La Cañada Flintridge", "Montrose", "Eagle Rock", "Atwater Village"],
        "note": "",
    },
    {
        "rank": 24, "name": "Huntington Beach", "slug": "huntington-beach", "region": "oc", "cost": "oc",
        "searches": "40", "found": 17, "active": 10, "wave": 4,
        "dept": "Community Development Department, Building Division",
        "permit": "Demolition permit",
        "fee": "$41 processing plus valuation-based inspection (July 2026)", "fee_short": "$41 + inspection",
        "doc": "pool demolition guidelines (2025)",
        "doc_url": "https://www.huntingtonbeachca.gov/Documents/Departments/Community%20Development/Building%20Inspections/Permit%20Centre/Applications%20&%20Forms/Additional%20Information%20&%20Forms/Guidelines%20for%20Swimming%20Pool%20Demolition.pdf",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Huntington Beach's Building Division issues a demolition permit for pools, and the city's {doc} set the "
            "procedure. The application needs a plot plan and a preliminary report from a licensed soils engineer "
            "describing how the pool will be demolished or abandoned. Holes go through the bottom, the decking and bond "
            "beam come off to within 12 inches below grade, electrical conduit and gas lines are removed, at least 6 "
            "inches of 3/4-inch gravel goes on the bottom, and the backfill is placed in 12-inch compacted lifts. A "
            "soils compaction report showing at least 90% is required. The fee is the general $41 processing charge "
            "plus inspection fees from the valuation table."
        ),
        "method_html": (
            "Huntington Beach's guidelines describe leaving the shell bottom in place with drain holes and state no "
            "use restriction. Because the soils engineer's report and 90% compaction apply either way, a full removal "
            "adds mainly hauling and fill cost. Three inspections cover the bottom and bond beam removal, utility "
            "disconnection, and final grade with the compaction report."
        ),
        "faqs": [
            ("Does Huntington Beach require a soils engineer?",
             "Yes. A preliminary soils report comes with the application and a compaction report showing at least 90% before final."),
            ("How many inspections does a Huntington Beach pool demolition need?",
             "Three: bottom and bond beam removal, utility disconnection, and final grade with the compaction report."),
            ("What do Orange County contractors charge?",
             "Frisch &amp; Sons publishes $12,000 to $20,000 partial and $18,000 to $30,000 or more for full removal."),
        ],
        "nearby": ["Fountain Valley", "Westminster", "Costa Mesa", "Seal Beach", "Newport Beach", "Sunset Beach"],
        "note": "Huntington Beach has the joint-highest search demand of cities 21 to 32.",
    },
    {
        "rank": 25, "name": "Elk Grove", "slug": "elk-grove", "region": "cv", "cost": "sac",
        "searches": "Under 10", "found": 8, "active": 4, "wave": 4,
        "dept": "Building Safety, Inspection and Permits",
        "permit": "Demolition permit", "fee": "$85 pool and spa demolition (July 2026)",
        "doc": "Policy B-26-41",
        "doc_url": "https://elkgrove.gov/residential-pools-patio-covers-and-storage-sheds/residential-swimming-pool-demolition",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Elk Grove is the only city in this directory with a pool-specific fee: $85 for pool and spa demolition, "
            "including utility capping, in the July 2026 fee booklet. The city's {doc} sets the rules. A Public Works "
            "encroachment permit at a flat $250 may be needed first, and a stormwater debris-tracking permit is "
            "required. Full removal is required if a building will go over or within 5 feet of the pool, with backfill "
            "under a soils engineer to at least 90% and a compaction report approved before final."
        ),
        "method_html": (
            "Abandoning a pool in place in Elk Grove means removing the bond beam and shell to at least 18 inches deep, "
            "capping drains, cutting two holes of at least 3 by 3 feet at the deep and shallow ends, and filling with "
            "sandy soil in 6-inch compacted layers under city inspection. The city then places a building restriction on "
            "the property: no construction in the pool area or within 5 feet. Full removal avoids that restriction."
        ),
        "faqs": [
            ("What does an Elk Grove pool demolition permit cost?",
             "$85 for pool and spa demolition including utility capping, in the July 2026 fee booklet."),
            ("When does Elk Grove require full removal?",
             "When a building will go over or within 5 feet of the pool."),
            ("Does Elk Grove restrict building over an abandoned pool?",
             "Yes. The city places a building restriction on the property covering the pool area and 5 feet around it."),
        ],
        "nearby": ["Sacramento", "Laguna", "Galt", "Rancho Murieta", "Wilton", "Florin"],
        "note": "The city's permit page ranks first in Google for pool removal in Elk Grove.",
    },
    {
        "rank": 26, "name": "Ontario", "title_name": "Ontario CA", "slug": "ontario", "region": "ie", "cost": "none",
        "searches": "Under 10", "found": 10, "active": 2, "wave": 4,
        "dept": "Building Department",
        "permit": "Building permit", "fee": "Valuation-based; not pool-specific (July 2026)",
        "doc": "Information Bulletin 111",
        "doc_url": "https://ontarioca.gov/sites/default/files/Ontario-Files/Building/IB%20111%20%28demolition%20of%20swimming%20pool%20%26%20spa%20Requirements%29-eff%2010-16-2024.docx",
        "confidence": "Medium", "rules": "published",
        "permit_html": (
            "Ontario's Building Department issues a building permit for pool and spa demolition through its Citizen "
            "Portal, with plan review. {doc}, effective 16 October 2024, requires the entire shell removed along with "
            "the above-ground equipment, gas lines capped and the electrical subpanel and conductors removed. The fill "
            "is self-compacting material such as sand, or clean dirt compacted to at least 90%, shown on a to-scale "
            "site plan. Fees follow the city's valuation-based building permit table."
        ),
        "method_html": (
            "Ontario allows only one route: the whole shell comes out. Abandonment in place is not addressed in the "
            "bulletin, so a partial fill-in is not an option without the Building Department's approval. Sand fill, "
            "which compacts itself, can avoid compaction testing, a cost worth comparing against clean dirt."
        ),
        "faqs": [
            ("Can a pool be filled in place in Ontario, California?",
             "No. {doc} requires the entire shell removed; abandonment in place is not addressed."),
            ("What fill does Ontario accept?",
             "Self-compacting fill such as sand, or clean dirt compacted to at least 90%."),
            ("Is this Ontario, California or Ontario, Canada?",
             "Ontario, California, in San Bernardino County; searches often show Ontario, Canada."),
        ],
        "nearby": ["Rancho Cucamonga", "Upland", "Montclair", "Chino", "Fontana", "Eastvale"],
        "note": "",
    },
    {
        "rank": 27, "name": "Santa Rosa", "slug": "santa-rosa", "region": "bay", "cost": "bay",
        "searches": "10", "found": 6, "active": 4, "wave": 4,
        "dept": "Planning and Economic Development Department, Building Division",
        "permit": "Building permit",
        "fee": "$50.10 plan check plus $200.38 inspection (2026, minor demolition)", "fee_short": "$250.48",
        "doc": "Policy 2.5.30",
        "doc_url": "https://www.srcity.org/documentcenter/view/20379",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Santa Rosa's Building Division issues a building permit for pool and spa removal, and {doc}, effective "
            "20 April 2016, sets out two options. The 2026 fee schedule lists minor demolition at $50.10 for plan check "
            "and $200.38 for inspection, and major demolition at $50.10 and $300.56; which category a pool falls under "
            "is not stated. Pool water goes to the sanitary sewer, not the storm drain, and every job has at least two "
            "inspections."
        ),
        "method_html": (
            "Santa Rosa's Option A suits an area staying as landscape or open space: the shell stays below grade, at "
            "least three 1-ft holes go through the bottom, 15 inches of drain rock goes in, the top 2 feet of shell "
            "comes off, and the top 24 inches of fill is clean soil. The owner signs an acknowledgement to use the area "
            "as open space only and to disclose it on sale. Option B, for anything built or paved there, removes the "
            "whole shell with a geotechnical report and fill in 8-inch lifts compacted to at least 90%."
        ),
        "faqs": [
            ("What does Santa Rosa require to leave a pool shell?",
             "Three 1-ft holes, 15 inches of drain rock, the top 2 feet removed and a signed open-space acknowledgement."),
            ("Where does Santa Rosa pool water go?",
             "To the sanitary sewer, not the storm drain."),
            ("What does a Santa Rosa pool removal permit cost?",
             "Minor demolition is $50.10 plan check plus $200.38 inspection on the 2026 schedule; the pool category is not stated."),
        ],
        "nearby": ["Rohnert Park", "Windsor", "Sebastopol", "Healdsburg", "Petaluma", "Kenwood"],
        "note": "",
    },
    {
        "rank": 28, "name": "Lancaster", "title_name": "Lancaster CA", "slug": "lancaster", "region": "la", "cost": "none",
        "searches": "Under 10", "found": 12, "active": 5, "wave": 4,
        "dept": "Development Services, Building and Safety",
        "permit": "General demolition permit (no pool rule)", "fee": "Not published",
        "doc": "Building and Safety permits page",
        "doc_url": "https://www.cityoflancasterca.org/our-city/departments-services/development-services/city-engineering/building-and-safety/permits",
        "confidence": "Low", "rules": "none",
        "permit_html": (
            "Lancaster publishes no pool removal rule. The city's {doc} states that a demolition permit is needed to "
            "demolish any structure that required a permit, and pools do. The demolition application asks for an "
            "Antelope Valley Air Quality Management District demolition notification and a Desert Region asbestos "
            "questionnaire along with the permit application. No fee line for pool removal was found."
        ),
        "method_html": (
            "With no published pool rule, Building and Safety decides whether a partial fill-in is accepted in "
            "Lancaster. Neighbouring Palmdale's code defines demolition to include filling the excavation, which "
            "suggests the Antelope Valley cities treat the fill as part of the permitted work."
        ),
        "faqs": [
            ("Does Lancaster publish pool removal rules?",
             "No. A general demolition permit applies; Building and Safety confirms the fill standard."),
            ("Does Lancaster pool demolition need an air district notice?",
             "Yes. The demolition application includes an Antelope Valley AQMD notification and an asbestos questionnaire."),
            ("Is this Lancaster, California?",
             "Yes, in the Antelope Valley of Los Angeles County; national searches often show Lancaster, Pennsylvania."),
        ],
        "nearby": ["Palmdale", "Quartz Hill", "Rosamond", "Lake Los Angeles", "Antelope Acres", "Littlerock"],
        "note": "Lancaster shares much of its contractor list with Palmdale.",
    },
    {
        "rank": 29, "name": "Rancho Cucamonga", "slug": "rancho-cucamonga", "region": "ie", "cost": "none",
        "searches": "Under 10", "found": 8, "active": 2, "wave": 4,
        "dept": "Building and Safety Services Department",
        "permit": "Pool demolition permit", "fee": "$490 (2026-27, general residential demolition line)",
        "doc": "form BSF-0027",
        "doc_url": "https://www.cityofrc.us/sites/default/files/2026-02/BSF-0027-Swimming%20Pool%20Demolition-E.pdf",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Rancho Cucamonga's Building and Safety Services Department sets its pool procedure in {doc}, revised in "
            "January 2026. The coping and 24 inches of wall come off all around, exposed steel is cut off, at least 40% "
            "of the bottom is removed, and steps and any diving board slab come out. Backfill goes in 24-inch layers "
            "after the inspector approves the preparation, with 90% compaction certified by a licensed geotechnical "
            "engineer, or clean washed sand or 3/8-inch pea gravel with documentation, then a final 12 inches of fill. "
            "The 2026-27 schedule lists residential demolition at $490."
        ),
        "method_html": (
            "Rancho Cucamonga's published method is abandonment: the shell stays with 40% of the bottom removed. The "
            "handout does not address full removal and says nothing about recording the area or making it "
            "non-buildable. Sand or pea gravel fill can replace the engineer's compaction certificate, which changes the "
            "cost comparison."
        ),
        "faqs": [
            ("How much of the pool bottom must come out in Rancho Cucamonga?",
             "At least 40%, along with the coping, 24 inches of wall, steps and any diving board slab."),
            ("Can sand replace a compaction report in Rancho Cucamonga?",
             "Yes. Clean washed sand or 3/8-inch pea gravel with documentation is accepted instead of certified compaction."),
            ("What does the Rancho Cucamonga permit cost?",
             "The 2026-27 schedule lists residential demolition at $490; whether that line applies to pools is not confirmed."),
        ],
        "nearby": ["Upland", "Ontario", "Fontana", "Alta Loma", "Etiwanda", "Claremont"],
        "note": "",
    },
    {
        "rank": 30, "name": "Oceanside", "slug": "oceanside", "region": "sd", "cost": "sd",
        "searches": "10", "found": 15, "active": 9, "wave": 4,
        "dept": "Development Services Department, Building Division",
        "permit": "General demolition permit (no pool rule)", "fee": "$284.55 (2025-26, general demolition permit)",
        "doc": "Informational Bulletin IB 116",
        "doc_url": "https://www.ci.oceanside.ca.us/home/showpublisheddocument/17714/639046801719930000",
        "confidence": "Low", "rules": "none",
        "permit_html": (
            "Oceanside publishes no pool-specific demolition handout. The city's building code requires a permit to "
            "demolish or remove any building or structure, as {doc} on permits and exempted work reflects, and the "
            "Building Division's fee schedule lists a demolition permit at $31.84 for plan check and $252.71 for "
            "inspection, $284.55 in total for 2025-26. No city document sets drainage holes, shell depth or compaction "
            "rules for pools."
        ),
        "method_html": (
            "Without a published pool rule, the Building Division decides what Oceanside accepts. Many Oceanside "
            "contractors also work in San Diego, where Information Bulletin 710 requires a soils compaction report for "
            "pools deeper than five feet, and that standard is a reasonable starting point for a quote."
        ),
        "faqs": [
            ("What does an Oceanside demolition permit cost?",
             "$284.55 for 2025-26: $31.84 plan check plus $252.71 inspection, not pool-specific."),
            ("Does Oceanside publish pool removal rules?",
             "No. The Building Division confirms the fill standard and any engineering required."),
            ("Do San Diego contractors work in Oceanside?",
             "Yes. Most Oceanside listings also serve San Diego."),
        ],
        "nearby": ["Carlsbad", "Vista", "Fallbrook", "Bonsall", "San Marcos", "Camp Pendleton area"],
        "note": "",
    },
    {
        "rank": 31, "name": "Garden Grove", "slug": "garden-grove", "region": "oc", "cost": "oc",
        "searches": "40", "found": 18, "active": 10, "wave": 4,
        "dept": "Community and Economic Development, Building and Safety Division",
        "permit": "Demolition permit", "fee": "Not published",
        "doc": "Information Bulletin 26-012",
        "doc_url": "https://ggcity.org/sites/default/files/swimming-pool-spa-demolition.pdf",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Garden Grove requires a demolition permit for every pool and spa demolition, obtained through the "
            "Development Access portal, and {doc} (2026) sets the method. At least two drainage openings of at least "
            "12 inches go through the bottom, one at the lowest point, and the bottom passes inspection before "
            "backfill. At least 12 inches of No. 4 rock goes in, then clean fill sand in moisture-conditioned lifts. "
            "The fee schedule has no demolition line; only $81 electrical and plumbing pool lines appear. An older, "
            "stricter 2020 policy is still online alongside the 2026 bulletin."
        ),
        "method_html": (
            "Garden Grove's published method leaves the shell with drainage openings. Landscape-only areas need no "
            "compaction testing, and the top 18 inches may be planting soil. Areas for future structures need 90% "
            "relative compaction and a geotechnical compaction report, and no structure may be built on the fill "
            "without a geotechnical foundation investigation."
        ),
        "faqs": [
            ("Does Garden Grove require compaction testing?",
             "Only where a structure may go; landscape-only areas need no compaction testing."),
            ("How many drainage openings does Garden Grove require?",
             "At least two of 12 inches or more, one at the lowest point, inspected before backfill."),
            ("Which Garden Grove pool rule applies?",
             "{doc} from 2026; an older 2020 policy is still online, so confirm with the Building and Safety Division."),
        ],
        "nearby": ["Westminster", "Anaheim", "Santa Ana", "Stanton", "Fountain Valley", "Orange"],
        "note": "Garden Grove has the joint-highest search demand of cities 21 to 32.",
    },
    {
        "rank": 32, "name": "Palmdale", "slug": "palmdale", "region": "la", "cost": "none",
        "searches": "Under 10", "found": 13, "active": 5, "wave": 4,
        "dept": "Building and Safety Division",
        "permit": "General demolition permit (no pool rule)",
        "fee": "$200 or $207.50 demolition inspection (2023 resolution)", "fee_short": "$200–$207.50",
        "doc": "Building and Safety Development Guide",
        "doc_url": "https://www.cityofpalmdaleca.gov/DocumentCenter/View/19916/Building-and-Safety-Development-Guide",
        "confidence": "Low", "rules": "none",
        "permit_html": (
            "Palmdale publishes no pool-specific rule. The city's {doc}, updated January 2026, requires a demolition "
            "permit for each structure demolished in part or whole, and the municipal code defines demolition to "
            "include filling the excavation it leaves. Demolition permits need Antelope Valley Air Quality Management "
            "District approval, a hazardous materials evaluation and a construction waste plan with deposit. The 2023 "
            "fee resolution shows the demolition inspection as both $200 and $207.50."
        ),
        "method_html": (
            "Without a published pool rule, the Building and Safety Division decides whether a partial fill-in is "
            "accepted in Palmdale. Because the code counts the fill as part of the demolition, the inspector will "
            "expect a compaction standard either way; full removal with certified compaction is the route for any "
            "later structure."
        ),
        "faqs": [
            ("Does Palmdale publish pool removal rules?",
             "No. A general demolition permit applies, and the code counts filling the excavation as part of the demolition."),
            ("What does a Palmdale demolition inspection cost?",
             "$200 or $207.50; the 2023 fee resolution shows both figures."),
            ("Do Lancaster contractors work in Palmdale?",
             "Yes. Palmdale shares most of its Antelope Valley contractor list with Lancaster."),
        ],
        "nearby": ["Lancaster", "Quartz Hill", "Littlerock", "Acton", "Lake Los Angeles", "Leona Valley"],
        "note": "",
    },
]


# ---------------------------------------------------------------------------
# City-specific depth for six pages (research of 12 October 2026, official
# sources only). "compact" swaps the shared template paragraphs for one-line
# summaries that link to the cost guide and FAQ, to cut repeated text.
# ---------------------------------------------------------------------------
SRC.update({
    "riv_fees": "https://riversideca.gov/finance/PDF/Fees-and-Charges-as-of-July-1,-2026.pdf",
    "riv_sewer": "https://riversideca.gov/publicworks/sewer/sewer-faq",
    "riv_cd": "https://riversideca.gov/publicworks/trash-recycling/recycling/construction-demolition-0",
    "fon_fees": "https://www.fontanaca.gov/DocumentCenter/View/48598/Fontana-User-Fees-2025-2026",
    "fon_cwmp": "https://www.fontanaca.gov/DocumentCenter/View/36886/Construction-Waste-Management-Plan-CWMP",
    "sbc_storm": "https://sbcountystormwater.org/residents/pool-owners/",
    "sb_fees": "https://www.sanbernardino.gov/DocumentCenter/View/2597/Public-Works-Department---Schedule-of-Fees-2020-PDF",
    "sb_cd": "https://www.sanbernardino.gov/1590/Construction-and-Demolition-CD",
    "sb_storm": "https://www.sanbernardino.gov/DocumentCenter/View/3121/Storm-Water-Drainage-System-PDF",
    "ont_fees": "https://www.ontarioca.gov/government/community-development/building/building-department-fees",
    "ont_cdrp": "https://content.ontarioca.gov/sites/default/files/migrated-files/Ontario-Files/Ontario-WaterWise/Construction%2520%2526%2520Demolition%2520Recycling%2520Plan%2520Packet_0.pdf",
    "ont_rates": "https://content.ontarioca.gov/sites/default/files/2026-07/IW%20Rate%20Sheet%207-1-2026%20-%20External.pdf",
    "ont_pools": "https://content.ontarioca.gov/sites/default/files/2025-01/best_management_practices_for_pool_maintenance.pdf",
    "mod_storm": "https://www.modestogov.com/2627/For-Home",
    "valley_release": "https://valleyair.org/media/suqkle3j/demo_release_form.pdf",
    "valley_8021": "https://ww2.valleyair.org/media/bhfgzedn/rule-8021.pdf",
    "bak_fees": "https://content.civicplus.com/api/assets/ca-bakersfield/6037d14a-6da2-493e-a86d-85a3e3f77ec3",
    "bak_rolloff": "https://content.civicplus.com/api/assets/ca-bakersfield/1e8d4959-59b3-4109-8f7f-b0d0914d6ad6",
    "bak_mtvernon": "https://content.civicplus.com/api/assets/ca-bakersfield/4de286db-80bb-4fa9-b88c-9e0fbc64d982",
    "bak_sewer": "https://bakersfield.municipal.codes/Code/14.12.220",
    "bak_storm": "https://bakersfield.municipal.codes/Code/8.35.020",
    "burrtec": "https://www.burrtec.com/",
    "kern_gate": "https://www.kernpublicworks.com/services/solid-waste/new-gate-fees",
})

STATEWIDE = "about $3,500 to $12,000 for a partial fill-in and $8,000 to $30,000 for a full removal"

CITY_DEPTH = {
    "riverside": {
        "compact": True,
        "fee": "$125 plus $41 issuance, with a 14% surcharge on issuance (FY 2026-27)",
        "fee_short": "$125 + $41",
        "doc": "pool demolition handout (revised October 2015)",
        "lead": ("Pool removal in Riverside needs a demolition permit from the city's Building and Safety Division, "
                 "and Pool Removal California found 7 businesses offering in-ground pool removal there, 2 with an "
                 "active state licence. The city's handout leaves the shell in place, with two 2 ft square holes in "
                 "the floor, the top cut 12 inches below grade and fill compacted to 90%."),
        "permit_html": (
            "Riverside's Building and Safety Division requires a demolition permit to remove a gunite in-ground pool "
            f'or spa. The city\'s <a href="{SRC["riv_fees"]}">fee schedule for 2026-27</a> lists residential '
            "demolition at $125 per structure plus a $41 permit issuance fee, which carries a 14% surcharge, and has "
            "no line written for pools. The city's {doc} asks for a site plan showing the pool and the other "
            "structures on the lot, and it tells owners to consult a geotechnical engineer before starting."),
        "method_html": (
            "Riverside's handout covers one method, a partial removal. Crews break a 2 ft square section out of the "
            "floor at the deepest point and another in the shallow end, or a 1 ft square on a spa, then remove the "
            "coping, gunite and rebar around the whole perimeter to at least 12 inches below grade. The geotechnical "
            "engineer approves the fill, and the engineer's report has to show 90% compaction or better. The handout "
            "warns that following it does not guarantee a future addition will be allowed over the area, so anyone "
            "planning to build there should ask Building and Safety about full removal first."),
        "extra_after_permit": [
            ("Inspections and paperwork on a Riverside job", [
                "Riverside's handout sets the order of the job:",
                "<ol><li>Approval from the Environmental Compliance Division at 951-351-6140 before the pool is "
                "drained.</li><li>Drainage holes broken and the perimeter cut to 12 inches below grade.</li>"
                "<li>Electrical conductors removed at the panel, conduits removed or capped, and the gas line to the "
                "heater capped.</li><li>An inspection by the building inspector, who must authorize backfill before "
                "any fill goes in.</li><li>Fill placed and compacted, with the geotechnical engineer's report showing "
                "90% or better.</li><li>Drainage slopes re-established across the yard, then the final inspection."
                "</li></ol>",
                "The handout is dated October 2015 and does not appear on the city's current forms page, so a call to "
                "Building and Safety confirms it is still the version inspectors use.",
            ]),
        ],
        "cost_html": [
            f"No contractor publishes Riverside prices, so statewide figures apply: {STATEWIDE}. Riverside's own "
            "costs sit on top, starting with the $125 demolition fee and the $41 issuance fee. The geotechnical "
            "engineer the handout requires adds a compaction report, which typically runs $1,500 to $4,000.",
        ],
        "extra_after_cost": [
            ("Hauling the debris in Riverside", [
                f'Riverside\'s <a href="{SRC["riv_cd"]}">construction and demolition recycling page</a> says '
                "recyclable building materials may not go in residential cans. It lists "
                f'<a href="{SRC["burrtec"]}">Burrtec</a> on Agua Mansa Road as '
                "taking clean dirt, concrete and asphalt, and Geo-Engelauf on Market Street as taking concrete and "
                "asphalt. Projects inside the city's construction and demolition program must divert at least 65% of "
                "their debris by weight and file hauler tickets before final inspection. The program ties residential "
                "projects to new or added living space, so Building and Safety confirms whether a pool-only job is "
                "included.",
            ]),
        ],
        "drain_html": (
            "Pool water has to go somewhere before demolition starts. Riverside asks owners to call Environmental "
            f'Compliance at 951-351-6140 before draining, and the city\'s <a href="{SRC["riv_sewer"]}">sewer FAQ</a> '
            "names the home's sewer clean-out as the preferred route. Water may go to the storm drain only when its "
            "chlorine residual is below 0.1 mg/L, and water with hazardous levels of algae or chemicals is pumped out "
            "and hauled away."),
        "faqs": [
            ("What does a Riverside pool demolition permit cost?",
             "$125 for residential demolition plus a $41 issuance fee with a 14% surcharge, on the 2026-27 schedule."),
            ("How far down must a Riverside pool shell be cut?",
             "At least 12 inches below grade around the whole perimeter, with two 2 ft square holes in the floor."),
            ("Where can Riverside pool water be drained?",
             "Call Environmental Compliance at 951-351-6140 first. The sewer clean-out is preferred, and the storm "
             "drain is allowed only below 0.1 mg/L of chlorine."),
            ("Does a Riverside pool removal need an engineer?",
             "Yes. The {doc} tells owners to consult a geotechnical engineer, who approves the fill and signs the "
             "compaction report."),
            ("Can a Riverside homeowner build over a filled pool?",
             "The handout gives no guarantee that a future addition will be allowed, so Building and Safety is the "
             "office to ask about full removal before work starts."),
        ],
    },
    "fontana": {
        "compact": True,
        "fee": "$210 per structure (fee list as of 1 January 2026)",
        "fee_short": "$210",
        "doc": "pool demolition handout (revised January 2026)",
        "opening_extra": (" When the shell stays, the city's handout asks for at least six openings through the floor "
                          "and the top two feet of wall removed."),
        "permit_html": (
            "Fontana's Department of Building and Safety issues a demolition permit for a pool or spa, applied for in "
            "person at the counter Monday through Thursday, 8 AM to 5 PM. The city's "
            f'<a href="{SRC["fon_fees"]}">fee list as of 1 January 2026</a> charges $210 per structure for a '
            "demolition permit, with no separate pool line. The city's {doc} sets out the work for a shell that stays "
            "in the ground and for one that comes out."),
        "method_html": (
            "When the shell stays, Fontana requires at least six openings through the floor, evenly spaced, each at "
            "least one foot square and broken through until earth shows, so water drains away. The top two feet of "
            "wall come off, leaving at least two feet of earth over what remains. When an addition is built, or may "
            "be built later, over the area, the whole shell must come out and the fill must reach at least 90% of "
            "maximum density, with a soils compaction report to certify it."),
        "extra_after_permit": [
            ("Inspections and paperwork on a Fontana job", [
                "Before the inspector arrives, Fontana's handout requires all pool equipment and pool lights removed, "
                "all electrical wire pulled from every conduit run, and the gas supply line capped at each end. The "
                "job then has two inspections:",
                "<ol><li>A pre-backfill inspection, in which a city inspector approves the openings or the removal "
                "before any fill goes in. It is booked at (909) 350-7693.</li><li>A final inspection, booked at "
                "(909) 350-7640 or 1 (800) 511-7691.</li></ol>",
                "The handout does not mention plan check or engineered drawings. It does require the soils compaction "
                "report on any full removal made for an addition.",
            ]),
        ],
        "cost_html": [
            f"No contractor publishes Fontana prices, so statewide figures apply: {STATEWIDE}. Fontana's own costs "
            "sit on top: the $210 demolition permit, Burrtec's bin or haul charges, and on a full removal the soils "
            "compaction report.",
        ],
        "extra_after_cost": [
            ("Hauling the debris in Fontana", [
                f'Fontana routes construction and demolition hauling through <a href="{SRC["burrtec"]}">Burrtec</a>. The city\'s <a href="'
                f'{SRC["fon_cwmp"]}">Construction Waste Management Plan form</a> says no permit is issued without an '
                "approved plan, names Burrtec as the only hauler, requires at least 65% of the debris diverted from "
                "landfill and asks for weigh tickets before final inspection. Residential projects may self-haul only "
                "when the owner owns both the container and the truck. Building and Safety confirms whether a pool "
                "demolition needs the full plan or the city's exemption form.",
            ]),
        ],
        "drain_html": (
            "Pool water has to go somewhere before demolition starts. Fontana is a permittee of the "
            f'<a href="{SRC["sbc_storm"]}">San Bernardino County Stormwater Program</a>, whose guidance for pool '
            "owners asks for chlorine tested at zero after the water stands three to five days, a pH between 6.5 and "
            "8.5 and water free of dirt and algae, with the flow controlled so it does not erode the yard or run onto "
            "a neighbouring property."),
        "faqs": [
            ("What does a Fontana pool demolition permit cost?",
             "$210 per structure on the city's fee list as of 1 January 2026; the list has no separate pool line."),
            ("Can a Fontana homeowner build over a filled pool?",
             "Only after the whole shell is removed and the fill compacted to at least 90% of maximum density, with a "
             "soils compaction report, as the {doc} requires for an addition."),
            ("What does Fontana require for a shell left in place?",
             "At least six evenly spaced openings, each one foot square or larger, and the top two feet of wall "
             "removed under at least two feet of earth."),
            ("How many inspections does a Fontana pool demolition need?",
             "Two: one before backfill, booked at (909) 350-7693, and a final, booked at (909) 350-7640."),
            ("Who hauls pool debris in Fontana?",
             "Burrtec, the city's construction and demolition hauler, unless the homeowner self-hauls in a truck and "
             "container they own."),
        ],
    },
    "san-bernardino": {
        "compact": True,
        "dept": "Public Works Department, Land Development Division",
        "permit": "Land Development activity (grading fees)",
        "fee": "Based on cubic yards; $397.80 plan check over 50 cu yd plus $225 inspection (2020 schedule)",
        "fee_short": "By cubic yard",
        "doc": "pool demolition handout (revised September 2017)",
        "lead": ("Pool removal in San Bernardino is a Land Development activity handled by the Public Works "
                 "Department's Land Development Division, and Pool Removal California found 9 businesses offering "
                 "in-ground pool removal there, 3 with an active state licence. The city's handout leaves the shell "
                 "in place, with 12-inch holes 6 ft apart each way and the top cut at least 2 ft below the surface."),
        "permit_html": (
            "San Bernardino treats a pool demolition as a Land Development activity, handled by the Land Development "
            "Division of the Public Works Department on North E Street. The application needs a site plan giving the "
            "pool's length, width and depth and its distance to existing structures. Fees are based on the cubic "
            f'yards used to fill the pool, and the city\'s <a href="{SRC["sb_fees"]}">Public Works fee '
            "schedule</a>, effective July 2020, lists grading plan check at $397.80 above 50 cubic yards and grading "
            "inspection at $225 for up to 1,000 cubic yards."),
        "method_html": (
            "The {doc} describes one method, in which the shell stays. Crews punch 12-inch holes at 6 ft on center "
            "each way across the bottom and cut the top of the pool down at least 2 ft below the surface. Owners who "
            "want another method, including full removal, submit plans for it to plan check. The handout says nothing "
            "about building over the filled area, so anyone planning a structure there should take that question to "
            "the Land Development Division before choosing a method."),
        "extra_after_permit": [
            ("Choosing the fill in San Bernardino", [
                "The handout gives two fill options, and the choice decides whether an engineer is needed:",
                "<ol><li>Soil only: a soils engineer prepares a compaction report during backfill, and the report is "
                "shown to the inspector at the site inspection.</li><li>Pea gravel (1/4 or 3/8 inch) or sand, with "
                "the top 24 inches backfilled with soil: no compaction report is required.</li></ol>",
                "The gravel or sand route removes the engineer's fee from the job, while soil fill keeps material "
                "costs down, so contractors can price both. Because the fee follows the cubic yards, the fill volume "
                "on the site plan also sets the permit cost.",
            ]),
        ],
        "cost_html": [
            f"No contractor publishes San Bernardino prices, so statewide figures apply: {STATEWIDE}. The city's own "
            "charges come from the 2020 Public Works schedule, $397.80 for grading plan check above 50 cubic yards "
            "and $225 for inspection, plus the soils engineer's report when the pool is filled with soil only.",
        ],
        "extra_after_cost": [
            ("Hauling the debris in San Bernardino", [
                f'San Bernardino\'s <a href="{SRC["sb_cd"]}">construction and demolition program</a> covers all '
                "demolition projects regardless of value and requires 65% of the debris diverted from landfill. "
                "Single-family projects and jobs under $100,000 still meet the 65% target but skip the deposit, the "
                "administrative fee and the waste management plan. "
                f'<a href="{SRC["burrtec"]}">Burrtec</a> holds the exclusive right to haul the '
                "city's waste, and hiring a non-franchised hauler, including for bins, is prohibited. Self-hauling "
                "needs approval, which takes one to two weeks, and the city's approved facilities include the Arcosa "
                "crushed concrete site in Rialto for self-haul loads.",
            ]),
        ],
        "drain_html": (
            f'Pool water has to go somewhere before demolition starts. The city\'s <a href="{SRC["sb_storm"]}">storm '
            "drain ordinance</a> bans draining pool water that contains chlorine or acids, and its list of allowed "
            "discharges includes dechlorinated swimming pool water. The "
            f'<a href="{SRC["sbc_storm"]}">San Bernardino County Stormwater Program</a> asks pool owners to let the '
            "water stand three to five days, test the chlorine at zero, and drain only water with a pH between 6.5 "
            "and 8.5 that is free of dirt and algae."),
        "faqs": [
            ("How is the San Bernardino pool permit fee set?",
             "By the cubic yards of fill. The 2020 Public Works schedule lists $397.80 for grading plan check above 50 "
             "cubic yards and $225 for inspection up to 1,000."),
            ("What does San Bernardino require for a shell left in place?",
             "12-inch holes at 6 ft on center each way across the bottom, and the top cut down at least 2 ft below "
             "the surface."),
            ("Does a San Bernardino pool fill need a compaction report?",
             "Only for soil-only fill. Pea gravel or sand with 24 inches of soil on top needs none."),
            ("Which office handles San Bernardino pool removal?",
             "The Land Development Division of the Public Works Department, on North E Street."),
            ("What does pool removal cost in San Bernardino?",
             "No local prices are published; statewide contractor ranges apply."),
        ],
    },
    "ontario": {
        "compact": True,
        "doc_url": ("https://content.ontarioca.gov/sites/default/files/2025-01/IB%20111%20%28demolition%20of%20"
                    "swimming%20pool%20%26%20spa%20Requirements%29-eff%2010-16-2024.docx"),
        "fee": "Valuation-based; plan check 80% of permit fee, $47.50 minimum",
        "fee_short": "By valuation",
        "opening_extra": (" Ontario requires the entire shell removed, so a partial fill-in is not an option without "
                          "the Building Department's approval."),
        "permit_html": (
            "Ontario's Building Department requires a building permit to demolish or remove an in-ground pool or spa, "
            "applied for through the Citizen Portal, which the city has required since July 2023. A homeowner, a B "
            "general contractor, a C-53 pool contractor or a C-21 demolition contractor may apply. {doc}, effective "
            "16 October 2024, asks for a site plan drawn to scale showing the pool's location, size and depth and its "
            "clearances from property lines, nearby structures and retaining walls. The permit fee follows the "
            f'valuation table on the city\'s <a href="{SRC["ont_fees"]}">building fee page</a>, with plan check at '
            "80% of the permit fee and a minimum permit fee of $47.50."),
        "method_html": (
            "Ontario allows one route: the whole shell leaves the site. The bulletin does not address leaving a shell "
            "in place, so a partial fill-in needs the Building Department's approval before anyone plans on it. The "
            "fill can be self-compacting material such as sand, or clean fill dirt compacted to at least 90% under "
            "the ASTM D1557 test, and the plan must show which."),
        "extra_after_permit": [
            ("Inspections and paperwork on an Ontario job", [
                "The plan goes through a concurrent review by Building, Planning, Engineering, Landscape, OMUC "
                "Environmental and Public Works, and a tracking number is assigned once the plan check fee is paid. A "
                "resubmittal waits until every department has finished its review.",
                "Before the final inspection, {doc} requires:",
                "<ol><li>The shell removed completely from the site.</li><li>All above-ground pool plumbing, "
                "including pumps and heaters, removed.</li><li>The gas line disconnected and capped at the meter and "
                "at the equipment.</li><li>The electrical subpanel and conductors removed back to the service supply."
                "</li><li>The fill placed as the plan shows.</li></ol>",
                "The bulletin names one inspection, the final, which can be booked at (909) 395-2362 or online.",
            ]),
        ],
        "cost_html": [
            "No contractor publishes Ontario prices. Because Ontario allows only full removal, the statewide "
            "full-removal range of about $8,000 to $30,000 is the one to plan around. The city's charges add the "
            "valuation-based permit and plan check, plus hauling: a 7-day bin at $95 and $369.29 for each inert or "
            "construction load on the July 2026 rate sheet.",
        ],
        "extra_after_cost": [
            ("Hauling the debris in Ontario", [
                f'An approved <a href="{SRC["ont_cdrp"]}">Construction and Demolition Recycling Plan</a> is a '
                "condition of any building or demolition permit in Ontario. The plan commits the job to divert at least "
                "65% of its debris and to use the City of Ontario hauling service, unless the contractor self-hauls in "
                "company-owned trucks and containers and keeps weight receipts, and it ends with a final compliance "
                "report to Integrated Waste. The program carries no extra fee. On the city's "
                f'<a href="{SRC["ont_rates"]}">July 2026 rate sheet</a>, a 7-day temporary bin rents for $95, an '
                "inert or construction load adds $369.29 for disposal, and loads over 12 tons pay $115 a ton.",
            ]),
        ],
        "drain_html": (
            f'Pool water has to go somewhere before demolition starts. Ontario\'s <a href="{SRC["ont_pools"]}">pool '
            "maintenance guidance</a> lists three routes: reuse the water on landscaping, send it to the sewer between "
            "midnight and 6 am, or dechlorinate it to zero residual and wait 24 hours before draining to the street or "
            "storm drain. Water treated with metal-based algaecides such as copper sulfate goes to the sewer, and the "
            "city's stormwater rules ban chlorinated water and algae solids from the storm drain."),
        "faqs": [
            ("Can a pool be filled in place in Ontario, California?",
             "No. {doc} requires the entire shell removed; leaving it in place is not addressed."),
            ("What fill does Ontario accept?",
             "Self-compacting fill such as sand, or clean fill dirt compacted to at least 90% under ASTM D1557."),
            ("How is an Ontario pool demolition permit priced?",
             "By project valuation on the city's building fee table, with plan check at 80% of the permit fee and a "
             "$47.50 minimum."),
            ("Who hauls pool debris in Ontario?",
             "The City of Ontario hauling service, unless the contractor self-hauls in its own trucks and containers "
             "and keeps weight receipts."),
            ("Is this Ontario, California or Ontario, Canada?",
             "Ontario, California, in San Bernardino County; searches often show Ontario, Canada."),
        ],
    },
    "modesto": {
        "compact": True,
        "fee": "$301 demolition line; $550 pool line (FY 2026-27)",
        "fee_short": "$301 or $550",
        "permit_html": (
            "Modesto publishes no rule specific to pool removal. The city's {doc} for July 2026 to June 2027 lists a "
            "$301 demolition permit and a separate $550 line for swimming pools of all types, without saying which "
            "covers a removal, so Building Safety on 10th Street (209-577-5232) confirms the permit before work "
            "starts. Applications and inspection requests go through the city's eTRAKiT portal. The municipal code's "
            "section on demolishing buildings requires a bond filed with the City Clerk and notice to the utilities "
            "so gas, electric, sewer and water lines can be capped."),
        "method_html": (
            "Without a pool rule, the code's general demolition section is the closest guide: it requires excavations "
            "filled with dirt or sand to street level within 10 days. A swimming pool covered by a valid building "
            "permit needs no separate grading and erosion control permit. Owners should ask Building Safety whether "
            "a partial fill-in is accepted and whether the area is then limited to landscaping, and nearby "
            '<a href="/stockton/">Stockton\'s published options</a> show what a Central Valley inspector may expect.'),
        "extra_after_permit": [
            ("Air district and code rules in Modesto", [
                "Modesto sits in the San Joaquin Valley Air Pollution Control District. The district's "
                f'<a href="{SRC["valley_release"]}">Demolition Permit Release form</a> must be signed and returned to '
                "the building department before a demolition permit is issued. The form is written for structures, "
                "so Building Safety confirms whether a pool-only job needs it. The district's "
                f'<a href="{SRC["valley_8021"]}">Rule 8021</a> on dust from demolition and excavation calls for a '
                "dust control plan only on residential sites of 10 acres or more or on work moving over 2,500 cubic "
                "yards a day, far above a backyard pool.",
                "The municipal code also lists abandoned swimming pools and spas among attractive nuisances, so an "
                "empty pool left open can be treated as a nuisance under the code.",
            ]),
        ],
        "cost_html": [
            f"No contractor publishes Modesto prices, so statewide figures apply: {STATEWIDE}. Modesto's own charges "
            "add the $301 demolition or $550 pool permit on the 2026-27 schedule, and the city adds 2.4% to card "
            "payments.",
        ],
        "extra_after_cost": [
            ("Hauling the debris in Modesto", [
                "Modesto's municipal code counts rock, concrete, asphalt and dirt from permitted building or "
                "demolition work as construction and demolition debris. The city holds exclusive service agreements "
                "with Bertolotti Disposal Service and Gilton Solid Waste Management, and the code lets businesses doing "
                "demolition or construction cleanup remove the rubbish and salvage their own work produces. The city "
                "adopted the 2025 CALGreen code in June 2026, which sets a 65% diversion target on the projects it "
                "covers.",
            ]),
        ],
        "drain_html": (
            "Pool water has to go somewhere before demolition starts. In Modesto it never goes to the street or storm "
            f'drain, even when dechlorinated: the city\'s <a href="{SRC["mod_storm"]}">stormwater guidance</a> and '
            "municipal code send it to the sanitary sewer through the yard's sewer cleanout, and Environmental "
            "Services takes reports of illegal discharges at 209-577-6200."),
        "faqs": [
            ("Does Modesto publish pool removal rules?",
             "No pool demolition handout exists. The 2026-27 schedule lists a $301 demolition permit and a $550 pool "
             "permit, and Building Safety confirms which applies."),
            ("Can Modesto pool water go to the storm drain?",
             "No. Even dechlorinated pool water goes to the sanitary sewer, usually through the yard's sewer cleanout."),
            ("Who hauls pool debris in Modesto?",
             "Bertolotti Disposal Service and Gilton Solid Waste Management hold the city's service agreements, and "
             "demolition firms may remove the debris their own work produces."),
            ("What does pool removal cost in Modesto?",
             "No local prices are published; statewide contractor ranges apply."),
            ("Do Stockton contractors work in Modesto?",
             "Several do; one named in the research serves Sacramento, Stockton and Modesto."),
        ],
    },
    "bakersfield": {
        "compact": True,
        "fee": "$291 minimum plus project valuation (July 2026)",
        "fee_short": "$291 minimum",
        "doc": "building permit application",
        "doc_url": "https://content.civicplus.com/api/assets/ca-bakersfield/755e6fba-fe20-4bba-9b9e-c44a8fa09756",
        "permit_html": (
            "Bakersfield publishes no rule specific to pool removal. The city's {doc} has separate boxes for pool and "
            "spa work and for demolition, without saying which covers a removal, so the Development Services Building "
            "Division on Chester Avenue (661-326-3720) confirms the permit type. The city's "
            f'<a href="{SRC["bak_fees"]}">fee schedule of 1 July 2026</a> charges a building permit at $291 minimum '
            "plus an amount based on project valuation, with no separate line for demolition or pools."),
        "extra_after_permit": [
            ("Air district rules in Bakersfield", [
                "Bakersfield sits in the San Joaquin Valley Air Pollution Control District, which requires a "
                f'<a href="{SRC["valley_release"]}">Demolition Permit Release form</a> from the district before a '
                "building official issues a demolition permit, and asbestos notification at least 10 working days "
                "ahead of demolition. Both are written for structures, so the Building Division confirms whether a "
                f'pool-only job needs them. The district\'s <a href="{SRC["valley_8021"]}">Rule 8021</a> requires a '
                "dust control plan only on residential sites of 10 acres or more or on work moving over 2,500 cubic "
                "yards a day, far above a backyard pool.",
            ]),
        ],
        "cost_html": [
            f"No contractor publishes Bakersfield prices, so statewide figures apply: {STATEWIDE}. Bakersfield's own "
            "charges add the $291 minimum building permit plus valuation and the haul: a city 15 cubic yard bin for "
            "concrete or dirt costs $149 to deliver and $369.45 a haul before the county gate fee of $95.65 a ton.",
        ],
        "extra_after_cost": [
            ("Hauling the debris in Bakersfield", [
                "Bakersfield limits waste collection to collectors licensed by city contract or franchise, and the "
                "municipal code leaves contractors paid to remove debris out of its self-haul definition. The city's "
                "roll-off service offers a 15 cubic yard bin for dirt, concrete, asphalt or heavy material, limited to "
                f'10 tons a load, on the <a href="{SRC["bak_rolloff"]}">2026-27 rate sheet</a>. The city\'s Mount '
                f'Vernon recycling facility does not take dirt, and its <a href="{SRC["bak_mtvernon"]}">facility '
                "handout</a> points to the Bena Landfill on Neumarkel Road for concrete and demolition debris, priced on "
                f'<a href="{SRC["kern_gate"]}">Kern County\'s gate fee list</a>, and to '
                "Bowman Asphalt and Sturgeon &amp; Son, which take concrete, asphalt and clean dirt at no charge.",
                "The city uses the state CW-1 construction waste management form, which carries the CALGreen target of "
                "at least 65% diversion.",
            ]),
        ],
        "drain_html": (
            "Pool water has to go somewhere before demolition starts. Bakersfield's "
            f'<a href="{SRC["bak_sewer"]}">sewer code</a> bars swimming pool drainage from the public sewer unless '
            f'the city engineer specifically authorizes it, and its <a href="{SRC["bak_storm"]}">stormwater code</a> '
            "bans unsanitary or harmful matter from the storm system. The city publishes no pool-draining guidance, so "
            "the Building Division or the city engineer's office confirms the route before a pool is emptied."),
        "faqs": [
            ("Does Bakersfield publish pool removal rules?",
             "No. The permit application has separate pool and demolition boxes, and the Building Division at "
             "661-326-3720 confirms which applies."),
            ("Can Bakersfield pool water go down the sewer?",
             "Only with the city engineer's specific authorization; the municipal code otherwise bars pool drainage "
             "from the public sewer."),
            ("Where does pool concrete go in Bakersfield?",
             "The Bena Landfill accepts concrete and demolition debris, and Bowman Asphalt and Sturgeon &amp; Son take "
             "concrete, asphalt and clean dirt."),
            ("What does pool removal cost in Bakersfield?",
             "No local prices are published; statewide contractor ranges run $3,500 to $12,000 partial and $8,000 to "
             "$30,000 full."),
            ("How many contractors serve Bakersfield?",
             "Five businesses were found, two with an active state licence; more are being checked by phone."),
        ],
    },
}

for _c in CITIES:
    _c.update(CITY_DEPTH.get(_c["slug"], {}))


# ---- Batch 2 (research of 12 October 2026) --------------------------------
SRC.update({
    "oak_moratorium": "https://www.oaklandca.gov/Planning-Building/Building-Construction-Permits-Inspections/Building-Inspections/Wet-Weather-Grading-Moratorium",
    "oak_demo": "https://www.oaklandca.gov/My-Household/Building-and-Remodeling/Homeowner-Projects-Permits/Demolition-Permits",
    "oak_cd": "https://www.oaklandca.gov/resources/construction-and-demolition-recycling-requirements",
    "oak_discharge": "https://www.oaklandca.gov/services/apply-for-a-temporary-discharge-permit",
    "acwp_pools": "https://www.cityofpleasantonca.gov/assets/our-government/public-works/clean-water-program/stormwater-pollution-prevention/pools-spas-and-fountains.pdf",
    "fre_fees": "https://www.fremont.gov/home/showpublisheddocument/19579/639039838228900000",
    "fre_cd": "https://fremont.gov/government/departments/environmental-services/construction-demolition-debris",
    "usd_pools": "https://unionsanitary.ca.gov/residents/disposal-of-wastes/disposal-of-residential-pool-water/",
    "ocs_fees": "https://www.ci.oceanside.ca.us/home/showpublisheddocument/10174/639257686213930000",
    "ocs_ib108": "https://www.ci.oceanside.ca.us/home/showpublisheddocument/17993/639094220975370000",
    "ocs_cd": "https://www.ci.oceanside.ca.us/government/development-services/building/construction-and-demolition-requirements",
    "ocs_drain": "https://www.ci.oceanside.ca.us/home/showpublisheddocument/17651/639034692769670000",
    "sdapcd": "https://www.sdapcd.org/content/dam/sdapcd/documents/compliance/Updated%20APCD%20Hazmat%20Submittal%20Process%20%2011-9-21.docx",
    "scv_fees": "https://santaclarita.gov/finance/wp-content/uploads/sites/6/2026/07/Website-FINAL-Fee-Schedule-2026-27-FINAL.pdf",
    "scv_cd": "https://greensantaclarita.com/construction-and-development/construction-and-demolition-recycling-ordinance/",
    "scv_bins": "https://greensantaclarita.com/construction-and-development/temporary-and-rolloff-bins/",
    "scv_drain": "https://santaclarita.gov/home/showpublisheddocument/9978/635950354435970000",
    "scv_pools": "https://greensantaclarita.com/green-friendly-info/swimming-pools/",
    "cv_fees": "https://www.chulavistaca.gov/home/showpublisheddocument/2416/638638971096170000",
    "cv_cd": "https://chulavistaca.gov/departments/clean/environmental-services/construction-demolition-debris",
    "cv_pools": "https://chulavistaca.gov/home/showpublisheddocument/11560/635875803445570000",
    "sa_fees": "https://storage.googleapis.com/proudcity/santaanaca/2026/07/fy-26-27-miscellaneous-fees-4.0-adopted-w-hyperlinks_compressed_v2-87abc58b.pdf",
    "sa_cd": "https://santa-ana.gov/construction-and-demolition-waste-services/",
    "sa_republic": "https://www.republicservices.com/sites/default/files/legacy_documents/Muni/California/Santa-Ana/Construction-and-Demolition-Flyer.pdf",
    "h2oc_pools": "https://h2oc.org/wp-content/uploads/2024/03/H2OC-Pools-and-Spa-Brochure-2024-02-26-WEB.pdf",
})


def _l(key, text):
    return f'<a href="{SRC[key]}">{text}</a>'


BATCH2 = {
    "oakland": {
        "compact": True,
        "dept": "Planning &amp; Building Department",
        "opening_extra": (" Oakland bars soil disturbance from 15 October to 15 April, so a pool job there has to finish "
                          "in the dry season."),
        "permit_html": (
            "Oakland publishes no rule specific to pool removal, and its permit pages do not say which permit covers "
            "one, so Planning &amp; Building on Frank H. Ogawa Plaza ((510) 238-3891) confirms the permit type and fee. "
            "The city's {doc} sets the triggers that can apply to the fill: a grading permit is needed for more than 50 "
            "cubic yards of fill where a slope exceeds 20% or the fill is more than 5 ft high, for more than 500 cubic "
            "yards of cut and fill combined, for any land disturbance on ground steeper than 20%, and wherever the city "
            "has information about land stability problems. Grading applications go through the Online Permit Center "
            "with an Initial Statement of the Engineer for Grading."),
        "method_html": (
            "Oakland's calendar shapes the job more than the method. The city's "
            + _l("oak_moratorium", "wet weather grading moratorium")
            + " prohibits disturbing soil from 15 October to 15 April, with exceptions only for emergency stabilization "
            "or an alternate methods request backed by a geotechnical engineer's letter, shoring plans and a schedule. "
            "A pool on a lot steeper than 20% falls inside the grading permit rules, which bring in the grading "
            "engineer's statement whichever method is used. On flatter ground, Planning &amp; Building confirms whether a "
            "partial fill-in is accepted."),
        "extra_after_permit": [
            ("Air district notice in Oakland", [
                "Oakland's " + _l("oak_demo", "demolition permit page") + " requires an asbestos demolition "
                "acknowledgment letter and job number from the "
                + _l("baaqmd", "Bay Area Air Quality Management District")
                + " before a building demolition permit is issued. The district's rule defines demolition as removing "
                "load-supporting members of a building or facility and does not mention pools, so the district or "
                "Planning &amp; Building confirms whether a pool-only job needs the notice.",
            ]),
        ],
        "cost_html": [
            "No Oakland contractor publishes prices, but Bay Area firms do: " + _l("souza", "Souza &amp; Son's")
            + " publishes $4,500 to $10,000 for a partial fill-in and $8,000 to $22,000 for a full removal, and "
            + _l("walberg", "Walberg, Inc.") + " gives $5,000 to $12,000 and $12,000 to $30,000 for Northern "
            "California. On a hillside lot, the grading engineer's statement and any grading permit add to those "
            "figures.",
        ],
        "extra_after_cost": [
            ("Hauling the debris in Oakland", [
                "Oakland's " + _l("oak_cd", "construction and demolition recycling rules") + " apply to all city "
                "building permits: debris goes to facilities that recover 100% of inert material such as concrete, "
                "asphalt and soil, and 65% of everything else, with a Waste Reduction and Recycling Plan filed online "
                "through Green Halo before the permit and a summary report at the end. Anyone hauling the debris needs "
                "a non-exclusive franchise from the city under Chapter 15.34 of the municipal code. Property owners are "
                "exempt, and so are contractors hauling their own work's debris in their own fixed-body trucks, but that "
                "exemption does not cover demolition contractors.",
            ]),
        ],
        "drain_html": (
            "Pool water has to go somewhere before demolition starts. Oakland's "
            + _l("oak_discharge", "temporary discharge permit page")
            + " says only rainwater should enter the city's storm drains, and other water needs a temporary storm drain "
            "or sanitary sewer discharge permit. The Alameda County "
            + _l("acwp_pools", "Clean Water Program guidance for pools")
            + " sends pool water to a sanitary sewer cleanout, prohibits draining water with residual chlorine or "
            "copper algaecide to a storm drain, and names EBMUD at (510) 287-1651 for sewer approval in Oakland."),
        "faqs": [
            ("Does Oakland publish pool removal rules?",
             "No. Planning &amp; Building at (510) 238-3891 confirms the permit type and fee."),
            ("When can a pool be removed in Oakland?",
             "Between 15 April and 15 October. The wet weather moratorium bars soil disturbance the rest of the year."),
            ("Does an Oakland pool removal need a grading permit?",
             "It can. More than 50 cubic yards of fill on a slope over 20% or over 5 ft high, more than 500 cubic "
             "yards in total, or work on ground steeper than 20% needs one."),
            ("Where can Oakland pool water be drained?",
             "To a sanitary sewer cleanout with EBMUD's approval; chlorinated water may not go to the storm drain."),
            ("Who can haul pool debris in Oakland?",
             "A city-franchised hauler, the property owner, or a contractor hauling its own work in its own trucks; "
             "demolition contractors need the franchise."),
        ],
    },
    "fremont": {
        "compact": True,
        "fee": "$266 flat (schedule amended January 2026)",
        "fee_short": "$266",
        "doc": "fee schedule (amended January 2026)",
        "doc_url": SRC["fre_fees"],
        "lead": ("Pool removal in Fremont runs on an express building permit at a flat $266, with no plan review, and "
                 "Pool Removal California found {found} businesses offering in-ground pool removal there, {active} "
                 "with an active state licence."),
        "permit_html": (
            "Fremont's {doc} lists residential swimming pool demolition and removal as an express permit at a flat "
            "$266, under a heading for permits with no plan review and inspection only. Extra inspections and "
            "reinspections cost $133 each. The Building and Safety FAQ says a building permit is needed before "
            "demolishing any structure, and the city publishes no technical rules for the holes, the wall or the "
            "fill."),
        "method_html": (
            "With no published fill rules and no plan review, the inspection is where Fremont judges the method. An "
            "owner planning to build over the area later should settle the compaction standard with Building and "
            "Safety before the work starts, since the express permit leaves no plan on file that sets it."),
        "extra_after_permit": [
            ("Air district notice in Fremont", [
                "The " + _l("baaqmd", "Bay Area Air Quality Management District") + " asks for notice at least 10 "
                "business days before every demolition, regardless of asbestos content, with a 72-hour option for "
                "residential buildings of four units or fewer. Its rule defines demolition as removing load-supporting "
                "members of a building or facility and does not mention pools, so the district confirms whether a "
                "pool-only job needs the notice.",
            ]),
        ],
        "cost_html": [
            "No Fremont contractor publishes prices, but East Bay firms do: " + _l("byebye", "Bye Bye Pool in Concord")
            + " quotes $3,500 to $7,000 for a partial fill-in and $9,000 to $19,000 for a full removal, and "
            + _l("souza", "Souza &amp; Son's") + " publishes $4,500 to $10,000 and $8,000 to $22,000. Fremont's own "
            "charges are the $266 express permit and $133 for any extra inspection.",
        ],
        "extra_after_cost": [
            ("Hauling the debris in Fremont", [
                "Fremont's " + _l("fre_cd", "construction and demolition page") + " lists all demolition among the "
                "projects with recycling requirements: a Waste Handling Plan goes into Fremont Waste Tracking before the "
                "permit is issued, and a Debris Disposal and Diversion Report closes the job. The city's plan form "
                "requires 100% of asphalt, concrete and soil recycled, with a penalty of $1,000 for each ton that is "
                "not. Republic Services is the only approved debris box hauler at construction sites, though separate "
                "loads of clean soil, asphalt or concrete are exempt when each is no more than 10% garbage, and "
                "contractors may self-haul to an approved facility.",
            ]),
        ],
        "drain_html": (
            "Pool water has to go somewhere before demolition starts. " + _l("usd_pools", "Union Sanitary District")
            + ", which serves Fremont, warns that pool water drained to a storm drain flows to creeks and the San "
            "Francisco Bay. The Clean Water Program guidance it links sends pool water to a sanitary sewer cleanout "
            "and prohibits draining water with residual chlorine or copper algaecide to a storm drain, and the "
            "district's number for sewer approval is (510) 477-7500."),
        "faqs": [
            ("What does a Fremont pool removal permit cost?",
             "$266 flat for a residential pool demolition or removal, on the schedule amended in January 2026."),
            ("Does a Fremont pool removal need plans?",
             "No. The city lists it as an express permit with no plan review and inspection only."),
            ("What happens to the concrete from a Fremont pool?",
             "It must be 100% recycled, with a penalty of $1,000 a ton for any that is not."),
            ("Who can supply a debris box in Fremont?",
             "Republic Services, though separate loads of clean concrete, asphalt or soil are exempt."),
            ("Where can Fremont pool water be drained?",
             "To a sanitary sewer cleanout with Union Sanitary District approval; chlorinated water may not go to the "
             "storm drain."),
        ],
    },
    "oceanside": {
        "compact": True,
        "fee": "$284.55 general demolition permit (FY 2026-27)",
        "fee_short": "$284.55",
        "permit_html": (
            "Oceanside publishes no pool-specific demolition handout. {doc}, based on the 2025 California codes, quotes "
            "the building code's rule that anyone who demolishes a building or structure must first obtain a permit, "
            "lists no exemption for pool removal, and notes that Building Division staff will not confirm an exemption "
            "verbally. The city's " + _l("ocs_fees", "building fee schedule for 2026-27") + " lists a demolition permit "
            "at $31.84 for plan check and $252.71 for inspection, $284.55 in total."),
        "method_html": (
            "No city document sets drainage holes, shell depth or fill rules for pools, so the Building Division decides "
            "what Oceanside accepts. The city's grading code does set general standards for permitted controlled fill: "
            "layers no thicker than 6 inches, compacted to at least 90% of maximum density. Grading outside the code's "
            "exemptions needs a permit from the City Engineer, and a minor grading plan carries a $300 administrative "
            "fee, so the depth of fill on a full removal decides whether Engineering is involved."),
        "extra_after_permit": [
            ("Soils reports and air district notice in Oceanside", [
                "Oceanside's " + _l("ocs_ib108", "Information Bulletin 108") + " requires a geotechnical report for new "
                "pools and wherever a grading plan is required. It says nothing about removing a pool, so the grading "
                "question decides whether a removal needs one.",
                "The " + _l("sdapcd", "San Diego County Air Pollution Control District") + " requires a demolition "
                "notification whenever a load-bearing structure is wrecked, and an asbestos survey before the building "
                "permit. The district does not say whether a pool shell counts, so the Building Division confirms it "
                "with the permit.",
            ]),
        ],
        "cost_html": [
            "No Oceanside contractor publishes prices, but San Diego firms do: " + _l("demodiego", "Demo Diego")
            + " quotes $5,000 to $9,000 for a partial fill-in and $9,000 to $15,000 for a full removal. Oceanside's own "
            "charges are the $284.55 demolition permit and, where a minor grading plan is needed, the $300 "
            "administrative fee.",
        ],
        "extra_after_cost": [
            ("Hauling the debris in Oceanside", [
                "Oceanside's " + _l("ocs_cd", "construction and demolition requirements") + " call for a Waste "
                "Management Plan before permits are issued and a signed affidavit at final inspection that the "
                "diversion target was met. The plan form sets a minimum of 65% recycled or salvaged under CALGreen, "
                "lists demolition among its project types and counts a Waste Management roll-off bin as one way to "
                "comply; Waste Management is the city's franchise service provider. The city code requires all debris "
                "removed within one week of the work finishing.",
            ]),
        ],
        "drain_html": (
            "Pool water has to go somewhere before demolition starts. Oceanside's "
            + _l("ocs_drain", "pool draining tips") + " say no permit is needed to drain a pool, but the water must "
            "test below 1 part per million of chlorine, and the city suggests leaving it in the sun for at least three "
            "days to get there. Filter backwash goes to the sewer, not the street, saltwater pools need total "
            "dissolved solids below 500 ppm before draining to the street, and the Urban Runoff Hotline is "
            "760-435-4500."),
        "faqs": [
            ("Does Oceanside publish pool removal rules?",
             "No. A demolition permit is required, at $284.55 for 2026-27, and the Building Division sets the method."),
            ("Does draining an Oceanside pool need a permit?",
             "No, but the water must test below 1 part per million of chlorine before it reaches the street."),
            ("Does an Oceanside pool removal need a Waste Management Plan?",
             "The city requires one before permits are issued, with at least 65% of the debris recycled or salvaged."),
            ("What does pool removal cost in Oceanside?",
             "No local prices are published; San Diego firms quote $5,000 to $9,000 partial and $9,000 to $15,000 full."),
        ],
    },
    "santa-clarita": {
        "compact": True,
        "doc": "pool abandonment bulletin (revised January 2020)",
        "doc_url": "https://santaclarita.gov/home/showpublisheddocument/13292/637486509545530000",
        "fee": "$38 issuance plus $95 for valuation up to $5,000 (FY 2026-27)",
        "fee_short": "$38 + $95",
        "lead": ("Pool removal in Santa Clarita needs a building permit from the city's Building and Safety Division, "
                 "whether the pool is filled in place or removed, and Pool Removal California found {found} businesses "
                 "offering in-ground pool removal there, {active} with an active state licence. A pool filled in place "
                 "leaves the property permanently recorded as having an abandoned structure."),
        "permit_html": (
            "Santa Clarita's Building and Safety Division requires a permit whether a pool is filled in place or "
            "removed completely, and its {doc} sets out the abandonment route. A building permit can be issued over the "
            "counter once the application is complete and two site plans, on paper at least 11 by 17 inches, show the "
            "property lines, adjacent streets and pool dimensions. The city's "
            + _l("scv_fees", "2026-27 fee schedule") + " has no pool line; its general building permit fees are $38 "
            "for issuance and $95 for work valued up to $5,000."),
        "method_html": (
            "The bulletin's catch is in its wording: a pool filled in place leaves the property permanently recorded as "
            "having an abandoned structure, and the pool may have to be removed completely if a future structure is "
            "proposed on or near it. Filling in place needs at least two 24-inch holes with the bottom broken up for "
            "drainage, the bond beam cut at least 12 inches below grade, and the fill named on the plan as gravel, sand "
            "or compacted earth. No compaction report is required unless a future structure is proposed."),
        "extra_after_permit": [
            ("Inspections and paperwork on a Santa Clarita job", [
                "The site plan also notes that pool equipment is removed and the electrical, water and gas lines are "
                "capped. The bulletin then sets two inspections:",
                "<ol><li>A pre-fill inspection of the drainage holes and the broken bottom, before any fill goes in."
                "</li><li>A final inspection confirming the pool was filled.</li></ol>",
                "At the final, the inspector signs the inspection card, which the bulletin describes as the property "
                "owner's record of the work, so owners should keep it with the property papers.",
            ]),
        ],
        "cost_html": [
            "No Santa Clarita contractor publishes prices, but Los Angeles firms do: "
            + _l("lapdc", "Los Angeles Pool Demolition Contractors") + " starts at $10,500 for a partial fill-in and "
            "$17,500 for a full removal, and " + _l("angi", "Angi's Los Angeles figures") + " run from $2,850 to "
            "$11,350 and $4,550 to $18,200. Santa Clarita's own charges add the building permit, the demolition debris "
            "deposit where it applies, and a compaction report only when a structure is planned.",
        ],
        "extra_after_cost": [
            ("Hauling the debris in Santa Clarita", [
                "Santa Clarita's " + _l("scv_cd", "construction and demolition recycling ordinance") + " covers all "
                "demolition projects and requires at least 65% of inert materials and 65% of everything else recycled. "
                "A Construction and Demolition Materials Management Plan and a refundable deposit of 10% or $15,000, "
                "whichever is less, are due before the building permit, and proof of diversion within 180 days of the "
                "final inspection. Bins and roll-offs must come from one of the city's "
                + _l("scv_bins", "franchised haulers") + ", which include Burrtec and Waste Management, and contractors "
                "may self-haul only under a state licence covering that scope.",
            ]),
        ],
        "drain_html": (
            "Pool water has to go somewhere before demolition starts. Santa Clarita's "
            + _l("scv_drain", "pool drainage form") + " allows the sewer only through a 3-inch P-trap installed under "
            "a city permit, never between 5 and 9 am on weekdays and never into a septic system. Water sent to the "
            "street gutter needs notice to Environmental Services at 661-286-4098 and must be dechlorinated, "
            "debrominated and pH neutral with no algaecides, and saltwater pools may not drain to the gutter or storm "
            "drain at all. The city's " + _l("scv_pools", "pool guidance") + " limits the flow to one outlet no wider "
            "than 2 inches."),
        "faqs": [
            ("Does a Santa Clarita pool filled in place stay on record?",
             "Yes. The {doc} says the property will be permanently recorded as having an abandoned structure."),
            ("Can a Santa Clarita homeowner build over a filled pool?",
             "The pool may have to be removed completely if a structure is proposed on or near it."),
            ("How many holes does Santa Clarita require?",
             "At least two 24-inch holes, with the bottom broken up for drainage."),
            ("Does Santa Clarita need a compaction report?",
             "Only when a future structure is proposed."),
            ("Can Santa Clarita pool water go to the street?",
             "Only dechlorinated, debrominated, pH-neutral water, after notice to Environmental Services at 661-286-4098."),
        ],
    },
    "chula-vista": {
        "compact": True,
        "fee": "$404 pool and spa demolition line (September 2024 schedule)",
        "fee_short": "$404",
        "permit_html": (
            "Chula Vista's Development Services Department requires a demolition permit whenever a building or "
            "structure is demolished. The city's {doc} asks for a New Construction Worksheet, the San Diego regional "
            "hazardous materials questionnaire and utility disconnect notices for anything connected to a utility. The "
            "city's " + _l("cv_fees", "Fee Bulletin 10-400") + ", from the September 2024 master fee schedule, has a "
            "line for swimming pool, spa and hot tub demolition at $123 intake and $281 inspection, $404 in total, and "
            "all fees are paid before the permit is issued."),
        "method_html": (
            "Chula Vista publishes no technical rule for pools, so Development Services confirms whether a partial "
            "fill-in is accepted and what fill it expects. The pool demolition fee line carries no plan check charge, "
            "only intake and inspection, so the method is settled with the department before work starts rather than "
            "through a reviewed plan."),
        "extra_after_permit": [
            ("Air district notice in Chula Vista", [
                "The " + _l("sdapcd", "San Diego County Air Pollution Control District") + " requires a demolition "
                "notification whenever a load-bearing structure is wrecked, filed at least 10 working days ahead, and "
                "an asbestos survey before the building permit. The district does not say whether a pool shell counts, "
                "so Development Services confirms it with the permit.",
            ]),
        ],
        "cost_html": [
            "No Chula Vista contractor publishes prices, but San Diego firms do: " + _l("demodiego", "Demo Diego")
            + " quotes $5,000 to $9,000 for a partial fill-in and $9,000 to $15,000 for a full removal, and "
            + _l("villa", "Villa Demolition") + " quotes $12,000 to $30,000 and $45,000 to $60,000. Chula Vista's own "
            "charges add the $404 permit and container rental.",
        ],
        "extra_after_cost": [
            ("Hauling the debris in Chula Vista", [
                "Chula Vista's " + _l("cv_cd", "construction and demolition rules") + " require 100% of inert "
                "materials such as concrete, and at least 65% of everything else, recycled. Environmental Services "
                "must approve a Waste Management Report before a demolition permit is issued, which takes up to 10 "
                "business days, and diversion records are due within 30 days after a demolition-only job finishes. "
                "Republic Services is the city's franchise hauler and rents containers at 619-421-9400. The city also "
                "takes a refundable performance deposit of 1.5% of valuation on most larger projects, so Environmental "
                "Services confirms whether a pool job needs one.",
            ]),
        ],
        "drain_html": (
            "Pool water has to go somewhere before demolition starts. Chula Vista's "
            + _l("cv_pools", "pool maintenance guidance") + " sends it to the sanitary sewer, or slowly onto "
            "landscaping with no runoff, and allows the storm drain only when chlorine tests below one part per "
            "million, the pH is 7 to 8 and the water is free of colour, algae and debris. Large volumes to the sewer "
            "need a call to Wastewater Engineering at (619) 691-5021 first, and saltwater pool water may not go to the "
            "storm drain."),
        "faqs": [
            ("What does a Chula Vista pool demolition permit cost?",
             "$404: $123 intake and $281 inspection on the September 2024 fee schedule."),
            ("What does Chula Vista need before issuing the permit?",
             "A New Construction Worksheet, the hazardous materials questionnaire, utility disconnect notices and an "
             "approved Waste Management Report."),
            ("What happens to the concrete from a Chula Vista pool?",
             "All inert material, concrete included, must be recycled."),
            ("Where can Chula Vista pool water be drained?",
             "To the sanitary sewer or slowly onto landscaping; the storm drain only below 1 ppm chlorine at pH 7 to 8."),
        ],
    },
    "santa-ana": {
        "compact": True,
        "doc": "Handout BLD-16 (revised March 2025)",
        "doc_url": "https://storage.googleapis.com/proudcity/santaanaca/2022/07/BLD-16_Abandoned-Pools.pdf",
        "fee": "Hourly: $294.06 demolition plan check, $212.11 inspection (FY 2026-27)",
        "fee_short": "Hourly",
        "lead": ("Pool removal in Santa Ana needs building, electrical and plumbing permits from the city's Planning and "
                 "Building Agency, and Pool Removal California found {found} businesses offering in-ground pool "
                 "removal there, {active} with an active state licence. Handout BLD-16 calls for five 3 ft by 3 ft "
                 "holes in the floor and the bond beam removed."),
        "permit_html": (
            "Santa Ana's Planning and Building Agency requires three permits to abandon a pool: a building permit with "
            "a site plan, an electrical permit and a plumbing permit, plus approvals from the Planning Department and "
            "from Public Works for construction runoff. The city's " + _l("sa_fees", "2026-27 fee schedule")
            + " bills demolition plan check at $294.06 an hour and inspection at $212.11 an hour, with an electrical "
            "demolition fee of $64.15 and a 26% stormwater surcharge on building and plumbing permits."),
        "method_html": (
            "{doc} describes abandoning the pool in place. Crews jack hammer five holes, each 3 ft by 3 ft, four in the "
            "deep end and one in the shallow end, remove the bond beam around the top, typically 12 to 18 inches deep, "
            "and take out any built-in spa walls. The shell is filled with pea gravel up to the bond beam and finished "
            "with clean soil, or filled with soil compacted to 90% of the laboratory standard, with a compaction report "
            "at final inspection. An addition over the old pool needs a compaction report from a professional "
            "engineer."),
        "extra_after_permit": [
            ("Inspections and paperwork on a Santa Ana job", [
                "BLD-16 sets the inspection order, booked at (714) 667-2738 or online:",
                "<ol><li>Electrical inspection, with every electrical connection terminated or disconnected.</li>"
                "<li>Plumbing inspection, with every water supply and drain connection capped.</li><li>Building "
                "inspection of the holes, which gives the go-ahead to backfill once electrical and plumbing have "
                "passed.</li><li>Final inspection, where any compaction report goes to the inspector and is filed with "
                "the finaled permit.</li></ol>",
            ]),
        ],
        "cost_html": [
            "No Santa Ana contractor publishes prices, but Orange County firms do: " + _l("frisch", "Frisch &amp; Sons")
            + " publishes $12,000 to $20,000 for a partial fill-in and $18,000 to $30,000 or more for a full removal. "
            "Santa Ana's own charges add hourly demolition plan check and inspection, the electrical and plumbing "
            "permits, and the $204 debris plan review.",
        ],
        "extra_after_cost": [
            ("Hauling the debris in Santa Ana", [
                "Santa Ana's " + _l("sa_cd", "construction and demolition page") + " names Republic Services for "
                "temporary debris bins, reached at (657) 467-6220, and cites the CALGreen minimum of 65% recycled. "
                "Republic's " + _l("sa_republic", "Santa Ana flyer") + " says a Waste Reduction and Recycling Plan must "
                "be submitted before a permit is issued, lists concrete, rock and dirt as clean debris and caps roll-off "
                "containers at 10 tons. The fee schedule charges $204 to review a residential debris recycling plan, "
                "with a refundable deposit of $1.14 a square foot and a $250 minimum.",
            ]),
        ],
        "drain_html": (
            "Pool water has to go somewhere before demolition starts. Santa Ana belongs to H2OC, the stormwater program "
            "shared by all 34 Orange County cities, whose " + _l("h2oc_pools", "pool drainage brochure") + " asks for "
            "pool water sent to the sanitary sewer when possible. The storm drain is allowed only for dechlorinated "
            "water with no more than 0.1 mg/L of chlorine, a pH of 6.5 to 8.5 and no filter media or acid waste, and "
            "saltwater pools may not use it. Santa Ana's storm drains carry water untreated to the ocean."),
        "faqs": [
            ("What permits does a Santa Ana pool removal need?",
             "Building, electrical and plumbing permits, plus Planning and Public Works approval."),
            ("How many holes does Santa Ana require?",
             "Five holes, each 3 ft by 3 ft: four in the deep end and one in the shallow end."),
            ("Can a Santa Ana homeowner build over a filled pool?",
             "Yes, with a compaction report from a professional engineer, as {doc} requires for an addition."),
            ("What does a Santa Ana pool removal permit cost?",
             "Demolition plan check is $294.06 an hour and inspection $212.11 an hour on the 2026-27 schedule, plus "
             "electrical and plumbing fees."),
            ("Where can Santa Ana pool water be drained?",
             "To the sanitary sewer when possible; the storm drain only below 0.1 mg/L chlorine at pH 6.5 to 8.5."),
        ],
    },
}

for _c in CITIES:
    _c.update(BATCH2.get(_c["slug"], {}))
