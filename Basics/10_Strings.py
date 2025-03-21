# In python
# Strings is a sequence of characters contained within two quotes
# We can use single quotes or double quotes to represent a string

s = "Hello"
print(s)
print(type(s))

x = 'Its good to learn programming '
print(x)

# If i want to print
# It's good to learn programming
# the above string contains single quote , so i need to delimit it with double quotes
# If a string contains - single quotes then delimit it with double quotes
# If a string contains double quotes in it then delimit the string with single quotes.
# Python allows , a string to contain spaces , digits & special characters
# Strings created by single or double quotes are called single line strings


sentence = "Hi , My name is Shaikh Abdul Samad"
# What if I want to have multi line strings
sentence2 = ''' It's good 
               learn to  
               programming '''

print(sentence)
print(sentence2)


# This is also valid
# These triple quotes strings are generally used for documentation purpose.
# These strings are known as documentation strings
sentence3 = """ It's good 
               learn to  
               programming """

# This is also valid
# When a string contains double and single quotes then it should delimited with three times double quotes
sentence4 = '''It is 'good' to "learn" programming'''
print(sentence4)