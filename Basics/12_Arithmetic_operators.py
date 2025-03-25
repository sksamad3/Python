# Arithmetic Operators
# There are 7 Arithmetic Operators in Python
#  + (Addition)
#  - (Subtraction)
#  * (Multiplication)
#  / (Division)
#  % (Modulus)
#  // (Integer Division / Floor Division )
#  ** (Exponential)


# IF the operators are among + , - , * (Addition , subtraction , multiplication)
# AND IF both the operands are integer then result will be integer
# AND IF any of the operands are float then result is float 

# Operand 1     Operator   Operand 2   Result
#   int            +         int      | int
#   int            -         int      | int
#   int             *         int     | int
#  float       (+,-,*,/)     int      | float
#  int         (+,-,*,/)      float   | float

# Python also prints negative results
print(10 +20) # Result : Integer
print(20-10)  # Result : Integer
print(20*10) # Result : Integer e

print(10 + 2.2) # Result is Float
print(10 - 2.5) # Result is Float
print(5 * 5.5) # Result is Float



# Division Operator
# The result of the division operator is always float even if both the operands are integer
print("Division Operation")
print(20 / 5) # Result of division is always float


# Modulus Operator
# This operator returns the remainder of the division
# IF both the operands are integer then the result is also integer
# IF any of the operand is a float then the result is also float
print("Modulo Operator")
print(14.75 % 4) # Returns float result


# Exponential Operator
# IF the type of both the operands are integer then the result is integer
# AND IF the type of any of the operand is float then the result will be float
# This operator is used to perform power  / raise to kind of operations
print("Exponential Operator ")
a =  2 ** 3  # This is nothing but 3 to the power 2 , or 2^3 ,  3 raised to 2
print(a)

print(3.5**2)


# Floor and Ceil Operations
# Consider an integer 10.25 , Ceil Operation performed on this integer will
# give a number greater than it . 10.25 --> 11

# Consider an integer 10.25 , Floor Operation performed on this integer will
# give a greatest number less than or equal to that number
# 10.25 -->  10 , as 10 is the greatest value less than or equal to 10.25

#    11       - Ceil
#   10.25
#    10      -  Floor


# Floor Division Operator
# In floor division operation , first the normal division is applied and then floor is applied to the result
#  ( 15 // 4 ) - the result will be 3.75 and then its floor will be 3 , so the result is 3

# IF any of the operand is float then the result of floor division will also be float
# (15.4 // 4 )  =  3.875 , then its floor will be 3 ;
j = 15.4// 4  # Output 3.0
k = 15 // 4 # Output 3
print("Value of j : ",j)
print(print("Hello"))

# We can also perform floor division on negative numbers
print(-5 // 2 )  # Prints the -3  , because normal division gives -2.5 and its floor will be -3

