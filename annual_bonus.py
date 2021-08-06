# Displays an employees annual bonus based on criteria

import employees
import random


def main():
    # collect common attributes (note: employee IDs are randomly generated)
    employee_name = collect_employee_name()
    employee_id = random.randint(10000, 99999)
    management_indicator = collect_management_indicator()
    salary = collect_annual_salary()

    # if the employee is a member of management, ask for their management level for calculating their bonus
    if management_indicator == 'y':
        management_level = collect_management_level()
        management = employees.Management(employee_name, employee_id, salary, management_level)

        management.greet_employee()
        management.calculate_bonus()

    # for individual contributors, ask if they are a supervisor for calculating their bonus
    else:
        supervisor_indicator = collect_supervisor_indicator()
        employee = employees.IndividualContributor(employee_name, employee_id, salary, supervisor_indicator)

        employee.greet_employee()
        employee.calculate_bonus()


# collect the employees full name. if it fails validation, return an error and collect again
# NOTE: the name cannot be null and has to be greater than 1 letter.
def collect_employee_name():
    employee_name = input('What is your full name? ')
    while employee_name == '' or len(employee_name) < 1:
        print('Please enter your name!')
        employee_name = input('Let us try again. What is your full name? ')

    return employee_name


# collect the employees salary. if it is not greater than 0, display an error and collect again
def collect_annual_salary():
    retry_display_text = 'Let us try again. What is your annual salary? '

    try:
        salary = float(input('What is your annual salary? '))
        while salary <= 0:
            print('Please enter a valid salary! It must be greater than 0')
            salary = float(input(retry_display_text))
    except ValueError:
        print('The salary cannot contain commas, spaces, or characters.')
        salary = float(input(retry_display_text))

    return salary


# determine if the employee is a member of management or not.
# return an error and collect again if the indicator is blank or invalid.
def collect_management_indicator():
    management_indicator = input('Are you a member of management? (y or n) ')
    while management_indicator == '' or management_indicator not in ['y', 'n']:
        print('Please enter a valid value!')
        management_indicator = input('Let us try again. Are you a member of management? (y or n) ')

    return management_indicator


# determine the manager's level
# return an error and collect again if the level is blank or invalid.
def collect_management_level():
    management_level = input('What is your level of management? ')
    while management_level == '' or management_level not in ['MID', 'EXECUTIVE', 'SENIOR']:
        print('Please enter a valid value!')
        management_level = input('Let us try again. What is your level of management? ')

    return management_level


# determine if the employee is a supervisor or not.
# return an error and collect again if the indicator is blank or invalid.
def collect_supervisor_indicator():
    supervisor_indicator = input('Are you currently a supervisor? (y or n) ')
    while supervisor_indicator == '' or supervisor_indicator not in ['y', 'n']:
        print('Please enter a valid value!')
        supervisor_indicator = input('Let us try again. Are you currently a supervisor? (y or n) ')

    return supervisor_indicator


main()
