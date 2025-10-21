# Arithmetic Operators--> used to perform mathematical operations.

# name            # Operators
# Addition               +
# Subtraction            -
# Multiplication         *
# Division               /
# Exponential            **
# Modulus                %
# Floor Division         //

a = 30
b = 35

# print(a + b)  # Output: 65
# print(a - b)  # Output: -5
# print(a * b)  # Output: 1050
# print(a / b)  # Output: 0.8571428571428571
# print(a ** 2)  # Output: 900--> This means raise 30 to the power of 2 (** = power)
# print(a % b)  # Output: 30--> The modulus operator gives the remainder when one number is divided by another.
# print(a // b)  # Output: 0--> The floor division operator divides two numbers and gives the whole number part (it drops anything after the decimal — no rounding).


# Assignment Operators
# Name       Evaluated As
# =          a=b
# +=         a += b or a = a + b
# -=         a -= b or a = a - b
# *=         a *= b or a = a * b
# **=        a **= b or a = a ** b
# /=         a /= b or a = a / b
# //=        a //= b or a = a // b
# %=         a %= b or a = a % b
# &=         a &= b or a = a & b
# **          =**
# ^=         a ^= b or a = a ^ b
# >>=        a >>= b or a = a >> b
# <<=        a <<= b or a = a << b

a = 3
b = 9

# a = b  # Output: 9
# a += b # Output: 12 
# a -= b  # Output: -6
# a *= b  # Output: 27
# a **= b # Output: 19683
# a /= b  # Output: 0.3333
# a //= b # Output: 0
# a %= b  # Output: 3
# a &= b  # Output: 1   &= means: take the bits of a and b, compare them, keep only the bits that are 1 in both, and then save that result back into a.
# # a ^= b  # Output: 10-->   a = 3 → 0011
#                             b = 9 → 1001
#                           ----------------
#                             a ^ b → 1010         It’s a bitwise XOR (exclusive OR)

# a <<= b # Output: 1536 
# # a << b  =  3 × (2 ** 9)
#          =  3 × 512
#          =  1536
      
# | Operation | Meaning         | Math    | Result   |
# | --------- | --------------- | ------- | -------- |
# | a << 1    | shift left by 1 | 3 × 2   | 6        |
# | a << 2    | shift left by 2 | 3 × 4   | 12       |
# | a << 9    | shift left by 9 | 3 × 512 | 1536     |


# a >>= b # Output: 0

# Right Shift (>>)
# Moves bits to the right
# Each shift = divide by 2 (and keep only the whole part)
# 12 >> 1   # 12 ÷ 2 = 6
# 12 >> 2   # 12 ÷ 4 = 3
# 12 >> 3   # 12 ÷ 8 = 1


# print(a)  

# Bitwise operators --> Bitwise operators are used to deal with binary operations.

# Name	              Operator	Example
# Bitwise--AND	         &	     a & b     # Already explain above
# Bitwise--OR	         |	     a | b
# Bitwise--NOT	         ~	     ~a
# Bitwise--XOR	         ^	     a ^ b     # Already explain above
# Bitwise--right shift	 >>	     a>>       # Already explain above
# Bitwise--left shift	 <<	     b<<       # Already explain above

a = 2
b = 3

# a1 = a | b  # Output: 3 --> (|) is the bitwise OR operator. It compares the bits (1s and 0s) of two numbers, bit by bit, and sets the result bit to 1 if either bit is 1.

# | Bit 1 | Bit 2 | Result |
# | ----- | ----- | ------ |
# | 0     | 0     | 0      |
# | 0     | 1     | 1      |
# | 1     | 0     | 1      |
# | 1     | 1     | 1      |


a2 = ~a  # Output: -3

# ~2 = -(2 + 1) = -3
# ~3 = -(3 + 1) = -4
# ~0 = -(0 + 1) = -1

# print(a1)
# print(a2)

# Comparison operators--> These operators are used to compare values.

# Name	                     Operator	Example
# Equal	                        ==	     a==b
# Not Equal	                    !=	     a!=b
# Less Than	                    <	     a<b
# Greater Than	                >	     a>b
# Less Than or Equal to	        <=	     a<=b
# Greater Than or Equal to	    >=	     a>=b

a = 3
b = 3
# print(a==b) #Output: True

a = 3
b = 3
# print(a!=b) #Output: False

a = 3
b = 6
# print(a<b) #Output: True

a = 3
b = 6
# print(a>b) #Output: False

a = 6
b = 6
# print(a<=b) #Output: True

a = 4
b = 6
# print(a>=b) #Output: False

# Identity operators:

# Name	  Example	   Evaluated As
# is	  a is b	   Returns True if a and b are same
# is not  a is not b   Returns True if a and b are not same

a = 3
b = 6
# print(a is b) #Output: False

a = 3
b = 6
# print(a is not b) #Output: True

# Logical operators--> These operators are used to deal with logical operations.

# Name	    Operator	Example
# AND	      and	    a=2 and b=3
# OR	      or	    a=2 or b=3
# NOT	      not	    Not(a=2 or b=3)

a = 3
b = 6
# print(a==2 and b==6) #Output: False --> Return true if both logics true

a = 3
b = 6
# print(a==3 or b==4) #Output: True --> Return true if any-one of the logic is true 

a = 3
b = 6
# print(not(a==3 or b==6)) #Output: False --> Return false if both logics are true

a = 3
b = 6
# print(not(a==3 or b==4)) #Output: False --> Still return false

a = 3
b = 6
# print(not(a==5 or b==4)) #Output: True --> Now, it will return true when both logics are false

# Membership operators:

# Name	     Example	   Evaluated As
# in	     a in b	       Returns True if a is present in given sequence or collection
# not in	 a not in b	   Returns True if a is not present in given sequence or collection

Favourite = "Cake", "Pizza"
add = "Burger"

# print("Cake" in Favourite)   # Output: True
# print("Burger" in Favourite)   # Output: False
# print("Burger" not in Favourite)  # Output: True
# print("Burger" in add)   # Output: True


