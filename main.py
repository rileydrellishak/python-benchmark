# Beneath each comment write the code and print out the result to check it works

'''LISTS'''

# Create a list and assign it to a variable
fruits = ['orange', 'raspberry', 'grape', 'apple', 'banana']

# Find the length of the list
len(fruits)

# Append an item to the list
fruits.append('strawberry')

# Find the value of an item in the list a specific index
third_item = fruits[2]

# Set the value of an item at a specific index
fruits[1] = 'cherry'

# Check whether an item is in the list
print('cherry' in fruits)
print('raspberry' in fruits)

# Sort the list
fruits.sort()

# Iterate over the list using range, printing out each element and the index
for i in range(0, len(fruits)):
    print(fruits[i])

# Iterate over the list without using range, printing out each element
for fruit in fruits:
    print(fruit)

'''TUPLES'''

# Create a tuple and assign it to a variable
veggies = 'broccoli', 'carrot', 'zucchini', 'pepper', 'celery'

# Find the length of the tuple
len(veggies)

# Find the value of an item in the tuple a specific index
second_item = veggies[1]

# Check whether an item is in the tuple
print('broccoli' in veggies)
print('pumpkin' in veggies)

# Iterate over the tuple using range, printing out each element and the index
for i in range(0, len(veggies)):
    print(veggies[i])

# Iterate over the tuple without using range, printing out each element
for veggie in veggies:
    print(veggie)

'''STRINGS'''

# Create a string and assign it to a variable
name = 'riley'

# Find the length of the string
len(name)

# Find the value of an character in the string a specific index
fifth_character = name[4]
last_character = name[-1]

# Check whether an item is in the string
print('e' in name)
print('q' in name)

# Concatenate (add) two strings together
name_2 = 'elizabeth'
first_middle_name = name + " " + name_2

# Create an f-string
f"{name} is my first name!"

# Split a string using .split
split_this = "my name is riley"
split_this.split(" ")
print(split_this.split(" "))

# Join a list of strings using .join
string_1 = 'what'
string_2 = 'name'
print(' '.join([string_1, string_2]))

# Iterate over the string using range, printing out each character and the index
for i in range(0, len(name)):
    print(name[i], i)

# Iterate over the string without using range, printing out each character
for character in name:
    print(character)
    
'''DICTIONARIES'''

# Create a dictionary and assign it to a variable

# Find the length of the dictionary

# Add a new key/value pair

# Replace value for a given key

# Check whether a key is in the dictionary

# Iterate over keys, printing each key

# Iterate over over key/value pairs using .items(), printing each key and value

'''SETS'''

# Create a set and assign it to a variable

# Find the length of the set

# Add a new element

# Remove an element

# Check whether a element is in the set

# Iterate over elements, printing each one out

'''NUMBERS'''

# Add / subtract / multiply 2 numbers

# Divide two numbers using normal (float) division

# Divide two numbers using integer division

# Find the modulo (remainder) of two numbers

# Check whether a number is even/odd

# Round a float down to an int


'''FUNCTIONS'''

# Write a function that takes no arguments and call it

# Write a function that takes one or more arguments and call it

# Write a function that returns a value. Call the function and store the return value in a variable

'''LOOPS'''

# Write a while loop

# Write a for loop that loops a set number of times (e.g. 10 times)

'''CONDITIONALS'''

# Write an if/elif/else statement

# Write conditionals for the following operators:
# ==
# !=
# <
# >
# <=
# >=

'''NESTED DATA'''

# Write a nested list (a list of lists) and assign it to a variable

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second

# Iterate through the nested data structure using range

# Iterate through the nested data structure without using range 

'''REMINDER'''

# You're doing great and you got this!
