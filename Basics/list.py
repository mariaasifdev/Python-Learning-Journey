# We use list to store multiple values in single variable.
a = ["Cake", "Chocolate", "Cherry", "Books"] 
print(a) # Return --> ['Cake', 'Chocolate', 'Cherry', 'Books']

# List item are in orderd form --> (in python list items are already defined in order that we can't changech), changeable, duplicate. Also the List items are indexed, the first item has index [0], the second item has index [1] etc.

b = ["Cake", "Chocolate", "Books", "Cherry", "Books"] # Like here in this list books are written two times
print(b)   # Returns --> ['Cake', 'Chocolate', 'Books', 'Cherry', 'Books']

# By using len(), we can also find the length of the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))  # Return --> 3

# List Items - Data Types --> List items can be of any data type.
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)   # Return --> ['apple', 'banana', 'cherry']
print(list2)   # Return --> [1, 5, 7, 9, 3]
print(list3)   # Return --> [True, False, False]

list4 = ["abc", 34, True, 40, "male"]
print(list4)    # Return -->  ['abc', 34, True, 40, 'male']
# Finding type()
print(type(list4))   # Return --> <class 'list'>

# The list() Constructor

list5 = list(("Apple", "Maria", 40, True))
print(list5)
print(type(list5))

# Access list items

fav = ["Apple", 'Orange', "Juice", 45, True]        # Why, becuase positive indexing start from (0) --> which is from left to right, and negative indexing start from (-1) --> which is from right to left.
print(fav[2:5])  # Return -->  ['Juice', 45, True]
print(fav[0:])  # Return -->  ['Apple', 'Orange', 'Juice', 45, True]
print(fav[:4])  # Return -->  ['Apple', 'Orange', 'Juice', 45] --> 4 number is not included.

# Negative Indexing
print(fav[-4:-1])  # Return --> ['Orange', 'Juice', 45]  --> -1 number is not included

# Check if item exist
print("Apple" in fav)   # Return --> True

# Chenging items from list
fav[1] = "Cookie"  # We said that change orange with cookie --> Return --> ['Apple', 'Cookie', 'Juice', 45, True]
print(fav)

# Chnage range of item values
fav[1:3] = "Biscuit", "Pizza"
print(fav)  # Return --> ['Apple', 'Biscuit', 'Pizza', 45, True] --> it change the value of index 1, 2 and exclude the 3 as always.

# Inserting item.
fav.insert(2, "Cookie") # --> Here, we are saying that insert cookie at index 2
print(fav)  # Return --> ['Apple', 'Biscuit', 'Cookie', 'Pizza', 45, True]

# Adding items to the end of the list by using .append()
fav.append("Football")
print(fav)  # Return --> ['Apple', 'Biscuit', 'Cookie', 'Pizza', 45, True, 'Football']

# Extending the list
most_fav = ["New York", "South Korea"]
fav.extend(most_fav)
print(fav)   # Return --> ['Apple', 'Biscuit', 'Cookie', 'Pizza', 45, True, 'Football', 'New York', 'South Korea']

# Add any iterable --> list,tuples,set,dict
tuple = ('Maria',)
fav.extend(tuple)
print(fav)   # Return --> ['Apple', 'Biscuit', 'Cookie', 'Pizza', 45, True, 'Football', 'New York', 'South Korea', 'Maria']

# Let's remove items from the list
fav.remove("Football") # Return --> ['Apple', 'Biscuit', 'Cookie', 'Pizza', 45, True, 'New York', 'South Korea', 'Maria']
print(fav)

# Removing specified index item from the list by using pop()
fav.pop(2)
print(fav)  # Return --> ['Apple', 'Biscuit', 'Pizza', 45, True, 'New York', 'South Korea', 'Maria'] --> cookie from index 2 is removed from the list.

# we can also delete items from list
del fav[0]
print(fav)   # Return --> ['Biscuit', 'Pizza', 45, True, 'New York', 'South Korea', 'Maria'] --> delete apple which is on index 0.

# We can also clear our list
fav.clear()
print(fav)   # Return --> []

# We can also use loop to print items in the list one by one (for-loop)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)   # Return --> one by one representation of the list.

# It will also work the same as above but here we are loop through index numbers
thislist1 = ["apple", "banana", "cherry"]
for i in range(len(thislist1)):
  print(thislist1[i])

# Using While loop
fav_lis = ["apple", "banana", "cherry"]
i = 0
while i < len(fav_lis):
  print(fav_lis[i])      # The loop keeps repeating as long as the condition is True (i < len(fav_lis)). When it becomes False, the loop stops automatically.
  i = i + 1  

# Loop using list comprehension --> writing shorter syntax
fav_lis1 = ["apple", "banana", "cherry"]
[print(x) for x in fav_lis1]  # Return items one by one 

# List comprehension --> offer a shorter syntax, what if we wanted to create a new list from the existing list, but we want only those items which have "a" in it. 

# Before List Comprehension:
# fruits = ["Apple", "Mango", "Banana", "Cherry", "Biscuit"]
# new_list = []

# for x in fruits:
#   if "a" in x:
#     new_list.append(x)

# print(new_list)   # Return --> ['Mango', 'Banana'] --> Now here, you will see it didn't return Apple in the new list....Why???....Because Apple start with capital A, simple as that, if we wanted it to return value wether its capital and smaller, we have to use this (.lower()) like this:
fruits = ["Apple", "Mango", "Banana", "Cherry", "Biscuit"]
new_list = []

for x in fruits:
  if "a" in x.lower():  # converts both A and a to lowercase
    new_list.append(x)

print(new_list)   # Return --> ['Apple', 'Mango', 'Banana']

# Now using List comprehension:
# Python looks at our list — fruits.
# It starts a loop, saying:
# “Okay, take each item from fruits one by one and temporarily call it x.”
# For each x, it checks:
# “Does this x contain the letter 'a'?”
# If the answer is yes, it adds that x into the new list being created.
# If no, it skips it.
# (Just for better understanding, i wrote all of the above explanation)

fruits_list = ["Apple", "Mango", 'Kiwi', "Cherry", "Banana"]
new_list1 = [x for x in fruits_list if "a" in x.lower()]
print(new_list1)   # Return --> ['Apple', 'Mango', 'Banana']

# Syntax --> newlist = [expression for item in iterable if condition == True]
new_list2 = [x for x in fruits_list if x != "Apple"]
print(new_list2)  # Return --> ['Mango', 'Kiwi', 'Cherry', 'Banana'] --> Only accept items that are not "apple"

newlist3 = [x for x in fruits]
print(newlist3)  # Return --> ['Apple', 'Mango', 'Banana', 'Cherry', 'Biscuit']

# Iterable --> we are using range() here:
newlist4 = [x for x in range(10)]  # Return --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(newlist4)

# Now we give condition as well:
numbers = [x for x in range(10) if x < 5]  # Only accepts numbers lower than 5
print(numbers)  # Return --> [0, 1, 2, 3, 4]

# We use expression as well:
newlist5 = [x.upper() for x in fruits]  # Returns new list with upper case values
print(newlist5)   # Return --> ['APPLE', 'MANGO', 'BANANA', 'CHERRY', 'BISCUIT']

# We can also set the outcome, whatever we like:
newlist6 = ["Hey" for x in fruits]
print(newlist6)  # Return --> ['Hey', 'Hey', 'Hey', 'Hey', 'Hey']

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist7 = [x if x != "Cherry" else "Orange" for x in fruits]
print(newlist7)  # Return --> ['Apple', 'Mango', 'Banana', 'Orange', 'Biscuit']   --> The expression in the example above says: "Return the item if it is not cherry, if it is cherry return orange".

# Sorting list
lis = ["Orange", "Maria", "Bia"]
lis.sort()
print(lis)  # Return --> ['Bia', 'Maria', 'Orange']  --> it will sort the list alphabetically

num = [0,8,4,7,1,9,10]
num.sort()
print(num)  # Return --> [0, 1, 4, 7, 8, 9, 10]

# Sort descending
lis.sort(reverse=True)
print(lis) # Return --> ['Orange', 'Maria', 'Bia']

num.sort(reverse=True)
print(num)  # Return --> [10, 9, 8, 7, 4, 1, 0]

# Customize sort function

def myfunc(n):
  return abs(n - 50)  # Just an example rule

num1 = [2, 345, 56, 90, 0, 34]
num1.sort(key = myfunc)
print(num1) # Return --> [0, 2, 34, 56, 90, 345]

# Case Insensitive Sort --> By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters --> Luckily we can use built-in functions as key functions when sorting a list. So if you want a case-insensitive sort function, use str.lower as a key function:

a = ["kiwi","Orange", 'Maria', "cherry"]
a.sort(key = str.lower)
print(a)   # Return --> ['cherry', 'kiwi', 'Maria', 'Orange'] --> will sort lower case first

# Reverse order
x = [0,1,2,3,4,5,6]
x.reverse()
print(x)  # Return --> [6, 5, 4, 3, 2, 1, 0]

# Copy method
a = [0,1,2,3]
b = a.copy()
print(b)  # Return --> [0, 1, 2, 3]

# We can also use built-in function list()
c = list(a)
print(c)   # Return --> [0, 1, 2, 3]

# We can also copy a list using slice(:) operator
d = a[:]
print(d)  # Return --> [0, 1, 2, 3]

# Join list --> there are several methods to join and concatenate list, but these are the easier ones.

num_1 = [0, 1, 2, 3, 4, 5]
num_2 = [0, 1, 42, 3, 43, 5]
num_3 = num_1 + num_2
# Or if we wanted to sort the list as well
num_3.sort()  # Return --> [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 42, 43]

print(num_3)  # Return --> [0, 1, 2, 3, 4, 5, 0, 1, 42, 3, 43, 5]

# We can also append num_2 into num_1
num_1 = [0, 1, 2, 3, 4, 5]
num_2 = [0, 1, 42, 3, 43, 5]

for x in num_2:
  num_1.append(x)

print(num_1)  # Return --> [0, 1, 2, 3, 4, 5, 0, 1, 42, 3, 43, 5]

# Or we can use extend()
num_1 = [0, 1, 2, 3, 4, 5]
num_2 = [0, 1, 42, 3, 43, 5]
num_1.extend(num_2)

print(num_1) # Return --> [0, 1, 2, 3, 4, 5, 0, 1, 42, 3, 43, 5]

