# The input taken from the user using input function is always a string
# The type of input is string
# x = input("Enter the value of x : ")

# print(x) # Print the value as text
# print(type(x)) # Output : <class 'str'>


#a = input("Enter a : ")
# b = input("Enter b : ")

#The input function is returning string and the result of a and b are concatenated
# print(a+b) #Output : 1020

# So to perform arithmetic addition , we will have to convert the data type of input
#g = input("Enter a number : ")
#h = input("Enter another number : ")

# we can also use float() to convert into floats
#print("Sum is : ",int(g) + int(h))
# print("Sum is : ",float(g) + float(h))


# eval() Function
# But what if we have mixed type of number then we can use eval() function
# The eval() function evaluates a string as a Python expression and returns the result.
# It extracts the key variables , operators and perform operation , returning the required result


# The eval() function implicitly converts the value of the variables to their respective data types

expr = "10 + 5 * 2 "
print("10 + 5 * 2 : ",eval(expr))

v = input("Enter a no. : ")
w = input("Enter another no. : ")

# even if a user enters a float and an int value , the addition will be performed on nos due to eval function.
# So if v was entered an int value and w was entered a float value , the addition will still be performed

print("Sum is : ", eval(v) + eval(w))