import pandas as pd

game_df = pd.read_csv('game.csv')
team_info_df = pd.read_csv('team_info.csv')

# game.csv


def get_all_season_years(df) -> list[str]:
    seasons = df["season"]
    seasons.drop_duplicates(inplace=True)

    arr_seasons = []
    for val in seasons:
        arr_seasons.append(str(val))

    return arr_seasons


# game.csv
def get_all_game_types(df) -> list[str]:
    game_types = df["type"]
    game_types.drop_duplicates(inplace=True)

    arr_types = []
    for val in game_types:
        arr_types.append(str(val))

    return arr_types


# team_info.csv
def get_all_teams(df) -> list[list]:
    df = df.drop_duplicates().dropna()

    arr_teams = []
    for idx in df.index:
        obj = df.loc[idx]
        team_id = obj["team_id"]
        short_name = obj["shortName"]
        team_name = obj["teamName"]
        abbr = obj["abbreviation"]

        arr_team = [team_id, short_name, team_name, abbr]

        arr_teams.append(arr_team)

    return arr_teams


# teams = get_all_teams(team_info_df)
# print(teams)
# game_types = get_all_game_types(game_df)
# print(game_types)
