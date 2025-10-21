a = 40
b = 30
if a < b:
    print("Yes")
else:
    print("No")  # Return --> No

number = 90
if number > 0:
    print("yes")  # Return --> Yes

# Indentation(blank space) is very important in if statements because if statement without indentation raise error:
# number = 90
# if number > 0:
# print("yes")   This will raise error

# Multiple statements
age = 27
if age >= 18:
    print("You're an adult")
    print("You can vote")
    print("Very good")   # Will retutn all the statements one by one

# Using Variables in Conditions --> Boolean variables can be used directly in if statements without comparison operators.
logged_in = True
if logged_in:
    print("WelcomeBack")  # Return --> WelcomeBack

# Python can evaluate many types of values as True or False in an if statement. Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True. This includes positive numbers (5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string).

a = None
if a:
    print("True")
else:
    print("False")  # Return --> False

if "":
    print("Yes")
else:
    print("No")  # Return --> No

if 0:
    print("Yes")
else:
    print("No")  # Return --> No and so on.

# The elif keyword --> Python's way of saying "if the previous conditions were not true, then try this condition". It allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

a = 3
b = 5
if a > b:
    print("Yes")
elif a < b:
    print("a is smaller.")  # Return -->  a is smaller.

# Multiple elif statements
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")   # Return --> C
elif score >= 60:
    print("D")

age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 35:
  print("You are an adult")  # Return --> You are an adult
elif age >= 65:
  print("You are a senior")

# Day of the week checker:

Day = 3

if Day == 1:
    print("Monday")
elif Day == 2:
    print("Tuesday")
elif Day == 3:
    print("Wednesday")  # Return --> Wednesday
elif Day == 4:
    print("Thursday")
elif Day == 5:
    print("Friday")
elif Day == 6:
    print("Saturday")
elif Day == 7:
    print("Sunday")

# Else keyword --> The else statement is executed when the if condition (and any elif conditions) evaluate to False.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")  # Return --> a is greater than b

# if we didn't write the else condition and any of the upper condition aren't true, the block of code will not execute, so we must have to put elde of elif condition to get the output we want.
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")

number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")   # Return --> The number is odd

# Complete If_elif_else statements 

temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")  # Return --> It's warm outside
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

# Else as Fallback
# The else statement acts as a fallback that executes when none of the preceding conditions are true. This makes it useful for error handling, validation, and providing default values.

user_name = "Maria"

if len(user_name) > 0:
   print(f"Welcome {user_name}")  # Return --> Welcome Maria
else:
   print("Error: user_name can't be empty.")

if len(user_name) < 0:
   print(f"Welcome {user_name}") 
else:
   print("Error: user_name can't be empty.")  # Return --> Error: user_name can't be empty.

# Short_hand if
a = 20
b = 20
if a == b: print("Yes")  # Return --> Yes

print("A") if a > b else print("B")  # Return --> B