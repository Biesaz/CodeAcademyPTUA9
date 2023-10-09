# Lesson 3: Data Structures (Part 1)

# friends = [] # Instantiating empty list

# my_list = []

# name = "Tom"
# my_list.append(name)
# print(my_list)

# my_list = [1, 1, 2 ,3 ,4 ,5]
# print(my_list.count(1))

# my_list = [1, 1, 2 ,3 ,4 ,5]
# my_list.insert(1, 50)
# print(my_list) # [1, 50, 1, 2, 3, 4, 5]

# my_list = [1, 1, 2 ,3 ,4 ,5]
# my_list.remove(1)
# print(my_list)

# my_list = [1, 1, 2 ,3 ,4 ,5]
# my_list.remove(my_list[-1]) # removing last item from the list
# print(my_list) [1, 1, 2, 3, 4]

# Python built-in List functions
# my_list = ["name", 123, None, True]
# print(len(my_list)) # 4

# my_list = [50, 99, 1, -50]
# print(max(my_list)) #99

# my_list = [50, 99, 1, -50]
# print(min(my_list)) #-50

# Iterating over elements within the list
# my_list = [1, 2, 3]
# for item in my_list:
#     print(item)

# my_list = [1, 2, 3]
# for item in my_list:
#     print(item + 20)

# Changing an existing value within the list
# my_list = [1, 2, 3]
# my_list[2] = 5
# print(my_list)

# Slicing
# my_list = ["first", "second", "third"]
# print(my_list[-1])
# print(my_list[:1])
# print(my_list[::2])
# print(my_list[::-1])
# print(my_list[0:2])

# Operator in with Lists
# my_list = [1, 2, 3]
# print(1 in my_list)  #True

# Tuple #objektų reikšmės yra nekeičiamos.
# Tuple užrašas python'e yra **( )** - du skliausteliai, tarp kurių vertės atskiriamos kableliais.
# Atkreipkite dėmesį, kad po kiekvieno elemento tuple turi būti kablelis, nors gali būti tik vienas elementas.
# empty_tuple = ()
# tuple_single_item = (1,)
# another_tuple = (1, 2, 3)

# my_tuple = (1, 2, 3)
# my_tuple[0] = 500 # TypeError: 'tuple' object does not support item assignment

# Tuple ir sąrašų palyginimas
# Dabar atrodo, kad sąrašai yra daug geresni už tuples, tačiau programavime ne visada viskas yra vienpusiška, 
# tai priklauso nuo tam tikrų situacijų. Paprastai statinėms reikšmėms, kurios nesikeičia, rekomenduojama naudoti Tuple, 
# nes python kalboje jis yra šiek tiek greitesnis nei sąrašai. O sąrašus turėtume naudoti visada, kai turime reikšmių, kurios keisis, arba kai pats sąrašas didės arba mažės.
# ------------------------------------------
# fruits = ["apple", "orange", "pear"]
# fruits_as_string = ""
# for fruit in fruits:
#     fruits_as_string = f"{fruits_as_string}{fruit} "    
# print(fruits_as_string)

# 🧠 Exercises:
# 1.
# Write a python program that sums up all items in the list (all items are integers or floats in list, create a list yourself)

# my_list = [1, 2, 3, 4, 5.5]
# total = sum(my_list)
# print(total)

# 2.
# Write a python program that multiplies all items in the list (all items are integers or floats in list, create a list yourself)

# import math
# my_list = [1, 2, 3, 4, 5.5]
# result = math.prod(my_list)
# print(result)

# 3.
# Write a python program that gets maximum value from the list (all items are integers or floats in list, create a list yourself)

# my_list = [1, 2, 3, 4, 5.5]
# print(max(my_list))

# 4.
# Write a python program that concatenates all strings in the list (all items are strings, create a list yourself)

# my_list = ["vienas", "du", "trys", "keturi", 'penki']
# print(my_list)

# 5.
# Create two lists and add them together, make sure it works the way you want it to.

# first_list = [1, 2, 3, 4, 5.5]
# second_list = ["vienas", "du", "trys", "keturi", 'penki']
# total_list = first_list + second_list
# print(total_list)

# 6.
# Write a python program that asks user to enter 3 integers and find the highest value entered.

# first_integer = int(input ("Enter first integer: "))
# second_integer = int(input ("Enter second integer: "))
# third_integer = int(input ("Enter third integer: "))
# integers_list = [first_integer, second_integer, third_integer]
# print(f"The highest value entered is: {max(integers_list)}")

# 7.
# Try doing same exercises with tuples.

# Convert a tuple to a string.
# my_tuple = ("one", "two", "three", "four", "five")
# my_string = " ".join(my_tuple)
# print(my_string)

# # Print the second item in the tuple.
# my_tuple = (1, "two", 3.0, True, None)
# print(my_tuple[1])

# Unpack a tuple into several variables.
# my_tuple = (1, 2, 3, 4, 5)
# a, b, c, d, e = my_tuple
# print(a, b, c, d, e)

# Add an item to a tuple.
my_tuple = (1, 2, 3, 4, 5)
my_tuple += (6,)
print(my_tuple)