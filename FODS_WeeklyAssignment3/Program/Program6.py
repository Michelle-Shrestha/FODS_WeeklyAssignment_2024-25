# 6. Create a class Student with the attributes such as id, name, address, admission year, level, 
# section. Instantiate the object of class to take input for all the attributes and display the output.

class Student:
    def __init__(self):
        #initializing tbea attributes of the object
        self.student_id= input("Enter student ID: ")
        self.student_name= input("Enter the name of student: ")
        self.student_address=input("Enter the address of student: ")
        self.student_admission_year=input("Enter the admission year of student: ")
        self.student_level=input("Enter the level of student: ")
        self.student_section=input("Enter the section of student: ")

    def display(self):
        # Prints all the student details
        print("\n ---Student details--- \n")
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)
        print("Student Address:", self.student_address)
        print("Student Admission Year:", self.student_admission_year)
        print("Student Level:", self.student_level)
        print("Student Section:", self.student_section)

student1= Student()# Creating an object of student class
#and calls the constructor (__init__) automatically
student1.display()