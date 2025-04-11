#8. Write a program to create a number guessing game for the user. 
# The program should ask the user to input a number. 
# The program specifications are as mentioned below.
#    I. The program should generate a random number for the answer.
#    II. The program should prompt the user for a number input.
#    III. The program should provide the feedback to the user after each guesses (e.g. “Too high”, “Too low” or “Correct number”).
#    IV. The program should check the user input for 5 times and allow the users to guess for
#    at most 5 times if their input don’t match the answer number.V. 
#    If the user is not able to guess the answer within 5 times, the program should display “Game Over” message and exit.

import random
number = random.randint(1,100) # give random from 1 to 100
guess = 0
for i in range (5,0,-1):
    guess= int(input(" Guess The Number: "))
    
    if guess > number:
        print (" Too High, Guess Lower!!! ")
    elif guess < number:
        print (" Too Low, Guess Higher!!! ")
    elif guess == number:
        print (" Correct number, CONGRATULATIONS!!! ")
        break
    print (f"You have {i-1} guess left")

if guess!=number:
    print (" Game over, Better Luck Next Time!!! ")