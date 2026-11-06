# IPL Analysis Dashboard using Power BI (2008–2026)

An educational Power BI project template for exploring IPL match outcomes, team performance, batting and bowling statistics, toss decisions, venues and season trends.

> **Current status:** This GitHub repository contains the project documentation, starter DAX, Power Query guidance and CSV schema templates. It does **not** yet contain populated IPL datasets or a finished Power BI `.pbix` report. The CSV templates contain headers only.

## Dashboard pages
1. **Overview** — matches, seasons, runs, wicket events and season trends.
2. **Batting** — leading run scorers, strike rate, boundaries and sixes.
3. **Bowling** — bowler-credited wickets, economy and legal balls.
4. **Teams & venues** — team wins, win percentage and venue comparisons.
5. **Toss & match insights** — toss decisions and match outcomes.

## Repository structure
- `01_Dataset/` — dataset instructions and target CSV schemas.
- `02_PowerBI/` — dashboard blueprint; save the finished PBIX report here.
- `03_DAX/` — starter DAX measures.
- `04_Documentation/` — data dictionary, Power Query guide, project report and resume description.
- `05_Screenshots/` — add genuine screenshots after building the report.

## Getting started
1. Download match-level and ball-by-ball data from a source listed in `01_Dataset/DATA_DOWNLOAD_INSTRUCTIONS.md`.
2. Keep original data in a `Raw` folder and cleaned data in a `Cleaned` folder.
3. Import the data into Power BI Desktop using **Get Data → Text/CSV**.
4. Standardize columns and data types using the Power Query guide.
5. Create the relationship `Matches[match_id]` (1) to `Deliveries[match_id]` (*).
6. Adapt the measures in `03_DAX/DAX_Measures.dax` to the actual source schema.
7. Build the report pages described in `02_PowerBI/Dashboard_Blueprint.md`.
8. Validate totals against scorecards, save as `02_PowerBI/IPL_Analysis_Dashboard.pbix`, and add screenshots.

## Data and calculation cautions
- Check each dataset's coverage, schema and license before use; the listed sources may differ.
- Legal balls exclude wides and no-balls. Batter balls faced and bowler runs conceded follow specific scoring rules.
- Not every dismissal is credited to the bowler; exclude run-outs and other non-bowler dismissals from bowler wicket totals.
- Identify super overs separately and standardize franchise names across seasons.
- Verify champion records independently; most league-stage wins do not automatically mean the season title.

## Dataset references
- Historical IPL (2008–2024): https://github.com/waquararshadkhan/ipl-analytics
- IPL 2026 structured data: https://github.com/sachin-dul/openIPL
- Alternative IPL 2026 ball-by-ball data: https://github.com/heisenricher/IPL-2026-BALL-BY-BALL-DATA-
- Cricsheet: https://cricsheet.org/

Follow each provider's license and attribution requirements. This is an independent educational project and is not affiliated with or endorsed by the BCCI or IPL.

## Skills demonstrated
Power BI · Power Query · DAX · Data Cleaning · Data Modeling · Data Visualization · Cricket Analytics
