#2. Write a program to copy the contents of one file to another.

source= input("Enter the name of source file: ")
destination= input("Enter the name of destination file: ")

try:
  with open (source, 'r') as source_file: #open file and read it as source file
    content = source_file.read() 
    print(content)
    
  with open (destination, 'w') as destination_file: #writes the content in destination filr
    destination_file.write(content)
  print ("You have copied the content of the file successfully")

except FileNotFoundError: #if file not found it prints ...
  print("The file doesnot exist")

except Exception as e: #shows what are the other errors
  print(f"The problem is: {e}")