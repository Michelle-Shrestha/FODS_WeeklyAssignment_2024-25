#6.Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
#between 1500 and 2000 (both included).

num=[] #empty list 
num1 = 1500
num2 = 2000
for i in range (num1, num2+1):
    if i%7==0 and i%5==0:
        num.append(i) #used append to store the value in the given empty num list
print (num)