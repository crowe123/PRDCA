"""Content and facts for the Pool Removal California site.

Every fact here comes from the site structure document of 10 October 2026
(permit table, cost table, FAQ notes and city table). Contractor listings are
not stored here: they load from data/businesses.csv, exported from the
workbook's Businesses and By city tabs.
"""

SITE_NAME = "Pool Removal California"
# Set to the live domain before deploying; used for canonical URLs and the sitemap.
SITE_URL = "https://www.poolremovalcalifornia.com"

# Open item in the plan: whether contractor cards link to each contractor's site.
LINK_CONTRACTOR_SITES = False

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

# The 20 cities, ranked by the 1 January 2026 population estimate.
# found = businesses found; active = active licence; searches = monthly searches.
CITIES = [
    {
        "rank": 1, "name": "Los Angeles", "slug": "los-angeles", "region": "la", "cost": "la",
        "searches": "50", "found": 20, "active": 9, "wave": 1,
        "dept": "Department of Building and Safety",
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
        ],
        "nearby": ["Burbank", "Glendale", "Pasadena", "Culver City", "Santa Monica", "Inglewood"],
        "note": "One contractor in the research trades under three different websites, so the listing merges them.",
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
        "dept": "Development Services Permit Center",
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
        "note": "San Jose has the deepest contractor pool of the 20 cities.",
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
        "dept": "Planning and Development Department",
        "permit": "Swimming Pool Abandonment Permit", "fee": "$321 (2013 figure)",
        "doc": "Bulletin 13-02",
        "doc_url": "https://www.fresno.gov/wp-content/uploads/2023/02/SwimmingPoolAbandonment.pdf",
        "confidence": "Medium-high", "rules": "published",
        "permit_html": (
            "Fresno issues a Swimming Pool Abandonment Permit through its Planning and Development Department, set out "
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
        "dept": "Community Development Department",
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
        "dept": "Development Services Building and Safety Bureau",
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
        "dept": "Development Services Building Division",
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
        "dept": "Planning and Building Department",
        "permit": "Building permit (general rule)", "fee": "Not found",
        "doc": "Handout B 804",
        "doc_url": "https://www.anaheim.net/DocumentCenter/View/41215",
        "confidence": "Low-medium", "rules": "fee-less",
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
        "dept": "Community Development Department",
        "permit": "Building permit", "fee": "$97.25 (FY 2026-27)",
        "doc": "Form BLDG-0014",
        "doc_url": "https://www.stocktonca.gov/Documents/Business/Building%20%26%20Life%20Safety/Building%20Forms/BLDG-0014_SWIMMING%20POOL%20DEMOLITION%20REQUIREMENTS.pdf",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Stockton has the best-documented pool permit of the 20 cities. The Community Development Department issues "
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
             "$97.25 for fiscal year 2026-27, the lowest published pool permit of the 20 cities."),
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
        "dept": "Community and Economic Development Building and Safety Division",
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
        "dept": "Community Development Building and Safety",
        "permit": "Building permit", "fee": "Minimum fees; amount not published",
        "doc": "pool removal page (Bulletin 217)",
        "doc_url": "https://cityofirvine.gov/building-permits-and-inspections/removing-single-family-residential-swimming-pool-or-spa",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Irvine's Building and Safety division issues a building permit at minimum fees, though the amount is not "
            "published. The city's {doc} requires the plans to state whether the area becomes landscaping or a building "
            "pad, and a soils engineer must supervise the backfill."
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
        "dept": "Planning and Building Agency",
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
        "dept": "Community Development Building Division",
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
        "dept": "Community and Economic Development Building and Safety",
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
        "dept": "Community and Economic Development Building Safety",
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
        "dept": "Building and Safety Division",
        "permit": "Demolition permit", "fee": "$120 (2023 schedule)",
        "doc": "pool demolition handout (2026)",
        "doc_url": "https://www.fontanaca.gov/DocumentCenter/View/48412/Demolition-of-Swimming-Pool-or-Spa-PDF",
        "confidence": "High", "rules": "published",
        "permit_html": (
            "Fontana's Building and Safety Division issues a demolition permit, priced at $120 on the 2023 schedule, "
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

# Images generated with kie.ai (scripts/generate_images.py). Pages use them when the file exists.
IMAGES = {
    "home-hero": "Excavator breaking up a concrete swimming pool in a California backyard",
    "partial-fill": "Old pool shell with drainage holes broken through the bottom before backfill",
    "full-removal": "Excavated hole after a pool shell has been fully removed",
    "compaction": "Fill soil being compacted in layers where a pool was removed",
    "after-landscape": "Drought-tolerant garden planted where a backyard pool used to be",
    "debris-haul": "Truck loaded with broken pool concrete leaving a residential street",
    "draining": "Pool being drained through a hose to a sewer clean-out before demolition",
    "permit-plans": "Building permit papers and a site plan for a pool removal on a clipboard",
}
