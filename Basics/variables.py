x = 30

# print(x)   # Output: 30

y = "Maria"

# print(y)  # Output: Maria

# print(x=y)  # It will show error why???? Because x is an integer and y is a string

# So, we can write it like this to avoid syntax error:
# print(x, y)  # Now the output will be: 30 Maria

# Variables Names:
# Legal Variables Names:
myvar = "Maria"
_my_var = "Maria"
my_var = "Maria"
myVar = "Maria"
MYVAR = "Maria"
myvar2 = "Maria"

# Illegal Variables Names:
# 2myvar = "Maria"
# my-var = "Maria"
# my var = "Maria"

# Multi Words Variables Names:
# Camel Case:
myVariableName = "Maria"

# Pascal Case:
MyVariableName = "Maria"

# Snake Case:
my_variable_name = "Maria" # This case has more readability than others but it's your choice to use. Just don't use illegal variables or it will show error.

# Assigning many values to multiple variables

x, y, z = "Orange", "Banana", "Cherry"

# print(x)  # Output Orange
# print(y)  # Output Banana
# print(z)  # Output Cherry

# # print(x, y, z)

# x=y=z = "Orange"

# print(x) # Output: Orange
# print(y) # Output: Orange
# print(z) # Output: Orange
# print(x, y, z)  # Output: Orange Orange Orange

# print(x=y=z) # Shows error because you can pass values or expressions, but not assignments (=)

# Python numbers
int = 30
float = 2.5
# complex = a + bj

# Data Conversion--> We use this to convert data
a = 13.5
b = int(a)
c = complex(a)

# print(a) # Output: 13.5
# print(b)   # Output: 13--> because originally a is written as float, but by using conversion method we turned a into integer.
# print(c)   # Output: 13.5 + 0j--> same thing happend here as well.

# Type Casting--> Similar to type conversion, but we use this when we want to specify a type on a variable
str1 = "7"          
str2 = "3.142"
str3 = "13"
num1 = 29
num2 = 6.67
 
# print(int(str1))       # Output: 7
# print(float(str2))     # Output: 3.142
# print(float(str3))     # Output: 13.0
# print(str(num1))       # Output: 29
# print(str(num2))       # Output: 6.67
# print(type(int(str1))) #  Output: <class 'int'> --> Like this you can do with the other as well.

# Output Variables:

x = "My name is Maria"
# print(x) # Output: My name is Maria

x = "My"
y = "Name"
z = "is Maria"
# # print(x,y,z)  # Output: My Name is Maria

x = 20
y = " I'm"
z = " Maria"
# print(x+y+z)  # It will show error because x is an integer.
# print(x,y,z)  # Output: 20  I'm  Maria, so in order to get an output, you have to put coma(,) in between the variables.

# Global Variables --> Think of it like a variable that belongs to the whole file — not just to one function.

x = "awesome" # Gloabl Variables

def myfunc():               # Function
  print("Python is " + x)   # Can use global variable inside the function

myfunc() # Output: Python is awesome
# print(x)  # Output: awesome --> it proves that the global variables belongs to whole file.


x = 10  # global variable

def my_func():
    y = 5   # local variable
    print("Inside function:", x)  # can access global
    print("Inside function:", y)  # can access local

my_func()

# print("Outside function:", x)  # can access global
# # print("Outside function:", y)  # ❌ ERROR — y is local only

# Changing a Global Variable Inside a Function

x = 10

def change():
    x = 20  # creates a *new* local variable named x
    print("Inside:", x)   # It will check inside the function, if x is available --> than print the local variable.

change()   # Calling function
# print("Outside:", x)  # Here, now it will print the glabal variable, because local variable no longer exist.

x = 10

def change():
    global x   # We use this keyword to tell python, "Hey, python we want to use this x as global variable, so change it with the existing Global variable."
    x = 20  # modifies the global variable
    print("Inside:", x)  # Output: Inside: 20

change()
print("Outside:", x)   # Output: Outside: 20








