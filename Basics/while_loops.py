# With while loop with execute set of statements as long as condition is true. And don't forget to add iteration(i), or else your loop will continue forever.

i = 1
while i < 6:
    print(i)
    i += 1  # Using this is must

# Using break statement
i = 1
while i < 8:
    print(i)
    if i == 4:  # this block of code runs until i == 4 --> this condition
        break   # and here loops break
    i += 1

# Continue statement
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue   # With the continue statement we can stop the current iteration, which is 3 and continue with the next
    print(i)

# Else statement --> we run a set of code, if all the condition didn't come true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6.")