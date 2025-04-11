#1. Write a program to take a number input from the user and 
# display whether the number is even or odd.

number = int (input("Enter a number: "))
if number%2==0:
    print (number, "is an even number ")
else:
    print (number, "is an odd number ")