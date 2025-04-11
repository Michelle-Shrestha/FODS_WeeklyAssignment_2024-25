Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> name = "Michelle"
>>> unicode_value= []
>>> #empty string to store unicode value of each character
>>> for char in name:
...     #takes each character of string name
...     unicode_value.append(ord(char))
... #ord() fun is used to get unicode for each character
... 
>>> print (unicode_value)
[77, 105, 99, 104, 101, 108, 108, 101]
