#  Just tinkering with strings in Python

#  This captures the phrase that a user enters
phrase = input('Please enter a phrase: ')
#  Next, this captures the word to search for in the above phrase
wordToSearchFor = input('What word would you like to search for? ')
#  If the word is found AND a specific first name is entered, we have some special recognition!
name = input('What is your first name? ')

#  First, remove some special characters that are typed by a user in the phrase
#  Next, split the phrase entered by a user based on the space delimiter
phrase = phrase.strip('\\,*,&,^,!,\'')
phrase = phrase.split(" ")

#  a boolean to track if we have found the word within the phrase, or not.
#  NOTE: unlike other languages, you have to type true or false like this - True or False.
found = False

#  Iterate through the phrase of words
#  1. convert the word to lower case
#  2. check if the word to search for is present in the phrase.
#  3. return True if present.
for word in phrase:
    word = word.lower()
    if wordToSearchFor.__eq__(word):
        found = True

if found:
    #  winner names
    names = ['Jenny', 'Richard', 'Mike', 'Catherine', 'Rachel', 'Laura', 'Andrew', 'Ashley', 'Alice', 'Luther']
    #  the capitalize function capitalizes the first letter of the string
    #  if the name starts with the letter 'L', they won a cruise!
    if names.__contains__(name) & name.startswith('L'):
        print('congratulations, ' + name + '!' + ' you just won a free cruise!!!'.capitalize())
    #  for all other qualifying users, they won a free dinner!
    elif names.__contains__(name):
        print('congratulations, ' + name + '!' + ' you are eligible for a free dinner on us from GrubHub!'.capitalize())
    #  otherwise, no dinner for other users. phrase is printed using the upper function.
    #  the upper function converts all characters in a string to uppercase
    else:
        print('winner winner chicken dinner...just kidding, no dinner for you!'.upper())
else:
    #  Nothing for those who lose...
    print("no soup for you!".capitalize())
