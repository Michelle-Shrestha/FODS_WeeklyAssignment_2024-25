#2. Write a program that prompts the user for two integer values and 
# displays the results of the first number divided by the second, 
# with exactly two decimal places displayed.

number1= int (input("Enter the number: "))
number2= int (input("Enter the second number: "))
division = number1/number2
solu=round(division,2)
print ("The quotient after dividing number 1 and number 2 is " , solu)