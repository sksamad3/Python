# Boolean data type in python supports two values
# True and False
# True and False are keywords in Python that starts with Upper case characters
x = True
print("Type of x : ",type(x))
print(x)


# Let's have a close look on types of variables
a = 10
b = 20
c = a > b  # c will store boolean (True or False) because an expression returns True or False
print("Type of a : ",type(a))
print("Type of b : ",type(b))
print("Type of c : ",type(c))
print(c) # This prints "False"


# Now we will look at None Data Type in Python
# 1. None in python means no value is associated
# None is a special data type in Python.
# It is represented by the class NoneType and is used to indicate the absence of a value or a null value
# None is also an object in Python of NoneType class

g = 10  # Type of g is int , means g is pointing to Int
print("Type of g : ",type(g))
g = None # Type of g now is NoneType
print("Now type of g : ",type(g))
print(g) # This prints None


# print() function in python doesn't return any value
a1 = 10
print(a1) # this will print the value of a1 as 10


a2 = print(a1)
print(a2) # This is display none , because print will not return any value and None will be stored in a2 variable.
# Any number of variables in python pointing to None will have only one object in memory


d = None
h = None
i = None

# They will point to same address location
# This means , only one object is created in memory of None type from NoneType class
print("Address of d : ",id(d))
print("Address of h : ",id(h))
print("Address of i : ",id(i))