#1. Write a function that accepts a string and calculate the number of upper case letters and lower case letters.

def calci (word):
    #Uppercase and lower case count
    lower_case = 0 
    upper_case = 0
    for ch in word:
        if ch.isupper(): #Checkes whether the character is in uppercase or not
            upper_case+=1  #if it is it adds by 1

        if ch.islower(): #Checks whether the character is in lowercase or not
            lower_case+=1 #if it is adds by 1
    print (f"The total upper case count is {upper_case}")
    print (f"The total lower case count is {lower_case}")

words = input("Please enter a sentence : ")
calci(words)
