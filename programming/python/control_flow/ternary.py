#!/usr/bin/python

""" TERNARY OPERATOR

    The ternary operator allows you to shorten the syntax of an if-else
    statement, making the conditional assignment of values easier.

    The following program prompts the user for their age and determines the
    ticket price based on it.
"""


def main():
    age = input("Enter your age: ")
    """
        This statement can be read as:

        If age is greather than or equal to 18, set the price to $20, otherwise
        set it to $5.
    """
    # variable = (value) if (condition) else (other value)
    price = 20 if int(age) >= 18 else 5
    print(f'Your ticket price is: ${price}.')


if __name__ == "__main__":
    main()
