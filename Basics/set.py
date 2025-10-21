# set --> collection of unordered, unchangeable*, and unindexed --> but we can add and remove new items in it.
s = {"maria", "45", "apple", "peanuts"}
print(s)  # Return --> {'apple', '45', 'maria', 'peanuts'}

# Duplicate items are not allowed
s1 = {"maria", "45", "apple", "peanuts", "maria"}
print(s1)  # Return --> {'apple', '45', 'maria', 'peanuts'} --> Duplicate value will be ignored.

# Value (True, 1) (False, 0) --> will treated as duplicates in sets and will be ignored
s2 = {"maria", "45", "apple", "peanuts", True, 1, 22}
print(s2)  # Return --> {True, 22, 'peanuts', 'maria', 'apple', '45'} -- 1 got ignored

s3 = {"maria", "45", "apple", "peanuts", False, 0, 23}
print(s3)  # Return --> {False, 23, 'peanuts', 'maria', 'apple', '45'} -- 0 got ignored

# Finding length and type of set
s4 = {"apple", "orange", "grapes"}
print(len(s4))  # Return --> 3

# we can store different value of data types in set as well
s5 = {2, 4, 6}
s6 = {"orange", "apple"}
s7 = {True, False}
print(type(s5))   # Return -->  <class 'set'>
print(type(s6))   # Return -->  <class 'set'>
print(type(s7))   # Return -->  <class 'set'>

# also single contain different data types as well
s8 = {True, False, 34, "apple"}
print(type(s8))  # Return -->  <class 'set'>

# using constructor set()
my_set = set(("apple", "orange"))  # must use double - round brackets
print(my_set)  # Return -->  {'orange', 'apple'}

# Access items from sets --> we can't refers to set items through index or any key, so we use for "loop" for this and if we wanted to ask for a specific item, than we use "in"
myset_ = {"orange", "apple", 45}
for x in myset_:
    print(x)  # Return --> orange, 45, apple -- 1 by 1

print("apple" in myset_) # Return --> True
print("banana" in myset_) # Return --> False
print("cherry" not in myset_) # Return --> True

# Adding items to a set --> we can use add() method to add single item and update() method to add multiple items
myset1 = {"orange", "apple", 45}
myset1.add("banana")
print(myset1) # Return --> {'banana', 'orange', 45, 'apple'}

myset1.update(["mango", "grapes", 99])
print(myset1) # Return --> {'banana', 99, 'mango', 'orange', 45, 'grapes', 'apple'} -- The object in update() method must be iterable (like list, tuple, dictionary, etc.)

# Removing items from a set --> we can use remove() and discard() method to remove specific item, pop() method to remove random item and clear() method to empty the set
myset2 = {"orange", "apple", 45, "banana"}
myset2.remove("orange") # If the item to remove does not exist, remove() will raise an error. 
print(myset2) # Return --> {'apple', 'banana', 45}
myset2.discard('apple') # If the item to remove does not exist, discard() will NOT raise an error.
print(myset2) # Return --> {'banana', 45}
myset2.pop() # Removes a random item
print(myset2) # Return --> {45} -- random item got removed
myset2.clear() # Empties the set
print(myset2) # Return --> set() -- empty set
del myset2 # Deletes the set completely
# print(myset2) # This will raise an error as the set is deleted.

# loop items in a set
myset3 = {"orange", "apple", 45, "banana"}
for x in myset3:
    print(x) # Return --> random order of items one by one

# join sets --> we can use union() method or update() method
setA = {"apple", "banana", 45}
setB = {"mango", "grapes", 99}
setC = setA.union(setB)
print(setC) # Return --> {'banana', 'grapes', 99, 'mango', 'apple', 45}
setA.update(setB)
print(setA) # Return --> {'banana', 99, 'mango', 'apple', 45, 'grapes'}

# Join multiple sets
setX = {"a", "b", "c"}
setY = {1, 2, 3}
setZ = {True, False}
setw = setX.union(setY, setZ)
print(setw) # Return --> {False, 'c', 1, 2, 3, 'b', 'a'}

# Using | operator to join sets
setM = {"apple", "banana", 45}
setN = {"mango", "grapes", 99}
setO = setM | setN
print(setO) # Return --> {'apple', 99, 'grapes', 'banana', 45, 'mango'}

# Join set and tuple
setP = {"apple", "banana", 45}
tuple1 = ("mango", "grapes", 99)
setQ = setP.union(tuple1)
print(setQ) # Return --> {99, 'grapes', 'mango', 45, 'banana', 'apple'}

# Intersection of sets --> we can use intersection() method or & operator
setD = {"apple", "banana", 45, "mango"}
setE = {"mango", "grapes", 45, "banana"}
setF = setD.intersection(setE)
print(setF) # Return --> {'banana', 'mango', 45}
setG = setD & setE # & operator only works between two sets
print(setG) # Return --> {'banana', 'mango', 45}

# Intersection update --> keeps only the items that are present in both sets
setH = {"apple", "banana", 45, "mango"}
setI = {"mango", "grapes", 45, "banana"}
setH.intersection_update(setI)
print(setH) # Return --> {'banana', 45, 'mango'}

# Difference and difference_update of sets --> we can use difference() method or - operator
setJ = {"apple", "banana", 45, "mango"}
setK = {"mango", "grapes", 45, "banana"}
setL = setJ.difference(setK)
print(setL) # Return --> {'apple'}
setM = setJ - setK # - operator only works between two sets
print(setM) # Return --> {'apple'}
setJ.difference_update(setK)
print(setJ) # Return --> {'apple'}

# Symmetric difference and symmetric difference update of sets --> we can use symmetric_difference() method or ^ operator
setN = {"apple", "banana", 45, "mango"}
setO = {"mango", "grapes", 45, "banana"}
setP = setN.symmetric_difference(setO)
print(setP) # Return --> {'apple', 'grapes'}
setQ = setN ^ setO # ^ operator only works between two sets
print(setQ) # Return --> {'apple', 'grapes'}
setN.symmetric_difference_update(setO)
print(setN) # Return --> {'apple', 'grapes'}

# Frozen set --> immutable version of set, we cannot add or remove items from it once created.
fset = frozenset({"apple", "banana", 45, "mango"})
print(fset) # Return --> frozenset({'mango', 45, 'banana', 'apple'})
# fset.add("grapes") # This will raise an error as we cannot add items to a frozenset.
# fset.remove("apple") # This will raise an error as we cannot remove items from a frozenset.

# However, we can loop through the items in a frozenset
for item in fset:
    print(item)  # Return --> random order of items one by one

# We can also perform union, intersection, difference, and symmetric difference operations on frozensets
fset1 = frozenset({"apple", "banana", 45})
fset2 = frozenset({"mango", "grapes", 45})
fset3 = fset1.union(fset2)
print(fset3) # Return --> frozenset({'banana', 'grapes', 45, 'mango', 'apple'})
fset4 = fset1.intersection(fset2)
print(fset4) # Return --> frozenset({45})
fset5 = fset1.difference(fset2)
print(fset5) # Return --> frozenset({'apple', 'banana'})
fset6 = fset1.symmetric_difference(fset2)
print(fset6) # Return --> frozenset({'grapes', 'banana', 'apple', 'mango'})

# Frozenset supports all non-modifying operations that a normal set does.
# Python has a built-in set of methods that can be used with sets and frozensets.
print(dir(set))  # List all methods available for set
print(dir(frozenset))  # List all methods available for frozenset

