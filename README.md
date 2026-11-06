# IPL Analysis Dashboard using Power BI (2008–2026)

An educational cricket analytics project built around Microsoft Power BI, Power Query and DAX. The goal is to explore IPL match results, team performance, player batting/bowling metrics, toss decisions, venues and season trends.

## Current repository status
- Project documentation, dashboard blueprint, Power Query starter and DAX measures are committed.
- The repository includes reference match-level files for IPL 2026.
- The full historical ball-by-ball data is generated locally from Cricsheet using the script in `scripts/`.
- **A finished Power BI `.pbix` report is not included yet.** Power BI Desktop is required to load the data, create the visuals and save the report.

## Build the full dataset
1. Open `01_Dataset/CRICSHEET_DOWNLOAD_GUIDE.md`.
2. Download the men's Indian Premier League JSON archive from Cricsheet: https://cricsheet.org/downloads/
3. From the repository root run:

```bash
python scripts/build_cricsheet_data.py
```

The script downloads Cricsheet's IPL JSON archive and creates:
- `01_Dataset/Processed/matches.csv`
- `01_Dataset/Processed/deliveries.csv`

Cricsheet's JSON match data is licensed under the Open Data Commons Attribution License 1.0 (ODC-BY). The XML data has a separate CC BY 4.0 license; this project uses JSON. Credit Cricsheet and follow its attribution terms. See the guide for metric definitions and limitations.

## Import into Power BI
1. Open Power BI Desktop.
2. Import both processed CSV files using **Get Data → Text/CSV**.
3. Create a one-to-many relationship: `Matches[match_id]` → `Deliveries[match_id]`.
4. Add the measures in `03_DAX/DAX_Measures.dax`.
5. Follow `02_PowerBI/Dashboard_Blueprint.md` to build the report pages.
6. Save as `02_PowerBI/IPL_Analysis_Dashboard.pbix`.

## Dashboard pages
1. Overview — matches, seasons, runs, wickets and season trends.
2. Batting — run scorers, strike rate and batter comparisons.
3. Bowling — bowler-credit wickets, economy and bowling comparisons.
4. Teams & venues — wins, win percentage and venue performance.
5. Toss insights — toss decisions and match outcomes.

## Repository structure
- `01_Dataset/` — dataset instructions, schema templates, reference files and processed-data output folder.
- `02_PowerBI/` — report blueprint and Power Query M starter.
- `03_DAX/` — DAX measures.
- `04_Documentation/` — data dictionary, build guide, project report and resume description.
- `05_Screenshots/` — add genuine screenshots after building the report.
- `scripts/` — Cricsheet data preparation script.

## Important metric notes
- Legal balls exclude wides and no-balls.
- Batter balls faced exclude wides and include no-balls.
- Bowler runs exclude byes, leg-byes and penalty runs.
- Bowler-credit wickets include bowled, caught, caught and bowled, lbw, stumped and hit wicket.
- Super overs are flagged separately and excluded from standard match metrics in the starter measures.
- Team names, venues and match records can be revised by data providers; validate key totals against scorecards.

## References
- Cricsheet downloads: https://cricsheet.org/downloads/
- Cricsheet data format: https://cricsheet.org/format/
- Cricsheet license: https://creativecommons.org/licenses/by/4.0/
- openIPL 2026 reference data: https://github.com/sachin-dul/openIPL

IPL is a trademark of the BCCI. This independent educational project is not affiliated with or endorsed by the BCCI or IPL.
