from __future__ import annotations

import json
from dataclasses import dataclass, asdict

from voila_floor.servicem8 import ServiceM8Client


RELEASE_1 = {
    "queue": [
        {"name": "Lead Follow-Up"},
        {"name": "Awaiting Customer Access"},
        {"name": "Awaiting Deposit Payment"},
        {"name": "Ready to Schedule"},
    ],
    "badge": [
        {"name": "Intake Review"},
        {"name": "Urgent"},
        {"name": "Deposit Required"},
        {"name": "Complaint/Rework"},
        {"name": "Do Not Request Review"},
        {"name": "Commercial Prospect"},
        {"name": "Property Manager"},
        {"name": "Photo Pack"},
        {"name": "Form Required"},
    ],
}


@dataclass
class Result:
    resource: str
    name: str
    uuid: str
    created: bool


def deploy_release_1(client: ServiceM8Client) -> list[Result]:
    results: list[Result] = []
    for resource, records in RELEASE_1.items():
        for record in records:
            payload = dict(record)
            name = payload.pop("name")
            uuid, created = client.ensure_named_record(resource, name, payload)
            results.append(Result(resource, name, uuid, created))
    return results


def main() -> None:
    client = ServiceM8Client()
    results = deploy_release_1(client)
    print(json.dumps([asdict(result) for result in results], indent=2))


if __name__ == "__main__":
    main()
