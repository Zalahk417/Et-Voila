# Voila Floor — Website Service Architecture

## Positioning
**Voila Floor Cleaning & Restoration** is a specialist floor-care business for residential, commercial, strata and contracted environments. The public website should present clear service families while the ServiceM8/automation catalogue remains more granular.

## Primary website navigation

### Carpet Cleaning & Restoration
Customer-facing scope:
- hot water extraction (HWE);
- low-moisture encapsulation;
- wool carpet specialist cleaning;
- stain and spot removal;
- urine contamination extraction and odour treatment;
- carpet repairs.

Lead-form questions should collect: property type, suburb/postcode, rooms or approximate m², carpet/fibre if known, wool yes/no/unknown, stains, pets/urine, occupancy, stairs/access, timing and photos.

### Upholstery & Leather Care
- fabric upholstery cleaning;
- leather cleaning and conditioning.

Lead form: item type, seat count, fabric/leather if known, stains/odours, age/condition, access and photos.

### Tile & Grout Cleaning
- deep tile and grout cleaning;
- controlled high-pressure extraction/sanitation cleaning for suitable installations.

Lead form: area/m², tile type if known, grout condition, indoor/outdoor/wet area, grease/soil level, failed grout/loose tile indicators, access and photos.

### Natural Stone Cleaning & Protection
- limestone, travertine, marble, slate and other suitable natural stone cleaning;
- penetrating/impregnating sealing.

Lead form: stone type if known, m², current sealer/coating if known, stains/etching, interior/exterior, desired result and photos. Unknown stone types route to assessment rather than an automated method recommendation.

### Vinyl & Resilient Floor Care
- deep cleaning;
- strip and seal;
- maintenance recoat/top-coat;
- buffing and burnishing.

Lead form: floor type if known, m², existing finish/coating, age/condition, current maintenance method, access, operating hours and photos.

### Concrete & Epoxy Floor Care
- concrete deep cleaning;
- epoxy/resin floor cleaning and maintenance.

Lead form: surface type, area, soil/grease/contamination, interior/exterior, drainage/access, coating condition and photos. Hazardous/chemical contamination routes to human review.

### Gym & Rubber Flooring
- rubber tiles;
- rolled rubber;
- compatible specialist gym/sports flooring.

Lead form: floor system if known, m², facility type, chalk/grease/body-oil/soil concerns, recurring frequency, operating hours and photos.

### Floor Sealing, Recoating & Finishing
- micron/penetrating sealing;
- natural-stone sealing;
- strip and seal;
- recoating;
- buffing/burnishing.

This page is solution-led and should cross-link to the relevant substrate page rather than imply every finish is compatible with every floor.

### Commercial, Strata & Contract Floor Care
For offices, retail, strata/common areas, accommodation, facilities, gyms, property/facilities managers, cleaning contractors and flooring companies.

Offer pathways:
- one-off specialist deep cleaning;
- programmed/recurring floor care;
- strata maintenance;
- contractor/subcontract delivery;
- technical floor-care component of larger tenders;
- site inspections, scopes and schedules of rates.

Important tender wording: Voila Floor can service the **technical floor-care package within a larger tender** without representing that it provides unrelated cleaning/facilities services unless expressly contracted.

## Market landing pages
The service catalogue and market segment are separate dimensions. Build landing pages for:
- Residential;
- Commercial;
- Strata & Property Management;
- Facilities / Recurring Maintenance;
- Contractors & Tender Support.

These pages should reuse canonical service content rather than duplicate service descriptions verbatim.

## Website-to-automation contract
Every enquiry form sends a structured payload containing:
- source and campaign;
- customer/contact details;
- customer segment;
- site location;
- website service group;
- requested specialist service/method if selected;
- measurements/items;
- condition/problem statements;
- preferred timing;
- attachments/photos;
- consent/marketing preference where applicable;
- free-text message.

n8n/AI may classify and extract, but deterministic rules control required fields, high-risk routing and whether acknowledgement is safe. Price, substrate treatment method and customer guarantees remain human-controlled unless driven by an approved deterministic price rule.

## SEO/service-page rule
Do not create dozens of thin pages merely to target keywords. Create one strong canonical page per meaningful service family, then add specialist subpages only where the service has distinct intent, process, expertise or search demand — e.g. wool carpet cleaning, urine treatment, strip & seal, natural stone and commercial floor care.
