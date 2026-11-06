let
    Source = Parquet.Document(
        Web.Contents("https://raw.githubusercontent.com/aadi-jn/indian-premier-league/main/data/marts/dim_teams.parquet")
    )
in
    Source