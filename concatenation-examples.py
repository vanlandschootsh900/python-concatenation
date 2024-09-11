# Student name
# Current date
# String Concatenation in Python

# Example 1

phrase1 = "Hello, everyone! How "

phrase2 = "are you doing today?"

full_sentence = phrase1 + phrase2

print(full_sentence)


# Example 2
# Assigning a string value to each variable

first_name = "Mike"
last_name = "Jenkins"

# Can also use single quotes to assign a string to
# a variable

# first_name = 'Mike'
# last_name = 'Jenkins'

# Concatenation means 'to join'

# Use the concatenation operator to join two strings
# and a blank space

# Remember to add a blank space to make output
# look nice

fullName = first_name + last_name

# fullName = first_name + " " + last_name

# Print my full name
print ("My full name is: " + fullName)


# Example 3: f-strings
# A more modern alternative to concatenation
person = "Bob"
greeting = f"Hi, {person}! How are you doing today?"
print(greeting)  # Output: Hi, Bob! How are you doing today?


# Example 4
# When using concatenation, you can't embed numeric data (numbers) directly into a Python string
# You must convert the numeric data to string data first before you can embed it in a string
age = 21 # A piece of numeric data (a number)
friend = 'Jason'
# Note the spaces I added to make the string look nice when it displays
birthday_wish = 'We wish you a happy birthday, ' + friend + ' because you are turning ' + str(age) + ' years old today.'
print(birthday_wish)
