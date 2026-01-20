# Name: Zachary White
# Instructor: Darrell Payne
# Date: January 15, 2026
# Assignment: Project 1.3 – Fiber Optic Installation Cost Calculator

# Purpose: This program calculates the total cost of installing fiber optic cable based on the number of feet entered by the user.

# Display a welcome message
print("Welcome to PureOptic Fiber Optic Installation Services")
print("This program calculates the cost of installing fiber optic cable by the foot.\n")

# Get the number of feet of fiber optic cable from the user
feet_of_cable = float(input("Please enter the number of feet to be installed: "))

# Cost per foot of fiber optic cable
cost_per_foot = 0.87

# Calculate the total installation cost
total_cost = feet_of_cable * cost_per_foot

# Display the results using f-strings.
# The 'f' before the quotes allows variables to be embedded directly into the text using {}. 
# This makes the output easier to read and format, especially for currency.
# The :.2f formatting ensures numeric values are displayed with two decimal places.
print("\nInstallation Summary:")
print(f"Company Name: PureOptic Fiber Optic Installation Services")
print(f"Feet of Fiber Optic Cable: {feet_of_cable}")
print(f"Cost per Foot: ${cost_per_foot:.2f}")
print(f"Total cost of installation: ${total_cost:.2f}")