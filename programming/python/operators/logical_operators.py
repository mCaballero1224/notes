#!/usr/bin/python

""" LOGICAL OPERATORS

    Logical operators are good for checking multiple conditions at once.
    Python provides three logical operators:

    - and
    - or
    - not
"""

a = 1 == 1
b = 1 > 2

""" AND
    Returns True when both conditions are true. Returns False otherwise.
"""
print(a and b)  # Output: False ( a is true, b is not )

""" OR
    Returns True when either condition is true. Returns False when neither are.
"""
print(a or b)  # Output: True

""" NOT
    Returns True when the condition is false. Returns True otherwise.
    You can also think about this like a negation.
"""
print(not a)  # Output: False
print(not b)  # Output: True
