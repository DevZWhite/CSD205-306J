# Name: Zachary White
# Instructor: Darrell Payne
# Date: January 23, 2026
# Assignment: Project 3.3 – interest rate calculator / years to double

# Purpose: 
# This program calculates the number of years required for an initial investment 
# to double in value based on a user-defined annual interest rate.

# Help Wanted!!! - At the end of my program how can I error handle the user entering something other than y/n 

# Logic:
# 1. The program uses input validation loops to ensure the initial investment and 
#    interest rate provided by the user are valid float values.
# 2. The interest rate is converted from a percentage to a decimal for calculation.
# 3. A 'while' loop executes as long as the current account balance is less than 
#    two times the starting principal.
# 4. Each iteration of the loop represents one year, adding the annual interest 
#    earned to the current balance and incrementing the year counter.
# 5. Once the investment has doubled, the loop terminates and the program 
#    displays the growth summary results.
# 6. prompt the user an end loop that can restart the application from the beginning sequence.

# Defining functions
def get_initial_investment():
    # Prompts the user to enter the initial investment of the account.
    while True:
        try:
            # Attempt to get input and convert it to a float
            user_input = input("Please enter the amount you want to invest: ")
            value = float(user_input)
            # If successful, return the appropriate float value
            return value
        except ValueError:
            # If the conversion fails, print an error message and the loop continues back to line 25'
            print(f"Error: {user_input} invalid, please try again.")

def get_interest_rate():
    # Prompts the user to enter the given interest rate of the account.
    while True:
        try:
            # Attempt to get input and convert it to a float
            user_input = input("Please enter the interest rate: ")
            value = float(user_input)
            # If successful, return the appropriate float value
            return value
        except ValueError:
            # If the conversion fails, print an error message and the loop continues back to line 38
            print(f"Error: {user_input} invalid, please try again.")

while True:
        
    # initialize the functions
    initial_investment = get_initial_investment()
    interest_rate = get_interest_rate()

    # Convert interest rate from percentage to decimal
    interest_rate = interest_rate / 100

    # Initialize variables
    current_value = initial_investment
    years = 0

    # Loop until the investment has doubled the investment
    while current_value < initial_investment * 2:
         current_value += current_value * interest_rate
         years += 1

    # Display results
    print("\nInvestment Growth Summary")
    print("--------------------------")
    print(f"Initial Investment: ${initial_investment:,.2f}")
    print(f"Annual Interest Rate: {interest_rate * 100:.2f}%")
    print(f"Years to Double Investment: {years}")
    print(f"Final Value: ${current_value:,.2f}")

    restart = input("Do you have another investment? (y/n): ").lower()
    if restart != 'y' and restart != 'yes':
        break # Exits the while True loop
    elif restart != 'n' and restart != 'no':
        exit
