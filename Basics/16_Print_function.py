# print() Function
# The print() function is used to display output in Python.
# It prints values to the console and supports multiple arguments, formatting, and different output control options.
# 1. We can have an argument inside a print() function
# 2. We can pass many arguments inside a print() function
# 3. It's valid even if we don't pass any argument to print() function

# Passing single argument to print() function
print("Hello")

# Passing a single argument to print() function , passing a variable containing a value
x = 10
print(x)

# Passing no arguments to print() Function
print()



# Escape Sequence characters
# Escape sequence characters are special characters used to represent certain whitespace, formatting, or special symbols inside strings in Python.
# They start with a backslash (\) followed by a specific character to perform an action.
# To include special characters like quotes (", ') in strings.
# To insert new lines (\n) or tabs (\t) inside strings.
# To add characters that cannot be typed directly, like Unicode characters.

# 1. To use double quotes
# Print : He said , "Hello"
print("He said , \"Hello\" ")

# 2. Print on new line
# Print : Hello
#       : World
print("Hello \nWorld !")


# 3. Print a tab space
# Print : Hello World !
print("Hello \t World ")

# 4. Print the backslash
# print : C:\Users\John\Documents
print("File Location : C:\\Users\\John\\Documents")

# 5. Carriage Return
# print : Python World
print("Hello World\rPython")

# 6. Backspace
# Print : HellWorld
print("Hello\bWorld")

# 7. Concatenation
# Print : HelloPython
print("Hello"+"Python")

# 8. Repetition
# Print : Python Python Python Python Python
print("Python "*5)

# Printing multiple variables
f = 10
g = 20
h = 30

f1 = '10'
g1 = '20'
h1 = '30'

# Here comma is used to send multiple arguments separately
# By default , the values are displayed seperated by spaces.
# Space is the default separator in print() function
print(f,g,h)
print(f+g+h) # prints 60
print(eval(f1)+eval(g1)+eval(h1)) # prints 60
# print(print(print(print(10))))