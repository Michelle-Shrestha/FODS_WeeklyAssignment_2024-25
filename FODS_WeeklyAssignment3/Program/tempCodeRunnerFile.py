        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    def to_list(self):
        # This method converts the object's attributes into a list format
        return [
            self.empid,
            self.name,
            self.address,
            self.contact_number,
            self.spouse_name,
            self.number_of_child,
            self.salary,
        ]


# Step 2: Function to take input for a single employee
def get_employee_details():
    try:
        empid = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        address = input("Enter Address: ")
        contact_number = input("Enter Contact Number: ")
        spouse_name = input("Enter Spouse Name: ")
        number_of_child = input("Enter Number of Children: ")
        salary = input("Enter Salary: ")

        # Return a new Employee object
        return Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)
    except Exception as e:
        print(f"An error occurred while entering details: {e}")
        return None


# Step 3: Write employee data to a CSV file
def write_to_csv(employee_list, file_name="employees.csv"):
    try:
        # Open the CSV file in write mode
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            # Write the header row
            writer.writerow(["EmpID", "Name", "Address", "Contact Number", "Spouse Name", "Number of Children", "Salary"])
            # Write employee details
            for employee in employee_list:
                writer.writerow(employee.to_list())
        print(f"Data written to {file_name} successfully.")
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")


# Step 4: Read and display employee data from the CSV file
def read_from_csv(file_name="employees.csv"):
    try:
        # Open the CSV file in read mode
        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            # Read and display each row
            print("\n--- List of Employees ---")
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print("The file does not exist. Please add some employee data first.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


# Step 5: Main Program Logic
def main():
    employees = []  # List to hold Employee objects

    while True:
        print("\n1. Add Employee")
        print("2. Save Employees to File")
        print("a. View Employees")
        print("4. Exit")
