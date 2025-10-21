t = ("apple", "orange", "grapes")   # Tuples are orderd and unchangeable and allow duplicate values.
print(t)  # Return --> ('apple', 'orange', 'grapes')
print(type(t))    # Return --> <class 'tuple'>

t1 = ("apple", "orange", "grapes", "apple")
print(t1)  # Return --> ('apple', 'orange', 'grapes', 'apple')
print(len(t1))  # Return --> 4

# If we wanted to create tuple with one item, we must put "," at the end of that tuple or else python will not recognize it.
tuple1 = ("cherry",)  # Recognize as tuple
print(type(tuple1))  # Return -->  <class 'tuple'>

tuple2 = ("cherry")  # Python will not recognize
print(type(tuple2))  # Return -->  <class 'str'>

# Tuple items - Data types
tu = ("apple", "cherry")  # using data type string as tuple items
tu1 = (2, 4, 5)   # using data type integer as tuple items
tu2 = (True, False)  # using data type boolean as tuple items
print(type(tu))   # Return -->  <class 'tuple'>
print(type(tu1))  # Return -->  <class 'tuple'>
print(type(tu2))  # Return -->  <class 'tuple'>

# One single tuple can also contain different data types
tup = ("maria", 34, True)
print(type(tup))  # Return --> <class 'tuple'>

# Tuple() constructor to create tuples
tup1 = tuple(("maria", 34, True))
print(tup1) #Return --> ('maria', 34, True)

# We can access tuples items by refering to the index inside the square brackets
t2 = ("maria", "bia", 56, True)
print(t2[3])  # Return --> True -- index 3 which is item true

# Lets do negative indexing which apply from right to left
t3 = ("maria", "bia", 56, True)
print(t3[-3])  # Return --> bia -- which in index (-3)

# We can also specify the range of indexing like from where it will start and where to end
t3 = ("maria", "bia", 56, True)
print(t3[1:3])  # Return --> ('bia', 56) -- The search will start at index 2 (included) and end at index 3 (not included).

t4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t4[:5])  # Return --> ('apple', 'banana', 'cherry', 'orange', 'kiwi') -- start searching from index 0 and end at 5 (melon --> not included)

t5 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t5[2:])  # Return --> ('cherry', 'orange', 'kiwi', 'melon', 'mango') -- start searching from index 2 and than print the whole tuple becuase we didn't specify the end.

t6 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t6[-5:-2])  # Return --> ('cherry', 'orange', 'kiwi') -- start searching from index -5 and end at -2 (melon --> not included)

# Lets check if items exist in tuple or not
t7 = ("apple", "maria")
if "maria" in t7:
    print("Yes, its present")  # Return --> Yes, its present

# lets say we wanted to change tuple values, but we can't do that, the reason is tuples are immutable and unchangeable, now what we can do because we really wanted to change values, so here is the solution:

x = ("apple", "maria")  # Tuple
y = list(x)  # we convert tuple into x by using conversion method
y[1] = "bia" # we change the index 1 item with maria
x = tuple(y) # after done changes in list, now we convert x back to its orignal form
print(x)  # Return --> ('apple', 'bia')
print(type(x))  # Return --> <class 'tuple'>  -- ta daaa, here we go we change the item in tuple without getting error.

# For adding items, we use the same method
x1 = ("apple", "maria")  # Tuple
y1 = list(x1)  # we convert tuple into x by using conversion method
y1.append("bia") # we add the bia at the end
x1 = tuple(y1) # after done changes in list, now we convert x back to its orignal form
print(x1)  # Return --> ('apple', 'maria', 'bia')
print(type(x1))  # Return --> <class 'tuple'>  -- ta daaa, here we go we add the item in tuple without getting error.

# Adding tuple to a tuple --> we are allowed to do this:
z = ("maria", "bia")
a = ("anaya",)  # addng coma at the end of the single item is must to avoid error
z += a
print(z)  # Return --> ('maria', 'bia', 'anaya')

# Removing tuple with same method
b = ("apple", "orange", "mango")
c = list(b)
c.remove("mango")
b = tuple(c)
print(b)  # Return --> ('apple', 'orange')

# deleting tuple
d = ("mango", "orange")
del d
# print(d)  # raise an error becuase tuple no longer exist

# Unpacking tuple --> normally, when we create a tuple, we assign values to it which is called packing --> but, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
fruits = ("mango", "orange", "grapes")
(x, y, z) = fruits  # extracting the values back in to variables
print(x) # Return --> mango
print(y) # Return --> orange
print(z) # Return --> grapes

# Using Asterisk *  --> If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits1 = ("mango", "orange", "grapes", "kiwi", "cherry")
(a, b, *c) = fruits1  # extracting the values back in to variables
print(a) # Return --> mango
print(b) # Return --> orange
print(c) # Return --> ['grapes', 'kiwi', 'cherry'] --> values assign as a list to variable c

# Loop through tuples
e = ("maria", "bia")
for x in e:
    print(x)  # Return -->  maria and bia --> 1 by 1

# Loop Through the Index Numbers
f = ("maria", "bia")
for i in range(len(f)):  # range means 0,1,2 and len means length of the tuple
    print(f[i])   # Return -->  maria and bia --> 1 by 1

# Using a While Loop
g = ("mango", "34", "basketball", "56", "word")
i = 0
while i < len(g):
    print(g[i])  # Return --> mango, 34, basketball, 56 and word --> 1 by 1
    i += 1   # increase the index by 1 after each iteration

# Joining tuples using +, * operators
h = ("maria",)
i = ("bia",)
j = h + i
print(j)  # Return --> ('maria', 'bia')

k = h * 2
print(k)  # Return --> ('maria', 'maria')

# Built-in methods
l = ("56", "34", "56", "45", "125", "56")
m = l.count("56")  # Returns the number of times a specified value occurs in a tuple
print(m)  # Return --> 3 

n = ("78", "maria", "bia", "anaya", "bia")
o = n.index("bia") # Searches the tuple for a specified value and returns the position of where it was found
print(o)  # Return --> 2