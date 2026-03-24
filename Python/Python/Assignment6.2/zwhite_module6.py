
# Name: Zachary White
# Instructor: Darrell Payne
# Date: February 14, 2026
# Assignment: Tuple Iteration and Display Program

# Purpose:
# This program demonstrates how to create and use a tuple in Python.
# The tuple is initialized with 20 related values (U.S. states).
# The program displays the entire tuple, iterates through it in
# forward order using formatted sentences, and then repeats the
# output in reverse order using a different contextual message.

# Logic:
# 1. A tuple named "states" is initialized with 20 U.S. state names.
# 2. The complete contents of the tuple are displayed in a single print statement.
# 3. A for loop iterates through the tuple in forward order.
# 4. Each state is displayed as part of a complete sentence using an f-string.
# 5. The reversed() function is used to iterate through the tuple in reverse order.
# 6. Each state is displayed again using a different context sentence.

def main():

    # Initialize tuple with 20 U.S. states
    states = (
        "Ohio",
        "Michigan",
        "Indiana",
        "Illinois",
        "Kentucky",
        "Tennessee",
        "Florida",
        "Georgia",
        "Texas",
        "California",
        "Nevada",
        "Arizona",
        "Colorado",
        "Utah",
        "New York",
        "Pennsylvania",
        "Virginia",
        "North Carolina",
        "South Carolina",
        "Alabama"
    )

    # Display contents in a single statement
    print("Here is the complete list of states in the tuple:")
    print(states)

    print("\n--- Forward Order ---")
    # Iterate through tuple (forward)
    for state in states:
        print(f"{state} is one of the states included in this tuple example.")

    print("\n--- Reverse Order ---")
    # Iterate through tuple (reverse)
    for state in reversed(states):
        print(f"Now backwards, we now highlight the state of {state}.")

# Ensures the program runs only when executed directly
if __name__ == "__main__":
    main()
