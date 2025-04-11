#7 Write a program that prompts the user to enter a list of names and store them in a list. 
# The program should display how many times the letter 'a appears within the list.

name_List = []
name = input("Enter the names separated by comma : ")
names= name.split(",") #Separating the name by comma to make a list
for word in names:
    name_List.append(word) #appending each name in list 
#Checking how many times a appeared
a_count = 0
for a in name_List:
    a_count += a.lower().count('a')
#OR #a_count= sum(word.a().count('a')for a in name_List)

print (f"The names are : {name_List}")
print (f"The letter 'a' appeared {a_count} times ")