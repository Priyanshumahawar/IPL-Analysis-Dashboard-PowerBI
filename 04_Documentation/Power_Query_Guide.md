# Power Query build guide

## Suggested normalized tables
Use these logical table names in the model:
- `Matches`: one row per match, unique `match_id`
- `Deliveries`: one row per delivery, many rows per `match_id`
- `Teams`: one row per standardized franchise/team name
- `Players`: one row per player identity (if a reliable player key exists)
- `Date`: calendar table related to `Matches[date]`

## Steps
1. In Power BI Desktop select **Get Data > Text/CSV** and import the match and delivery files.
2. In Power Query use **Use First Row as Headers** where needed.
3. Set `match_id` to Whole Number or Text consistently in both tables.
4. Set dates to Date, runs/over/ball to Whole Number, and names/categories to Text.
5. Trim and clean text fields; replace inconsistent team and venue spellings using mapping tables.
6. Preserve original columns; create standardized columns rather than destroying source values.
7. Append season files only after confirming their schemas match.
8. Create a one-to-many relationship: `Matches[match_id]` (1) to `Deliveries[match_id]` (*).
9. Use single-direction filtering from dimensions to facts where possible.
10. Validate match counts, innings totals, player scorecards and bowling figures against source records.

## Data-quality checks
- Match IDs should be unique in `Matches`.
- Every delivery `match_id` should exist in `Matches`.
- Check null match IDs, dates, teams, batter and bowler names.
- Identify super overs and abandoned/no-result matches.
- Confirm whether the source stores wides/no-balls/byes/leg-byes separately.
- Compare total runs per innings with published scorecards before publishing.

## Important
Different datasets use different field names and scoring conventions. The DAX file is a starter template, not a guarantee that every formula works unchanged. Adapt it to the actual schema and document assumptions.