# This program calculates and displays average rainfall based on rainfall amounts per month entered by the user.

# constant for number of months in a year
NUMBER_OF_MONTHS_IN_YEAR = 12

# stores the number of years entered by the user
number_of_years = int((input('Please enter the number of years: ')))

# if the initial entry for number of years is less than or equal to zero, display an error message.
# also, ask user to reenter number of years.
while number_of_years <= 0:
    print('Invalid entry! The number of years must be greater than zero.')
    # stores the number of years entered by the user (subsequent attempt).
    number_of_years = int(input('Please reenter the number of years: '))

# accumulator variable for rainfall total.
total_rainfall = 0.0

# iterate once per year
for year in range(number_of_years):
    # years start at 1, not 0. format as a string for display purposes.
    print('Enter monthly rainfall for year ' + str(year + 1))
    # iterate for the number of months in a year (Gregorian calendar).
    for month in range(NUMBER_OF_MONTHS_IN_YEAR):
        # months start at 1, not 0. format as a string for display purposes.
        display_month = str(month + 1)

        # stores the monthly rainfall entered by the user.
        # format as a string for display purposes
        monthly_rainfall = float(input('Enter rainfall for month ' + display_month + ': '))

        # if the entry for monthly rainfall is less than zero, display an error message and ask user to reenter value.
        while monthly_rainfall < 0:
            print('Invalid entry! Monthly rainfall must be greater than zero.')
            # stores the monthly rainfall entered by the user (subsequent attempt).
            monthly_rainfall = float(input('Reenter rainfall for month ' + display_month + ': '))

        total_rainfall += monthly_rainfall

# Display the total number of months. As a reminder, months begin at 1 and not 0.
total_months = int(display_month) * number_of_years
print('Number of months: ' + str(total_months))
# Displays the total rainfall for all months. Formatted to display 2 decimal places.
print('Total inches of rainfall: ' + format(total_rainfall, ',.2f'))
# The average rainfall formula is TOTAL RAINFALL divided by the NUMBER OF MONTHS.
# Formatted to display 2 decimal places.
print('Average rainfall: ' + format(total_rainfall/total_months, '.2f'))
