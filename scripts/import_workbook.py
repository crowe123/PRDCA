#!/usr/bin/env python3
"""Convert the businesses workbook into data/listings.csv for the site build.

Usage:  python3 scripts/import_workbook.py path/to/pool_removal_california_businesses.xlsx

Writes one row per city and business (the workbook's By city tab), joined with
the licence and site details from the Businesses tab. Every status is kept;
build.py decides what is published.
"""
import csv
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "listings.csv"
FIELDS = ["city", "business", "phone", "base_city", "licence_number", "licence_status", "licence_name",
          "classifications", "status", "basis", "clarity", "site_says", "website"]


def rows(ws):
    it = ws.iter_rows(values_only=True)
    head = [str(h).strip() if h else "" for h in next(it)]
    for r in it:
        if any(v not in (None, "") for v in r):
            yield {h: ("" if v is None else str(v).strip()) for h, v in zip(head, r)}


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    wb = openpyxl.load_workbook(sys.argv[1], read_only=True, data_only=True)
    biz = {r["Business"]: r for r in rows(wb["Businesses"])}
    out = []
    for r in rows(wb["By city"]):
        b = biz.get(r["Business"], {})
        out.append({
            "city": r["City"],
            "business": r["Business"],
            "phone": r["Phone"],
            "base_city": r["Base city"],
            "licence_number": r["Licence number shown on site"],
            "licence_status": b.get("State board status (11 Oct 2026)", ""),
            "licence_name": b.get("Name on the licence", ""),
            "classifications": r["Classifications"],
            "status": r["Status"],
            "basis": r["Basis for listing under this city"],
            "clarity": b.get("How clearly it offers pool removal", ""),
            "site_says": b.get("What the site says", ""),
            "website": r["Website"],
        })
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, FIELDS)
        w.writeheader()
        w.writerows(out)
    print(f"Wrote {len(out)} city listings for {len(biz)} businesses to {OUT}")


if __name__ == "__main__":
    main()
