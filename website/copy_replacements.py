"""Plain-language copy applied to the generated static site."""

GLOBAL_REPLACEMENTS = [
    (
        "Vinyl &amp; Resilient Floor Care",
        "Vinyl Floor Cleaning &amp; Maintenance",
        1,
    ),
    (
        "Vinyl & Resilient Floor Care",
        "Vinyl Floor Cleaning & Maintenance",
        1,
    ),
    (
        "Floor Sealing, Recoating &amp; Finishing",
        "Floor Sealing &amp; Protective Finishes",
        1,
    ),
    (
        "Floor Sealing, Recoating & Finishing",
        "Floor Sealing & Protective Finishes",
        1,
    ),
    (
        "HWE vs encapsulation: which carpet-cleaning method fits the job?",
        "Steam cleaning or low-moisture cleaning: which suits your carpet?",
        1,
    ),
    (
        "HWE vs encapsulation: which carpet method fits the job?",
        "Steam cleaning or low-moisture cleaning: which suits your carpet?",
        1,
    ),
    (
        "the method should follow the surface, soil and required outcome — not the other way around.",
        "we choose the cleaning method to suit your floor, the problem and the result you want.",
        3,
    ),
    ("Local floor-care principle:", "Our approach:", 3),
]

SERVICE_PATHS = [
    "services/carpet-cleaning/index.html",
    "services/upholstery-leather/index.html",
    "services/tile-grout-cleaning/index.html",
    "services/natural-stone/index.html",
    "services/vinyl-resilient-floors/index.html",
    "services/concrete-epoxy/index.html",
    "services/gym-rubber-flooring/index.html",
    "services/floor-sealing-finishing/index.html",
]

SERVICE_REPLACEMENTS = [
    ("What we can assess and deliver", "How we can help"),
    ("How method selection works", "How we choose the right approach"),
    (
        "We consider surface/fibre type, construction, existing coatings or treatments, soil load, access, drying requirements and the result you need. The website does not promise a method before those facts are understood.",
        "We look at the floor or fabric, its condition, any previous treatments, the type and amount of dirt or staining, access and drying time. Then we recommend the safest practical option for the result you want.",
    ),
    ("<b>Important</b>", "<b>What to expect</b>"),
    (
        "No cleaning method can reverse permanent wear, colour loss, physical damage or every chemical/stain reaction. We explain limitations before committing to scope.",
        "Cleaning can greatly improve many floors, but it cannot undo permanent wear, colour loss, physical damage or every stain. We will explain the likely result and any limitations before work begins.",
    ),
    (
        "One-off restoration work and planned recurring maintenance are both available. Regional work can be assessed based on scope and mobilisation.",
        "One-off deep cleaning and regular maintenance are both available. Regional jobs are considered based on size, travel and availability.",
    ),
    ("Recurring contractor / tender packages", "Ongoing and contract work"),
    ("Send the useful details once.", "Ready for a clearer answer?"),
    (
        "Choose the service, add approximate area/items, note stains or damage, and attach photos when available. The intake workflow routes complex or higher-risk work to human review.",
        "Tell us the floor type, approximate size, what is bothering you and when you need help. We will let you know whether we can quote from those details or need to inspect the floor.",
    ),
]

PAGE_REPLACEMENTS = {
    "index.html": [
        (
            "Clean floors.<br><em>Properly understood.</em>",
            "Bring tired floors<br><em>back to their best.</em>",
        ),
        (
            "Carpet, upholstery, tile &amp; grout, natural stone, vinyl, concrete, epoxy and specialist commercial floor care — method selected for the surface, soil load and outcome you actually need.",
            "Professional cleaning and restoration for carpet, upholstery, tile, stone, vinyl, concrete, epoxy and commercial floors — with the right approach for your floor and the result you want.",
        ),
        ("Surface-led methods", "The right care for every floor"),
        (
            "HWE, encapsulation, extraction, pressure, sealing and finish systems where suitable.",
            "Deep cleaning, faster-drying carpet care, pressure cleaning and protective finishes where suitable.",
        ),
        (
            "Fibre-aware carpet cleaning with controlled chemistry and moisture.",
            "Careful carpet cleaning for wool and other delicate fibres.",
        ),
        (
            "One floor-care company.<br>More technical range.",
            "One specialist team<br>for every floor.",
        ),
        (
            "We don’t sell one machine or one cleaning method as the answer to every floor. Voila Floor selects the process around the surface, construction, condition, access and required result.",
            "Different floors need different care. We check the material, condition and access before recommending a safe, practical way to achieve the best result possible.",
        ),
        (
            "Care for stone that needs more than generic floor chemistry.",
            "Careful cleaning and sealing for limestone, travertine, marble and slate.",
        ),
        (
            "Deep cleaning, stripping, sealing and finish maintenance.",
            "Deep cleaning, worn-finish removal, resealing and polishing for suitable vinyl floors.",
        ),
        (
            "Technical cleaning for robust commercial and residential surfaces.",
            "Deep cleaning and ongoing care for concrete and coated floors.",
        ),
        (
            "Protection and maintenance systems for suitable floors.",
            "Sealing and protective finishes to help suitable floors last longer.",
        ),
        (
            "Periodic deep cleans, recurring maintenance and technical tender packages.",
            "One-off deep cleaning, regular maintenance and commercial contract work.",
        ),
        (
            "Use Voila Floor as your specialist floor-care contractor — directly, through property/strata management, or as the technical floor component inside a broader facilities contract.",
            "Choose Voila Floor for direct commercial work, property and strata maintenance, or specialist floor cleaning within a larger facilities contract.",
        ),
        (
            "Recurring carpet encapsulation / extraction",
            "Regular carpet maintenance and deep cleaning",
        ),
        (
            "Vinyl strip, seal, recoat &amp; burnish",
            "Vinyl deep cleaning, resealing and machine polishing",
        ),
        ("Local knowledge, useful answers.", "Helpful floor-care advice for Geraldton."),
        (
            "The Floor Journal is our practical library for Geraldton property owners, facility teams and cleaners who want to understand surfaces rather than chase cleaning myths.",
            "The Floor Journal gives Geraldton property owners and facility teams clear, practical advice about common floor problems and maintenance choices.",
        ),
        (
            "Why method selection depends on soil, construction, drying and maintenance goals.",
            "How carpet type, dirt, drying time and your goals affect the right cleaning choice.",
        ),
        (
            "A practical look at soil loading, residues and when extraction makes sense.",
            "Why dirt and cleaning product build up in grout, and when a deeper clean can help.",
        ),
        (
            "How periodic maintenance can protect appearance and reduce disruptive restoration work.",
            "How regular care can protect appearance and avoid larger restoration jobs.",
        ),
        (
            "Tell us what the floor is, what happened, and what outcome you need.",
            "Tell us about your floor and what you would like improved.",
        ),
        ("Need a scope, not a guess?", "Need a clear quote?"),
        (
            "Our enquiry form asks for the useful details up front, so we can identify whether the job can be quoted remotely or needs an inspection.",
            "Share a few useful details and we will let you know whether we can prepare a quote or need to inspect the floor first.",
        ),
    ],
    "services/index.html": [
        ("Service catalogue", "Our services"),
        ("Cleaning, restoration &amp; maintenance by surface.", "Professional care for every type of floor."),
        (
            "From wool carpet and upholstery to stone, resilient flooring, rubber and epoxy — the service starts with understanding the material and desired outcome.",
            "From wool carpet and upholstery to stone, vinyl, rubber and epoxy, we match the cleaning method to the material and the result you want.",
        ),
        (
            "Care for stone that needs more than generic floor chemistry.",
            "Careful cleaning and sealing for limestone, travertine, marble and slate.",
        ),
        (
            "Deep cleaning, stripping, sealing and finish maintenance.",
            "Deep cleaning, worn-finish removal, resealing and polishing for suitable vinyl floors.",
        ),
        (
            "Technical cleaning for robust commercial and residential surfaces.",
            "Deep cleaning and ongoing care for concrete and coated floors.",
        ),
        (
            "Protection and maintenance systems for suitable floors.",
            "Sealing and protective finishes to help suitable floors last longer.",
        ),
    ],
    "services/carpet-cleaning/index.html": [
        (
            "Deep carpet care for homes, offices and facilities. HWE, encapsulation, wool-safe methods, targeted stain treatment, urine extraction and selected carpet repairs.",
            "Deep carpet cleaning for homes, offices and facilities. We choose between a thorough hot-water rinse, faster-drying low-moisture cleaning and targeted treatments based on what your carpet needs.",
        ),
        ("Hot Water Extraction (HWE)", "Deep hot-water cleaning (often called steam cleaning)"),
        ("Encapsulation / low-moisture cleaning", "Low-moisture carpet cleaning"),
        ("Wool carpet specialist cleaning", "Careful cleaning for wool carpet"),
        ("Urine extraction & odour treatment", "Pet urine and odour treatment"),
        (
            "HWE, encapsulation, wool-safe methods, targeted stain treatment, urine extraction and selected carpet repairs.",
            "Deep hot-water and low-moisture cleaning, wool-safe care, stain and odour treatment, and selected carpet repairs.",
        ),
    ],
    "services/upholstery-leather/index.html": [
        (
            "Fibre-appropriate upholstery cleaning plus suitable finished-leather cleaning and conditioning.",
            "Careful cleaning for fabric upholstery, plus cleaning and conditioning for suitable finished leather.",
        ),
        ("Low-moisture or extraction methods where suitable", "Low-moisture or deeper rinsing when suitable"),
    ],
    "services/tile-grout-cleaning/index.html": [
        (
            "Agitation, extraction and controlled high-pressure cleaning where the installation is suitable.",
            "We loosen built-up dirt, rinse it away and use controlled pressure cleaning only where the floor can safely handle it.",
        ),
        ("Mechanical agitation", "Machine scrubbing where suitable"),
        ("Extraction rinsing", "Thorough rinsing and dirty-water removal"),
        ("Controlled high-pressure cleaning where suitable", "Controlled pressure cleaning where suitable"),
        ("Commercial wet-area programs", "Planned cleaning for commercial bathrooms and wet areas"),
    ],
    "services/natural-stone/index.html": [
        (
            "Care for stone that needs more than generic floor chemistry. Cleaning and suitable penetrating protection for limestone, travertine, marble, slate and related stone after assessment.",
            "Careful cleaning and sealing for limestone, travertine, marble, slate and similar stone after we inspect its type and condition.",
        ),
        ("Stone identification / testing", "Check the stone type and condition"),
        ("Penetrating / impregnating sealers", "Protective penetrating sealers"),
        ("Maintenance planning", "Ongoing care advice"),
    ],
    "services/vinyl-resilient-floors/index.html": [
        (
            "Deep cleaning, stripping, sealing and finish maintenance. Machine cleaning, strip-and-seal, recoats, buffing and burnishing for compatible resilient floors.",
            "Deep machine cleaning, removal of worn finish, resealing and regular polishing for suitable vinyl floors.",
        ),
        ("Strip & seal", "Remove worn finish and reseal"),
        ("Maintenance recoats", "Refresh the protective finish"),
        ("Buffing / burnishing", "Machine polishing"),
        ("Periodic maintenance programs", "Scheduled floor care"),
    ],
    "services/concrete-epoxy/index.html": [
        (
            "Technical cleaning for robust commercial and residential surfaces. Deep cleaning and maintenance of suitable concrete and epoxy/resin systems.",
            "Deep cleaning and ongoing care for suitable concrete, epoxy and other coated floors in homes and commercial properties.",
        ),
        ("Epoxy / resin floor cleaning", "Epoxy and coated floor cleaning"),
        ("Mechanical agitation", "Machine scrubbing where suitable"),
        ("Extraction", "Dirty-water removal"),
    ],
    "services/gym-rubber-flooring/index.html": [
        (
            "Material-appropriate chemistry and mechanical cleaning for compatible rubber and sports-floor systems.",
            "Deep cleaning with low-residue products and equipment suited to rubber and sports flooring.",
        ),
        ("Compatible low-residue chemistry", "Low-residue cleaning products"),
        ("Recurring facility programs", "Scheduled gym and facility cleaning"),
    ],
    "services/floor-sealing-finishing/index.html": [
        (
            "Protection and maintenance systems for suitable floors. Micron/penetrating sealing, stone sealing, recoats, strip-and-seal and finish maintenance.",
            "Sealing and finish renewal to protect suitable floors, improve their appearance and make ongoing care easier.",
        ),
        ("Micron / penetrating sealing", "Penetrating floor sealers"),
        ("Strip & seal", "Remove old finish and reseal"),
        ("Maintenance recoat", "Refresh the protective finish"),
        ("Buffing / burnishing", "Machine polishing"),
    ],
    "commercial/index.html": [
        (
            "The specialist floor-care layer for your facility or contract.",
            "Professional floor care for your facility or contract.",
        ),
        (
            "Direct commercial service, planned recurring maintenance, strata/common areas, property management work and technical floor-care packages delivered inside broader tenders.",
            "Commercial floor cleaning, planned maintenance, strata and common-area care, property management work, and specialist floor services within larger tenders.",
        ),
        (
            "Planned carpet, hard-floor and specialist surface care with defined frequencies and scope.",
            "Regular carpet and hard-floor care with a clear schedule and agreed list of work.",
        ),
        ("Periodic restoration", "Planned deep cleaning and finish renewal"),
        (
            "Deep cleans, strip-and-seal, extraction, grout restoration and other periodic technical tasks.",
            "Deep cleaning, old-finish removal, resealing, grout cleaning and other planned specialist work.",
        ),
        ("Tender technical package", "Floor-care support for tenders"),
        (
            "We can price and deliver the specialist floor-care portion of a larger cleaning or facilities tender without pretending to own the whole contract.",
            "We can price and deliver the floor-care portion of a larger cleaning or facilities tender while working clearly within your contract structure.",
        ),
        ("Built for measurable scope.", "Clear plans and predictable pricing."),
        (
            "Commercial pricing should come from surface area, condition, production rate, access, frequency and required finish — not a generic hourly guess.",
            "Commercial pricing is based on floor area, condition, access, service frequency and the finish you need, so the quote reflects the actual work.",
        ),
        ("What a commercial scope can include", "What your service plan can include"),
        ("Surface inventory and measurements", "Floor types and measurements"),
        ("Method and frequency recommendation", "Recommended cleaning method and schedule"),
        ("Access / after-hours assumptions", "Access and after-hours arrangements"),
        ("Periodic and recurring tasks", "One-off and regular tasks"),
        ("Service schedule or BOQ-based pricing", "Itemised or schedule-based pricing"),
        ("Procurement &amp; facilities", "Facilities and tender enquiries"),
        (
            "Send it through the enquiry form. We can review the technical floor-care component and identify where a site inspection is required.",
            "Send it through the enquiry form. We can review the floor-care requirements and confirm whether a site inspection is needed.",
        ),
    ],
    "about/index.html": [
        (
            "A floor-care specialist, not a general cleaner pretending every floor is the same.",
            "Specialist care for the floors throughout your home or business.",
        ),
        (
            "Voila Floor Cleaning &amp; Restoration is the independent floor-care trading direction of Midwest Trade Hub Pty Ltd, built around technical method selection, clear scope and better operating systems.",
            "Voila Floor Cleaning &amp; Restoration is a Geraldton-based service from Midwest Trade Hub Pty Ltd, focused on cleaning, restoring and maintaining carpet and hard floors.",
        ),
        ("Our operating idea", "Our approach"),
        (
            "Different surfaces need different chemistry, agitation, moisture, pressure and protection systems. We aim to choose the least complicated method that can safely achieve the required outcome — and explain when a limitation is permanent or outside our scope.",
            "Every floor is different. We choose products, equipment and moisture levels to suit the material and its condition. We explain what can be improved, what may be permanent and when a different service is needed.",
        ),
        (
            "Geraldton and the surrounding Mid West are the core service area, with regional commercial work assessed by scope and mobilisation requirements.",
            "Geraldton and the surrounding Mid West are our core service area. Regional commercial jobs are considered based on job size, travel and availability.",
        ),
        (
            "Technology should reduce admin, not remove judgement.",
            "Clear communication from enquiry to completion.",
        ),
        (
            "Our systems are being built so enquiries, documentation and routine follow-up can be streamlined while pricing, technical scope, safety-sensitive work and customer commitments remain human-controlled.",
            "We use simple systems to keep enquiries and follow-up organised, while every recommendation, quote and customer commitment is reviewed by a person.",
        ),
    ],
    "areas/index.html": [
        (
            "Our core service area is Geraldton and surrounding suburbs. Larger regional commercial work is assessed based on scope, travel and mobilisation.",
            "We serve Geraldton and surrounding suburbs. Larger regional commercial jobs are considered based on job size, travel and availability.",
        ),
        ("Local SEO without fake suburb pages", "Local service, honest information"),
        (
            "We publish genuinely useful Geraldton-specific service information and project evidence instead of creating dozens of near-identical pages that simply swap a suburb name.",
            "We provide floor care for Geraldton homes, businesses and facilities. If you are unsure whether we cover your area, call, text or send an enquiry.",
        ),
        (
            "For larger commercial, contractor and tender scopes outside Geraldton, submit the location and approximate floor area so mobilisation can be assessed.",
            "For larger commercial jobs outside Geraldton, tell us the location and approximate floor area. We will confirm travel and availability.",
        ),
    ],
    "contact/index.html": [
        ("Structured enquiry", "Request a quote"),
        ("Tell us enough to assess the next step.", "Tell us about your floor."),
        (
            "Approximate areas, floor type, condition, timing and photos can make the difference between a useful response and twenty questions later.",
            "Share the floor type, approximate size, condition and preferred timing. A few useful details help us give you a clearer response.",
        ),
        ("Request a quote / assessment", "Request a quote"),
        ("Complex jobs are reviewed by a person", "Some jobs need a closer look"),
        (
            "Water damage, mould/contamination, hazardous materials, insurance/liability issues, guarantee requests and technically ambiguous work are not auto-approved by the intake system.",
            "Water damage, mould, hazardous materials, insurance claims or uncertain floor damage need a personal review before we recommend any work.",
        ),
        (
            "Photo upload will be enabled once the production file-storage workflow is connected. For now, submit the enquiry first and we can request images securely.",
            "Photo upload is coming soon. For now, submit the enquiry or call or text us, and we can arrange a safe way to share photos.",
        ),
        (
            "Tender schedules, floor plans and BOQs can be reviewed after initial contact.",
            "Tender schedules, floor plans and itemised work lists can be reviewed after initial contact.",
        ),
    ],
    "privacy/index.html": [
        (
            "Voila Floor collects only information reasonably needed to respond to enquiries, scope work, schedule service and maintain business records.",
            "Voila Floor collects only the information needed to respond to enquiries, understand and quote work, schedule services and keep business records.",
        ),
        ("Automation and AI-assisted processing", "How enquiry information is handled"),
        (
            "Enquiry information may be processed by business software and controlled automation to structure the request, identify missing information and prepare drafts. Higher-risk or ambiguous decisions are routed for human review. We do not intentionally use customer enquiries to train public AI models.",
            "Business software may help organise your enquiry, check for missing details and prepare internal drafts. A person reviews unusual, complex or higher-risk requests. Customer enquiries are not intentionally used to train public AI models.",
        ),
        ("Data minimisation", "Information you should not send"),
    ],
    "case-studies/index.html": [
        (
            "The right method depends on the surface, its construction, its condition and the outcome required.",
            "Every floor is different, so we check its material and condition before recommending the safest practical approach.",
        ),
        (
            "Different floors.<br>Surface-led care.",
            "Different floors.<br>Results you can see.",
        ),
        (
            "These comparisons show completed Voila Floor projects across residential and commercial settings. Captions identify the surface only; an inspection is needed before any process or outcome can be recommended.",
            "These are real Voila Floor projects from homes and commercial properties. We still need to inspect your floor before recommending a treatment or predicting the result.",
        ),
        ("Resilient floor corridor", "Vinyl floor corridor"),
        ("Commercial resilient floor", "Commercial vinyl floor"),
        ("Resilient floor tiles", "Vinyl floor tiles"),
        ("Explore resilient floor service", "Explore vinyl floor service"),
        ("Need a floor assessed?", "Want to know what may be possible for your floor?"),
        (
            "Show us the surface and what needs attention.",
            "Show us the floor and tell us what needs attention.",
        ),
        (
            "Share the floor type, approximate area, condition and preferred timing. We’ll identify whether the job can be scoped remotely or needs an inspection.",
            "Share the floor type, approximate area, condition and preferred timing. We will let you know whether we can quote from those details or need to inspect the floor.",
        ),
    ],
    "blog/index.html": [
        (
            "Practical guides for Geraldton homes, property teams and facilities — built around real surfaces, maintenance decisions and common problems rather than generic SEO filler.",
            "Clear, practical guides for Geraldton homes, property teams and facilities, based on common floor problems and real maintenance choices.",
        ),
        (
            "Choosing between deep extraction and low-moisture maintenance.",
            "A simple guide to choosing a deeper clean or a faster-drying maintenance clean.",
        ),
        (
            "Residue, soil loading and the limits of surface-only cleaning.",
            "Why dirt and cleaning product can build up in grout.",
        ),
        (
            "Maintenance intervals, appearance and avoiding avoidable restoration cycles.",
            "How regular care can protect appearance and avoid larger restoration jobs.",
        ),
    ],
    "blog/hwe-vs-encapsulation-geraldton/index.html": [
        (
            "Carpet cleaning in Geraldton is not a choice between a “good” machine and a “bad” one. Hot water extraction and encapsulation solve different maintenance problems.",
            "Carpet cleaning is not about one machine being better than every other option. A deeper hot-water clean and a faster-drying low-moisture clean suit different situations.",
        ),
        ("What the process actually does", "How the two cleaning options work"),
        (
            "Hot water extraction (HWE) uses controlled solution application, agitation where required and extraction to remove suspended soil and residues. Encapsulation uses low-moisture chemistry designed to surround remaining soil so it can be removed through subsequent vacuuming.",
            "Deep hot-water cleaning, often called steam cleaning, rinses the carpet and removes loosened dirt and cleaning residue. Low-moisture cleaning uses much less water and leaves loosened dirt ready to be removed during later vacuuming.",
        ),
        ("Where professional method selection matters", "Which option may suit your carpet"),
        (
            "HWE is often appropriate when carpet needs restorative flushing, heavy-soil removal or extraction of residues. Encapsulation is useful for suitable commercial carpet maintenance, faster drying and areas where repeated low-moisture care makes operational sense.",
            "A deep hot-water clean may suit heavily marked carpet or built-up residue. Low-moisture cleaning can be useful for routine commercial maintenance, faster drying and areas that need to return to use sooner.",
        ),
        ("What can go wrong", "Why the carpet still needs to be checked"),
        (
            "For wool and wool-rich carpet, fibre identification, chemistry, heat, agitation and moisture control matter. The method should be selected after considering construction, dye stability and condition — not because one method is fashionable.",
            "Wool and wool-rich carpets need careful product, temperature and moisture choices. We check the fibre, colour stability, construction and condition before recommending a cleaning method.",
        ),
        (
            "If you are comparing quotes, ask what method is being proposed and why. A useful answer should connect the method to your carpet, soil load, access and required outcome.",
            "If you are comparing quotes, ask which cleaning option is being recommended and why. The answer should relate to your carpet, the dirt or staining, access, drying time and the result you want.",
        ),
    ],
    "blog/tile-grout-maintenance-geraldton/index.html": [
        ("What the process actually does", "Why grout gets dirty again"),
        (
            "Grout is typically more porous and textured than the face of a glazed tile. Soil, cleaning residues and contaminated solution can accumulate in low points while a mop repeatedly moves material across the surface.",
            "Grout is usually more porous and textured than the tile itself. Dirt and leftover cleaning product can settle into the grout while a mop repeatedly moves dirty water across the floor.",
        ),
        ("Where professional method selection matters", "When a deeper clean can help"),
        (
            "A professional deep clean may combine suitable chemistry, dwell time, mechanical agitation and extraction. Controlled high-pressure cleaning can be useful on appropriate installations, but pressure is not automatically suitable for every grout line, substrate or waterproofing situation.",
            "A professional deep clean may use a product suited to the tile, time for it to work, thorough scrubbing and rinsing that removes dirty water instead of spreading it around. Pressure cleaning can help on suitable floors, but not every grout line, base or waterproofed area can safely handle it.",
        ),
        ("What can go wrong", "Why inspection matters"),
        (
            "If grout is failing, loose, heavily eroded or the substrate is moisture-sensitive, aggressive cleaning can make a building problem worse. That is why inspection matters before selecting pressure or chemistry.",
            "If grout is loose, badly worn or sitting over a moisture-sensitive base, aggressive cleaning can make the problem worse. We inspect the floor before deciding whether pressure cleaning is safe.",
        ),
        (
            "After restoration, simpler maintenance usually works better: correct dilution, clean solution, frequent pad/mop changes and avoiding unnecessary product buildup.",
            "After a deep clean, use the recommended amount of product, fresh water and clean mop heads or pads. Too much product can leave a sticky film that attracts more dirt.",
        ),
    ],
    "blog/commercial-floor-care-programs-geraldton/index.html": [
        (
            "For many Geraldton facilities, the cheapest floor-care plan is not “clean it when it looks bad”.",
            "For many Geraldton facilities, waiting until a floor looks bad can make the eventual clean more expensive and disruptive.",
        ),
        ("What the process actually does", "Why planned care costs less"),
        (
            "Carpet, resilient floors, rubber, tile, grout and coated surfaces all change gradually under traffic. By the time a floor looks obviously poor, the required intervention can be much more disruptive than a planned maintenance task.",
            "Carpet, vinyl, rubber, tile, grout and coated floors all change gradually with use. By the time a floor looks obviously worn or dirty, restoring it may require more time, cost and disruption than regular planned care.",
        ),
        ("Where professional method selection matters", "How a maintenance plan helps"),
        (
            "A practical plan separates routine in-house cleaning from periodic specialist work. Commercial carpet may alternate regular vacuuming with scheduled encapsulation and less frequent extraction. Resilient floors may need cleaning plus periodic recoats or burnishing before a full strip becomes necessary.",
            "A practical plan separates day-to-day cleaning from periodic professional work. Commercial carpet may need regular vacuuming, faster-drying maintenance cleans and occasional deep rinsing. Vinyl floors may need machine cleaning and a refreshed protective finish before a full strip and reseal becomes necessary.",
        ),
        ("What can go wrong", "How often should it be done?"),
        (
            "The right frequency is site-specific. Foot traffic, soil entry, weather, building use, matting, cleaning standards and appearance expectations all matter. A useful contractor should be able to explain the trigger for each task.",
            "The right schedule depends on foot traffic, sand and dirt brought inside, weather, building use, entrance matting and the appearance you need to maintain. We explain what each service is for and when it is likely to be needed.",
        ),
        (
            "For tender and facilities work, we can scope only the technical floor-care component — measurements, method, periodic frequency, production assumptions and exclusions — so it can sit cleanly inside a larger contract.",
            "For tenders and facilities work, we can measure the floors, recommend methods and service intervals, and clearly list what is included so the floor-care work fits into a larger contract.",
        ),
    ],
}

