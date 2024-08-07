#!/usr/bin/python

""" IF

    In instances where you want to run a snippet of code ONLY when a certain
    condition is true or false, you can use the if statement like so.
"""

# Get user input
value = input("Enter a number: ")

# Convert user input into an integer
value = int(value)

# Create a boolean based on user input
condition = value > 100

# If the condtion is true, run the indented code
if (condition):
    print(f'{value} is greater than 100!')

""" ELSE

    Use the else statement to run code when the condition of your else
    statement is false"
"""

value = input("Enter another number: ")
value = int(value)

condition = value < 20

if (condition):
    print(f"{value} is less than 20")
else:
    print(f"{value} is greather than 20")


""" ELIF

    Additionally, you can use the elif statement to add another condition
    that your code can account for.
"""

value = input("Enter another number: ")
value = int(value)

if (value > 100):
    print(f'{value} is greater than 100')
elif (value < 100 and value > 0):
    print(f'{value} is less than 100 and greater than 0')
else:
    print(f'{value} is less than or equal to 0')
