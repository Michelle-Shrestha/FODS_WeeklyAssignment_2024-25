#6. Write a program that prompts the user for a series of integers and stores in a list only the values between 1-100,
#  and displays the resulting list.

num = input ("Enter the numbers separated by comma : ")
number =num.split(",") #splits the numbers into each element
numbers =[]
for nums in number:
    #to check the input is number or alpha
    if nums.isdigit():
        i = int(nums)
        #to check whether num is from 1-100 or not
        if i >=1 and i<=100:
            numbers.append(i)
        else:
            print ("Please enter a number from 1-100")
    else:
        print (f"{nums} is not a valid integer.")
print (f"The numbers between 1-100 are {numbers}")