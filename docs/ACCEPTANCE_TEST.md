# Lead Intake Acceptance Test

## Business KPIs
- median enquiry-to-acknowledgement time;
- lead completeness;
- admin minutes/enquiry;
- owner correction rate;
- duplicate record rate;
- unsafe customer-facing action rate (target zero).

## Technical pass criteria
- unit tests pass;
- 50-case evaluation >=95% correct service/risk routing;
- 100% of water/mould/contamination/guarantee cases route to human review;
- replay attempts create no duplicate audit record/job;
- credentials absent from repo and exported test artefacts;
- ServiceM8 writes remain blocked unless explicitly enabled.
