#  Handling and throwing various exceptions. A party, indeed!

def divide_by_zero():
    number = 100 / 0


#  Can't divide by zero. This handles that error
try:
    divide_by_zero()
except ZeroDivisionError as error:
    print('Cannot divide by zero...handling this exception: ', error)

#  If someone doesn't enter an age, handle that error!
try:
    user_age = int(input('What is your age? '))
except ValueError:
    print('That is not a valid value! Please enter your age!')

#  In this instance, someone is attempting to print out a fictitious variable
try:
    name = 'Rachel Belle Pepperstaffere'
    print(color)
except NameError:
    print('You tried printing out the wrong variable value!')

#  This does not handle an exception, rather it is the equivalent of "throwing" an exception in Java.
ACCEPTABLE_ANSWER = 'butter chicken'
favorite_food = 'pizza'
#  Um, hello! Butter chicken is delish!
if ACCEPTABLE_ANSWER != favorite_food:
    raise ValueError(favorite_food.title() + ' is not an acceptable answer!')
