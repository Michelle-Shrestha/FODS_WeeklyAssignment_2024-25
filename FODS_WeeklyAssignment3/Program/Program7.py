#7.Write a program to implement a class called employee with attributes such as 
# empid, name, address, contact_number, spouse name, number_of_child, salary.
# Instantiate this class to input the values for multiple employees and write it in a file “employees.csv”. 
# Allow the user of your program to see the list of employees and their details as well. 
# Try to use the concept of try/except too in the program. 

import csv

class Employee:
    #initializing employee attributes
    def __init__(self, empid, name, address, contact_number, spouse_name, child_count, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.child_count = child_count
        self.salary = salary

def employee_data():#reuturns the instance of employee
    try:
        empid = int(input("Enter the Employee ID: "))
        name = input("Enter the Name: ")
        address = input("Enter the Address: ")
        contact_number = int(input("Enter the Contact Number: "))
        spouse_name = input("Enter the Spouse Name: ")
        child_count = int(input("Enter the Number of Children: "))
        salary = float(input("Enter the Salary: "))
        return Employee(empid, name, address, contact_number, spouse_name, child_count, salary)
    except Exception as e:
        print(f"The Error is {e}")
        return None

def write_employee_csv(employees, filename="employees.csv"): #writes the list of employee to csv file
    try:
        with open(filename, 'w', newline='') as file:#open file in write mode
            writer = csv.writer(file)
            #writing the row to the file
            writer.writerow(["Employee ID", "Name", "Address", "Contact Number", "Spouse Name", "Number of Children", "Salary"])
            for employ in employees:
                writer.writerow([employ.empid, employ.name, employ.address, employ.contact_number, employ.spouse_name, employ.child_count, employ.salary])
        print("Employee details written successfully.")
    except Exception as e:
        print(f"The problem is {e}")

def display_employess(employees):
    if not employees:
        print("There is no employee data to display.")
    else:
        for employ in employees:#iterate over the list and displays the details
            print(f"Employee ID: {employ.empid}, Name: {employ.name}, Address: {employ.address}, "
                  f"Contact: {employ.contact_number}, Spouse: {employ.spouse_name}, Children: {employ.child_count}, Salary: {employ.salary}")

def main():
    employees = [] #initializing empty list
    while True:
        print("\n--- Employee Details ---\n")
        print("1. Add an employee")
        print("2. Display Employee Details")
        print("3. Save details to the CSV")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            employ = employee_data()
            if employ: #adds employ if theres no error
                employees.append(employ)
        elif choice == 2:
            display_employess(employees)
        elif choice == 3:
            write_employee_csv(employees)
        elif choice == 4:
            print("You are exiting the program...")
            break
        else:
            print("Invalid choice. Please choose a valid number (1-4).")

if __name__ == '__main__':
    main() #main function is executed when all the data are valid