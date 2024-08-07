#!/usr/bin/python

# To get user input, use the input() function
# input() only returns strings
accumulator = 0
value = input("Enter a number: ")
# You can get around this by using the int() function
value = int(value)


print(f'{accumulator} + {value} = {accumulator + value}')
accumulator += value
value = input("Enter a number: ")
value = int(value)

print(f'{accumulator} + {value} = {accumulator + value}')

"""
    The following type conversion functions are also available in Python

    - float(str) - convert string -> float
    - bool(val) - convert value -> boolean
    - str(val) - converts val -> string

"""

# You can use the type() function to get the type of a value
print(f'Type of {10}: {type(10)}')
