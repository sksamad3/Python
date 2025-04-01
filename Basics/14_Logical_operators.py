# Logical Operators in Python
# Logical operators are used to combine multiple conditions and return True or False based on their evaluation.
# The Operands when using Logical operators are always boolean

# Note :
# 1. If the operands are boolean in an expression using logical operators then output will always be a boolean value
# 2. IF the operands are Non-boolean in an expression using logical operators then output will always be a Non-boolean value


# Types of Logical Operators


# 1. and operator
# Returns True only if both conditions are True.
# If any one condition is False, the result is False.


# 1st Operand     2nd Operand   Result
#    True            True         True
#    True            False        False
#    False           True         False
#    False           False        False



# 2. Logical or Operator
# Returns True if at least one condition is True.
# Returns False only if both conditions are False.

# 1st Operand     2nd Operand   Result
#    True            True         True
#    True            False        True
#    False           True         True
#    False           False        False



# 3. Logical not Operator
# Logical not operator is a unary operator that works only on single operand
# Negates the condition (converts True → False and False → True).

#    Operand        Result
#    True            False
#    False           True


# Logical not operator on Non-boolean Operands
# If the operands of logical operators are int , float , string , then the output is also not a boolean.
# To understand this , first we need to understand about truthy and falsy .


# 1. Truthy
# Any non-zero number , and non-empty string , any non-empty array , non-empty tuple , list are considered truthy value
# Any value that is not falsy is truthy.
# Non-zero numbers (1, -10, 3.14)
# Non-empty strings ("Python", "Hello")
# Non-empty collections ([1,2,3], {"key": "value"}, (1,2))
# True

# Example :
# 20 is a truthy value
# 0 is not a truthy value
# "" is not a truthy value , because the string is empty
# "Hello" is a truthy value , because the string is non empty
# (1, 2, 3 ,4) is a truthy  , because the tuple is non-empty and contains values
# To check whether the nature of anything is truthy of falsy , we can use bool() function

print("10 is Truthy or Falsy : ",bool(10))
print("0 is Truthy or Falsy : ",bool(0))
print("'hello' is Truthy or Falsy : ",bool('hello'))
print("'' is Truthy or Falsy : ",bool(''))


# 2. Falsy
# Any zero number , and empty string , any empty array , empty tuple , list are considered Falsy values
# Any value that is not Truthy is falsy.
# Example

# Falsy Values                   Reason
# None	                    Represents "nothing"
# False	                    Boolean False
# 0 (zero)	                Integer zero
# 0.0 (zero)	            Floating-point zero
# "" (empty string)	        Strings with no characters
# [] (empty list)	        Lists with no elements
# {} (empty dictionary)     Dict with no key-value pairs
# set() (empty set)	        Empty set
# () (empty tuple)	        Tuple with no elements


# Logical Operators on Non-Boolean Values
# 1. and Operator
# And evaluates from left to right.
# If it finds a falsy value, it stops immediately and returns that value.
# If all operands are truthy, it returns the last operand.
print(0 and 10)       # Output: 0 (First falsy, stops here)
print("" and "Hello") # Output: "" (First falsy, stops here)
print(None and 100)   # Output: None (First falsy, stops here)
print("Hello" and 10) # Output: 10 (Se

# 2. or Operator
# Returns the first truthy value encountered.
# If all values are falsy, it returns the last falsy value.
# Evaluates from left to right and stops as soon as a truthy value is found.
print("" or 10)        # Output : 10 (First truthy , stops here
print(10 or 20)        # Output: 10 (First truthy, returned immediately)
print("" or "Python")  # Output: "Python" (First falsy, moves to second)
print(None or 100)     # Output: 100 (First falsy, moves to second)

# More examples
print(not 10) # Output : False , because 10 is a true value and its opposite is false
print(not 0)  # Output : True , because 0 is a falsy value and its opposite is True
print(not "") # Output : True , because "" is an empty string and its false , so opp. of false is true
print(not "p") # Output : False , because , "p" is a non empty string and its considered true , but its opposite is false due to not operator



# Difference Between and & or
# and	- Returns First falsy value, or last truthy if all are truthy
# or	- First truthy value, or last falsy if all are falsy


# More Practical from Instructor
# and - Returns First falsy value, or last truthy if all are truthy
# Logical operators on Boolean values
print(" ")
print(" ")
print("AND Operator ")
x = True
y = True

print("True and True : ",x and y) # Output : True

x = True
y = False

print("True and False : ",x and y) # Output : False


x = False
y = True

print("False and True : ",x and y) # Output : False

x = False
y = False

print("False and False : ",x and y) # Output : True


# or Operator
# or Operator - First truthy value, or last falsy if all are falsy
print(" ")
print(" ")

print("OR Operator ")
x = True
y = True

print("True or True : ",x or y) # Output : True

x = True
y = False

print("True or False : ",x or y) # Output : True

x = False
y = True

print("False or True : ",x or y) # Output : True

x = False
y = False

print("False or False : ",x or y) # Output : True

# Not operator
print(" ")
print(" ")

print("Not Operator ")
x = True
print("not x : ", not x)

x = False
print("not y : ", not x)

# More examples
print(not 10) # Output : False , because 10 is a true value and its opposite is false
print(not 0)  # Output : True , because 0 is a falsy value and its opposite is True
print(not "") # Output : True , because "" is an empty string and its false , so opp. of false is true
print(not "p") # Output : False , because , "p" is a non empty string and its considered true , but its opposite is false due to not operator



