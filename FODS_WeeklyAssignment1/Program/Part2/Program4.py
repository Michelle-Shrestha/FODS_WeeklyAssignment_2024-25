#Write a program to find the Euclidean distance between two coordinates.
#  Take both the coordinates from the user as input.

import math
x1= int (input("Enter the value of x1 coordinate : " ))
x2= int (input("Enter the value of x2 coordinate : "))
y1= int (input("Enter the value of y1 coordinate : "))
y2= int (input("Enter the value of y2 coordinate : "))
#using euclidean distance formula
ed = math.sqrt(pow((x2-x1),2) + pow((y2-y1),2)) 
ED= round (ed, 5) #printing only 5 decimal placesS
print ("The Euclidean Distance of the given coordinates is ", ED)