# Lesson 6: Python built in functions
# 🐍 Built-in functions

# #print()
# As we have seen before we used print couple of times already and made ourselves familiar with it. 
# We did not create the function itself as it comes out of the box right after installing python. 
# It is important to mention that this function is not as dull as it may seem from the first glance, in fact it's quite versatile.

# print(object(s), sep=separator, end=end, file=file, flush=flush)

# argument  	    meaning
# object(s)	        Any object, and as many as you like. Will be converted to string before printed
# sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
# end='end'	        Optional. Specify what to print at the end. Default is '\n' (line feed)
# file	            Optional. An object with a write method. Default is sys.stdout
# flush	            Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False

# Some examples:

# Simple print
# print("hello world")
# Gets the same result but slightly different:
# print("hello", "world")
# Gets the same result but is even more different:
# print(*["hello", "world"])
# let's play with separator:
# print("hello world", sep=",")
# some more
# print("hello", "world", sep=" amazing ")

# #type()
# Another useful function for us to understand what we are dealing with in python is type. 
# Often it helps us to understand what instance of the object are we dealing with. 
# Basically it tells us what kind of object we are dealing with.

# Examples:

# greet = "Hello World"
# print(type(greet))  #<class 'str'>

# number = 2022
# print(type(number)) #<class 'int'>

# my_list = [1, 2, 3]
# print(type(my_list))    #<class 'list'>
# print(type(my_list[0])) #<class 'int'>
# This becomes really helpful later on when dealing with more complex programs.

# #len()
# We have already seen this function before with list, so we are also a bit familiar with in.
# As you remember it returns the length of the list or tuple. 
# Nevertheless it still works with strings as well.

# Examples:

# word = "something"
# length = len(word)
# print(f"length of the word {word} is: {length}")

# Reminder how it works with lists:

# my_list = [1, 2, 3]
# print(f"length of the list {my_list} is: {len(my_list)}")

# #round()
# Function allows to round float to a certain decimal point. It is also quite useful.

# round(number, ndigits=None)

# argument	meaning
# number	    number that needs to be rounded
# ndigits	    decimal places, by default None, meaning that it will be rounded to integer value

# Examples:

# print(round(1.999))     #2
# print(round(1.5555, 2)) #1.56

# #sorted
# What if we would like to sort values in the list or tuple

# sorted(iterable, key=None, reverse=False)

# argument	    meaning
# iterable	    A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
# reverse	    (Optional) - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.
# key	        (Optional) - A function that serves as a key for the sort comparison. Defaults to None.

# Examples:

# my_list = [45, 20, 14, 55]
# sorted_list = sorted(my_list)
# print(sorted_list)  #[14, 20, 45, 55]
# sorted_reverse_list = sorted(my_list, reverse=True)
# print(sorted_reverse_list)  # [55, 45, 20, 14]

# What about string values?

# my_list = ["Albert", "Nicola", "Thomas"]
# sorted_list = sorted(my_list)
# print(sorted_list) #['Albert', 'Nicola', 'Thomas']
# sorted_reverse_list = sorted(my_list, reverse=True) 
# print(sorted_reverse_list) # ['Thomas', 'Nicola', 'Albert']

# Still works!
# There are plenty more built-in functions to explore at link Some of them are yet too early for us but as we progress throughout the course we will be using more and more of them.

# 🧠 Exercises:
# 1.
# Create a list of different types of python objects, and print all the types. The one who gets the the most unique types wins respect points:

# known_python_objects = ["Vygantas", 12, 15.5, [1, 2, 3], (4, 5, 6), {"baba": "mot"}]
# for item in known_python_objects:
#     print(type(item))

# 2.
# print all the items separated with "|"

# known_python_objects = ["Vygantas", 12, 15.5, [1, 2, 3], (4, 5, 6), {"baba": "mot"}]
# for item in known_python_objects:
#     print(item, end="|")  

# 3.
# create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.

# floats_list = [1.123, 2.123, 3.123]
# rounded_list = []
# for item in floats_list:
#     rounded_list.append(round(item, 2))
# print(floats_list, rounded_list)

# 4
# Create a list with student names and sort them, print the result to the terminal.

# students_list = ["Alice", "Bob", "Carol", "Dave", "Eve"]
# sorted_list = sorted(students_list, reverse=True)
# print(sorted_list)

5.
# write a program that allows user to write in any float number and then round it.

# any_float_number = input("Enter any decimal number: ")
# rounded = round(float(any_float_number), 1)
# print(rounded)






# [21:59] Saulius  Anusas      
#         Saulius 5 užduotis
number = input("Enter the number with minimum 3 digits after point: ")
no_check_dot = number.replace(".","").isnumeric()
no_check_comma = number.replace(",","").isnumeric()
if no_check_dot and len(number)>=5:    
    number = round(float(number), 1)    
    print(f"Rounden number value: {number}")
elif no_check_comma and len(number)>=5:
    number = number.replace(",",".")   
    number = round(float(number),1)    
    print(f"Rounden number value: {number}")
else:
    print(f"You have failed enter the number")
    
    
  
  






# We've got a very long string, containing a bunch of User IDs. 
# This string is a listing, which seperates each user ID with a comma and a whitespace ("' "). 
# Sometimes there are more than only one whitespace. Keep this in mind! Futhermore, 
# some user Ids are written only in lowercase, others are mixed lowercase and uppercase characters. 
# Each user ID starts with the same 3 letter "uid", e.g. "uid345edj". But that's not all! 
# Some stupid student edited the string and added some hashtags (#). User IDs containing hashtags are invalid, so these hashtags should be removed!

# Task
# Remove all hashtags
# Remove the leading "uid" from each user ID
# Return an array of strings --> split the string
# Each user ID should be written in only lowercase characters
# Remove leading and trailing whitespaces

# [19:46] Vytautas Sluckas
# test.assert_equals(get_users_ids("uid12345"), 
# ["12345"])test.assert_equals(get_users_ids("   uidabc  "), 
# ["abc"])test.assert_equals(get_users_ids("#uidswagger"), 
# ["swagger"])test.assert_equals(get_users_ids("uidone, uidtwo"), 
# ["one", "two"])test.assert_equals(get_users_ids("uidCAPSLOCK"), 
# ["capslock"])test.describe("Advanced tests")test.assert_equals(get_users_ids("uid##doublehashtag"), 
# ["doublehashtag"])test.assert_equals(get_users_ids("  uidin name whitespace"), 
# ["in name whitespace"])test.assert_equals(get_users_ids("uidMultipleuid"), 
# ["multipleuid"])test.assert_equals(get_users_ids("uid12 ab, uid#, uidMiXeDcHaRs"), 
# ["12 ab", "", "mixedchars"])test.assert_equals(get_users_ids(" uidT#e#S#t# "), 
# ["test"])