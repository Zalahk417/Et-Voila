from __future__ import annotations
import argparse, json
from pathlib import Path
from .audit import log_decision
from .lead_intake import decide

def main() -> int:
    parser = argparse.ArgumentParser(description="Voila Floor lead intake dry-run")
    parser.add_argument("--input", required=True, help="JSON enquiry file")
    parser.add_argument("--no-audit", action="store_true")
    args = parser.parse_args()
    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    decision = decide(payload).to_dict()
    if not args.no_audit: decision["audit_inserted"] = log_decision(decision)
    print(json.dumps(decision, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__": raise SystemExit(main())
