# Name: Zachary White
# Instructor: Darrell Payne
# Date: Feb 27, 2026
# Assignment: Student Cumulative GPA Calculator Program

# Purpose:
# This program defines a Student class that calculates
# and displays a student's cumulative GPA. The program
# prompts the user for the student's first and last name,
# then repeatedly asks for course credits and letter grades.
# After the user finishes entering courses, the program
# calculates and displays the student's cumulative GPA.

# Logic:
# 1. Define a Student class with attributes for first name,
#    last name, total quality points, and total credits.
# 2. Create a method to convert letter grades into grade points.
# 3. Create a method to add a course (credits and grade),
#    updating total quality points and total credits.
# 4. Create a method to calculate cumulative GPA.
# 5. Prompt the user for the student's first and last name.
# 6. Create a Student object using the provided names.
# 7. Use a loop to repeatedly ask the user for course credits
#    and letter grade until they choose to stop.
# 8. After exiting the loop, calculate and display the GPA.


# Define the Student class
class Student:
    # Constructor method to initialize student information
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.total_quality_points = 0.0
        self.total_credits = 0.0

    # Method to convert letter grade to grade points
    def grade_to_points(self, grade):
        grade_scale = {
            "A": 4.0,
            "B": 3.0,
            "C": 2.0,
            "D": 1.0,
            "F": 0.0
        }

        grade = grade.upper()

        if grade in grade_scale:
            return grade_scale[grade]
        else:
            raise ValueError("Invalid grade entered. Please enter A, B, C, D, or F.")

    # Method to add a course to the student's record
    def add_course(self, credits, grade):
        points = self.grade_to_points(grade)
        self.total_quality_points += points * credits
        self.total_credits += credits

    # Method to calculate cumulative GPA
    def calculate_gpa(self):
        if self.total_credits == 0:
            return 0.0
        return self.total_quality_points / self.total_credits

    # Method to display student information and GPA
    def display_gpa(self):
        gpa = self.calculate_gpa()
        print(f"\nStudent: {self.first_name} {self.last_name}")
        print(f"Cumulative GPA: {gpa:.2f}")


# Main function to run the program
def main():
    # Prompt the user for student's first and last name
    first_name = input("Enter the student's first name: ").strip()
    last_name = input("Enter the student's last name: ").strip()

    # Create a Student object
    student = Student(first_name, last_name)

    # Loop to enter courses
    while True:
        print("\nEnter course information (or type 'done' to finish).")

        credits_input = input("Enter number of credits: ").strip()

        # Allow user to exit loop
        if credits_input.lower() == "done":
            break

        try:
            credits = float(credits_input)

            grade = input("Enter letter grade (A, B, C, D, F): ").strip()

            # Add the course to the student's record
            student.add_course(credits, grade)

            print("Course added successfully.")

        except ValueError as e:
            print(f"Error: {e}")

    # Display the final cumulative GPA
    student.display_gpa()


# Entry point — only run main() if this script is executed directly
if __name__ == "__main__":
    main()