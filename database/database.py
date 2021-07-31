import sqlite3

connection = sqlite3.connect('simple_database.db')  # this is how easy it is to connect to a database!
conn = connection.cursor()  # simple_database will be created in the same directory as this program

# create a couple of tables
conn.execute('''CREATE TABLE SUPER_HERO_NAMES(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    real_name VARCHAR(50), 
                    super_hero_name VARCHAR(50))''')

conn.execute('''CREATE TABLE HERO_UNIVERSE(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    super_hero_name VARCHAR(50), 
                    universe VARCHAR(50))''')

# insert data into tables
insert_super_hero_names = 'INSERT INTO SUPER_HERO_NAMES (id, real_name, super_hero_name) values(?, ?, ?)'
name_data = [
    (1, 'Clark Kent', 'Superman'),
    (2, 'Tony Stark', 'Iron Man'),
    (3, 'Arthur Curry', 'Aquaman'),
    (4, 'Jessica Jones', 'Jewel'),
    (5, 'Natasha Romanoff', 'Black Widow'),
    (6, 'Hal Jordan', 'Green Lantern'),
    (7, 'Bruce Banner', 'Hulk'),
    (8, 'Bruce Wayne', 'Batman'),
    (9, 'Carol Danvers', 'Captain Marvel')
]

insert_universe_names = 'INSERT INTO HERO_UNIVERSE (id, super_hero_name, universe) values(?, ?, ?)'
universe_data = [
    (1, 'Superman', 'DC'),
    (2, 'Iron Man', 'Marvel'),
    (3, 'Aquaman', 'DC'),
    (4, 'Jewel', 'Marvel'),
    (5, 'Black Widow', 'Marvel'),
    (6, 'Green Lantern', 'DC'),
    (7, 'Hulk', 'Marvel'),
    (8, 'Batman', 'DC'),
    (9, 'Captain Marvel', 'Marvel')
]

conn.executemany(insert_super_hero_names, name_data)
conn.executemany(insert_universe_names, universe_data)
connection.commit()
