# This program tracks the purchase and sale of stock based on investor input.

# constant percentage for how much commission an investor earns.
COMMISSION_RATE = 0.03

# PURCHASE OF STOCK SECTION

# Stores the name of the investor when entered.
investor_name = input('What is your name? ')
# Stores the number of shares purchased (assuming whole numbers only)
number_of_shares_purchased = int(input('How many shares did you purchase? (whole numbers only) '))
# Stores the price per share. Assumption: USD format
price_per_share = float(input('What is the price per share? (in dollars) '))

# the product between number of shares purchased and price per share
purchase_amount = number_of_shares_purchased * price_per_share
# the investor earns 3% of the purchase amount
purchase_commission = purchase_amount * COMMISSION_RATE

# Displays the purchase amount as a floating point with a precision of 2 decimal places
print('The purchase amount is $' + format(purchase_amount, ',.2f'))

# Displays the total commission earned for the purchase as a floating point with a precision of 2 decimal places
print('The commission earned for this purchase is $' + format(purchase_commission, ',.2f'))

# SALE OF STOCK SECTION

# Stores of the name of the investor when entered.
investor_name = input('What is your name? ')
# Stores the number of shares sold (assuming whole numbers only)
number_of_shares_sold = int(input('How many shares did you sell? (whole numbers only) '))
# Stores the cost per share. Assumption: USD format
cost_per_share = float(input('What is the price per share? (in dollars) '))

# the product between number of shares sold and the cost per share
sale_amount = number_of_shares_sold * cost_per_share
# the investor earns 3% of the sale amount.
sale_commission = sale_amount * COMMISSION_RATE

# Displays the sale amount as a floating point with a precision of 2 decimal places
print('The sale amount is $' + format(sale_amount, ',.2f'))
# Displays the total commission earned for the sale as a floating point with a precision of 2 decimal places
print('The commission earned for this sale is $' + format(sale_commission, ',.2f'))

# SUMMARY OF TRANSACTIONS SECTION

# This is the total commission earned by the investor as a floating point with a precision of 2 decimal places.
total_commission = float(format((purchase_commission + sale_commission), '.2f'))
# Displays the investor's name
print('Name of investor: ' + investor_name)
# Prints the total commission earned by the investor as a floating point with a precision of 2 decimal places.
print('Total commission earned: $' + format(total_commission, ',.2f'))
# Prints an amount which represents either a profit or loss and is the result between the purchase and sale amounts.
# The format is a floating point with a precision of 2 decimal places
print('Profit/Loss amount: $' + format((sale_amount -
                                        (number_of_shares_sold * price_per_share) - total_commission), ',.2f'))
