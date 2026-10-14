#!/usr/bin/env python3
"""Cross-check the MarkPS4 frontend against the real PS4 payload API."""
from pathlib import Path

ui = Path("app/index.html").read_text(encoding="utf-8")
server = Path("reference/ps4-app/onconsole/server_ps4.c").read_text(encoding="utf-8")
lane = Path("reference/ps4-app/onconsole/github_lane.h").read_text(encoding="utf-8")

checks = {
    "download route": '"/api/engine/fetch"' in server and '"/api/download/status"' in server,
    "local package install": '"/api/install"' in server and '"install_key"' in server,
    "install job polling": '"/api/engine/job"' in server,
    "health route": '"/api/health"' in server,
    "HTTPS redirect handling": "sceHttpSetAutoRedirect(tmpl, 1);" in lane,
    "MarkPS4 UI requests download": "/api/engine/fetch?" in ui,
    "MarkPS4 UI requests status": "/api/download/status" in ui,
    "MarkPS4 UI installs local PKG": "'local:' + path" in ui,
}
failed = [name for name, ok in checks.items() if not ok]
for name, ok in checks.items():
    print(("OK" if ok else "FAIL") + ": " + name)
if failed:
    raise SystemExit("API integration checks failed: " + ", ".join(failed))
print("Cross-repository API compatibility checks passed.")
