#!/usr/bin/python

""" FOR LOOPS

    For loops allow you to execute a block of code multiple times.

"""

for index in range(10):
    print(f'Index: {index}')

# What is range(10)? Let's find out!
print(range(10))

# A range() function returns an Object that gives a range of integers

# You can define the stop/start of the range function
for index in range(1, 6):
    print(f'Index: {index}')

# You can also define the "step" of the range function
for index in range(0, 11, 2):
    print(f'Index: {index}')

# Using for loop to calculate the sum of a sequence
accumulator = 0  # variable to hold the sum
for num in range(101):
    accumulator += num

print(f'Sum: {accumulator}')

# If you're a math nerd, you can use this formula as well
n = 100
sum = n * (n+1)/2
print(f'Sum: {sum}')


""" WHILE LOOPS

    While loops allow for the execution of code numerous times based on 
    a condition.

"""

max = 5
counter = 0

while counter < max:
    print(f'Counter: {counter}')
    counter += 1


""" USING BREAK

    The `break` keyword allows you to exit a loop prematurely regardless of 
    the conditional test of the loop.
"""

for x in range(5):
    for y in range(5):
        if y > 2:
            break
        print(f'({x}, {y})')


""" USING CONTINUE

    The `continue` statement skips the current iteration of the loop and
    continues onto the next iteration.
"""

# Print even numbers
for index in range(10):
    if index % 2:
        continue
    print(f'Index: {index}')

# print odd numbers
counter = 0
while counter < 10:
    counter += 1
    if not counter % 2:
        continue
    print(f'Counter: {counter}')


""" USING PASS

    The `pass` statment does...nothing. Absolutely nothing. It can be pretty
    useful when you're programming something, and need a placeholder function
    until you're ready to write the logic.

    For example:

    if counter <= max:
        counter += 1
    else:
        # implement later


    The above code would give a Syntax error since there's nothing in the else
    statement.

"""

# The following code uses the `pass` statment to prevent a SyntaxError
for i in range(1, 100):
    pass


# Placeholder function
def test_function():
    pass
