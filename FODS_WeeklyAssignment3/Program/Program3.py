#3. Write a program to find and replace a specific word in a file with another word.

file_name= input('Enter the name of your file: ')
old_word= input('Enter the word that should be replaced: ')
new_word= input('Enter the new word: ')

try: 
  with open (file_name, "r") as file:#opening file in read mode
    content = file.read()

  replaced_word = content.replace(old_word , new_word)#replacing old word by new

  with open (file_name,"w" ) as file: #opening file in write mode
    file.write(replaced_word)
    print("The word replaced successfully")
  
except FileNotFoundError:
  print("The file doesnot exist")

except Exception as e:
  print (f"The problem is {e}")
