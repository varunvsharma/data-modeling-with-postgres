# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (timestamp numeric,
                                                                  user_id int,
                                                                  level varchar,
                                                                  song_id varchar,
                                                                  artist_id varchar,
                                                                  session_id numeric,
                                                                  location varchar,
                                                                  user_agent varchar)""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int,
                                                          first_name varchar,
                                                          last_name varchar,
                                                          gender varchar,
                                                          level varchar)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar,
                                                          title varchar,
                                                          artist_id varchar,
                                                          year int,
                                                          duration float)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar,
                                                              artist_name varchar,
                                                              artist_location varchar,
                                                              artist_latitude float,
                                                              artist_longitude float)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (timestamp numeric,
                                                         hour int,
                                                         day int,
                                                         weekofyear int,
                                                         month int,
                                                         year int,
                                                         weekday int)""")
