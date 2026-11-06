# Data dictionary (normalized target schema)

## Matches table
| Column | Meaning |
|---|---|
| match_id | Unique identifier for a match |
| season | IPL season label/year |
| date | Match date |
| city | City where match was played |
| venue | Stadium/venue |
| team1, team2 | Competing teams |
| toss_winner | Team winning the toss |
| toss_decision | Bat or field decision |
| winner | Match-winning team; blank for no result |
| result | Result type/method |
| result_margin | Runs/wickets margin where applicable |
| player_of_match | Player of the match |

## Deliveries table
| Column | Meaning |
|---|---|
| match_id | Match identifier linking to Matches |
| innings | Innings number |
| over, ball | Over and delivery sequence in source format |
| batting_team, bowling_team | Teams for this delivery |
| batter, bowler, non_striker | Player names |
| batsman_runs | Runs credited to batter |
| extra_runs | Extras on the delivery |
| total_runs | Total runs from the delivery |
| extras_type | Wide, no-ball, bye, leg-bye, etc. |
| is_wicket | Whether a wicket event occurred |
| player_dismissed | Batter dismissed, if any |
| dismissal_kind | Type of dismissal |

## Model notes
This is a target schema for the project, not a claim that every source uses these exact headers. Map source columns into this schema in Power Query. Use stable IDs for players/teams if supplied; names alone can be inconsistent.