from dataclasses import dataclass, asdict, field
from typing import Any

@dataclass
class Lead:
    source: str = "unknown"
    customer_name: str = ""
    email: str = ""
    phone: str = ""
    job_address: str = ""
    suburb: str = ""
    postcode: str = ""
    customer_type: str = "unknown"
    service: str = "unknown"
    message: str = ""
    measurements: str = ""
    preferred_timing: str = ""
    attachments_present: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

@dataclass
class LeadDecision:
    lead: Lead
    missing_fields: list[str]
    risk_flags: list[str]
    human_review_required: bool
    safe_acknowledgement_allowed: bool
    idempotency_key: str
    servicem8_job_draft: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "lead": self.lead.to_dict(),
            "missing_fields": self.missing_fields,
            "risk_flags": self.risk_flags,
            "human_review_required": self.human_review_required,
            "safe_acknowledgement_allowed": self.safe_acknowledgement_allowed,
            "idempotency_key": self.idempotency_key,
            "servicem8_job_draft": self.servicem8_job_draft,
        }
