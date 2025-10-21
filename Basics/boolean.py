# In python, if you wanted to evaluate or compare two values, the answer will return "True" or "False"
a = 10
b = 20
c = 30
print(a>b) # Output: False
print(a<c) # Output: True

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")  # Output: b is not greater than a

# Evaluate values and variables
# In Python, everything has a truth value. When you wrap something in bool(...), Python checks: “Is this value considered empty or zero or None?”
# If not → it returns True.
# If yes → it returns False.

# | Value type        | When it’s `False`   | Otherwise → `True`   |
# | ----------------- | ------------------- | -------------------- |
# | Strings           | "" (empty string)   | Any non-empty string |
# | Numbers           | 0, 0.0              | Any nonzero number   |
# | Lists/Tuples/Sets | [], (), set()       | If not empty         |
# | Dicts             | {}                  | If not empty         |
# | Special values    | None, False         | —                    |

print(bool("Hello"))  # True --> because the string is not empty
print(bool(15))   # True --> because 15 ≠ 0

print(bool(""))   # False  (empty string)
print(bool(0))    # False  (zero)

class myclass():
  def __len__(self):
    return 0           # False --> because this function return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

def myfunc():
  return True

if myfunc():
  print("Yes")     # Print "YES!" if the function returns True, otherwise print "NO!"

else:
  print("No")

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))  
# x is the object → 200

# int is the class (type) you’re checking against
# So Python asks --> “Is 200 an instance of the int class?”

# Answer → Yes → returns True. 

# Python has built-in Boolean operators, which are used to combine conditional statements:
# AND operator --> Returns True if both statements are true

