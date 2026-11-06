// Power Query M starter
// Update the root folder path to the local repository location.
let
    RootFolder = "C:\\PATH\\TO\\IPL-Analysis-Dashboard-PowerBI\\01_Dataset\\Processed\\",
    MatchesSource = Csv.Document(
        File.Contents(RootFolder & "matches.csv"),
        [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    MatchesHeaders = Table.PromoteHeaders(MatchesSource, [PromoteAllScalars=true]),
    MatchesTypes = Table.TransformColumnTypes(
        MatchesHeaders,
        {
            {"match_id", type text}, {"season", type text}, {"date", type date},
            {"team1", type text}, {"team2", type text}, {"winner", type text},
            {"toss_winner", type text}, {"toss_decision", type text},
            {"venue", type text}, {"city", type text}
        }
    )
in
    MatchesTypes

// Create a second blank query named Deliveries and use the same pattern:
// let
//     RootFolder = "C:\\PATH\\TO\\IPL-Analysis-Dashboard-PowerBI\\01_Dataset\\Processed\\",
//     Source = Csv.Document(File.Contents(RootFolder & "deliveries.csv"),
//         [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
//     Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
//     Types = Table.TransformColumnTypes(Headers, {
//         {"match_id", type text}, {"season", type text}, {"date", type date},
//         {"innings", Int64.Type}, {"over", Int64.Type}, {"ball", Int64.Type},
//         {"batter_runs", Int64.Type}, {"extra_runs", Int64.Type},
//         {"total_runs", Int64.Type}, {"bowler_runs", Int64.Type},
//         {"is_legal_ball", Int64.Type}, {"batter_ball_faced", Int64.Type},
//         {"is_wicket", Int64.Type}, {"is_bowler_credit_wicket", Int64.Type},
//         {"is_super_over", Int64.Type}
//     })
// in
//     Types
