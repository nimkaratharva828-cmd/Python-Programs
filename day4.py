price__ = 103.40

print(price__)


#How to import all keywords in Python
import keyword
print(keyword.kwlist)

keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 
 'async', 'await', 'break', 'class', 'continue', 
 'def', 'del', 'elif', 'else', 'except', 'finally', 
 'for', 'from', 'global', 'if', 'import', 
 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
 'pass', 'raise', 
 'return', 'try', 'while', 'with', 'yield']

print("Total keywords in python: ",len(keywords))


#How import function works

# import day2
# print("Total Marks: ", day2.total)
# print("Percentage is: ",day2.percentage)

from day2 import total,percentage  # from day2 import *
print("Total Marks: ", total)
print("Percentage is: ",percentage)

import this