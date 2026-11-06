# IPL dataset download instructions

## Recommended full historical source: Cricsheet
Use Cricsheet's official downloads page: https://cricsheet.org/downloads/

Choose **Indian Premier League → Men → JSON**. The current competition archive includes match files across the available IPL seasons. The Cricsheet downloads page lists 1,243 IPL matches at the time this project was prepared. Coverage can change as records are updated.

Cricsheet data is licensed under **CC BY 4.0**. Attribute Cricsheet as the source and follow the license terms:
- https://cricsheet.org/
- https://creativecommons.org/licenses/by/4.0/

## Generate Power BI CSV files
From the repository root run:

```bash
python scripts/build_cricsheet_data.py
```

The script downloads the IPL JSON ZIP and creates:
- `01_Dataset/Processed/matches.csv`
- `01_Dataset/Processed/deliveries.csv`

The script requires Python 3.10+ and uses only the Python standard library.

## Additional 2026 reference files
The `Raw/` folder includes `matches_2026.csv` and `points_table_2026.csv` sourced from openIPL. They are optional reference files; use the Cricsheet-generated tables as the primary dataset to avoid duplicate matches. openIPL states that its derived cricket data is sourced from Cricsheet and licensed CC BY 4.0: https://github.com/sachin-dul/openIPL

## Notes
- The schema template CSVs in this folder contain headers only; they are not real match data.
- Do not append reference files until you check duplicate matches and normalize match IDs.
- Validate season totals, match outcomes and player statistics against scorecards before publishing.
