#!/usr/bin/python

""" COMMAND PROMPT

    This program uses a while loop to evaluate user input, creating a simple
    command prompt.
"""


def help_message():
    pass


while True:
    command = input('> ').lower()
    if (command == 'quit'):
        print('Exiting program...')
        break
    print(f"Echo: {command}")
