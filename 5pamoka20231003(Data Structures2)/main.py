# Lesson 5: Data Structures (Part 2)
# Dictionary

# key: value
# A very powerful data structure which is going to be used a lot. Dictionary hold key: value pairs, with which we can access it's attributes. Dictionaries are:

# mutable ✔️ (can be changed)
# dynamic ✔️ (can grow and shrink in size)
# nested ✔️ (can contain other dictionaries or other complex structures)
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.

# Main difference between python list and dictionary is that values in dictionaries are accessed by keys.

# Creating a dictionary and adding values to it is as simple as:
# my_dictionary = {}
# my_dictionary["name"] = "Tom"
# print(my_dictionary["name"])
# my_dictionary = {"name": "Tom"}
# print(my_dictionary["name"])

# Access dictionary values
# my_dictionary = {"name": "Tom", "surname": "Edison"}
# print(f"name: {my_dictionary['name']}")
# print(f"surname: {my_dictionary['surname']}")
# If the value is non existent we shall get a KeyError as such key does not exist:

# my_dictionary = {"name": "Tom", "surname": "Edison"}
# print(f"favourite car: {my_dictionary['car']}")
# Similarly as with lists, dictionaries may hold anything in it's key and values. But usually keys would be string values and values could be anything at all.

# Changing values in dictionary
# my_dictionary = {"name": "Tom", "surname": "Edison"}
# my_dictionary["name"] = "Charles"
# print(f"name: {my_dictionary["name"]}")

# Droping key from dictionary
# my_dictionary = {"name": "Tom", "surname": "Edison"}
# del my_dictionary ["name"] arba my_dictionary.pop("name")
# print(my_dictionary)

# Dictionary to list of tuples with .items()
# There will be a lot of situations, mostly when we want to iterate through dictionary we will be using in-built .items() method of dictionary.

# d = {'a': 10, 'b': 20, 'c': 30}
# print(list(d.items()))
# .keys()
# returns us all the dictionary keys:

# d = {'a': 10, 'b': 20, 'c': 30}
# list(d.keys())
# .values()
# d = {'a': 10, 'b': 20, 'c': 30}
# list(d.values())
# .pop
# d = {'a': 10, 'b': 20, 'c': 30}
# d.pop('a')
# print(d)
# .update() 
# If is a dictionary, d.update() merges the entries from into d. For each key in : If the key is not present in d, the key-value pair from is added to d. If the key is already present in d, the corresponding value in d for that key is updated to the value from .

# Examples:

# d1 = {'a': 10, 'b': 20, 'c': 30}
# d2 = {'b': 200, 'd': 400}
# d1.update(d2)
# print(d1)
# d1 = {'a': 10, 'b': 20, 'c': 30}
# d1.update([('b', 200), ('d', 400)])
# print(d1)
# d1 = {'a': 10, 'b': 20, 'c': 30}
# d1.update(b=200, d=400)
# print(d1)
# Iterating through dictionary
# Example:

# d = {'a': 10, 'b': 20, 'c': 30}
# for key, value in d.items():
#     print(key, value)
# converting two lists into a dictionary
# Note that lists must be of the same size here:

# test_keys = ["Albert", "Tom", "Stephen"]
# test_values = [1, 4, 5]
# my_dictionary= dict(zip(test_keys, test_values))
# print(my_dictionary)
# Sets
# Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are [List] A set is a collection which is unordered, unchangeable*, and unindexed.

# Note: Set items are unchangeable, but you can remove items and add new items.

# Notation:

# my_set = {1, 2, 3}
# Another important property is that in sets we cannot have duplicates:

# my_set = {1, 2, 3, 1}
# print(my_set)
# getting unique values from python list:

# numbers_list = [1, 2, 3, 4, 5, 5, 5, 6]
# numbers_set = set(numbers_list)
# print(numbers_set)


# 🧠Exercises
# 1.
# Write python program that asks user to enter name, surname, age. Put these values into a dictionary and print dictionary
# 
# name = input ("Enter your name: ")
# surname = input("Enter your surname: ")
# age = int(input("Enter your age: "))
# #1 variantas
# my_dictionary = {"name": name, "surname": surname, "age": age}
# print(my_dictionary)
# # 2 variantas
# my_dictionary = {}
# my_dictionary["name"] = name
# my_dictionary["surname"] = surname
# my_dictionary["age"] = age
# print(my_dictionary) 

# User name is "vardas", user surname is "pavarde", user age is "amzius"
# print(f"User name is: {my_dictionary['name']}, user surname is: {my_dictionary['surname']}, user age is: {my_dictionary['age']}")

# 2
# Try creating structure like one here: link from an empty dictionary: my_dict = {}

# manufacturer = input("Enter car manufacturer: ")
# model = input("Enter car model: ")
# year = input("Enter year of manufacture: ")
# my_dictionary = {}
# my_dictionary["producer"] = manufacturer
# my_dictionary["style"] = model
# my_dictionary["birthday"] = year
# print(my_dictionary)


name = input ("Enter your name: ")
surname = input("Enter your surname: ")
my_dictionary = {"name": name, "surname": surname}
my_ocupation = {"role": "profesor", "workplace": "Univer"}
languages = ["German", "Polish", "Italian"]
my_dictionary["languages"] = languages
my_dictionary["my ocupation"] = my_ocupation
print(my_dictionary)
                 