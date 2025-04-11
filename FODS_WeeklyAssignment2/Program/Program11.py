#11. Create three dictionaries:
#dic1 = {1:10, 2:20}
#dic2 = {3:30, 4:40}
#dic3 = {5:50, 6:60}
#(a) Write code to concatenate these dictionaries to create a new one.
#  Create a variable called nums to store the resulting dictionary.
#(b) Write code to add a new key/value pair to the dictionary nums: (7, 70)
#(c) Write code to update the value of the item with key 3 in nums to 80
#(d) Write code to remove the third item from dictionary nums.
#(e) Write code to sum all the items in the dictionary nums
#(f) Write code to multiply all the items in the dictionary nums
#(g) Write code to retrieve the maximum and minimum values in nums

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

nums= {} #empty dictionaries
nums.update(dic1) #adds items 
nums.update(dic2)
nums.update(dic3)
print(f"The concatenated dictionary: {nums}")

nums[7]= 70 #adding new key and value in nums dictionary
print (f"Dictionary after adding new key and value: {nums}")

nums[3]= 80 #updating the key 3 value to 80
print(f"Dictionary after updating the key 3 value to 80: {nums}")

nums.pop(3)
print (f"Dictionary after removing the third item: {nums}")

total_sum = 0
for value in nums.values(): #adding the only values not keys
  total_sum+=value
print(f"The total sum of all items: {total_sum}")

total_multiple = 1
for value in nums.values(): #adding the values only not keys
  total_multiple*=value
print(f"The total product of all items: {total_multiple}")

maximum_value = max(nums.values())
minimum_value = min(nums.values())
print (f"Maxinum Value: {maximum_value}\nMinimum Value: {minimum_value}")