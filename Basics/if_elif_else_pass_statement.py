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

# Assign value with if/else
a1 = 4
b1 = 3
bigger = a1 if a1 > b1 else b1
print("bigger is ", bigger)  # Return --> bigger is  4
# The syntax follows this pattern --> (variable = value_if_true if condition else value_if_false)

# Multiple condition on one line

A = 40
B = 50
print("A") if A < B else print("=") if A == B else print("B")  # Return --> A

# Setting a default value example
user_namee = ""
display = user_namee if user_namee else "Guest"
print("user_name is ", display)  # Return --> user_name is  Guest

# user_nameee = input("Enter your user_name: ")
# display_name = user_nameee if user_nameee else "Guest"
# print("user_name is ", display_name)  # Return --> user_name is  Maria

# Python logical operators

# AND operator 
x = 40
y = 45
if x < y and x > y:  # Why, because in and operator both conditions must be true
   print("X is greater than y")
else:
   print("Y is greater than x")  # Return --> Y is greater than x

# OR operator
z = 6
c = 7
if z < c or z > c: # In or opeartors, if any one of the condition is true than the return will be true as well
   print("z is less than c")   # Return --> z is less than c
else:
   print("Error")

# NOT operator
d = 6
e = 6
if not d == e: # Why, because in not operator the output will be false even the condition is true, because its run in reverse
   print("Yes, both d & e is equal")
else:
   print("No")  # Return --> NO 

# Truth Table:
# and --> true-true is true, True-false is false, false-true is false, False-False is False
# or --> True-True is True, true-False is True, false-true is true, False-false is False
# not --> True-True is False, False-True is False, True-false is false, False-False is True

# Combine multiple operators
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")
# The logic means: You get a discount if:
# (You're under 18 OR over 65) AND you're not a student, OR
# You have a discount code

# Nested If Statements --> we can have if statements inside if statements. This is called nested if statements.
f = 5
g = 6
if f < g:
   print("Yes") # Return --> Yes
   if g > f:
      print("g is greater than f")  # Return --> g is greater than f
   else:
      print("No")

h = 6
i = 5
if h < i:
   print("Yes") 
   if i > h:
      print("g is greater than f")  
   else:
      print("No")
# In this example, the inner if statement only runs if the outer condition (f < g, h < i) is true. thats why the second block of code will not run

# How it works
age = 17
has_license = False

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

# Multiple nested if
score = 75
attendance = 50
submitted = True
if score >= 60:
   if attendance >= 75:
      if submitted:
         print("You are pass with good standing")
      else:
         print("Pass but missing assignment")
   else:
      print("Pass but low attendance")  # Return --> Pass but low attendance
else:
   print("Fail")

# More example
username = ""
password = "123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")

# Some more practices
# 1. temperature checker
temperature = int(input("Enter temperature: "))
if temperature < 0:
    print("Freezing")
else:
    if temperature <= 20:
        print("Cold")
    else:
        if temperature <= 35:
            print("Warm")
        else:
            print("Hot")

# Travel Clothing Recommender --> Write a program that helps you decide what to wear based on temperature and weather condition.
temperature = int(input("Enter a temperature: "))
weather = input("Enter the weather: ").lower()

if temperature < 10:
    if weather == "snowy":
        print("Wear a thick jacket and boots.")
    else:
        if weather == "rainy":
            print("Carry an umbrella and wear a raincoat.")
        else:
            if weather == "sunny":
                print("Wear light clothes and sunglasses.")
            else:
                print("Just dress comfortably.")
else:
    print("Just dress comfortably.")

# Using pass statements
value = int(input("Enter a value: "))

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")



   