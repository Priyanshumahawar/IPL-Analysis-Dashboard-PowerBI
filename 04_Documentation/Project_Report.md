# IPL Analysis Dashboard using Power BI
## Project report

### 1. Introduction
The Indian Premier League (IPL) produces match-level and ball-by-ball data that can be used to study team results, player contributions, venue patterns and season trends. This project uses Microsoft Power BI to transform historical IPL data into an interactive analytical dashboard.

### 2. Objectives
- Study team performance and match outcomes across seasons.
- Identify leading run scorers and wicket takers.
- Compare batting and bowling performance metrics.
- Explore toss decisions and venue-level patterns.
- Present findings through interactive filters and visualizations.

### 3. Tools and technologies
- Microsoft Power BI Desktop
- Power Query for data cleaning and transformation
- DAX for measures and calculated columns
- CSV/Excel datasets
- GitHub for project versioning and documentation

### 4. Data requirements
The project uses match-level records and ball-by-ball delivery records. The match table should contain match date, season, teams, toss, venue and result. The delivery table should contain innings, batter, bowler, runs, extras and dismissal information. Refer to `Data_Dictionary.md`.

### 5. Methodology
1. Collect data from documented public sources.
2. Preserve raw source files and record their attribution/license.
3. Standardize column names, data types, team names and venue names.
4. Validate match IDs and reconcile innings totals with scorecards.
5. Build a relational model linking matches to deliveries.
6. Create DAX measures for runs, wickets, strike rate, economy and team results.
7. Design report pages and add slicers for season, team, player and venue.
8. Validate outputs and document assumptions and limitations.

### 6. Dashboard design
- Overview: headline KPIs, season trend and champions.
- Batting: top run scorers, strike rate and boundaries.
- Bowling: wickets, economy and bowling performance.
- Teams and venues: wins, win percentage and venue comparisons.
- Toss and match insights: toss decision outcomes and result patterns.

### 7. Key metrics
- Total matches: distinct match IDs.
- Total runs: sum of delivery total runs, with super-over handling documented.
- Batter runs: sum of runs credited to batters.
- Wickets: wicket events, with bowler-credit wickets separated from all dismissals.
- Strike rate: batter runs divided by balls faced, multiplied by 100.
- Bowling economy: bowler runs conceded per six legal balls.
- Team win percentage: wins divided by matches played by that team.

### 8. Expected outcomes
The dashboard should make it easier to compare teams and players, explore changes across seasons, and identify venue and toss-related patterns. Actual findings must be written only after the dataset is loaded, validated and analyzed.

### 9. Limitations
- Public datasets may differ in coverage, schema and scoring conventions.
- Team names and franchise identities can change over time.
- Some historical records may be incomplete or corrected.
- Balls faced, bowler runs conceded and bowler-credited wickets require cricket-specific rules.
- Correlation between toss decisions and match results does not prove causation.

### 10. Conclusion
This project demonstrates an end-to-end business intelligence workflow: data collection, cleaning, modeling, DAX calculations and interactive visualization. The final dashboard converts IPL records into accessible analytical views for exploring team and player performance.

### 11. References and attribution
List the exact dataset repository, original data provider, download date, license and any transformations used. Follow the terms of each source. IPL and team marks are trademarks of their respective owners; this independent educational project is not affiliated with or endorsed by the BCCI or IPL.