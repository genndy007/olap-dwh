import pandas as pd

game_df = pd.read_csv('game.csv')
team_info_df = pd.read_csv('team_info.csv')
game_officials_df = pd.read_csv('game_officials.csv')


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
        team_id = int(obj["team_id"])
        short_name = str(obj["shortName"])
        team_name = str(obj["teamName"])
        abbr = str(obj["abbreviation"])

        arr_team = [team_id, short_name, team_name, abbr]

        arr_teams.append(arr_team)

    return arr_teams


# game.csv
def get_all_venues(df) -> list[str]:
    venues = df["venue"].drop_duplicates().dropna()

    arr_venues = []
    for val in venues:
        venue = str(val).strip()
        arr_venues.append(str(venue))

    return arr_venues


# game_officials.csv
def get_all_officials(df) -> list[list[str, str]]:
    df = df.drop_duplicates().dropna()

    arr_officials = []
    for idx in df.index:
        obj = df.loc[idx]
        official_name = str(obj["official_name"])
        official_type = str(obj["official_type"])

        arr_official = [official_name, official_type]

        arr_officials.append(arr_official)

    return arr_officials


# game.csv
def get_all_timezones(df):
    df = df.drop_duplicates().dropna()

    arr_tzs = []
    for idx in df.index:
        obj = df.loc[idx]
        tz_location = obj["venue_time_zone_id"]
        tz_offset = obj["venue_time_zone_offset"]
        tz_abbr = obj["venue_time_zone_tz"]

        arr_tz = [tz_location, tz_offset, tz_abbr]

        if arr_tz not in arr_tzs:
            arr_tzs.append(arr_tz)

    return arr_tzs


timezones = get_all_timezones(game_df)
print(timezones)
