#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


RELEASE_INFO_RELATIVE = Path("paper/release_info.tex")
OUTPUT_RELATIVE = Path("paper/paper_release_manifest.json")
PDFS = {
    "observers_are_all_you_need": Path("paper/observers_are_all_you_need.pdf"),
    "reality_as_consensus_protocol": Path("paper/reality_as_consensus_protocol.pdf"),
    "recovering_relativity_and_standard_model_structure_from_observer_overlap_consistency_compact": Path(
        "paper/recovering_relativity_and_standard_model_structure_from_observer_overlap_consistency_compact.pdf"
    ),
}


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    release_info = (repo_root / RELEASE_INFO_RELATIVE).read_text(encoding="utf-8")
    release_id = extract_macro(release_info, "OPHPaperReleaseID")
    release_date = extract_macro(release_info, "OPHPaperReleaseDate")

    manifest = {
        "release_id": release_id,
        "released_at": release_date,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "papers": {},
    }
    for paper_id, relative_path in PDFS.items():
        pdf_path = repo_root / relative_path
        manifest["papers"][paper_id] = {
            "pdf_path": str(relative_path),
            "sha256": sha256(pdf_path),
            "size_bytes": pdf_path.stat().st_size,
        }

    output_path = repo_root / OUTPUT_RELATIVE
    output_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output_path)
    return 0


def extract_macro(text: str, macro_name: str) -> str:
    pattern = re.compile(r"\\newcommand\{\\%s\}\{([^}]*)\}" % re.escape(macro_name))
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"missing macro {macro_name} in release info")
    return match.group(1).strip()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


if __name__ == "__main__":
    raise SystemExit(main())
