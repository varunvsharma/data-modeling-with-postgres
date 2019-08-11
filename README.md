# sparkifydb

### Purpose and Context

The database sparkifydb has been set up to help Sparkify analyse the data they’ve been collecting on songs and user activity on their new music streaming app.  

The raw data resides in a directory of JSON logs making the process of querying and analysing that information less than optimal. The new database aims to address this issue and provides an optimised solution for queries on song play analysis.

### Database Schema

The schema for the database is a star schema centred around song play data.  

Given that the primary goal for creating the new database is to help Sparkify analyse information in relation to user activity, it is optimal to have a central table (fact table) with transactions at a granularity level of user actions (i.e., choosing to play a song).  

Each action in turn occurs in a context that needs to be taken into account to derive additional information about it. The elements/dimensions that make up this context can occur in various permutations and combinations for multiple actions. Every value of a dimension also has additional information associated with that value however this information isn’t dependent on a user’s actions and is solely related to that particular dimensional value. Therefore this additional information needs to be maintained separately in dimension tables that only contain information about the various dimensions, instead of the fact table. This reduces data redundancy, improves data integrity and provides flexibility to the end user. The foreign keys provided in each transaction of the fact table should allow an analyst/application to gather additional information about a particular dimension as and when required.  

Visualising these tables displays a star shaped pattern with a central fact table that is linked to surrounding dimension tables.

##### ***Fact table in sparkifydb***

Records that represent the action of playing a song (i.e., records with page NextSong) form the fact table. This table also contains foreign keys to 4 dimension tables (users, songs, artists and time) that provide additional information in relation to the played songs  

##### ***Dimension tables in sparkifydb***

Below are the dimensions tables that were implemented in sparkifydb  

1. **Users:** This table contains first name, last name, gender and level of user ids stored in the log data.

2. **Songs:** This table contains the ids, titles, years and durations of various songs along with their associated artist ids in the song data files

3. **Artists:** This table contains artist ids, artist names, their location, their longitude and their latitude based on records in the song data files

4. **Time:** This table contains a breakdown of the timestamps stored in the log data  

### ETL Pipeline  

A Python script has been developed to automate the ETL pipeline which starts the process by gathering a list of song and log files that contain JSON data. These files are then read into pandas dataframes and appropriate transformations are carried out to gather/generate the requisite information for the various database tables. These values are then inserted using SQL procedures that are stored in a related Python script. SQL statements to create/reset the database and create new tables are also stored in the related script. Overall these scripts automate the entire data extraction, transformation and load process providing an easy / repeatable mechanism to update the database.  

Listed below is a short description of each of the files in this project:  

1. **sql_queries.py:** This script contains the SQL statements used by the etl files to insert data into the database. It also contains SQL statements that are used by create_tables.py to create the sparkify database, drop existing tables and create new tables.

2. **create_tables.py:** This script uses the SQL statements stored in sql_queries.py to reset the sparkify database and create fact and dimension tables

3. **etl.ipynb:** This jupyter notebook contains the etl script to insert extract, transform and load a small test sample into the database along with detailed markdown comments.

4. **test.ipynb:** This jupyter notebook allows the programmer to test the success of the ETL script

5. **etl.py:** This script utilises the test script in etl.ipynb and applies the ETL process to the entire song and log dataset.

To run the etl pipeline, follow the steps below:  

1. Run create_tables.py to create/reset the sparkify database and create all the necessary tables  

2. Run etl.ipynb (for one file) or etl.py (for all files) to extract information from the song and log files and load the data into the database tables  

3. Run test.ipynb to check if the data has been inserted correctly. Restart the kernel to ensure the connection to the database is closed.  

### Example Query:  

**Input**

    SELECT songs.title,
           artists.artist_name,
           COUNT(*) AS "play_count"

    FROM songplays
    JOIN songs
    ON songplays.song_id = songs.song_id
    JOIN artists
    ON songs.artist_id = artists.artist_id
    WHERE songs.title = 'Setanta matins'
    GROUP BY songs.title, artists.artist_name

**Output**

title | artist_name | play_count
--- | --- | ---
Setanta matins | Elena | 1
