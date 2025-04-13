#9. Given the table below,...
# a.	Write a query to select only the Name and Salary columns.
# b.	How would you filter out all employees in the "IT" department?
# c.  Write code to select employees who are older than 30 and find the average salary of employees in each department.
# d.	Write code to count the number of employees in each department.
# e.	Add a new column Bonus which is 10% of each employee's salary.
# f.	Replace all occurrences of "HR" in the Department column with "Human Resources."
# g.	Find the employee(s) with the longest tenure (based on JoinDate).
# h.	Create a new column SalaryCategory where salaries above 75,000 are categorized as "High" and the rest as "Low."
# i.  Write a program to check if there are any duplicate EmployeeIDs and remove them if found.
# j.	Use Pandas to calculate the median Age of all employees.

import pandas as pd
import numpy as np

details = { "EmployeeID": [101,102,103,104,105],
            "Name": ["John Smith", "Alice Brown", "Bob White", "Emma Green", "Charlie Red"],
           "Department": ["IT", "HR", "IT", "Finance", "HR"], 
           "Age": [30,28,35,40,25],
           "Salary": [70000, 60000, 80000, 90000, 55000],
           "JoinDate": ["2018-07-15", "2020-03-10", "2016-11-01", "2012-05-25", "2021-06-01"],
           "ExperienceYears": [5,3,7,11,2]}

#a.	
data = pd.DataFrame(details)
name_salary = data [["Name", "Salary"]] #selecting only the Name and Salary column
print(f"The name and salary column:\n{name_salary}\n")

#b.
IT_employees= data[data["Department"]=="IT"] #Filtering the Employees of IT department
print(f"Employees of IT department:\n{IT_employees}\n")

#c.
Older_than_30=data[data["Age"]>30] #selecting employees who are older than 30
avg_salary =Older_than_30.groupby("Department")["Salary"].mean()# finding the average salary of older than 30 of each department 
print(f"Average salary of employees who are older than 30:\n{avg_salary}\n")

#d.
count_employees= data["Department"].value_counts()
print(f"Number of employees in each department are:\n{count_employees}\n")

#e.
data["Bonus"] = data["Salary"]*0.10# it calculates 10% of each employee salary
print(f"Bonus of each employees:\n{data[["Name", "Salary", "Bonus"]]}\n") # printing only name,salary and bonous

#f.
data["Department"]= data["Department"].replace("HR","Human Resources")# replacing HR with human resources
print(f"HR in department column is replaced by human resources:\n{data[["Name","Department"]]}\n") #printing name and department only

#g.	
data["JoinDate"] = pd.to_datetime(data["JoinDate"]) #for formatting the JoinDate str in datetime format
longest_tenure = data[data["JoinDate"] == data["JoinDate"].min()]
print(f"Employees of longest tenure:\n{longest_tenure[["Name","JoinDate"]]}\n ") #printing the name and join date of oldest tenure

#h.	
data["SalaryCategory"] = data["Salary"].apply(lambda x: "High" if x>75000 else "Low")#  new column is created (SalaryCategory)
print(data[["Name", "Salary", "SalaryCategory"]], "\n")

#i.
if data["EmployeeID"].duplicated().any():  # checks duplicate employee id
    data = data.drop_duplicates(subset="EmployeeID") # removes the duplicate id row 
    print("Duplicate ID has been removed")
else:
    print("No Duplicate ID are found.")

print(data[["EmployeeID","Name"]],"\n")

#j.
median_age = data["Age"].median()
print(f"Median age of all employees are: {median_age}" "\n")