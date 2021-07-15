# This class is responsible for managing a greeting
# A simple example of classes in Python

class Greeting:

    # init method for the customer's name (name passed in and assigned to customer_name)
    def __init__(self, name):
        self.customer_name = name

    # this method returns a greeting based on if a customer is older than or younger than 21 years of age.
    def greet_customer(self, age):
        # variables for greeting
        over_twenty_one_greeting = 'Welcome! It is our pleasure to treat you to an adult beverage, '
        under_twenty_one_greeting = 'Hey there! Would you like coke or apple juice, '

        if age >= 21:
            return over_twenty_one_greeting + self.customer_name + '!'
        else:
            return under_twenty_one_greeting + self.customer_name + '?'
