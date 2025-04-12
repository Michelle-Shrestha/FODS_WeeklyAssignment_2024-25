#5. Develop a program that counts the occurrence of each word in a file

file_name = input("Enter the name of your file: ")

try: 
    # Open the file in read mode
    with open(file_name, "r") as file:  # Opens the file in read mode
        content = file.read()
    
    content = content.lower()  # Converts the content to lowercase
    words = content.split()  # Splits the content into words
    word_count = {}  #empty dictionary

    # Iterate over each word
    for word in words:
        if word not in word_count:  # Checks if the word is not already in the dictionary
            word_count[word] = 1  # Adds the word with an initial count of 1
        else:
            word_count[word] += 1  # Increments the count for repeated words

    # Print the word counts
    print("\nWords and its occurrence:")
     # Each word ans its count iterates through the dictionary
    for word, count in word_count.items():  #.items() returns key-value pairs as tuples
        fileWord = word
        occurrence = count
        print(f"{fileWord}: {occurrence}")

except FileNotFoundError:
    print("File does not exist.")
except Exception as e:
    print(f"The problem is {e}")