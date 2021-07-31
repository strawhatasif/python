# Displays super hero information (real names and universe) based on user input
# NOTE: I haven't figured out how to format the result, yet
import sqlite3

connection = sqlite3.connect('simple_database.db')
conn = connection.cursor()


def main():
    super_hero_name = collect_super_hero_name()
    retrieve_real_name(super_hero_name)
    retrieve_universe_for_super_hero(super_hero_name)


def collect_super_hero_name():
    super_hero_name = input('Which super heroes information you like to look up? ')
    while super_hero_name == '':
        print('Please enter a name!')
        super_hero_name = input('Please try again. Which super heroes real name would you like to look up? ')

    return super_hero_name


def retrieve_real_name(super_hero_name):
    conn.execute("SELECT real_name FROM SUPER_HERO_NAMES WHERE super_hero_name=?", (super_hero_name,))
    print('Real Name: ', conn.fetchone())  # we know there's only one result
    connection.commit()


def retrieve_universe_for_super_hero(super_hero_name):
    conn.execute('SELECT universe FROM HERO_UNIVERSE WHERE super_hero_name=?', (super_hero_name,))
    print('Universe: ', conn.fetchone())  # we know there's only one result
    connection.commit()


main()
