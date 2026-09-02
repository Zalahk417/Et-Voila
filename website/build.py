from pathlib import Path
import base64
import io
import shutil
import zipfile

HERE = Path(__file__).resolve().parent
DIST = HERE / "dist"
ARCHIVE = HERE / "archive"
CONTENT = HERE / "content"
PARTS = [
    "part-01.b64",
    "part-02.b64",
    "part-03a.b64",
    "part-03b.b64",
    "part-04a.b64",
    "part-04b.b64",
]

PHONE_DISPLAY = "0402 221 071"
PHONE_E164 = "+61402221071"


def add_public_phone_details() -> None:
    footer_anchor = '<a href="/contact/">Request a quote</a><a href="/areas/">'
    footer_with_phone = (
        '<a href="/contact/">Request a quote</a>'
        f'<a href="tel:{PHONE_E164}">Call {PHONE_DISPLAY}</a>'
        f'<a href="sms:{PHONE_E164}">Text {PHONE_DISPLAY}</a>'
        '<a href="/areas/">'
    )
    contact_panel = '<div class="info"><h3>Complex jobs are reviewed by a person</h3>'
    contact_panel_with_phone = (
        '<div class="info"><div class="surface"><b>Prefer to call or text?</b><br>'
        f'<a href="tel:{PHONE_E164}">Call {PHONE_DISPLAY}</a> · '
        f'<a href="sms:{PHONE_E164}">Text {PHONE_DISPLAY}</a></div>'
        '<h3>Complex jobs are reviewed by a person</h3>'
    )
    privacy_draft = (
        "Contact details for privacy requests will be published before public launch. "
        "This page is a website implementation draft and must be reviewed against the "
        "final business contact details and systems before production activation."
    )
    privacy_contact = (
        f'For privacy questions, access requests or corrections, call or text '
        f'<a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a>.'
    )

    replacements = {"footer": 0, "contact": 0, "privacy": 0, "schema": 0}
    html_paths = list(DIST.rglob("*.html"))

    for html_path in html_paths:
        html = html_path.read_text(encoding="utf-8")
        replacements["footer"] += html.count(footer_anchor)
        replacements["contact"] += html.count(contact_panel)
        replacements["privacy"] += html.count(privacy_draft)
        html = html.replace(footer_anchor, footer_with_phone)
        html = html.replace(contact_panel, contact_panel_with_phone)
        html = html.replace(privacy_draft, privacy_contact)

        if html_path == DIST / "index.html":
            schema_anchor = '"url":"https://www.voilafloor.com.au","areaServed"'
            replacements["schema"] += html.count(schema_anchor)
            html = html.replace(
                schema_anchor,
                f'"url":"https://www.voilafloor.com.au","telephone":"{PHONE_E164}","areaServed"',
            )

        html_path.write_text(html, encoding="utf-8")

    expected = {"footer": len(html_paths), "contact": 1, "privacy": 1, "schema": 1}
    if replacements != expected:
        raise RuntimeError(f"Phone detail injection mismatch: {replacements} != {expected}")

    site_js = DIST / "assets" / "site.js"
    javascript = site_js.read_text(encoding="utf-8")
    fallback_message = "We could not send that enquiry. Please try again shortly."
    if javascript.count(fallback_message) != 1:
        raise RuntimeError("Enquiry error fallback message was not found exactly once")
    javascript = javascript.replace(
        fallback_message,
        f"We could not send that enquiry. Please call or text {PHONE_DISPLAY}.",
    )
    site_js.write_text(javascript, encoding="utf-8")


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    payload = "".join((ARCHIVE / name).read_text(encoding="utf-8").strip() for name in PARTS)
    data = base64.b64decode(payload, validate=True)

    root = DIST.resolve()
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        for member in archive.infolist():
            target = (DIST / member.filename).resolve()
            if target != root and root not in target.parents:
                raise RuntimeError(f"Unsafe archive path: {member.filename}")
        archive.extractall(DIST)

    if CONTENT.exists():
        shutil.copytree(CONTENT, DIST, dirs_exist_ok=True)

    add_public_phone_details()

    files = sum(1 for path in DIST.rglob("*") if path.is_file())
    print(f"Voila Floor website built: {files} static files -> {DIST}")


if __name__ == "__main__":
    main()

