"""PEP8 Styling Helper

This file displays some examples of proper PEP8 styling.

All examples provided were created using the PEP8 styling guide, which can be
found @ "https://www.python.org/dev/peps/pep-0008/".

NOTE: PEP8 calls inline comments distracting, but sometimes useful, which is
why they are used in this file to showcase styling preferences.

To make PEP8 implementation and enforcement easier, see the reference docs for
the flake8 tool @ "https://flake8.pycqa.org/en/latest/".
"""

################################  CODE LAYOUT  ################################

import sys                    # Imports should be at the beginning of the file.
import random                 # Imports should be on separate lines, unless
from Math import ceil, floor  # they are from the same library.


def long_function_name(var_one, var_two,        # Separate arguments over
                       var_three, var_four):    # multiple lines, start at the
    print (var_one)                             # same left side location.


def proper_indentation():    # Standard indentation is 4-spaces per level.
    return None


def display_proper_indentation(
        first_var, second_var, third_var,  # If the line will carry over,
        fourth_var):                       # indent an extra level so that the
    return "Much Better"                   # next line has a clear start point.


my_list = [
    1, 2, 3, 4,             # Separate long lists out to clearly see
    5, 6, 7, 8              # all the contents.
]

income = (gross_wages                # Placing the operator at the beginning of
          + taxable_interest         # the line, which is much easier to read.
          + (divs - qualified_divs)
          - ira_deduction
          - student_loan_interest)


def display_proper_indentation(
        first_var
        ,second_var
        ,third_var   # If the line will carry over,
        ,fourth_var):                        # indent an extra level to the next
    fourth_var = "Much Better"              # line has a clear beginning.


#########################  BLANK LINES AND WHITESPACE  ########################


def foo_bar(arg1, arg2, arg3):   # Spaces inbetween function arguments.
    return arg1, arg2, arg3
                            # Two empty lines surrounding top level functions.

def bar(arg1, arg2, arg3):     # No whitespace after function name.
    print([arg1+arg2, arg3])  # No whitespace for + inside of function calls.
    return arg1 + arg2         # Spaces around operators out of function calls.


class Lesson:               # Two empty lines preceeding class declarations.
    def one(self):          # Avoid whitespace during function declaration.
        return 1
                            # One empty line between class functions.
    def two(self):          # No extra whitespace.
        rerturn 2


my_dictionary = {"Name": "Brandon", "Age": 33}  # Spaces after colons.
correct = "like this"       # No unecessary whitespace after variable name.
name = my_dict["Name"]      # Spaces around assignment operator (=).

if (1 < 2):                 # Spaces surrounding logic operators.
    print ('It works!')     # Compound statements are generally discouraged.

#############################  NAMING CONVENTIONS  ############################

my_variable = "value"       # Use lower case with underscore for variables.


def my_function():          # As well as functions.
    pass


class UseThisConvention(object):  # CapWords is used for class names.
    pass


CONSTANT = "value"          # Uppercase should be used for constant variables.

L = "Ah, it's L!"           # Avoid interpretable single character assignment.
