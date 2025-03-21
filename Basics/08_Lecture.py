# Data Types in Python
# int      - Number
# float    - Number
# complex  - Number
# bool     - Boolean
# str      - String
# list
# tuple
# set
# dictionary
# frozenset
# bytes
# bytearray
# None
# range

# Variables in Python
my_var = 10

# Updating my_var
my_var = 20


# Pointing to same location
a = 34
b = a  # a and b points to same location and value 20
print("Address of a : ",id(a))
print("Address of b : ",id(b))


# Static Vs Dynamic programming languages
# Statically Typed languages : c , c++ , java , in this type of data needs to be explicitly mentioned
# Dynamically Typed languages : python , type of data is determined during runtime.

# Everything in python is an object
# What are objects :
# Objects are instance of a class that have their own identity , state and behaviour
# Identity : They have unique memory address
# State : They have their own variables and data
# Behaviour : Defined by function ex. sum()


x = 10  # 10 is an object of class int , and x is the reference variable pointing at address of 10
print("Type of 10 : ",type(x))
print("Address of x : ",id(x))
print("Value of x : ",x)



a1 = 5
a2 = 10.53
a3 = "Hello"
print(type(a1))
print(type(a2))
print(type(a3))

# Assign values to variables
p , q , r = 10 , 20 , 30



# Keywords in Python
# Keywords are reserved words in Python
# Reserved words have a predefined meaning in any programming language
# They are used to define syntax and structure in Python Language
# They cannot be used to define any identifier such as variable name , function name , or class name
# True , False and None are keywords that start from capital letters rest all keywords begin with small letters

# Listing all keywords
import keyword
print(keyword.kwlist)



# Comments in Python

# Hash (#) is used to comment statement in Python
# When # hash is encountered , python will ignore the comment
# There is no concept of multi line comment in python
# To comment multiple lines  ,each line has to be commented individually using hash
# Though triple quoted strings are provided in python, but its used as documentation string and not a comment

