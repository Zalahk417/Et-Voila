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

    files = sum(1 for path in DIST.rglob("*") if path.is_file())
    print(f"Voila Floor website built: {files} static files -> {DIST}")


if __name__ == "__main__":
    main()
