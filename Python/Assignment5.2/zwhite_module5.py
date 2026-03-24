# Name: Zachary White
# Instructor: Darrell Payne
# Date: February 02, 2026
# Assignment: User Information File Writer

# Purpose:
# This program collects user information including name, street address,
# and phone number, then writes the data to a file specified by the user.
# The data is stored in a comma-separated format and read back to verify
# successful file creation and data storage.

# Logic:
# 1. The program prompts the user to enter a base file name.
# 2. The user is prompted to enter their name, street address, and phone number.
# 3. The program appends " data.txt" to the user-provided file name.
# 4. The user information is written to the file as a single comma-separated line.
# 5. After writing, the file is reopened in read mode.
# 6. The contents of the file are read and displayed to the user.

# Prompt for the base file name
base_filename = input("Enter a file name: ")

# Prompt for user details
name = input("Enter your name: ")
street_address = input("Enter your street address: ")
phone_number = input("Enter your phone number: ")

# Create the full file name
filename = f"{base_filename} data.txt"

# Write the data to the file as a comma-separated line
with open(filename, "w") as file:
    file.write(f"{name},{street_address},{phone_number}\n")

# Read the file and display its contents
with open(filename, "r") as file:
    contents = file.read()
    print("\nFile contents:")
    print(contents)
