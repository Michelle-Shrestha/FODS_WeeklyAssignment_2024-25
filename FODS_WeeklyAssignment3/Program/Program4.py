#4. Implement a program to read a CSV file and display its contents in a tabular format

import csv

file_name = input('Enter the name of your file: ')

try:
  with open(file_name,'r')as file: #opens the file in read mode
    reader = csv.reader(file)  #reads the content row by row
    print ("\nThe content of the CSV file: ")

    for row in reader:
         #for tabular formatting
         print('\t'.join(row)) #Row are printed separated by tabs 

except FileNotFoundError:
   print("The file does not exist")

except Exception as e:
   print (f"The error is : {e}")