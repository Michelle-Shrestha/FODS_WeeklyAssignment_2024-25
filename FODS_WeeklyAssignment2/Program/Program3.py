#3. Write a function to check whether the given number is Armstrong or not.

def arm_num (num):
    a = num
    sum = 0
    length = len(str(num)) #to find the length 
    while (a>0):
        rem = a%10
        sum = sum + pow(rem, length)
        a= a//10
    return sum==num #Checks is sum and number are equal or not

number=int(input("Enter a number : "))
if arm_num(number)==False:
    print("the number is not armstrong")
elif arm_num(number)==True:
    print("the number is armstrong")

