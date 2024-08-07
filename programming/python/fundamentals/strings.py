#!/usr/bin/python

""" INTRO TO PYTHON STRING """

message = 'This is a string in Python'
message = "This is also a string."

# Use double quotes for strings containing single quotes
message = "It's a Eva!"

# For strings containing double quotes, you can wrap them in single quotes
message = '"Beautiful is better than ugly.". Said Tim Peters'

# Use a backslash to escape quotes
message = 'It\'s another Eva!'

"""
    The python interpreter will treat the backslash character special. You can
    override that with a raw string.
"""
message = r'C:\python\bin'

""" CREATING MULTILINE STRINGS """

# Use triple-quotes for multline strings
help_message = '''
Usage: mysql command
    -h hostname
    -d database name
    -u username
    -p password
'''

print(help_message)

""" USING VARIABLES IN STRINGS """

# f-strings allow the use of variables within a string
name = 'Michael'
message = f'Hello, {name}.'
print(message)

# CONCATENATING STRINGS

# Python will automatically concatenate strings placed next to each other
greeting = 'Good ' 'Morning!'
print(greeting)

# You can achieve the same effect with the `+` operator
greeting = 'Good'
time = 'Afternoon'
greeting = greeting + time + '!'

"""
    ACCESSING STRING ELEMENTS

    Strings are a sequence of characters, and individuals characters can be
    accessed like you would access elements of an array.
"""

str = "Python String"
print(str[0])  # Output: P
print(str[1])  # Output: y

# Negative indexes returns the character starting from the end of the string
print(str[-1])  # Output: g
print(str[-2])  # Output: n

"""
    The following illustrates the indexes of the string "Python String"

    +---+---+---+---+---+---+---+---+---+---+---+---+---+
    | P | y | t | h | o | n |   | S | t | r | i | n | g |
    +---+---+---+---+---+---+---+---+---+---+---+---+---+
      0   1   2   3   4   5   6   7   8   9   10  11  12
    -13 -12 -11 -10  -9  -8  -7  -6  -5  -4   -3  -2  -1

"""

# GETTING THE LENGTH OF A STRING

str_len = len(str)
print(str_len)

"""
    SLICING STRINGS

    Slicing allows you to pull a substring from a string.

    Slicing syntax:
        string[start:end]

    Note that the start is inclusive, while the end is exclusive. You can
    also omit either value. `start` defaults to 0, while `end` defaults to
    the string's length.
"""

print(str[0:2])  # Output: Py


"""
    PYTHON STRINGS ARE IMMUTABLE

    This means you can't change the contents of a string. The following
    python statement will cause an error.

    str[0] = 'J'

    To change the contents of a string, you need to create a new one from the
    existing string.
"""

new_str = 'J' + str[1:]
print(new_str)  # Output: Jython String
