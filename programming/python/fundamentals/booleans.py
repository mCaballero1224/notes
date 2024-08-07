#!/usr/bin/python

# Booleans provide True/False values

is_active = True
is_admin = False

# Booleans are given when comparing numbers
greater_than = 20 > 10
print(f'20 is greater than 10: {greater_than}')

greater_than = 20 < 10
print(f'20 is less than 10: {greater_than}')

# This applies with strings
print(f'\'a\' is greather than \'b\': {'a' > 'b'}')

print(f'\'a\' is less than \'b\': {'a' < 'b'}')

# You can use the bool() function to check if a value is true/false
value = 'Hi'
truth_value = bool(value)
print(f'{value}: {truth_value}')

value = ''
truth_value = bool(value)
print(f"'': {truth_value}")

value = 100
truth_value = bool(value)
print(f'{value}: {truth_value}')

value = 0
truth_value = bool(value)
print(f'{value}: {truth_value}')

""" FALSE AND TRUTHY VALUES

The following are falsy values

    - The number zero (0)
    - An empty string
    - False
    - None
    - An empty list []
    - An empty tuple ()
    - An empty dictionary {}

Truthy values are anything that aren't the above

"""
