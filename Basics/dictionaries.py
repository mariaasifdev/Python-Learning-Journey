# Dictionaries is a collection of key-value pairs where each key is unique. Dictionaries are mutable, meaning they can be changed after their creation. They are defined using curly braces {} with key-value pairs separated by commas.
# Example of a dictionary
my_dict = {
    "name": "Maria",
    "age": 30,
    "city": "New York"
}
# Accessing values in a dictionary
print(my_dict["name"]) # Return --> Maria
# Duplicate keys are not allowed in dictionaries. If a duplicate key is used, the last value assigned to that key will overwrite the previous value.
# Example of duplicate keys
duplicate_dict = {
    "name": "Maria",
    "age": 25,
    "name": "Bia"  # This will overwrite the previous "name" key
}
print(duplicate_dict["name"]) # Return --> Bia
print(duplicate_dict) # Return --> {'name': 'Bia', 'age': 25}
print(len(duplicate_dict)) # Return --> 2

# The value in dictionaries can be of any data type, including lists, tuples, and even other dictionaries.
complex_dict = {
    "name": "Maria", # String as a value
    "age": 30, # Integer as a value
    "boolean": True, # Boolean as a value
    "hobbies": ["reading", "traveling", "swimming"],   # List as a value
    "address": { 
        "street": "123 Main St",
        "city": "New York"
    } # Nested dictionary as a value
}  
print(complex_dict["hobbies"]) # Return --> ['reading', 'traveling', 'swimming']
print(type(complex_dict)) # Return --> <class 'dict'>
print(type(complex_dict["age"])) # Return --> <class 'int'> -- find the type of the value
# If we wanted to get nested values, we can chain the keys.
print(complex_dict["address"]["city"]) # Return --> New York -- i want to get the city from the nested dictionary

# dict constructor -- Another way to create a dictionary is by using the dict() constructor.
another_dict = dict(name="Maria", age=28, city="Los Angeles")
print(another_dict) # Return --> {'name': 'Maria', 'age': 28, 'city': 'Los Angeles'}

# we can also use get() method to access values in a dictionary. The get() method returns None if the key does not exist, instead of raising a KeyError.
print(my_dict.get("age")) # Return --> 30
print(my_dict.get("country")) # Return --> None

# key() method -- The keys() method returns a view object that displays a list of all the keys in the dictionary.
print(my_dict.keys()) # Return --> dict_keys(['name', 'age', 'city'])

# The list of keys is a view object, which means it reflects any changes made to the dictionary.
# before adding a new key-value pair
print(my_dict.keys()) # Return --> dict_keys(['name', 'age', 'city'])
my_dict["country"] = "USA" # adding a new key-value pair
# after adding a new key-value pair
print(my_dict.keys()) # Return --> dict_keys(['name', 'age', 'city', 'country']) -- any changes, we will make it reflects to our original dictionary

# values() method -- The values() method returns a view object that displays a list of all the values in the dictionary.
print(my_dict.values()) # Return --> dict_values(['Maria', 30, 'New York', 'USA'])

# make a change in the original dictionary and see the changes in the values view object
# before changing a value
print(my_dict.values()) # Return --> dict_values(['Maria', 30, 'New York', 'USA'])
# after changing a value
my_dict["age"] = 31
print(my_dict.values()) # Return --> dict_values(['Maria', 31, 'New York', 'USA'])

# items() method -- The items() method returns a view object that displays a list of dictionary's key-value tuple pairs.
print(my_dict.items()) # Return --> dict_items([('name', 'Maria'), ('age', 31), ('city', 'New York'), ('country', 'USA')])

# make a change in the original dictionary and see the changes in the items view object
# before changing a value
print(my_dict.items()) # Return --> dict_items([('name', 'Maria'), ('age', 31), ('city', 'New York'), ('country', 'USA')])
# after changing a value
my_dict["city"] = "San Francisco"
print(my_dict.items()) # Return --> dict_items([('name', 'Maria'), ('age', 31), ('city', 'San Francisco'), ('country', 'USA')])

# Checking if a key exists in a dictionary using the 'in' keyword
if "name" in my_dict:
    print("Key 'name' exists in the dictionary.") # Return --> Key 'name' exists in the dictionary.

# Change a value in the dictionary using update() method
my_dict.update({"age": 32})
print(my_dict) # Return --> {'name': 'Maria', 'age': 32, 'city': 'San Francisco', 'country': 'USA'}

# add a new key-value pair using update() method or simply by assignment
my_dict.update({"profession": "Engineer"})
# or
my_dict["hobby"] = "Photography"
print(my_dict) # Return --> {'name': 'Maria', 'age': 32, 'city': 'San Francisco', 'country': 'USA', 'profession': 'Engineer', 'hobby': 'Photography'}

# Remove a key-value pair using pop(), popitem(), clear(), del method
# Using pop() method
my_dict.pop("hobby")
print(my_dict) # Return --> {'name': 'Maria', 'age': 32, 'city': 'San Francisco', 'country': 'USA', 'profession': 'Engineer'}

# Using popitem() method -- removes the last inserted key-value pair
my_dict.popitem()
print(my_dict) # Return --> {'name': 'Maria', 'age': 32, 'city': 'San Francisco', 'country': 'USA'}

# Using del method
del my_dict["country"]
print(my_dict) # Return --> {'name': 'Maria', 'age': 32, 'city': 'San Francisco'}

# del also can be used to delete the entire dictionary
# del my_dict
# print(my_dict) # This will raise a NameError as my_dict is deleted

# Using clear() method -- removes all items from the dictionary
my_dict.clear()
print(my_dict) # Return --> {}

# Looping through a dictionary
sample_dict = {
    "name": "Maria",
    "age": 25,
    "city": "Chicago"
}
for key in sample_dict:
    print(key, ":", sample_dict[key]) # Return -->
# name : Maria 
# age : 25
# city : Chicago

# Looping through keys and values using items() method
for key, value in sample_dict.items():
    print(key, "->", value) # Return -->
# name -> Maria
# age -> 25
# city -> Chicago
# values only
for value in sample_dict.values():
    print(value) # Return -->
# Maria
# 25
# Chicago
# keys only
for key in sample_dict.keys():
    print(key) # Return -->
# name
# age
# city

# Copy method --> we cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2
my_dict1 = {
    "name": "Maria"
}
thisdict = my_dict1.copy()
print(thisdict)  # Return --> {'name': 'Maria'}

# We can also use dict() method for copy
my_dict2 = {
    "name": "Maria"
}
thisdict1 = dict(my_dict2)
print(thisdict1)  # Return --> {'name': 'Maria'}

# Nested dictionary
information = {
  "Personal" : {
    "name" : "Emil",
    "DOB" : 2001
  },
  "contact" : {
    "number" : 23456,
    "email" : "abc@gmail.com"
  }
}
print(information["contact"]["email"])   # Return --> abc@gmail.com -- how, i just wanted to get the email, so i give a command that, "hey, python --> give me the email from dictionary name information inside that there is a key conttact and in that contact there is another key name email and in return python give me the eamil"

# Loop through nested dictionary
for x, obj in information.items():
  print(x)   # this loop will print only (personal and contact) --> because in this loop x refering to them

  for y in obj:    # Here, obj contain the inner information of the dictionary which is name, DOB, number, email and their values and separate them usin : colon
    print(y + ':', obj[y])
    # The first loop goes through each information (outer dictionary). The second loop goes through each detail of that information (inner dictionary).

new_info = information.setdefault("City", "New York") # Returns the value of the specified key. If the key does not exist: it will insert the key, with the specified value
print(new_info)   # Return --> New York
print(information)   # Return --> {'Personal': {'name': 'Emil', 'DOB': 2001}, 'contact': {'number': 23456, 'email': 'abc@gmail.com'}, 'City': 'New York'}
new_info1 = dict.fromkeys(information)  # Returns a dictionary with the specified keys and value
print(new_info1)  # Return --> {'Personal': None, 'contact': None, 'City': None}
