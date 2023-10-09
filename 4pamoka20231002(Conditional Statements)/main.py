# Lesson 4: Conditional Statements
# sąlygos ir If teiginiai

# #if <test_expression>:
#     statement(s)

# Equals:                        a == b
# Not Equals:                    a != b
# Less than:                     a < b
# Less than or equal to:         a <= b
# Greater than:                  a > b
# Greater than or equal to:      a >= b

# number1 = 500
# number2 = 600
# if number1 < number2:
#     print("number1 is greater than number2 !")

# #Elif  Ką daryti, jei norime išplėsti programą ir išspausdinti ką nors kitą tikrinant kitą sąlygą?

# number1 = 500
# number2 = 600
# if number1 < number2:
#     print("number1 is greater than number2 !")
# elif number1 == number2:
#     print("numbers are equal !")
# elif...

# #Else  Raktiniu žodžiu else sugaunama viskas, ko nesugauna ankstesnės sąlygos.

# number1 = 500
# number2 = 600
# if number1 < number2:
#     print("number1 is greater than number2 !")
# elif number1 == number2:
#     print("numbers are equal !")
# else:
#     print("number2 is greater than number1 !")

# #Short version of if ... else
# a = 200
# b = 450
# print("A") if a > b else print("B")

# 3 conditions example:
# a = 200
# b = 200
# print("A") if a > b else print("=") if a == b else print("B")

# #and
# a = 200
# b = 400
# c = 500
# if c > a and c > b:
#     print("C is the greatest of them all!")

# # or
# a = 200
# b = 400
# c = 500
# if b > a or b > c:
#     print("B is at least greater than one of the values !")

# # Nested if (Įterptinis if)
# x = 15
# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")

# # pass
# If we want to have an empty if statement for some reason we can simply do pass and nothing will happen.
# a = 50
# b = 80
# if b > a:
#   pass

# # If with string values
# name = input("Input your name: ")
# if name == "Tom":
#   print("Nice to see you Tom")
# elif name == "Alice":
#   print("Hi Alice!")
# else:
#   print("welcome, user")

# # What is more we can also combine this knowledge with lists as well!
# user = "Johnny"
# privileged_users = ["Tom", "Albert", "Stephen"]
# if user in privileged_users:
#     print(f"Welcome home {user}")
# else:
#     print("INTRUDER ALLERT. Silently calling police...")

#  # Or even dictionaries:
# my_dict = {"name": "Steven", "born": "1955-02-24", "interests": "Apples"}
# if my_dict["name"] == "Steven":
#     print("This guy does not like Windows")
# else:
#     print("No clue who this is")

# # Or even:
# my_dict = {"name": "Bill", "born": "1955-10-28", "interests": "small software"}
# if "Bill" in my_dict.values():
#     print("This guy hates apples")
# else:
#     print("No clue who this is")

# # 🤔 shorter version of ifs ❗❗❗
# Instead of doing this:
# ...
# if name != "":
#   print("Name was not entered")
# ...
# ...
# if len(name) == 0:
#   print("Name was not entered")
# ...
# Do this:
# if not name:
#   print("Name was not entered")

# my_list = []
# if not my_list:
#   print("oh no, list is empty")  
# ------------------------------------------------

# weight_lower_limit = 75.5
# weight_higher_limit: float = 100.0
# weight = float(input("Enter your weight: "))
# if weight > weight_higher_limit:
#     if weight > 150:
#         print("WTF")
#     print("Mindaugas is kebab")
# elif weight < weight_lower_limit:
#     print("Mindaugas is hungry") 
# else: 
#     print("Mindaugas is cool") 

# [19:03] Mindaugas Rudzevičius
# Task nr.1 Updated
# Create a program, which takes 10 random numbers as user inputs.
# The program should produce list of input values what are less than 50 and tuple of all other values.
# After input is done, program should return the the mathematicaldiffernce between the highest and lowest number from non primary numbers, 
# and sum of primary numbers from tuple.

# first_number = int(input ("Enter first number: "))
# second_number = int(input ("Enter second number: "))
# third_number = int(input ("Enter third number: "))
# four_number = int(input ("Enter four number: "))
# five_number = int(input ("Enter five number: "))
# six_number = int(input ("Enter six number: "))
# seven_number = int(input ("Enter seven number: "))
# eith_number = int(input ("Enter eith number: "))
# nine_number = int(input ("Enter nine number: "))
# ten_number = int(input ("Enter ten number: "))

# my_list = []
# my_tuple_list = []
# if first_number < 50:
#     my_list.append(first_number)
# else:
#     my_tuple_list.append(my_tuple_list)
# if second_number < 50:
#     my_list.append(second_number)
# else:
#     my_tuple_list.append(my_tuple_list)
# if third_number < 50:
#     my_list.append(third_number)
# else:
#     my_tuple_list.append(my_tuple_list)
# if four_number < 50:
#     my_list.append(four_number)
# else:
#     my_tuple_list.append(my_tuple_list)
# if five_number < 50:
#     my_list.append(five_number)
# else:
#     my_tuple_list.append(my_tuple_list)
# if six_number < 50:
#     my_list.append(six_number)
# else:
#     my_tuple_list.append(my_tuple_list)
# if seven_number < 50:
#     my_list.append(seven_number)
# else:
#     my_tuple_list.append(my_tuple_list)
# if eith_number < 50:
#     my_list.append(eith_number)
# else:
#     my_tuple_list.append(my_tuple_list)
# if nine_number < 50:
#     my_list.append(nine_number)
# else:
#     my_tuple_list.append(my_tuple_list)
# if ten_number < 50:
#     my_list.append(ten_number)
# else:
#     my_tuple_list.append(my_tuple_list)
# print(my_list)
# print(tuple(my_tuple_list)) 
# print(max(my_list) - min(my_list))
# print((my_tuple_list) + (my_tuple_list))

# Task nr.0
# Program takes 3 random numbers as user input. Update lsit and tuple data structures with those values and print it.

# first_number = float(input ("Enter first number: "))
# second_number = float(input ("Enter second number: "))
# third_number = float(input ("Enter third number: "))
# numbers_list = [first_number, second_number, third_number]
# numbers_float = (first_number, second_number, third_number)
# print(numbers_list, numbers_float)

# a = 50
# b = int(input("Enter number: "))
# if b >= a:
#     print(b)
# else:
#      print(a)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter threh number: "))
# d = int(input("Enter forth number: "))
# if a < b and b < c:
#     print (f"first condition if: {b}")
# elif a > c:
#     print(f"elif: {a}, {b} ,{c}")
# else:
#     print (f"else. {a}, {b}, {c}, {d}")








# 🧠 Exercises:
# 1.
# Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.

# name = input ("Enter your name: ")
# surname = input("Enter your surname: ")
# age = int(input("Enter your age: "))
# if age < 21:
#     print("Too young")
# else:
#     print("Welcome!")

# 2.
# Create a database (List of privileged users) print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

# name = input ("Enter your name: ")
# database = ["Jon", "Tom", "Len", "Sim"]
# if name in database:
#      print(f"Welcome home, {name}")
# else:
#      print(f"Welcome otherwise, {name}")     

# 3.
# allow user to enter two numbers, print out which one is higher than the other, or are they equal?

# first_number = input ("Enter first number: ")
# second_number = input ("Enter second number: ")
# if first_number > second_number:
#     print(first_number)
# if first_number < second_number:
#     print(second_number)  
# if first_number == second_number:
#     print("They are equal :)")   
# 4.
# Write a small calculator application, that allows user to enter two numbers and a symbol, given and then do the operation and print an answer.

# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
# symbol = input("Enter symbol (+, -, *, /): ")
# if symbol == "+":
#     print(first_number + second_number)
# elif symbol == "-":
#     print(first_number - second_number)
# elif symbol == "*":
#     print(first_number * second_number)
# elif symbol == "/":
#     print(first_number / second_number)
# else:
#     print("Invalid symbol.")

# 5.
# create a number guessing game from 1-10, with random library. (IDEA FOR LATER MAYBE)

import random
random_numer = random.randint(1, 10)
guess_number = int(input("Guess the number from 1 to 10: "))
if guess_number == random_numer:
    print(f"You've gussed it! It's {random_numer}")
else: print(f"You haven't guessed, the right answer is {random_numer}")



