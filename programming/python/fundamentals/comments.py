#!/usr/bin/python

"""
    It's important to document stuff. The you of one-week ago may have been
    brain diseased or something. Doucmenting what you're doing allows you to
    pick up where you left off and while also contemplating on what the hell
    you were thinking a week ago.
"""

# Python comments start with a single hash symbol

# increase price by 5%
price = 3.00
price = price * 1.05

salary = 30000.00
#  increase salary by 2%
salary = salary * 1.02

""" PYTHON DOCSTRINGS

    Docstrings are special in that they can be accessed at run-time via the
    `obj.__doc__` attribute where `obj` is the name of the function. They're
    not technically comments, but reference the strings that contain
    documentation. They're not ignored by the interpreter.

    It can be read by your LSP to provide the documentation for a function as
    you're writing it.
"""

""" ONE-LINE DOCSTRINGS """


def quicksort():
    """ sort the list using quicksort algorithm """
    pass


""" MULTI-LINE DOCSTRINGS """


def increase(salary, rating):
    """ increase salary based on rating and percentage
    rating 1 - 2: no salary increase
    rating 3 - 4: increase 5%
    rating 5 - 6: increase 10%
    """
    percentage = 0
    if rating >= 3:
        percentage = 0.05
    if rating >= 5:
        percentage = 0.10
    return salary * percentage
