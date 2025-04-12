#1. Write a program to count the number of lines, words, and characters in a text file.

#opening file in read mode
f= open("program1.txt", 'r')
#counting the length of lines
lines = len(f.readlines())
print('Total number of line:', lines)

#the readline moved the pointer to end of file
f.seek(0) #to move pointer at first
word_count= 0
line = f.read() #reading the entire content and stores in variable data
words = line.split() #splits words at every whitespace
#iterating over every element of words 
for word in words:
  word_count+=1
print(f"The total number of word:{word_count}")

#to print count of character
ch_count = 0
for ch in line: #iterate over each character
  ch_count+=1
print(f"The total number of character: {ch_count}")
f.close()