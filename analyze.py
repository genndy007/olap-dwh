import pandas as pd

#game_df = pd.read_csv('game.csv')
# team_info_df = pd.read_csv('team_info.csv')
# game_officials_df = pd.read_csv('game_officials.csv')


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

        game_id = str(obj["game_id"])
        official_name = str(obj["official_name"]).strip()
        official_type = str(obj["official_type"]).strip()

        if official_type != 'Referee' and official_type != 'Linesman':
            continue

        arr_official = [game_id, official_name, official_type]

        arr_officials.append(arr_official)

    return arr_officials


# game.csv
def get_all_game_times(df):
    times_serie = df['date_time_GMT']
    times_serie = pd.to_datetime(times_serie)
    times_serie = times_serie.drop_duplicates().dropna()

    arr_times = []
    for time in times_serie:
        arr_times.append(time)

    return arr_times


# game.csv
def get_all_timezones(df) -> list[list[str, int, str]]:
    df = df.drop_duplicates().dropna()

    arr_tzs = []
    for idx in df.index:
        obj = df.loc[idx]
        tz_location = str(obj["venue_time_zone_id"])
        tz_offset = int(obj["venue_time_zone_offset"])
        tz_abbr = str(obj["venue_time_zone_tz"])

        arr_tz = [tz_location, tz_offset, tz_abbr]

        if arr_tz not in arr_tzs:
            arr_tzs.append(arr_tz)

    return arr_tzs


# game.csv
def get_facts(df, seasons, game_types, venues, officials, timezones, game_times):
    arr_facts = []

    for idx in df.index:
        row = df.loc[idx]
        # Season id
        season = str(row["season"])
        season_id = int(search_id_array(season, seasons))
        # Type id
        game_type = str(row["type"])
        game_type_id = int(search_id_array(game_type, game_types))
        # Teams id
        away_team_id = int(row["away_team_id"])
        home_team_id = int(row["home_team_id"])
        # Venue id
        venue = str(row["venue"])
        venue_id = int(search_id_array(venue, venues))
        # Official id
        game_id = str(row["game_id"])
        official_id = int(search_id_official(game_id, officials))
        # Timezone id
        tz_abbr = str(row["venue_time_zone_tz"])
        tz_id = int(search_id_timezone(tz_abbr, timezones))

        # Game time id
        game_time = pd.to_datetime(row['date_time_GMT'])
        game_time_id = int(search_id_array(game_time, game_times))

        # Concrete fact information
        away_goals = int(row["away_goals"])
        home_goals = int(row["home_goals"])
        outcome = str(row["outcome"])

        # Fact!
        fact = [season_id, game_type_id, home_team_id, away_team_id,
                venue_id, tz_id, official_id, game_time_id, away_goals, home_goals, outcome]
        arr_facts.append(fact)

    return arr_facts


def search_id_official(game_id, officials):
    for idx in range(len(officials)):
        if game_id == officials[idx][0]:
            return idx+1
    return -1


def search_id_array(el, arr):
    for idx in range(len(arr)):
        if arr[idx] == el:
            return idx+1
    return -1


def search_id_timezone(abbr, timezones):
    for idx in range(len(timezones)):
        if abbr == timezones[idx][2]:
            return idx+1
    return -1


# TEST ZONE
# seasons = get_all_season_years(game_df)
# game_types = get_all_game_types(game_df)
# #teams = get_all_teams(team_info_df)
# venues = get_all_venues(game_df)
# officials = get_all_officials(game_officials_df)
# timezones = get_all_timezones(game_df)

#game_times = get_all_game_times(game_df)

# print(game_df.info())

# print("Dimensions arrays filled out!")

# facts = get_facts(game_df, seasons, game_types, venues, officials, timezones)

# counter = 10
# for fact in facts:
#     counter -= 1
#     print(fact)
#     if counter < 0:
#         break
