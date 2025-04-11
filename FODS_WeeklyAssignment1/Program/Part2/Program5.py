#5. Write a program to find the simple interest when the value of 
# principle, rate of interest and time period is provided by the user.

P= int(input("Please Enter the Principle amount : "))
T= int(input("Please Enter the Time period : "))
R= int(input("Please Enter the Interest rate : "))
si = round((P*T*R)/100,3) #displayed upto 3 decimal place
print ("The Simple Interest is ", si)