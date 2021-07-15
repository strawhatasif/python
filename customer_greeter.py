# this program imports the Greeting class which greets customers based on their age.
# A simple example demonstrating importing and working with classes in Python

import greeting


def main():
    # collect the customer's name
    customer_name = input('What is your name? ')

    # if the customer forgot to enter a name, ask them to enter their name
    while customer_name == '':
        print('Please enter your name!')
        customer_name = input('Let\'s try again. What is your name? ')

    # create an instance of the Greeting class.
    customer_greeting = greeting.Greeting(customer_name)

    # collect the customer's age
    customer_age = int(input('What is your age? '))

    # validate that the customer's age is greater than 0, and not greater than 100 years old.
    while customer_age <= 0 or customer_age > 100:
        print('Please enter a valid age!')
        customer_age = int(input('Let\'s try again. What is your age? '))

    # display a greeting based on the customers age
    print(customer_greeting.greet_customer(customer_age))


main()
