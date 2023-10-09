# Lesson 2: Data Types and Operations

# INTEGERS sveikas sk.
# a = 5
# print(a)

# FLOAT
# a = 5.5
# b = 25.3
# c = a + b 
# print(c)
# STRING

# name = "Code Academy"
# print(name[::-1])
# # ymedacA edoC

# Conversion of types
# a = "Hello"
# b = int(a)

# name = "Code Academy"
# print(name.upper())

# Excercises 🧠
# 
# 1
# Create a program that allows user to Enter his/her name and Age
# Calculate the year in which user was born
# Print the answer to the Terminal

# name = input ("Enter you name: ")
# age = input ("Enter your age: ")
# age = int(age)
# born = 2023-age
# print(f"Your name is {name}, you are born in {born}")
      
# 2
# Create a program that allows user to enter a full sentence
# print the sentence backwards
# print every second letter in the sentence

# sentence = input ("Enter a full sentence: ")
# print(sentence[::-1])
# print(sentence[1::2])

# 3
# Create a program that expects user to enter two numbers
# multiply those numbers and print the answer
# Create similar programs with other signs.

# number_one = int(input("Enter Number 1: "))
# number_two = int(input("Enter Number 2: "))
# multiply = number_one * number_two
# print(f"Counting multiplication is: {multiply}")

# 4
# Create program that allows user to enter text
# Convert that text to Leet speak 1337
# print outcome

text = input ("Enter a text: ") #cia man nepavyko :(

# print(text.replace('a', '4'))
# print(text.replace('b', '8'))
# print(text.replace('e', '3'))
# print(text.replace('f', '7'))
# print(text.replace('g', '9'))
# print(text.replace('i', '1'))
# print(text.replace('o', '0'))
# print(text.replace('r', '2'))
# print(text.replace('s', '5'))

replaced_text = text.replace('a', '4').replace('b', '8').replace('c', '<').replace('d', '|)').replace('e', '3').replace('f', '7').replace('g', '9').replace('h', '|-|').replace('i', '1').replace('j', '|_').replace('k', '|<').replace('l', '|_').replace('m', '|V|').replace('n', '|\|').replace('o', '0').replace('p', '|o').replace('r', '|2').replace('s', '5').replace('t', '+').replace('u', '|_|').replace('v', '\/').replace('w', '\/\/').replace('x', '}{').replace('y', '\|/').replace('z', '7_')
print(replaced_text)
# text = input('Enter some text: ')   #permete Šarūnas Staskevičius ketvirtadienis 18:27
# lowercase_text = text.lower()
# replaced_text = lowercase_text.replace('a', '4').replace('b', '8').replace('c', '<').replace('d', '|)').replace('e', '3').replace('f', '7').replace('g', '9').replace('h', '|-|').replace('i', '1').replace('j', '|_').replace('k', '|<').replace('l', '|_').replace('m', '|V|').replace('n', '|\|').replace('o', '0').replace('p', '|o').replace('r', '|2').replace('s', '5').replace('t', '+').replace('u', '|_|').replace('v', '\/').replace('w', '\/\/').replace('x', '}{').replace('y', '\|/').replace('z', '7_')
# print(replaced_text)

