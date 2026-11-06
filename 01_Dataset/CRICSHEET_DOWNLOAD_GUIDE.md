# Build the full IPL dataset (2008–2026)

## Recommended canonical source
Use Cricsheet's Indian Premier League men's JSON archive: https://cricsheet.org/downloads/

On the downloads page, choose **Indian Premier League → Men → JSON**. Cricsheet's page lists the archive by competition and year. The current archive is the source of truth for the latest available match coverage.

Cricsheet data is licensed under **CC BY 4.0**. Keep attribution to Cricsheet and follow the license terms. The project is independent and is not affiliated with the BCCI or IPL.

## Generate Power BI CSV files
1. Install Python 3.10 or newer.
2. Clone this repository or download it as a ZIP.
3. Open a terminal in the repository folder.
4. Run:

```bash
python scripts/build_cricsheet_data.py
```

The script downloads the IPL JSON archive and creates:
- `01_Dataset/Processed/matches.csv` — one row per match
- `01_Dataset/Processed/deliveries.csv` — one row per delivery

The script uses only Python's standard library; no pip packages are required.

## Import into Power BI
1. Open Power BI Desktop.
2. Select **Get Data → Text/CSV**.
3. Import both CSV files from `01_Dataset/Processed/`.
4. Set data types: date as Date; runs, over, ball, innings as Whole Number; other columns as Text.
5. Create a one-to-many relationship from `matches[match_id]` to `deliveries[match_id]`.
6. Use the DAX measures in `03_DAX/DAX_Measures.dax` as a starting point; adapt names to the generated schema.
7. Save the report as `02_PowerBI/IPL_Analysis_Dashboard.pbix`.

## Cricket metric definitions used by the generator
- Legal ball: a delivery that is not a wide or no-ball.
- Batter ball faced: excludes wides; includes no-balls.
- Bowler runs: total delivery runs less byes, leg-byes and penalty runs.
- Bowler-credit wicket: only bowled, caught, caught and bowled, lbw, stumped and hit wicket.
- Super overs: marked separately using the innings metadata / innings sequence.

Always validate edge cases against scorecards. Dataset providers may revise historical records, and the Cricsheet archive can change over time.

## Existing match-level CSVs
The `01_Dataset/Raw/` folder also contains a separate 2026 match list and points table from openIPL. Those files are optional reference material; do not append them to the Cricsheet-generated match table unless you first check for duplicate matches and normalize match IDs.
