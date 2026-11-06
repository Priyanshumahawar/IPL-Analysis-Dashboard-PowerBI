# Dashboard build blueprint

## Theme
Use a clean sports-analytics layout. Suggested palette: navy background, white cards, restrained orange accent and light grey chart labels. Keep contrast high and avoid clutter.

## Global slicers
Season, team, venue, player and match stage. Ensure slicers interact consistently across pages.

## Page 1 — Overview
- KPI cards: Matches, Seasons, Total Runs, Wicket Events
- Column chart: matches by season
- Bar chart: team wins
- Table: season champion (only if champion mapping is verified)
- Line chart: average first-innings score by season

## Page 2 — Batting
- Bar chart: top batters by runs
- Scatter chart: runs vs strike rate
- KPI cards: runs, boundaries, sixes
- Season and team slicers
- Add a minimum balls-faced threshold for fair strike-rate comparisons

## Page 3 — Bowling
- Bar chart: top bowlers by bowler-credited wickets
- Scatter chart: economy vs wickets
- KPI cards: wickets, runs conceded, legal balls
- Add a minimum overs threshold for economy comparisons

## Page 4 — Teams and venues
- Team wins by season
- Win percentage by team
- Matches and average score by venue
- Venue slicer

## Page 5 — Toss and match insights
- Toss decision count (bat/field)
- Win after winning toss
- Toss winner vs match winner
- Result type and innings outcome
- Include no-results and abandoned matches in denominator logic only when appropriate

## Design checks
- Use descriptive titles and units.
- Add tooltips for definitions.
- Keep all visuals responsive to slicers.
- Test totals against source scorecards.
- Add a "Data last refreshed" card only when refresh date is genuinely populated.