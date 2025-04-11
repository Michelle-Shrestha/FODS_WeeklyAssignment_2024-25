#8. Write a program that prompts the user to enter integer values to populate two lists,
# then prints messages to determine the following:
# (a) Whether the lists are of the same length.
# (b) Whether the elements in each list sum to the same value.
# (c) Whether there are any values that occur in both lists

lst1 = input (" Enter the elements of list 1 separated by comma ").split(",")
#Spliting the input element into individual number
lst2 = input (" Enter the elements of list 2 separated by comma ").split(",")
num1= [int(num) for num in lst1] #converting each element into integer
num2= [int(num) for num in lst2]
print (f"List 1: {num1} \n List 2: {num2}")
if len(num1)== len(num2):
  print (f"List 1 and List 2 have the same length.That is : {len(num1)}")
else:
  print (f"List 1 length : {len(num1)} \nList 2 length : {len(num2)}")

sum_num1 = 0
sum_num2 = 0
for num in num1: #adding the value of list 1
  sum_num1+=num
for num in num2: #adding the value of list 2
  sum_num2+=num

if sum_num1 == sum_num2:
  print (f"The sum of List1 and the sum of List 2 are equal : {sum_num1}")
else:
  print (f"The sum of List 1 : {sum_num1} \nThe sum of List 2 : {sum_num2}")

intersection = set(num1) & set(num2) #using logical AND to check if there are common numbers or not
if intersection:
  print (f"The common elements of List1 and List2 are {intersection}")
else:
  print ("List 1 and List 2 dont have any common elements")