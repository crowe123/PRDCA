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
    "baaqmd": "https://www.baaqmd.gov/permits/asbestos-demolition-renovation",
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
                "revised in June 2026, and each version comes with three inspections: an initial meeting, a bottom "
                "inspection and a final inspection. On a partial fill-in, the bottom inspection happens after the "
                "drainage holes are broken and before any soil goes in. The bulletin requires at least one of those "
                "holes at the deepest point of the shell, and the backfill must be clean soil or gravel, moistened and "
                "compacted by tractor rolling or a mechanical tamper.",
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
            f'Bay Area jobs also need a <a href="{SRC["baaqmd"]}">Bay Area Air Quality Management District</a> notice for '
            "demolition work."
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
