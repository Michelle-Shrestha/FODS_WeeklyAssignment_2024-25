#9. Write a function called add_daily_temp that is given a (possibly empty) dictionary meant to hold the average daily temperature
#  for each day of the week, a temperature value, and the day of the week for the recorded temperature. 
# The function should then add the temperature to the dictionary only if it does not already contain a temperature for that day.
#  The function should return the resulting dictionary, whether it is updated or not.

#Creating function with 3 parameters
def add_daily_temp(temp_dict, temperature, day):
    if day not in temp_dict:
        temp_dict[day] = [temperature] #add the particular day to temp_dict
    return temp_dict #return the updated temp_dict

#Dictionary with some initial temperature value
temp_week = {'Sunday' : 20,'Tuesday':21, 'Thursday':22 }


temp_week = add_daily_temp(temp_week,26,'Sunday') #passing the arguments
temp_week = add_daily_temp(temp_week,27,'Friday')
temp_week = add_daily_temp(temp_week,27,'Wednesday')
print(temp_week)
