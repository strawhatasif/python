# This program calculates and displays shipping charge information for packages based on package weight and destination.

# sales tax rate for the state of Arkansas.
ARKANSAS_TAX_RATE = 0.0650
# sales tax rate for the state of Kansas.
KANSAS_TAX_RATE = 0.0650
# sales tax rate for the state of Louisiana.
LOUISIANA_TAX_RATE = 0.05
# sales tax rate for the state of New Mexico.
NEW_MEXICO_TAX_RATE = 0.05125
# sales tax rate for the state of Oklahoma.
OKLAHOMA_TAX_RATE = 0.0450
# sales tax rate for the state of Texas.
TEXAS_TAX_RATE = 0.0625

# rate per pound for packages less than 2 pounds
TWO_POUNDS_OR_LESS_RATE = 1.50
# rate per pound for packages between 2 and 6 pounds
BETWEEN_TWO_AND_SIX_POUNDS_RATE = 3.00
# rate per pound for packages between 6 and 10 pounds
BETWEEN_SIX_AND_TEN_POUNDS_RATE = 4.00
# rate per pound for packages greater than 10 pounds
GREATER_THAN_TEN_POUNDS_RATE = 4.75

# this variable captures the weight of the package
weight_of_package = float(input('What is the weight of the package? '))

if weight_of_package <= 0:
    print("Invalid entry! Weight of the package cannot be less than zero pounds.")

# Prerequisite - the weight MUST be greater than 0.0 pounds!
else:
    # valid list of state abbreviations (ref: page 322 from textbook)
    valid_state_abbreviations = ['AR', 'KS', 'LA', 'NM', 'OK', 'TX']

    # this package captures the state that the user wishes to ship the package to (NOTE: two letter abbreviation).
    state_of_package = input('Enter the state abbreviation to ship to: ')
    # for convenience and display purposes, convert state of package abbreviation to UPPERCASE.
    state_of_package = state_of_package.upper()
    # validate that the state abbreviation for delivery is valid! (ref: page 355 from textbook)
    if state_of_package not in valid_state_abbreviations:
        print("Invalid value! The state abbreviation must be either AR, KS, LA, NM, OK, or TX")
    # Prerequisite - the state abbreviation MUST be valid!
    else:
        # Shipping Summary
        print('SHIPPING SUMMARY')
        # Declaring variables for display text as they will be reused by multiple conditions.
        rate_per_pound_display_text = 'The rate per pound is $'
        shipping_charge_display_text = 'The shipping charge is $'
        shipping_state_display_text = 'The state that this will be shipped to is: '
        state_sales_tax_rate_display_text = 'The state sales tax rate is '
        state_sales_tax_display_text = 'The state sales tax is $'
        total_shipping_charge_display_text = 'The total shipping charge is $'

        # stores the shipping charge (to be used later to calculate the shipping total)
        shipping_charge = 0.0

        # Based on the weight of the package, display the rate per pound
        # Then, calculate the shipping charge by multiplying the weight of the package by the rate per pound
        if weight_of_package <= 2:
            shipping_charge = weight_of_package * TWO_POUNDS_OR_LESS_RATE
            print(rate_per_pound_display_text + format(TWO_POUNDS_OR_LESS_RATE, '.2f'))
            print(shipping_charge_display_text + format(shipping_charge, ',.2f'))
        elif 2 < weight_of_package <= 6:
            shipping_charge = weight_of_package * BETWEEN_TWO_AND_SIX_POUNDS_RATE
            print(rate_per_pound_display_text + format(BETWEEN_TWO_AND_SIX_POUNDS_RATE, '.2f'))
            print(shipping_charge_display_text + format(shipping_charge, ',.2f'))
        elif 6 < weight_of_package <= 10:
            shipping_charge = weight_of_package * BETWEEN_SIX_AND_TEN_POUNDS_RATE
            print(rate_per_pound_display_text + format(BETWEEN_SIX_AND_TEN_POUNDS_RATE, '.2f'))
            print(shipping_charge_display_text + format(shipping_charge, ',.2f'))
        elif weight_of_package > 10:
            shipping_charge = weight_of_package * GREATER_THAN_TEN_POUNDS_RATE
            print(rate_per_pound_display_text + format(GREATER_THAN_TEN_POUNDS_RATE, '.2f'))
            print(shipping_charge_display_text + format(shipping_charge, ',.2f'))

        # Display the state that the package is being shipped to
        print(shipping_state_display_text + state_of_package)

        # stores the sales tax amount, to be used later for calculating the shipping total
        sales_tax_total = 0.0

        # Based on the state that the package will be sent to, display the state sales tax rate and amount
        if state_of_package == 'AR':
            # calculate the shipping charge by multiplying the shipping charge and state tax rate
            sales_tax_total = shipping_charge * ARKANSAS_TAX_RATE
            print(state_sales_tax_rate_display_text + format((ARKANSAS_TAX_RATE * 100), '.3f') + '%')
            print(state_sales_tax_display_text + format(sales_tax_total, '.2f'))
        elif state_of_package == 'KS':
            # calculate the shipping charge by multiplying the shipping charge and state tax rate
            sales_tax_total = shipping_charge * KANSAS_TAX_RATE
            print(state_sales_tax_rate_display_text + format((KANSAS_TAX_RATE * 100), '.3f') + '%')
            print(state_sales_tax_display_text + format(sales_tax_total, '.2f'))
        elif state_of_package == 'LA':
            # calculate the shipping charge by multiplying the shipping charge and state tax rate
            sales_tax_total = shipping_charge * LOUISIANA_TAX_RATE
            print(state_sales_tax_rate_display_text + format((LOUISIANA_TAX_RATE * 100), '.3f') + '%')
            print(state_sales_tax_display_text + format(sales_tax_total, '.2f'))
        elif state_of_package == 'NM':
            # calculate the shipping charge by multiplying the shipping charge and state tax rate
            sales_tax_total = shipping_charge * NEW_MEXICO_TAX_RATE
            print(state_sales_tax_rate_display_text + format((NEW_MEXICO_TAX_RATE * 100), '.3f') + '%')
            print(state_sales_tax_display_text + format(sales_tax_total, '.2f'))
        elif state_of_package == 'OK':
            # calculate the shipping charge by multiplying the shipping charge and state tax rate
            sales_tax_total = shipping_charge * OKLAHOMA_TAX_RATE
            print(state_sales_tax_rate_display_text + format((OKLAHOMA_TAX_RATE * 100), '.3f') + '%')
            print(state_sales_tax_display_text + format(sales_tax_total, '.2f'))
        elif state_of_package == 'TX':
            # calculate the shipping charge by multiplying the shipping charge and state tax rate
            sales_tax_total = shipping_charge * TEXAS_TAX_RATE
            print(state_sales_tax_rate_display_text + format((TEXAS_TAX_RATE * 100), '.3f') + '%')
            print(state_sales_tax_display_text + format(sales_tax_total, ',.2f'))

        # Display the total shipping charge
        print(total_shipping_charge_display_text + format(shipping_charge + sales_tax_total, ',.2f'))
