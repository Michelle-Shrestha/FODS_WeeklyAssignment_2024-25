#.10.  Write a function named get_daily_temps that prompts the user for the average temperature 
# for each day of the week and returns a dictionary containing the information the user entered.

def daily_temp():
  temperature = {}#creating empty dictionary to store values later
  i = 0
  for i in range (7):#iterates 7 times 0-6
    day = input ("Enter the day of the week : ").capitalize()
    temp = float(input(f" Enter the average temperature of {day} : "))
    temperature[day]= temp # this line indicates day as a key and temp as its vaule in temperature dictionary
  return temperature 
temp = daily_temp()
print (f"The daily temeratures are : {temp}")