fruits = ['apple', '56', 45, True]
nested_l = ["red", "big", "tasty"]
for i in fruits:
    print(i)

# Looping through strings
for x in 'apple':
    print(x)
    # output
    # a
    # p
    # p
    # l
    # e

# Break statements
for x in fruits:
    if x == '56':   # Return --> apple --> loop only run until it reach '56' in the list
        break

for x in fruits:
    if x == '56':   # Return --> apple --> loop only run until it reach '56' in the list
        break
    print(x)    # this will not execute

# Continue statement
for x in fruits:
    if x == 45:       # With the continue statement we can stop the current iteration of the loop, and continue with the next
        continue
    print(x)

# Range function
for i in range(6):
    print(i)       # This loop will run from 0-5

for x in range(2, 10):
    print(x)       # This loop will run from 2-9

for x in range(2, 30, 3):
  print(x)     # Start at 2, go up to (but not including) 30, increasing by 3 each time. --> 2,5,8,11,14,17,20,23,26,29

# Else in for loop
for x in range(6):
    if x == 3: break    # Return --> 0-2
    print(x)
else:
    print("Finished Finally!")     # If the loop breaks, the else block is not executed.

for x in range(6):   # Return --> 0-5
    print(x)
else:
    print("Finished Finally!")

# Nested loop

for x in fruits:
  for y in nested_l:
    print(x, y)
    # Return
    # apple red
    # apple big
    # apple tasty
    # 56 red
    # 56 big
    # 56 tasty
    # 45 red
    # 45 big
    # 45 tasty
    # True red
    # True big
    # True tasty

# Pass statement
for x in range(2, 20):
    pass     # because of this set of code will not executed
