let
    Source = Parquet.Document(
        Web.Contents("https://raw.githubusercontent.com/aadi-jn/indian-premier-league/main/data/marts/mart_bowler_season_stats.parquet")
    )
in
    Source