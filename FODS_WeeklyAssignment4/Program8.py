#8. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

import pandas as pd
import numpy as np

a = pd.Series([1,2,3,4,5])
b = pd.Series([6,7,8,9,10])
print (f"The sum is:\n{a+b}\n")
print (f"The subtraction is:\n{a-b} \n")
print (f"The multiple is: \n{a*b} \n")
print (f"The quotient is: \n{a/b}")