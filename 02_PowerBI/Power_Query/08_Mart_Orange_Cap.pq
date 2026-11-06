let
    Source = Parquet.Document(
        Web.Contents("https://raw.githubusercontent.com/aadi-jn/indian-premier-league/main/data/marts/mart_orange_cap.parquet")
    )
in
    Source