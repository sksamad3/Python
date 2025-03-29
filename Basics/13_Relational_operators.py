# Relational Operators
# These operators always evaluates to a boolean value. No matter what the operand's data type is
# These operators always provide boolean results.
#   <    - Less than
#   <=   - Less than or equal to
#   >    - Greater than
#   >=   - Greater than or equal to

x = 10
y = 20

print(x<y)
print(x<=y)
print(x>y)
print(x>=y)

# Relational operators are also used for negative numbers
a = -10
b = True
print("Is a > b ? : ",a > b)

# When Strings are compared using comparison operators then
# Python actually compares the Unicode Integers / value of the characters
# and returns a boolean value based on the evalution.

g = 'Python'
h = 'Pythor'

print("g > h ? : ",g>h) # Result : False
# String Python gets compared with Pythor word by word
# First 'P' is compared with 'P' , their ASCII value is compared if they are same
# then the next character is scanned
# we can see that the last characters are different
# r gets compared 'n', since ascii value of r is greater than n , so Pythor is greater than Python , and result is False

# To know the ASCII value of a character
# In python we can use ord() function
cx = 'P'
cy = 'Q'

print("ASCII value of P : ",ord(cx))
print("ASCII value of Q : ",ord(cy))

print("P > Q : ",('P'>'Q'))
# Note : Python doesn't allow comparing string with integers , it will throw error if done so.

# Equality Operators in Python
# ==  - (Checks whether two values are equal )
# !=  -  (Checks whether two values are not equal , returns true if two values are not equal otherwise returns false
# We can use boolean operators on int , float , boolean , string
# The equality opeators can also be used between strings and integers
# But relational and comparison operators cannot be applied between strings and integers

a1 = 10
a2 = 10
print("10 == 10 : ? ",(a1 == a2)) # Returns true


a1 = 102
a2 = 1032
print("102 != 1032: ? ",(a1 != a2)) # Prints True


a1 = 10
a2 = True
print("10 == True : ? ",(a1 == a2))

a1 = 10
a2 = 10.0
print("10 == 10.0 : ? ",(a1 == a2))

a1 = 1
a2 = True
# Internally true is represented as 1  , so output is true
print("1 == True : ? ",(a1 == a2))

a1 = "hello"
a2 = True
print(" hello == True : ? ",(a1 == a2)) # Python don't convert strings to boolean when using == , so python directly returns false


a1 = "Hello"
a2 = "Python"
print("'Hello' == 'Python' : ? ",(a1 == a2))

a1 = "Hello"
a2 = "Hello"
# Prints true because strings exactly matching
print("'Hello' == 'Python' : ? ",(a1 == a2))

a1 = "Python"
a2 = "python"
# Python compares strings character by character so, so false
print("'Python' == 'python' : ? ",(a1 == a2))


# This will print false because at first , 10 is not equal to 20 , so false
print("10 == 20 == 30 == 40 : ? ",10 == 20 == 30 == 40 )

# This will return true
print("10 != 20 != 30 != 40 : ? ",10 != 20 != 30 != 40)

print("10 < 20 != 30 < 40 : ? ",10 < 20 != 30 < 40)