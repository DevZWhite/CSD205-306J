# Name: Zachary White
# Instructor: Darrell Payne
# Date: January 21, 2026
# Assignment: Project 2.2 – Fiber Optic Installation Cost Calculator based on feet bought

# Purpose: This program calculates the total cost of installing fiber optic cable
# based on the number of feet entered by the user.

# Display a welcome message
print("Welcome to PureOptic Fiber Optic Installation Services")
print("This program calculates the cost of installing fiber optic cable by the foot.\n")

# Get the number of feet of fiber optic cable from the user
feet_of_cable = float(input("Please enter the number of feet to be installed: "))

# Determine cost per foot based on quantity
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
print("\nInstallation Summary:")
print(f"Company Name: PureOptic Fiber Optic Installation Services")
print(f"Feet of Fiber Optic Cable: {feet_of_cable}")
print(f"Cost per Foot: ${cost_per_foot:.2f}")
print(f"Total cost of installation: ${total_cost:.2f}")
