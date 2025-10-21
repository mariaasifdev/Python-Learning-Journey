# Data Types:
# 01 Integers are basically number --> 30,40,60,2,3
# 02 Strings are basically numbers or anything which comes inside the single quotation--> '30' or Double quotation--> "Maria"
# 03 Floating point numbers are basically decimal numbers--> 30.7, 40.8, 3.2
# 04 Boolean are basically True or False
# 05 None are basically special data types which represents "nothing" or "no value at all"

# Built-in Data Types --> data type is an important concept. Variables can store data of different types, and different types can do different things.

# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview
# None Type:	    NoneType

# You can get the data type of any object by using type() function

x = 3.5
y = "Maria"
z = True
a = 30

# print(type(x))  # Output: <class 'float'>
# print(type(y))  # Output: <class 'string/str'>
# print(type(z))  # Output: <class 'Boolean/bool'>
# print(type(a))  # Output: <class 'Integer/int'>

data = "Some info"   # None Example, now data variable has assign some info, but what if we want clear that info than what we will do, ofcourse we use none.
data = None  # Now what will happen, simple this new assign value will replace the previous assign value, now the output will be None
# # print(data)  # Output: Some info
# # print(data)  # Output: None


# # Setting the Data Type
# # In Python, the data type is set when you assign a value to a variable:

x = frozenset({"apple", "banana", "cherry"})  # frozenset() = a read-only set-Use it when you want a fixed group of unique items that can’t be modified.
# # print(x)

x1 = b"Hello"		
x2 = bytearray(5)		
x3 = memoryview(bytes(5))

# print(x1)  # Output: b'Hello' --> is not a normal string — it’s the binary version of "Hello".
# print(x2)
# print(x3)
# # print(x3.tolist())

# # | Variable                             | Output              | Meaning                           |
# # | ------------------------------------ | ------------------- | --------------------------------- |
# # | `b'Hello'`                           | raw bytes           | immutable binary data             |
# # | `bytearray(b'\x00\x00\x00\x00\x00')` | mutable binary data | can be edited                     |
# # | `<memory at 0x...>`                  | memory view         | a pointer to data without copying |




x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))


import random

# print(random.randrange(1, 10))

complex = 3 = 2j
a = int(complex)
# print(type(a)) # shows error--> Because we can't convert complex into any number type.


