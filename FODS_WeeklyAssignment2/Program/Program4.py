#4. Write a function to accept a list of names and return the sorted order of names back.

def lst_name (name):
    name_lst= name.split(",") #Converts the string into a list whenever comma appears
    name_lst= [name.strip() for name in name_lst] #removes whitespace
    #strip() method is applied to all names in the list before sorting them
    return sorted(name_lst)

names= input ("Enter names sparated by commas : ")
print(lst_name(names))