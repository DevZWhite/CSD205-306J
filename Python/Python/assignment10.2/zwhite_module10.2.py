# Name: Zachary White
# Instructor: Darrell Payne
# Date: March 4, 2026
# Assignment: Employee and Production Worker Class Program

# Purpose:
# This program defines two classes: Employee and ProductionWorker.
# The Employee class stores basic employee information including
# name, gender, hourly pay rate, and employee number.

# The ProductionWorker class inherits from the Employee class and
# adds one additional field: shift number. The shift number represents
# the employee's working shift:
# 1 = Day Shift
# 2 = Swing Shift
# 3 = Graveyard Shift

# The program creates two Employee objects and two ProductionWorker
# objects. The field values are set using setters (no user input).
# Finally, the program displays all employee information in a clear
# and readable format.

# Logic:
# 1. Define an Employee class with fields for name, gender,
#    hourly pay rate, and employee number.
# 2. Create setter and getter methods for each field.
# 3. Define a ProductionWorker class that inherits from Employee.
# 4. Add a shift number field with its own setter and getter.
# 5. In the main function, create two Employee objects and two
#    ProductionWorker objects.
# 6. Set all values using setter methods.
# 7. Display all information in a readable format.


# Define the Employee class
class Employee:

    # Constructor method
    def __init__(self):
        self.employee_name = ""
        self.employee_gender = ""
        self.hourly_pay_rate = 0.0
        self.employee_number = 0

    # Setter methods
    def set_employee_name(self, name):
        self.employee_name = name

    def set_employee_gender(self, gender):
        self.employee_gender = gender

    def set_hourly_pay_rate(self, rate):
        self.hourly_pay_rate = rate

    def set_employee_number(self, number):
        self.employee_number = number

    # Getter methods
    def get_employee_name(self):
        return self.employee_name

    def get_employee_gender(self):
        return self.employee_gender

    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate

    def get_employee_number(self):
        return self.employee_number


# Define the ProductionWorker class that inherits from Employee
class ProductionWorker(Employee):

    # Constructor method
    def __init__(self):
        super().__init__()
        self.shift_number = 0

    # Setter for shift number
    def set_shift_number(self, shift):
        self.shift_number = shift

    # Getter for shift number
    def get_shift_number(self):
        return self.shift_number

    # Method to return shift name
    def get_shift_name(self):
        if self.shift_number == 1:
            return "Day Shift"
        elif self.shift_number == 2:
            return "Swing Shift"
        elif self.shift_number == 3:
            return "Graveyard Shift"
        else:
            return "Unknown Shift"


# Main function to run the program
def main():

    # Create Employee objects
    employee1 = Employee()
    employee2 = Employee()
    employee3 = Employee() 

    # Set values using setters
    employee1.set_employee_name("Alice Johnson")
    employee1.set_employee_gender("Female")
    employee1.set_hourly_pay_rate(22.50)
    employee1.set_employee_number(1001)

    employee2.set_employee_name("Mark Stevens")
    employee2.set_employee_gender("Male")
    employee2.set_hourly_pay_rate(24.75)
    employee2.set_employee_number(1002)
    
    employee3.set_employee_name("Zachary White")
    employee3.set_employee_gender("Male")
    employee3.set_hourly_pay_rate(19.99)
    employee3.set_employee_number(1003)

    # Create ProductionWorker objects
    worker1 = ProductionWorker()
    worker2 = ProductionWorker()
    worker3 = ProductionWorker()
    worker4 = ProductionWorker()

    # Set values using setters
    worker1.set_employee_name("Brian Carter")
    worker1.set_employee_gender("Male")
    worker1.set_hourly_pay_rate(26.00)
    worker1.set_employee_number(2001)
    worker1.set_shift_number(1)

    worker2.set_employee_name("Samantha Lee")
    worker2.set_employee_gender("Female")
    worker2.set_hourly_pay_rate(27.25)
    worker2.set_employee_number(2002)
    worker2.set_shift_number(3)

    worker3.set_employee_name("Jessica Brown")
    worker3.set_employee_gender("Female")
    worker3.set_hourly_pay_rate(25.50)
    worker3.set_employee_number(2003)
    worker3.set_shift_number(2)

    worker4.set_employee_name("Arian White")
    worker4.set_employee_gender("Female")
    worker4.set_hourly_pay_rate(19.50)
    worker4.set_employee_number(2004)
    worker4.set_shift_number(1)

    # Display Employee information
    print("\n--- Employee Information ---")

    print("\nEmployee 1")
    print("Name:", employee1.get_employee_name())
    print("Gender:", employee1.get_employee_gender())
    print("Employee Number:", employee1.get_employee_number())
    print("Hourly Pay Rate: $", employee1.get_hourly_pay_rate())

    print("\nEmployee 2")
    print("Name:", employee2.get_employee_name())
    print("Gender:", employee2.get_employee_gender())
    print("Employee Number:", employee2.get_employee_number())
    print("Hourly Pay Rate: $", employee2.get_hourly_pay_rate())

    print("\nEmployee 3")
    print("Name:", employee3.get_employee_name())
    print("Gender:", employee3.get_employee_gender())
    print("Employee Number:", employee3.get_employee_number())
    print("Hourly Pay Rate: $", employee3.get_hourly_pay_rate())


    # Display Production Worker information
    print("\n--- Production Worker Information ---")

    print("\nProduction Worker 1")
    print("Name:", worker1.get_employee_name())
    print("Gender:", worker1.get_employee_gender())
    print("Employee Number:", worker1.get_employee_number())
    print("Hourly Pay Rate: $", worker1.get_hourly_pay_rate())
    print("Shift:", worker1.get_shift_name())

    print("\nProduction Worker 2")
    print("Name:", worker2.get_employee_name())
    print("Gender:", worker2.get_employee_gender())
    print("Employee Number:", worker2.get_employee_number())
    print("Hourly Pay Rate: $", worker2.get_hourly_pay_rate())
    print("Shift:", worker2.get_shift_name())

    print("\nProduction Worker 3")
    print("Name:", worker3.get_employee_name())
    print("Gender:", worker3.get_employee_gender())
    print("Employee Number:", worker3.get_employee_number())
    print("Hourly Pay Rate: $", worker3.get_hourly_pay_rate())
    print("Shift:", worker3.get_shift_name())

    print("\nProduction Worker 4")
    print("Name:", worker4.get_employee_name())
    print("Gender:", worker4.get_employee_gender())
    print("Employee Number:", worker4.get_employee_number())
    print("Hourly Pay Rate: $", worker4.get_hourly_pay_rate())
    print("Shift:", worker4.get_shift_name())

# Entry point
if __name__ == "__main__":
    main()