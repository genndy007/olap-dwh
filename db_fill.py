from configparser import ConfigParser
import psycopg2
import pandas as pd
from analyze import get_all_season_years, \
    get_all_game_types, get_all_teams, get_all_venues, \
    get_all_officials, get_all_timezones, get_all_game_times, get_facts

import pickle

# Parse config


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    auth = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            auth[param[0]] = param[1]

    else:
        raise Exception(f'Section {section} not in {filename} file')

    return auth


def connect():
    conn = None
    try:
        params = config()
        print("Connecting to Postgres...")

        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print('Version: ', db_version)

        cur.close()
    except:
        print('Error')
    finally:
        if conn is not None:
            conn.close()

# Fill seasons table


def insert_seasons(seasons):
    sql = """INSERT INTO seasons(season_year) VALUES (%s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for season in seasons:
            cur.execute(sql, (season,))

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_game_types(game_types):
    sql = """INSERT INTO game_types(game_type) VALUES (%s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for t in game_types:
            cur.execute(sql, (t,))

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_venues(venues):
    sql = """INSERT INTO venues(venue_name) VALUES (%s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for v in venues:
            cur.execute(sql, (v,))

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_teams(teams):
    sql = """INSERT INTO teams(team_id, short_name, team_name, abbr) \
        VALUES (%s, %s, %s, %s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for team in teams:
            cur.execute(sql, (team[0], team[1], team[2], team[3]))

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_officials(officials):
    sql = """INSERT INTO officials(official_name, official_type) 
            VALUES (%s, %s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for off in officials:
            cur.execute(sql, (off[1], off[2]))

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print(off)
    finally:
        if conn is not None:
            conn.close()


def insert_timezones(timezones):
    sql = """INSERT INTO timezones(timezone_location, timezone_offset, timezone_abbr) 
            VALUES (%s, %s, %s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for zone in timezones:
            cur.execute(sql, (zone[0], zone[1], zone[2]))

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print(zone)
    finally:
        if conn is not None:
            conn.close()


def insert_facts(facts):
    sql = """INSERT INTO outcome_facts(season_id, game_type_id, home_team_id, away_team_id, venue_id, timezone_id, official_id, game_time_id, away_goals, home_goals, outcome) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for f in facts:
            if -1 not in f:
                try:
                    cur.execute(sql, tuple(f))
                    conn.commit()
                except (Exception, psycopg2.DatabaseError) as error:
                    print("execute error:", error)
                    continue

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print(f)
    finally:
        if conn is not None:
            conn.close()


def insert_game_times(game_times):
    sql = """INSERT INTO game_times(game_time) 
            VALUES (%s)"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for time in game_times:
            cur.execute(sql, (time,))

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# TEST ZONE
# 1. Dataframes
game_df = pd.read_csv('game.csv')
# team_info_df = pd.read_csv('team_info.csv')
# game_officials_df = pd.read_csv('game_officials.csv')

# 2. Data from frames
# seasons = get_all_season_years(game_df)
# game_types = get_all_game_types(game_df)
# venues = get_all_venues(game_df)
# teams = get_all_teams(team_info_df)
# officials = get_all_officials(game_officials_df)
# timezones = get_all_timezones(game_df)
game_times = get_all_game_times(game_df)


#facts = get_facts(game_df, seasons, game_types, venues, officials, timezones)

# save data to binary file
# with open('facts.pickle', 'wb') as f:
#     pickle.dump(facts, f)

# with open('facts.pickle', 'rb') as f:
#     facts = pickle.load(f)

#print("File loaded")


# 3. Insert to db
# inserting to seasons table
# insert_seasons(seasons)

# game_types table
# insert_game_types(game_types)

# venues table
# insert_venues(venues)

# teams table
# insert_teams(teams)

# officials table
# insert_officials(officials)

# timezones table
# insert_timezones(timezones)

# game_times table
# insert_game_times(game_times)

# outcome_facts table
# insert_facts(facts)
