#5. Create a program called calculator with functions to perform the following arithmetic calculations,
#  each should take two decimal parameters and return the result of the arithmetic calculation in question.
# A. Addition
# B. Subtraction
# C. Multiplication
# D. Division
# E. Truncated division
# F. Modulus
# G. Exponentiation

def addition (a,b):
    add = a + b
    return add
def subtraction (a,b):
    sub = a - b
    return sub
def multiplication (a, b):
    multi = a * b
    return multi
def division (a,b):
    quotient = a/b
    quotient = round(quotient,2)
    return quotient
def Truncated_div (a,b):
    quotient = a//b #doesnot returns decimal point
    return quotient
def modulus (a,b):
    rem = a%b
    return rem
def exponential (a,b):
    expo = pow(a,b)
    return expo
num1 = int (input("Enter the first number : "))
num2 = int (input("Enter the second number : "))
print (f"The addition of {num1} and {num2} is {addition(num1,num2)}")
print (f"The subtraction of {num1} and {num2} is {subtraction(num1,num2)}")
print (f"The multiplication of {num1} and {num2} is {multiplication(num1,num2)}")
print (f"The division of {num1} and {num2} is {division(num1,num2)}")
print (f"The truncated division of {num1} and {num2} is {Truncated_div(num1,num2)}")
print (f"The modulus of {num1} and {num2} is {modulus(num1,num2)}")
print (f"The exponentiation of {num1} and {num2} is {exponential(num1,num2)}")