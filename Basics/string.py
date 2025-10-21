# Both output will be same either, we use single quotation or double quotation.
a = "Hello"
a1 = 'Hello'

# print(a, a1)

# Quote inside quote

x = "Hey, i'm maria"                 # Output: Hey, i'm maria
x1 = "Hey, how are you, 'Bia'."      # Output: Hey, how are you, 'Bia'.
x2 = 'I love "Python".'              # Output: I love "Python".

# print(x)
# print(x1)
# print(x2)

# Multi line strings:

a = """
I am learning Python.           
"""

# print(a)      # Output: I am learning Python.

# Single quote string:

a = '''
Hey, Bia.
'''

# print(a)    # Output: Hey, Bia.

# Slicing Strings --> We can return a range of characters by using the slice syntax.

a = "Hello"

# print(a[2:5])  # Output: llo --> we specify start index which is 2 than add colon to separate the start index, so that we can write the end index which is 5, also during slicing end index not included, while returning the string, that's why we get ll0 --> which is 2 to 4, (H-0, e-1, l-2, l-3, o-4) --> so, when we run the function it will only print string from 2-4 excluding 5.

# Strings are arrays --> strings in Python are arrays of unicode characters.

a = "Hello, Bia..!"

# print(a[1]) # Output: e
# print(a[6]) # Output: empty space
# print(a[-6]) # Output: B

# Looping Through a String --> 

# for x in "banana":
#   print(x) 

# Finding Length in strings

a = "Hello, World..!"
# print(len(a))  # Output: 15

# Check string --> To check if a certain phrase or character is present in a string, we can use the keyword in.

fav = "I love eating fries"
# print("love" in fav)  # Output: True

# We can also use if statement to check wether the string is presesnt or not.
# if "love" in fav:
#     print("Yes, love is in the string")   # Output: Yes, love is in the string

# Now, let's check if the given character is present in the string or not by using (not in).

fav = "I love reading thriller and mystery books"
# print("horror" not in fav) # Output: True

# Same we can do this with if statement
# if "horror" not in fav:
#     print("Yes, it's not present in the string")    # Output: Yes, it's not present in the string.

# Slicing in strings

a = "Hello world..!"
# print(a[2:5]) # Output: llo

# Slicing from start
a = "Hello world..!"
# print(a[0:]) # Output: Hello, world..!

# Slicing from the end
a = "Hello world..!"
# print(a[:14]) # Output: Hello world..!
# print(a[:5])  # Output: Hello

# Negative indexing
a = "Happy"
# print(a[-4:-1])

# Modify string --> Built-in methods, we use in strings
# Upper case:
a = "hello"
# print(a.upper())  # Output: HELLO

# Lower case:
a = "HELLO"
# print(a.lower())  # Output: hello

# Remove white space:
a = "    Hello"
# print(a.strip())  # Output: Hello --> remove the white space, we given to our variable a's hello.

# Replace string:
a = "Hello"
# print(a.replace("H", "Y"))  # Output: Yello

# Spliting strings:
a = "Hello, world"
# print(a.split(","))  # Output: ['Hello', ' World!']

# String Concatenation --> to concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
# print(c)  # Output: HelloWorld

# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
# print(c)  # Output: Hello World

# String Format:
age = 36
#This will produce an error:
# txt = "My name is John, I am " + age
# print(txt) 

# We can use f'string format to combine numbers and strings.
age = 36
# txt = f"My name is Maria, I am {age}"
# print(txt)   # Output: My name is Maria, I am 36

# Placeholders and Modifiers --> placeholder can contain variables, operations, functions, and modifiers to format the value.
price = 48
value = f"The price is {price} dollars"
# print(value)

price = 59
# txt = f"The price is {price:.2f} dollars"    # Output: The price is 59.00 dollars --> .2f which means fixed point number with 2 decimals
txt = f"The price is {20 * 59} dollars"   # Output: The price is 1180 dollars
# print(txt)

# Escape Character --> escape character is a backslash \ followed by the character we want to insert.
# txt1 = "We are the so-called "Vikings" from the north."  # we will get an error if we use double quotes inside a string that is surrounded by double quotes

txt1 = "We are the so-called \"Vikings\" from the north."  # So, we use escape character like this.
# print(txt1)   # Output: We are the so-called "Vikings" from the north.


# Other escape characters used in Python:
# Code	   Result	
# \'	   Single Quote	
# \\	   Backslash	
# \n	   New Line	
# \r	   Carriage Return	
# \t	   Tab	
# \b	   Backspace	
# \f	   Form Feed	
# \ooo	   Octal value	
# \xhh	   Hex value

txt2 = 'It\'s alright.'
# print(txt2)  # Output: It's alright.

txt3 = "This will insert one \\ (backslash)."
# print(txt3)  # Output: This will insert one \ (backslash).

txt4 = "Hello\nWorld!"
# print(txt4)

txt5 = "Hello\rWorld!"  # returns: world!
print(txt5)




