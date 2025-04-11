#13. Create a function called word_intersection that prompts the user for two English words, 
# and displays which letters the two words have in common.

def word_intersection():
  word1= input("Enter the first english word: ").lower() #lower is used to make case-insensitive
  word2= input("Enter the second english word: ").lower()

  common_letters=""#creating empty string
  for letter in word1:
    #Checking for unique common letters 
    if letter in word2 and letter not in common_letters:
      common_letters+=letter

  return common_letters

common_letter = word_intersection()
print (f"The common letters are : {common_letter}")