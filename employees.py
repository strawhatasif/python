# Generic Employee class
class Employee:
    # init accepts an argument to assign the employee name and ID
    def __init__(self, employee_name, employee_identification_number, salary):
        self.employee_name = employee_name
        self.employee_identification_number = employee_identification_number
        self.salary = salary

    def greet_employee(self):
        print('Your employee ID number is: ' + str(self.employee_identification_number) + '.')


# The Individual Contributor class is a subclass of Employee
class IndividualContributor(Employee):
    # constants for bonus (10% for everyone, 15% for supervisors)
    REGULAR_PERCENTAGE = 0.10
    SUPERVISOR_PERCENTAGE = 0.15

    # pass all the required attributes to the superclasses init method
    # also, supervisor attribute is specific to this class for calculating bonus
    def __init__(self, employee_name, employee_identification_number, salary, supervisor):
        Employee.__init__(self, employee_name, employee_identification_number, salary)
        self.supervisor = supervisor

    # calculate bonus based on if the individual contributor is a supervisor or not.
    # supervisors have a higher percentage
    def calculate_bonus(self):
        if self.supervisor == 'y':
            print('Congratulations, ' + self.employee_name + '! Your bonus is: $'
                  + format((self.salary * self.SUPERVISOR_PERCENTAGE), ',.2f'))
        else:
            print('Thank you for your contributions, ' + self.employee_name + '! Your bonus is: $'
                  + format((self.salary * self.REGULAR_PERCENTAGE), ',.2f'))


# The Individual Contributor class is a subclass of Employee
class Management(Employee):
    # constants for bonus (25% for mid, 35% for executive, and 40% for senior management)
    MID_MANAGEMENT_PERCENTAGE = 0.25
    EXECUTIVE_MANAGEMENT_PERCENTAGE = 0.35
    SENIOR_MANAGEMENT_PERCENTAGE = 0.45

    # pass all the required attributes to the superclasses init method
    # also, management_level attribute is specific to this class for calculating bonus
    def __init__(self, employee_name, employee_identification_number, salary, management_level):
        Employee.__init__(self, employee_name, employee_identification_number, salary)
        self.management_level = management_level

    # calculate bonus based on the managers management level.
    # mid, executive, and senior managers receive different bonuses
    def calculate_bonus(self):
        greeting = 'Congratulations, '
        bonus_display_text = '! Your bonus is: $'
        management_levels = ['MID', 'EXECUTIVE', 'SENIOR']

        self.management_level = str(self.management_level).upper()

        while self.management_level not in management_levels:
            print('Please enter a valid management level!')
            input('What is your management level? ')

        if self.management_level == 'SENIOR':
            print(greeting + self.employee_name + bonus_display_text
                  + format((self.salary * self.SENIOR_MANAGEMENT_PERCENTAGE), ',.2f'))
        elif self.management_level == 'EXECUTIVE':
            print(greeting + self.employee_name + bonus_display_text
                  + format((self.salary * self.EXECUTIVE_MANAGEMENT_PERCENTAGE), ',.2f'))
        else:
            print(greeting + self.employee_name + bonus_display_text
                  + format((self.salary * self.MID_MANAGEMENT_PERCENTAGE), ',.2f'))
