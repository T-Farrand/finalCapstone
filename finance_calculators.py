import math

# The menu for calculation options
print("investment - to calculate the amount of interest you'll earn on your investment\nbond       - to calculate the amount you'll have to pay on a home loan\n")

# The user's chosen calculation
calculation_type = input("From the above menu, please choose either 'investment' or 'bond': ")

# Check to ensure the calculation can be performed by the program
while True:
    if calculation_type.lower() == "investment" or calculation_type.lower() == "bond":
        break
    else:
        calculation_type = input("I cannot calculate that, please enter one of the options from the menu: ")

# Runs the investment block if the user entered 'investment', regardless of capitalisation
if calculation_type.lower() == "investment":
    # The initial sum of money. For £1000, you would enter 1000
    deposit = float(input("How much money are you depositing (do not include currency type): "))

    # The value of the interest rate, i.e., for a 6% interest rate, you would enter 6
    interest_rate = float(input("What is the value of the interest rate (do not include the %): "))/100

    investment_years = int(input("How many years are you planning to invest for: "))

    # Choosing the type of interest associated with the user's interest
    interest = input("Would you like 'simple' or 'compound' interest? ")

    # Check to ensure 'simple' or 'compound' was chosen
    while True:
        if interest.lower() == "simple" or interest.lower() == "compound":
            break
        else:
            interest = input("I cannot calculate that. Please choose between 'simple' or 'compound' interest: ")
    
    # Calculates the total investment
    # No check is needed for the 'compound' calculation as the user can only reach this point by entering 'compound' at the above input
    # Round to 2 decimal places as currency goes to 2 decimal places too
    if interest.lower() == "simple":
        total_investment = round(deposit*(1 + (interest_rate)*investment_years),2)
    else:
        total_investment = round(deposit * math.pow((1+interest_rate),investment_years),2)
    print("Your total investment will be " + str(total_investment) + ".")

# Runs the bond block if the user entered 'bond', regardless of capitalisation
# No check is needed for the 'bond' calculation as the user can only reach this point by entering 'bond' from the menu
else:
    present_value = float(input("What is the present value of the house (do not include currency type): "))
    interest_rate = float(input("What is the value of the interest rate (do not include the %): "))/100
    months_taken = int(input("How many months do you plan to take to repay your bond? "))

    monthly_interest = interest_rate/12
    
    # Round to 2 decimal places as currency goes to 2 decimal places too
    repayment = round((monthly_interest * present_value)/(1 - (1 + monthly_interest)**(-months_taken)),2)

    print("Your monthly paymont amount is " + str(repayment) + ".")