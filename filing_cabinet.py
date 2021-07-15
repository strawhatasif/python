#  Basic I/O with files. Throwback to the days of a physical filing cabinet.

# create a file to store the super hero names
super_hero_names_file = open('superHeroNames.txt', 'a')


def main():
    # Open the super heroes file in READ ONLY MODE
    super_hero_real_names_file = open('superHeroRealNames.txt', 'r')

    #  read each line and invoke a function that writes a super heroes name based on their real name
    for line in super_hero_real_names_file:
        words = line.split(',')
        #  removing the blank line separator at the end of the line.
        real_name = words[1].rstrip('\n')
        # write the super hero name to a new file
        write_super_hero_names(words[0], real_name)

    #  closing files as best practice for file I/O
    super_hero_real_names_file.close()
    super_hero_names_file.close()


#  This function is responsible for writing the super heroes names based on their real names
def write_super_hero_names(unique_identifier, real_name):
    # the following is a Python dictionary. this is equivalent to a HashMap in Java.
    super_hero_names = {'Clark Kent': 'Superman', 'Diana Prince': 'Wonder Woman', 'Tony Stark': 'Iron Man',
                        'Arthur Curry': 'Aquaman', 'Jessica Jones': 'Jewel', 'Natasha Romanoff': 'Black Widow',
                        'Hal Jordan': 'Green Lantern', 'Bruce Banner': 'Hulk', 'Bruce Wayne': 'Batman',
                        'Carol Danvers': 'Captain Marvel'}

    super_hero_names_file.write(unique_identifier + ',' + super_hero_names[real_name] + '\n')


main()
