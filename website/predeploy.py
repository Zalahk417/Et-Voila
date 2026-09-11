from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Mapping

HERE = Path(__file__).resolve().parent
PUBLIC_LAUNCH_ENV = "VOILA_PUBLIC_LAUNCH"
PRODUCTION_BRANCH = "main"
TRUTHY = {"1", "true", "yes", "on"}


def require_public_launch_authorisation(env: Mapping[str, str] | None = None) -> None:
    """Block Cloudflare production builds until Voilà is explicitly authorised for launch.

    Cloudflare Pages exposes the current Git branch as CF_PAGES_BRANCH. Preview
    branches remain buildable for QA. The production branch is deliberately
    fail-closed while JCC Geraldton remains the live customer-facing brand.
    """

    environment = os.environ if env is None else env
    branch = environment.get("CF_PAGES_BRANCH", "")
    launch_authorised = environment.get(PUBLIC_LAUNCH_ENV, "").strip().lower() in TRUTHY

    if branch == PRODUCTION_BRANCH and not launch_authorised:
        raise RuntimeError(
            "Production website deployment blocked: JCC Geraldton remains the live "
            "customer-facing brand. Set VOILA_PUBLIC_LAUNCH=true in Cloudflare only "
            "when the owner has explicitly approved the Voilà public cutover."
        )


def main() -> None:
    require_public_launch_authorisation()
    subprocess.run([sys.executable, "build.py"], cwd=HERE, check=True)


if __name__ == "__main__":
    main()
