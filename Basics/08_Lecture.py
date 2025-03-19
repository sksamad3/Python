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