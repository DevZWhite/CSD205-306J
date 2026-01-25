# Name: Zachary White
# Instructor: Darrell Payne
# Date: January 21, 2026
# Assignment: Project 2.2 – Fiber Optic Installation Cost Calculator based on feet bought

# Purpose: This program calculates the total cost of installing fiber optic cable
# logic: user is displayed a welcome screen, user is asked for number of feet.
# Error handling loops the user into a valid input float, conditional if/elifs to apply credited discounts.
# calculation, the user is then returned the expected value and asked if interested in making an additional installation.

# Declaring get_feet_of_cable function.
def get_feet_of_cable():
    # Prompts the user to enter the number of feet to be installed and validates that the input is a valid floating-point number.
    while True:
        try:
            # Attempt to get input and convert it to a float
            user_input = input("Please enter the number of feet to be installed: ")
            value = float(user_input)
            # If successful, return the appropriate float value
            return value
        except ValueError:
            # If the conversion fails, print an error message and the loop continues back to line 12
            print(f"Error: {user_input} is not a valid input, please try again.")

# --- MAIN PROGRAM LOOP ---
while True:
    # Displaying my welcome message
    print("\nWelcome to PureOptic Fiber Optic Installation Services")
    print("This program calculates the cost of installing fiber optic cable by the foot.\n")

    # calling function for get feet of cable...
    feet_of_cable = get_feet_of_cable()
    print(f"Successfully recorded: {feet_of_cable} feet of cable.")

    # Determine cost per foot based on quantity specifically 'more than' operators.
    if feet_of_cable > 500:
        cost_per_foot = 0.50
    elif feet_of_cable > 250:
        cost_per_foot = 0.70
    elif feet_of_cable > 100:
        cost_per_foot = 0.80
    else:
        cost_per_foot = 0.87

    # Calculate the total installation cost
    total_cost = feet_of_cable * cost_per_foot

    # Display the results using f-strings
    print("\n--- Installation Summary ---")
    print(f"Company Name: PureOptic Fiber Optic Installation Services")
    print(f"Feet of Fiber Optic Cable: {feet_of_cable}")
    print(f"Cost per Foot: ${cost_per_foot:.2f}")
    print(f"Total cost of installation: ${total_cost:.2f}")
    print("-----------------------------\n")

    # --- RESTART MAIN PROGRAM LOOP ---
    restart = input("Do you want to calculate another installation? (y/n): ").lower()
    if restart != 'y' and restart != 'yes':
        print("Thank you for using PureOptic services. Goodbye!")
        break # Exits the while True loop
