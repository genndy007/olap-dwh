-- game.csv
CREATE TABLE seasons (
    season_id serial PRIMARY KEY,
    season_year varchar(8)
);
-- game.csv
CREATE TABLE game_types (
    game_type_id serial PRIMARY KEY,
    game_type varchar(1)
);
-- team-info.csv
CREATE TABLE teams (
    team_id int PRIMARY KEY,
    short_name varchar(20),
    team_name varchar(20),
    abbr varchar(3)
);
-- game.csv
CREATE TABLE venues (
    venue_id serial PRIMARY KEY,
    venue_name varchar(30)
);
-- game_officials.csv
CREATE TABLE officials (
    official_id serial PRIMARY KEY,
    official_name varchar(30),
    official_type varchar(10)
);
-- game.csv 
CREATE TABLE timezones (
    timezone_id serial PRIMARY KEY,
    timezone_location varchar(30),
    timezone_offset int,
    timezone_abbr varchar(3)
);
-- game.csv
CREATE TABLE outcome_facts (
    outcome_id serial PRIMARY KEY,
    season_id int REFERENCES seasons(season_id),
    game_type_id int REFERENCES game_types(game_type_id),
    home_team_id int REFERENCES teams(team_id),
    away_team_id int REFERENCES teams(team_id),
    venue_id int REFERENCES venues(venue_id),
    timezone_id int REFERENCES timezones(timezone_id),
    official_id int REFERENCES officials(official_id),
    away_goals int,
    home_goals int,
    outcome varchar(20)
);