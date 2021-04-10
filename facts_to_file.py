import pickle
import pandas as pd
from analyze import get_all_season_years, \
    get_all_game_types, get_all_teams, get_all_venues, \
    get_all_officials, get_all_timezones, get_all_game_times, get_facts

game_df = pd.read_csv('game.csv')
#team_info_df = pd.read_csv('team_info.csv')
game_officials_df = pd.read_csv('game_officials.csv')


seasons = get_all_season_years(game_df)
print("seasons got")
game_types = get_all_game_types(game_df)
print("game_types got")
#teams = get_all_teams(team_info_df)
print("teams got")
venues = get_all_venues(game_df)
print("venues got")
officials = get_all_officials(game_officials_df)
print("officials got")
timezones = get_all_timezones(game_df)
print("timezones got")
game_times = get_all_game_times(game_df)
print("game_times got")


facts = get_facts(game_df, seasons, game_types, venues,
                  officials, timezones, game_times)
print('facts got')


with open('facts.pickle', 'wb') as f:
    pickle.dump(facts, f)


print(facts[:10], sep="\n")
