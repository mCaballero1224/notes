#!/usr/bin/python

import keyword

"""
    Python uses whitespace and  indentation to construct code structure. 
    No semicolons here.

    Terms:
        * Identifiers: names that ID variables, function, modules,
        classes, and objects
            - needs to begin with a letter or an underscore
        * Keywords: words with special meaning in Python (True/False,
        and, if, etc.)
"""


def string_literals():
    s = 'This is a string'
    print(s)
    s = "Another string using double quotes"
    print(s)
    s = ''' string that spans
        multiple lines '''
    print(s)


def continuation(a, b, c):
    # use backslashes to continue a statement on the next line
    if (a == True) and (b == False) and \
       (c == True):
        print("Continuation of statements")


# define main funciton to print out something
def main():
    a = True
    b = False
    c = True
    i = 1
    max = 10
    while (i < max):
        print(i)
        i += 1

    continuation(a, b, c)
    print(keyword.kwlist)  # print list of current keywords
    string_literals()


# call main function
main()
