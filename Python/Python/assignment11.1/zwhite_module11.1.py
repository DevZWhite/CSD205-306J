# Name: Zachary White
# Instructor: Darrell Payne
# Date: March 13, 2026
# Assignment: Recursive and Non-Recursive Counting Program

# Purpose:
# This program demonstrates two different approaches to solving
# the same problem:
#   1. A recursive function
#   2. A non-recursive (iterative) function
# Each function accepts an integer argument n and prints the
# numbers from 1 up to and including n.
# The program also validates input to ensure that the user
# cannot enter a negative number or zero.

# Logic:
# 1. Create a recursive function that prints numbers using
#    self-calling behavior until a base case is reached.
# 2. Create a non-recursive function that prints numbers
#    using a loop structure.
# 3. Validate user input so only positive integers are allowed.
# 4. Display which function is being executed at the start
#    and end of each output section.
# 5. Call both functions from main() for testing.


# -----------------------------------------------------------
# Recursive Function
# -----------------------------------------------------------
def recursive_count(n):
    """
    Recursive Approach Explanation:
    This function solves the problem by calling itself repeatedly.
    Each call reduces the value of n until it reaches the base case.
    
    Base Case:
        When n == 1, the recursion stops.
    
    Recursive Case:
        The function calls itself with (n - 1) first,
        then prints the current value of n.
    
    This allows numbers to be printed in ascending order
    from 1 to n as the call stack unwinds.
    """

    # Base case
    if n == 1:
        print(1)
    else:
        recursive_count(n - 1)
        print(n)


# -----------------------------------------------------------
# Non-Recursive Function
# -----------------------------------------------------------
def iterative_count(n):
    """
    Non-Recursive (Iterative) Approach Explanation:
    This function uses a loop instead of recursion.
    
    A for-loop starts at 1 and continues until n,
    printing each value sequentially.
    
    Unlike recursion, this method does not use
    additional function calls or a call stack,
    making it simpler and more memory efficient.
    """

    for i in range(1, n + 1):
        print(i)


# -----------------------------------------------------------
# Input Validation Function
# -----------------------------------------------------------
def get_positive_integer():
    """
    Prompts the user until a valid positive integer (> 0)
    is entered. Prevents negative numbers and zero.
    """
    while True:
        try:
            value = int(input("Enter a positive integer: "))
            if value <= 0:
                print("ERROR: Value must be greater than 0.\n")
            else:
                return value
        except ValueError:
            print("ERROR: Please enter a valid integer.\n")


# Main Function
def main():

    # Get validated user input
    number = get_positive_integer()

    # Recursive function execution
    print("\n===== START: Recursive Function =====")
    recursive_count(number)
    print("===== END: Recursive Function =====\n")

    # Non-recursive function execution
    print("===== START: Non-Recursive Function =====")
    iterative_count(number)
    print("===== END: Non-Recursive Function =====")


# Entry point
if __name__ == "__main__":
    main()