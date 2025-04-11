#12. Create two sets:
#set1 = {20, 40, 60}
#set2 = {10, 20, 30, 40, 50, 60}
#(a) Write code to perform a union of these sets. Print the length of the resulting set.
#(b) Write code to perform an intersection of set1 and set2.
#(c) Write code to compute the symmetric difference between set1 and set2
#(d) Write code to add the value 40 to set1, did the set change?
#(e) Write code to remove value 20 from set2

set1 = {20,40,60}
set2 = {10,20,30,40,50,60}

union_set = set1.union(set2) #can also use set1 | set2 ("|" is an union operator)
union_set_length = len(union_set)
print(f"The union of set 1 and set2: {union_set}")
print(f"Length of the union set: {union_set_length}")

intersection_set = set1 & set2 # "&" is an intersection operator
print (f"The intersection of set1 and set2: {intersection_set}")

symmetric_difference_set = set1 ^ set2 # "^" is a symmetric difference operator
print(f"The symmetric difference between set1 and set2: {symmetric_difference_set}")

set1.add(40)
print(f"Set1 after adding 40: {set1}")
print("The set didn't changed after adding 40 because set stores unique value")

set2.remove(20)
print(f"Set2 after removing 20: {set2}")