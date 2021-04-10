import psycopg2
from db_fill import config


def change_fact_venue_tz(venue_id, new_tz_id):
    sql = """UPDATE outcome_facts SET timezone_id=%s WHERE venue_id=%s"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(sql, (new_tz_id, venue_id))
        print(f'Now venue_id {venue_id} has timezone_id {new_tz_id}')

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def change_team_name(team_id, new_team_name):
    sql = """UPDATE teams SET team_name=%s WHERE team_id=%s"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(sql, (new_team_name, team_id))
        print(f'Now venue_id {venue_id} has timezone_id {new_tz_id}')

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


change_fact_venue_tz(6, 7)
