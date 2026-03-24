# Name: Zachary White
# Instructor: Darrell Payne
# Date: February 17, 2026
# Assignment: Name Initials Display Program

# Purpose:
# This program prompts the user to enter their full name
# including first, middle, and last names. The program
# then extracts the first letter of each name and displays
# the person's initials in the format:
# FirstInitial. MiddleInitial. LastInitial.
# The program also saves each entry to a text file log
# and allows the user to view all previously saved records.

# Logic:
# 1. Display a menu with options to enter a name, view records, or quit.
# 2. Prompt the user to enter their full name (first, middle, last).
# 3. Store the input as a single string.
# 4. Split the string into a list using spaces as separators.
# 5. Access the first character of each name and convert to uppercase.
# 6. Display the initials in the format: F. M. L.
# 7. Append the name and initials as a new entry in 'initials_log.txt'.
# 8. If the user selects view records, open and read the log file
#    and display all saved entries to the screen.

import os  # Import os module to check if the log file exists

# The name of the file where all entries will be saved
FILENAME = "initials_log.txt"


# Function to extract and return initials from a full name
def get_initials(full_name):
    # Remove leading/trailing whitespace and split the name into a list of words
    parts = full_name.strip().split()

    # Make sure the user entered exactly three names (first, middle, last)
    if len(parts) != 3:
        raise ValueError("Please enter exactly a first, middle, and last name.")

    # Take the first character of each name, capitalize it, and join with ". "
    # Then add a final period at the end (e.g. "Z. D. W.")
    return ". ".join(part[0].upper() for part in parts) + "."


# Function to append a new name and initials entry to the log file
def write_to_file(name, initials):
    # Open the file in append mode so existing entries are not overwritten
    with open(FILENAME, "a") as f:
        # Write the name and its initials on a new line
        f.write(f"Name: {name} | Initials: {initials}\n")

    # Confirm to the user that the entry was saved2
    print(f"Entry saved to '{FILENAME}'.")


# Function to read and display all entries from the log file
def read_from_file():
    # Check if the log file exists before trying to open it
    if not os.path.exists(FILENAME):
        print("No records found. The log file does not exist yet.")
        return  # Exit the function early if there is no file

    # Open the file in read mode and store its contents
    with open(FILENAME, "r") as f:
        contents = f.read()

    # If the file has content, display it; otherwise notify the user it is empty
    if contents.strip():
        print(f"\n--- Contents of '{FILENAME}' ---")
        print(contents)
        print("--------------------------------")
    else:
        print("The log file is empty.")


# Main function that drives the program with a menu loop
def main():
    # Keep looping until the user chooses to quit
    while True:
        # Display the menu options to the user
        print("\nOptions:")
        print("  1. Enter a name and get initials")
        print("  2. View saved records")
        print("  3. Quit")

        # Capture the user's menu choice and remove any extra whitespace
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            # Prompt the user to enter their full name
            name = input("Enter your first, middle, and last name: ").strip()

            try:
                # Attempt to get the initials from the entered name
                initials = get_initials(name)

                # Display the initials to the user
                print(f"Your initials are: {initials}")

                # Save the name and initials to the log file
                write_to_file(name, initials)

            except ValueError as e:
                # If the name was not in the correct format, display the error
                print(f"Error: {e}")

        elif choice == "2":
            # Read and display all previously saved records from the log file
            read_from_file()

        elif choice == "3":
            # Exit the loop and end the program
            print("Goodbye!")
            break

        else:
            # Handle any input that is not 1, 2, or 3
            print("Invalid choice. Please enter 1, 2, or 3.")


# Entry point — only run main() if this script is executed directly
if __name__ == "__main__":
    main()