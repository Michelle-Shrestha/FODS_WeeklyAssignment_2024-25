#2. Write a function to check whether the given number is prime or not.

def prime (num):
    i=1 
    count = 0 #how many time a number can be divided 
    if num <=1: 
        return False
    for i in range (i,num+1):
        if num%i==0:
            count +=1
    if count >2: #if num is divided by number more than itself and 1
        return False
    return True
number = int(input("Please Enter a number: "))
#to check 
if prime(number):
    print(f"{number} is a Prime number ")
else: 
    print(f"{number} is not a prime number")