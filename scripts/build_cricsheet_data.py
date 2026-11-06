#!/usr/bin/env python3
"""
Build Power BI-ready IPL match and delivery CSVs from Cricsheet's IPL JSON archive.

Usage:
    python scripts/build_cricsheet_data.py

Outputs:
    01_Dataset/Processed/matches.csv
    01_Dataset/Processed/deliveries.csv

Source: https://cricsheet.org/downloads/ipl_json.zip
Data attribution: Cricsheet (CC BY 4.0). Keep the attribution in this repository.
"""
from __future__ import annotations

import csv
import json
import urllib.request
import zipfile
from pathlib import Path
from io import BytesIO

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "01_Dataset" / "Processed"
ZIP_URL = "https://cricsheet.org/downloads/ipl_json.zip"

MATCH_FIELDS = [
    "match_id", "season", "date", "city", "venue", "match_type",
    "match_stage", "team1", "team2", "toss_winner", "toss_decision",
    "winner", "result", "result_margin", "result_margin_type",
    "player_of_match", "method", "overs"
]
DELIVERY_FIELDS = [
    "match_id", "season", "date", "innings", "over", "ball",
    "batting_team", "bowling_team", "batter", "bowler", "non_striker",
    "batter_runs", "extra_runs", "total_runs", "bowler_runs",
    "extras_type", "is_legal_ball", "batter_ball_faced",
    "is_wicket", "player_dismissed", "dismissal_kind", "fielder",
    "is_bowler_credit_wicket", "is_super_over"
]
BOWLER_CREDIT_DISMISSALS = {
    "bowled", "caught", "caught and bowled", "lbw", "stumped", "hit wicket"
}

def joined(values):
    return " | ".join(str(x) for x in values if x not in (None, ""))

def write_csv(path: Path, fields: list[str], rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

def main():
    print("Downloading Cricsheet IPL JSON archive...")
    request = urllib.request.Request(ZIP_URL, headers={"User-Agent": "IPL-PowerBI-Portfolio/1.0"})
    with urllib.request.urlopen(request, timeout=120) as response:
        archive_bytes = response.read()

    match_rows = []
    delivery_rows = []
    with zipfile.ZipFile(BytesIO(archive_bytes)) as archive:
        json_files = [n for n in archive.namelist() if n.lower().endswith(".json")]
        for index, name in enumerate(json_files, start=1):
            try:
                data = json.loads(archive.read(name).decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue

            info = data.get("info", {})
            teams = info.get("teams", [])
            toss = info.get("toss", {})
            outcome = info.get("outcome", {})
            by = outcome.get("by", {}) or {}
            event = info.get("event", {}) or {}
            dates = info.get("dates", [])
            match_id = Path(name).stem
            date = dates[0] if dates else ""
            winner = outcome.get("winner", "")
            margin_type = next(iter(by.keys()), "")
            margin_value = by.get(margin_type, "") if margin_type else ""
            result = outcome.get("result", "normal" if winner else "no result")

            match_rows.append({
                "match_id": match_id,
                "season": info.get("season", ""),
                "date": date,
                "city": info.get("city", ""),
                "venue": info.get("venue", ""),
                "match_type": info.get("match_type", ""),
                "match_stage": event.get("stage", event.get("match_number", "")),
                "team1": teams[0] if len(teams) > 0 else "",
                "team2": teams[1] if len(teams) > 1 else "",
                "toss_winner": toss.get("winner", ""),
                "toss_decision": toss.get("decision", ""),
                "winner": winner,
                "result": result,
                "result_margin": margin_value,
                "result_margin_type": margin_type,
                "player_of_match": joined(info.get("player_of_match", [])),
                "method": outcome.get("method", ""),
                "overs": info.get("overs", "")
            })

            for innings_number, innings in enumerate(data.get("innings", []), start=1):
                batting_team = innings.get("team", "")
                is_super_over = bool(innings.get("super_over", False) or innings_number >= 3)
                for over_record in innings.get("overs", []):
                    over_number = over_record.get("over", 0)
                    for ball_number, delivery in enumerate(over_record.get("deliveries", []), start=1):
                        runs = delivery.get("runs", {}) or {}
                        extras = delivery.get("extras", {}) or {}
                        wickets = delivery.get("wickets", []) or []
                        extra_types = list(extras.keys())
                        is_legal = not any(k in extras for k in ("wides", "noballs"))
                        byes = extras.get("byes", 0) + extras.get("legbyes", 0) + extras.get("penalty", 0)
                        bowler_runs = runs.get("total", 0) - byes
                        dismissed = [w.get("player_out", "") for w in wickets]
                        dismissal_kinds = [w.get("kind", "") for w in wickets]
                        fielders = []
                        for wicket in wickets:
                            for fielder in wicket.get("fielders", []) or []:
                                fielders.append(fielder.get("name", "") if isinstance(fielder, dict) else str(fielder))
                        delivery_bowler = delivery.get("bowler", "")
                        delivery_rows.append({
                            "match_id": match_id,
                            "season": info.get("season", ""),
                            "date": date,
                            "innings": innings_number,
                            "over": over_number,
                            "ball": ball_number,
                            "batting_team": batting_team,
                            "bowling_team": next((t for t in teams if t != batting_team), ""),
                            "batter": delivery.get("batter", ""),
                            "bowler": delivery_bowler,
                            "non_striker": delivery.get("non_striker", ""),
                            "batter_runs": runs.get("batter", 0),
                            "extra_runs": runs.get("extras", 0),
                            "total_runs": runs.get("total", 0),
                            "bowler_runs": bowler_runs,
                            "extras_type": joined(extra_types),
                            "is_legal_ball": int(is_legal),
                            "batter_ball_faced": int("wides" not in extras),
                            "is_wicket": int(bool(wickets)),
                            "player_dismissed": joined(dismissed),
                            "dismissal_kind": joined(dismissal_kinds),
                            "fielder": joined(fielders),
                            "is_bowler_credit_wicket": int(any(k in BOWLER_CREDIT_DISMISSALS for k in dismissal_kinds)),
                            "is_super_over": int(is_super_over)
                        })

            if index % 100 == 0:
                print(f"Processed {index:,}/{len(json_files):,} JSON files...")

    match_rows.sort(key=lambda r: (str(r["date"]), str(r["match_id"])))
    delivery_rows.sort(key=lambda r: (str(r["date"]), str(r["match_id"]), int(r["innings"]), int(r["over"]), int(r["ball"])))
    write_csv(OUT / "matches.csv", MATCH_FIELDS, match_rows)
    write_csv(OUT / "deliveries.csv", DELIVERY_FIELDS, delivery_rows)
    print(f"Done. Matches: {len(match_rows):,}; deliveries: {len(delivery_rows):,}")
    print(f"Files written to: {OUT}")

if __name__ == "__main__":
    main()
