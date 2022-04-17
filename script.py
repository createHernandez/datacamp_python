# Comments
# Using the hashtag makes everything after it invisible to the compiler. Which can be used to write comments within your code. 
# This is a comment 

# PRINT() function 
# Takes what is between the paratheses and outputs it to the console. 
print (6/3) # 2 

# Modulus operator *
# The operator returns the remainder of the number to the left by the number on its right. 
print(18%7) # 4

# Exponentation operator **
# Takes the number to its left to the power of the number on the right. 
print(4**2) # 16

# Variables 
# They store information that can then be used later in the program. 

# Assigment operator =
# Assigns the value on the right to the variable on the left. 
x = 5 

# Calculations with variables 
x = 5 + x 
print(x) # 10

# Data types or Variable types 
# int is short for integer, a number without a fractional part. 
number = 1 

# float is short for floating point, a number with an integer and fractional part. 
numberTwoPointO = 2.0

# str is short for string, a data type used to represent text by using sing or double quotes. 
stringOne = 'stringOne'
stringTwo = "stringTwo"
# bool is short for boolean, a data type used to represent logical values such as True or False. In Python when assigning the logical value to a bool the capitalized version of true must be used.
bool = True 

# TYPE() function 
# Returns the data type of a value or variable. 
a = 3
type(a) # int 

# STR() function 
# Explicitly converts the type of the variable to a string. 
a = 3
str(a) # 3

# INT() function 
# Explicitly converts the type of the variable to a string. 
int(a) # 3

# FLOAT() function 
# Explicitly converts the type of the variable to a string. 
float(a) # 3.0

# BOOL() function 
# Explicitly converts the type of the variable to a string. 
bool(a) #

# Python doesn't like concatenating strings and intergers or floats together. 

# Lists 
# List declaration 
my_list = [1, 2, 3]

# Python allows for the mixing of data types within a list, including a list of lists. 

# Subsetting Lists 
# You can select a specific element of the list by using the appropriate index. 
# The first element's index is NOT 1, but instead 0. 
my_list = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
my_list[7]  # 1.89
my_list[-1] # 1.89

# List Slicing 
# You can select a consecutive range of elements from the list by using the index of the first element a : and the index of the last element. The start number is inclusive meaning that the choosen index's element is also included in the range. While the end number is exclusive meaning that the choosen index's element is NOT included in the range. 
# ex| my_list[start:end]
my_list[3:5]
