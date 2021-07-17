import pytest
import greeting

greeting = greeting.Greeting("Rachel Belle Pepperstaffere")
over_twenty_one_greeting = 'Welcome! It is our pleasure to treat you to an adult beverage, Rachel Belle Pepperstaffere!'
under_twenty_one_greeting = 'Hey there! Would you like coke or apple juice, Rachel Belle Pepperstaffere?'


def test_greet_customer_younger_than_twenty_one():
    customer_greeting = greeting.greet_customer(18)
    assert customer_greeting == under_twenty_one_greeting


def test_greet_customer_older_than_twenty_one():
    customer_greeting = greeting.greet_customer(30)
    assert customer_greeting == over_twenty_one_greeting
