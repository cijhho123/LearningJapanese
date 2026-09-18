"""Download a learning resource into the repo so it is available offline.

HTTPS only, with certificate verification left on, including across redirects.
Anything else is refused with an explanation rather than silently downgraded.

Usage:
    python fetch_resource.py <https-url> --topic Grammar --title "Tae Kim"
    python fetch_resource.py <https-url> --topic Kanji --dry-run
"""

from __future__ import annotations

import argparse
import re
import ssl
import sys
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb  # noqa: E402

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):  # pragma: no cover
        pass

MAX_BYTES = 200 * 1024 * 1024          # refuse to silently pull down a DVD image
TIMEOUT = 60
USER_AGENT = "japanese-tutor/0.1 (+local study tool)"

_CONTENT_EXT = {
    "text/html": ".html",
    "text/plain": ".txt",
    "text/markdown": ".md",
    "application/pdf": ".pdf",
    "application/json": ".json",
    "application/zip": ".zip",
    "application/epub+zip": ".epub",
}


class InsecureRedirect(urllib.error.URLError):
    pass


class _HttpsOnlyRedirectHandler(urllib.request.HTTPRedirectHandler):
    """A server can redirect anywhere. Re-check the scheme on every hop."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urlsplit(newurl).scheme.lower() != "https":
            raise InsecureRedirect(
                "refused: the server redirected to a non-HTTPS address (%s)" % newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _opener():
    # Default context: verifies certificates and checks hostnames. Never relaxed.
    context = ssl.create_default_context()
    return urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=context), _HttpsOnlyRedirectHandler()
    )


def _safe_name(text, fallback="resource"):
    text = unquote(text)
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r'[<>:"/\\|?*\x00-\x1f]', " ", text)
    text = re.sub(r"\s+", " ", text).strip(" .")
    return (text or fallback)[:120]


def fetch(url, topic, title=None, dry_run=False):
    scheme = urlsplit(url).scheme.lower()
    if scheme != "https":
        return {
            "ok": False,
            "error": "Only HTTPS addresses are downloaded (this one is %r).\n"
                     "If the site has no HTTPS version, save the page manually into\n"
                     "Resources/%s/ and register it with:\n"
                     "  python kb.py resource-add \"<path>\" \"<title>\""
                     % (scheme or "a local path", topic),
        }

    # Validate the topic at the boundary: it is joined into a filesystem path,
    # so "../.." would write outside the repo and then be registered as active.
    resources_root = (kb.repo_root() / "Resources").resolve()
    dest_dir = (resources_root / topic).resolve()
    if not (dest_dir == resources_root or resources_root in dest_dir.parents):
        return {"ok": False,
                "error": "Topic %r resolves outside Resources/. Use a plain topic "
                         "folder name." % topic}
    if not dest_dir.exists():
        return {"ok": False,
                "error": "No such topic folder: %s\nExisting topics: %s"
                         % (dest_dir, ", ".join(sorted(
                             p.name for p in (kb.repo_root() / "Resources").iterdir()
                             if p.is_dir())))}

    if dry_run:
        return {"ok": True, "dry_run": True, "would_save_under": str(dest_dir)}

    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with _opener().open(request, timeout=TIMEOUT) as response:
            declared = response.headers.get("Content-Length")
            if declared and int(declared) > MAX_BYTES:
                return {"ok": False,
                        "error": "That file is %.1f MB, over the %d MB limit. Download it "
                                 "manually if you really want it."
                                 % (int(declared) / 1e6, MAX_BYTES // 1024 // 1024)}
            payload = response.read(MAX_BYTES + 1)
            content_type = (response.headers.get("Content-Type") or "").split(";")[0].strip()
            final_url = response.geturl()
    except InsecureRedirect as exc:
        return {"ok": False, "error": str(exc)}
    except (urllib.error.HTTPError, urllib.error.URLError, OSError, ValueError) as exc:
        return {"ok": False, "error": "Could not download it: %s" % exc}

    if len(payload) > MAX_BYTES:
        return {"ok": False, "error": "File exceeded the %d MB limit; nothing saved."
                                      % (MAX_BYTES // 1024 // 1024)}

    parts = urlsplit(final_url)
    stem = Path(unquote(parts.path)).name
    suffix = Path(stem).suffix or _CONTENT_EXT.get(content_type, ".html")
    label = title or Path(stem).stem or parts.netloc
    folder = dest_dir / _safe_name(label)
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / _safe_name(Path(stem).stem or "index", "index")
    target = target.with_suffix(suffix)
    target.write_bytes(payload)

    (folder / "SOURCE.txt").write_text(
        "Downloaded by japanese-tutor\nsource: %s\ncontent-type: %s\nbytes: %d\n"
        % (final_url, content_type or "unknown", len(payload)),
        encoding="utf-8",
    )

    rel = target.relative_to(kb.repo_root()).as_posix()
    kb.add_resource(rel, title or label, topic=topic, status="active",
                    notes="downloaded from %s" % final_url)
    return {"ok": True, "saved": rel, "bytes": len(payload),
            "content_type": content_type, "source": final_url, "status": "active"}


def main(argv=None):
    p = argparse.ArgumentParser(prog="fetch_resource.py")
    p.add_argument("url")
    p.add_argument("--topic", required=True,
                   help="a folder name under Resources/, e.g. Grammar")
    p.add_argument("--title")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args(argv)

    result = fetch(a.url, a.topic, a.title, a.dry_run)
    if result.get("ok"):
        if result.get("dry_run"):
            print("Would save under: %s" % result["would_save_under"])
        else:
            print("Saved   : %s (%d bytes, %s)"
                  % (result["saved"], result["bytes"], result["content_type"] or "?"))
            print("Source  : %s" % result["source"])
            print("Status  : active - the tutor can now teach from it")
            print()
            print("Note: this did not edit any Resources/*/readme.md. Mention it there")
            print("yourself if you want it in the topic guide.")
        return 0
    print("Not downloaded.")
    print(result["error"])
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
