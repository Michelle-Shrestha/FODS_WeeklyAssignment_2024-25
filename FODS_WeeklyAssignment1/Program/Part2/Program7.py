#7. Write a Python program that accepts a string and calculates the number of digits and letters.

word= input ("Please Enter a sentence : ")
Num_Letters = 0
Num_Digits = 0
for ch in word: #Iterates over each letter of the sentence

    if ch.isdigit(): #Checks if character is a number or not
        Num_Digits+=1 #if it is it adds by 1

    elif ch.isalpha(): #Checks if character is a string or not
        Num_Letters+=1 #if it is it adds by 1

print (f"Number of letters are : {Num_Letters}") 
print (f"Number of digits are : {Num_Digits}")