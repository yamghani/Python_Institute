# PEP 20 (The Zen of Python)
# PEP 8 (Style Guide for Python Code)
# PEP 257 (Docstring conventions)
# how to avoid common errors and mistakes when writing code;
# how to write elegant and effective code.

# ----------------------------------------------------------------------
# Python Enhancement Proposals
# https://www.python.org/dev/peps/.
# is a collection of guidelines, best practices, descriptions of(new) features and implementations, as well as
# processes, mechanisms and important information surrounding Python.

# PEP : the language standards and provides information about many changes and processes related to Python.

# PEP 1 – PEP Purpose and Guidelines, which provides information about the purpose of PEPs, their types, and
# introduces general guidelines;
# PEP 8 – Style Guide for Python Code, which gives conventions and presents best practices for Python coding;
# PEP 20 – The Zen of Python, which presents a list of principles for Python’s design;
# PEP 257 – Docstring Conventions, which provides guidelines for conventions and semantics associated with Python
# docstrings.

# There are three different types of PEPs:
#
# Standards Track PEPs, which describe new language features and implementations;
# Informational PEPs, which describe Python design issues, as well as provide guidelines and information to the
# Python community;
# Process PEPs, which describe various processes that revolve around Python (e.g., propose changes, provide
# recommendations, specify certain procedures).

# Python’s Steering Council, i.e., a five-person committee and the final authorities who accept or reject PEPs;
# Python’s Core Developers, i.e., the group of volunteers who manage Python, and;
# Python’s BDFL, i.e., Guido van Rossum, the original creator of Python, who served as the project’s Benevolent Dictator
# For Life until 2018, when he resigned from the decision-making process.

# ----------------------------------------------------------------------
# PEP 20 -- The Zen of Python
#
# 19-line poem on the Python mailing list in 1999

import this


# ----------------------------------------------------------------------

print("A" > "a")
print(1.0 == 1)
print("1" == 1)
print(True == "1")
print(True == 1)
print(True == 1.0)
print("1" + "1")
print(1 + 1)
print(1 + "1")

integer_number = int(input("Enter an integer number: "))
# 15.6
# '15.6'
# ----------------------------------------------------------------------
# Functions, classes, objects, modules, packages… they’re all namespaces. This fact results in the following: a more
# specific namespace cannot be altered by a less specific namespace, as they reside within two different scopes
# (e.g., a local variable inside a function doesn’t influence a global variable*). However, a more specific namespace
# has access to a less specific namespace (e.g., a global variable can be accessed from within a function).

# *Using the global keyword before a global variable inside the function is a mechanism that allows you to alter
# that variable, even though it resides in a different scope (bad practice).

# good sample
# from instruments import guitars
#
# guitars.fender(page)
# guitars.ibanez(vai)

# bad sample
# from instruments.guitars import fender, ibanez
#
# fender(page)
# ibanez(vai)

# ----------------------------------------------------------------------
# PEP 8

# pycodestyle (formerly called pep8, but the name was changed to avoid confusion) - Python style guide checker;
# it lets you check your Python code for conformance with the style conventions in PEP 8. You can install the tool with
# the following command in the terminal:

# $ pip install pycodestyle


# You can also install autopep8 to automatically format your Python code to conform to the PEP 8 guidelines.
# To be able to use it, you need the pycodestyle installation on your machine in order to indicate those parts of
# the code which require formatting fixes.

# PEP 8 online is an online PEP 8 checker created by Valentin Bryukhanov which lets you paste your code or
# upload a file, and validate it against the PEP 8 style guidelines. The online tool is built using Flask,
# Twitter Bootstrap, and the PEP8 module (the very same module we’ve just described).

# http://pep8online.com/about

# ----------------------------------------------------------------------
# When writing code in Python, you should remember to follow these two simple rules:
#
# Use four spaces per indentation level, and;
# Use spaces rather than tabs.

# Note: Mixing tabs and spaces for indentation is not allowed in Python 3. This will raise a TabError exception:
# “TabError: inconsistent use of tabs and spaces in indentation”.

# For convenience, if agreed by a team (or teams) working on a given project, according to PEP 8,
# it’s possible to increase the line length to 99 characters (this does not relate to docstrings/comments,
# whose line length should still remain limited to 72 characters).
#
# Still, the Python Standard Library is conservative in this matter, and requires you to use no more than
# 79 characters per line (72 for comments/docstrings).

# it is recommended that you follow Donald Knuth’s style suggestions and break before binary operators as
# this results in a more readable, eye-friendly code.

# Example:

# Recommended

# total_fruits = (apples
#                 + pears
#                 + grapes
#                 - (black currants - red currants)
#                 - bananas
#                 + oranges)


# ----------------------------------------------------------------------

# PEP 8 states that “all identifiers in the Python standard library MUST use ASCII-only identifiers, and
# SHOULD use English words whenever feasible".

# See PEP 3131 (Supporting Non-ASCII Identifiers) for more information about the rationale as well as
# the pros and cons of using non-ASCII identifiers.


# ----------------------------------------------------------------------
# Imports
# You should always put imports at the beginning of your script, between module comments/docstrings and module globals
# and constants, respecting the following order:
#
# Standard library imports;
# Related third-party imports;
# Local application/library specific imports.
# Make sure you insert a blank line to separate each of the above groups of imports.

# Bad:

# import sys, os

# Good:

# import os
# import sys

# Still, it’s correct to make a one-line import using the from … import … syntax:
#
# from subprocess import Popen, PIPE
#
#
# If possible, use absolute imports (i.e., imports that use absolute paths separated by full stops). For example:
#
# import animals.mammals.dogs.puppies
#
#
# Such imports are preferred in Python, especially when your application is not overgrown or extremely complex.
#
# You shouldn’t (and actually you cannot) use implicit relative imports, as these are no longer present in Python 3.
# You should also avoid using wildcard imports, for example:
#
# from animals import *


# ----------------------------------------------------------------------

# However, to improve readability, PEP 8 recommends that you should try to avoid using backslashes (escape characters)
# in strings. This means that:
#
# if your string contains single-quote characters, it’s recommended that you use double-quoted strings;
# if your string contains double-quote characters, it’s recommended that you use single-quoted strings.
# In the case of triple-quoted strings, PEP 8 recommends that you always use double-quote characters to maintain
# consistency with the docstring convention detailed in PEP 257 (we’re going to tell you more about this soon).


# ----------------------------------------------------------------------

# Generally, you should avoid using single-letter names like l (the lowercase letter el), I (the uppercase letter eye),
# and O (the uppercase letter oh), because they can easily be mistaken for the numbers 1 and 0, and make your code much
# less readable.
#
# mysamplename – lowercase
# my_sample_name – lowercase with underscores (snake_case)
# MYSAMPLENAME – uppercase
# MY_SAMPLE_NAME – uppercase with underscores (SNAKE_CASE)
#
#
#
# MySampleName – CamelCase (also known as capitalized words, StudlyCaps, or CapWords)
#
# A short note: when you use acronyms, you should capitalize all the letters that make up the acronym, e.g.,
# HTTPServerError
#
# mySampleName – mixed case, which actually differs from CamelCase only by having an initial lowercase character
#
# My_Sample_Name – capitalized words with underscores (considered ugly by PEP 8)
#
# _my_sample_name – a name that starts with a single leading underscore indicates a weak "internal use", e.g.,
# the instruction from SAMPLE import * will not import objects whose names start with an underscore.
#
# my_sample_name_ -– a single trailing underscore is used by convention in order to avoid any conflicts with
#     Python keywords, e.g., class_
#
# __my_sample_name – a name that starts with a double leading underscore is used for class attributes where it invokes
# name mangling, e.g., inside the class MySampleClass, __room will become _MySampleClass__room
#
# __my_sample_name__ – a name that starts and ends with a double underscore is used for "magic" objects and attributes
# that reside in user-controlled namespaces, e.g., __init__, __import__, or __file__.
# You shouldn't create such names, but only use them as documented.

# ----------------------------------------------------------------------

# PEP 8 provides for a specific naming convention with regard to a specific identifier.
#
# When giving a name to a variable, you should use a lowercase letter or word(s), and separate words by underscores,
# e.g., x, var, my_variable. The same convention applies to global variables.
#
# Functions follow the same rules as variables, i.e., when giving a name to a function, you should use a lowercase letter
# or word(s) separated by underscores, e.g., fun, my_function.
#
# When giving a name to a class, you should adopt the CamelCase style, e.g., MySampleClass, or if
# there''s only one word, start it with a capital letter, e.g., Sample.
#
# When giving a name to a method, you should use a lowercase word or words separated by underscores, e.g., method,
# my_class_method. You should always use self for the first argument to instance methods, and cls for the first argument
# to class methods.
# When giving a name to a constant, you should use uppercase letters and separate words by underscores,
# e.g., TOTAL, MY_CONSTANT.

# When giving a name to a module, you should use a lowercase word or words, preferably short, and separate them with
#     underscores, e.g., samples.py, my_samples..
#
# When giving a name to a package, you should use a lowercase word or words, preferably short ones. You shouldnt
# separate words, e.g., package, mypackage.
#
# Type variable names should follow the CamelCase convention and be short, e.g., AnyStr, or Num.
#
# When giving a name to an exception, you should follow the same convention as with classes (bear in mind that
# exceptions should actually be classes), i.e., use the CamelCase style.
#
# Note: You can use a different style, e.g., mixed case (mySample) for functions and variables, but only if this helps
# to retain backwards compatibility, and if that's the prevailing style.

# For more detailed information about PEP 8 naming conventions, go to the PEP 8 official page:
# https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions.


# ----------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# PEP 257 (Docstring conventions)

# What should Python docstrings contain?
# How should Python docstrings be used?

# A docstring is "a string literal that occurs as the first statement in a module, function, class, or
# method definition. Such a docstring becomes the __doc__ special attribute of that object." (PEP 257)

# comments are used for commenting your code, while docstrings are used for documenting your code

# comments
# TODO: Add a function that takes the val and prc arguments.

# ----------------------------------------------------------------------

# Type hinting is a mechanism introduced with Python 3.5 and desecribed in PEP 484 that allows you to equip your code
# with additional information without using comments. It is an optional, but more formalized, feature that makes it
# possible for you to use the Python built-in typing module to provide type hint information in your code in order to
# leave certain suggestions, mark certain possible problems that may come up in the development process, and label
# specific names with type information.


# No type information added:
def hello(name):
    return "Hello, " + name


# Type information added to a function:
def hello(name: str) -> str:
    return "Hello, " + name

# You must remember that type hinting in Python is not used at runtime, which means all the type information you
# leave in the code in the form of annotations is erased when the program is executed. In other words, type hinting
# does not have any effect on the operation of your code.

# we encourage you to have a closer look at
# PEP 483 – The theory of type hints,
# PEP 484 – Type hints (information about the syntax for type annotations, static analysis and refactoring, type checking)
# PEP 3107 – Function Annotations (information about the syntax for adding metadata annotations to Python functions).

# ----------------------------------------------------------------------
#DocStrings

# they can still be extracted by some specific software tools (for more information about these, consult PEP 256,
# which provides information about Docutils, a Python Dosctring Processing System).

# attribute docstrings, which are located immediately after an assignment statement at the top level of a module
# (module attributes), class (class attributes), or the __init__ method definition of a class (instance attributes)
# . These are interpreted by the extraction tools, such as Docutils, as "the docstrings of the target of the " \
#                                                                       "assignment statement."
# (If you are interested in learning more about attribute docstrings, you are more than welcome to dive into
# PEP 224 yourself. At this point, we just want you to be aware of these.)
# additional dosctrings, which are located immediately after another docstring.
# (The original idea for additional docstrings was taken from PEP 216, which in turn was later superseded by
# PEP 287 – again, you're more than welcome to take a look at those PEPs.)


def my_function():
    """I am a docstring."""
    ...

# If you need to use any backslashes in your docstrings, then you should follow the r"""raw triple double quotes"""
# format
# If you need to use Unicode docstrings, then follow the u"""Unicode triple-quote strings""" format.

# a docstring should begin with an upper-case letter (unless an identifier begins the sentence) and end with a period;
# a docstring should prescribe the code segment's effect, not describe it. In other words, it should take the form of
# an imperative (e.g. "Do this", "Return that", "Compute this", "Convert that", etc.), not a description
# (e.g. "Does this", "Returns that", "Forms this", "Extends that", etc.). For example:

def greeting(name):
    """Take a name and return its replicated form."""
    return name * 2
# ----------------------------------------------------------------------


def king_creator(name="Greg", ordinal="I", country="Neverland"):
    """Create a king following the article title naming convention.

    Keyword arguments:
    :arg name: the king's name (default: Greg)
    :type name: str
    :arg ordinal: Roman ordinal number (default: I)
    :type ordinal: str
    :arg country: the country ruled (default: Neverland)
    :type country: str
    """
    if name == "Voldemort":
        return "Voldemort is a reserved name."
    ...


class Vehicle:
    """A class to represent a Vehicle.

    Attributes:
    -----------
    vehicle_type: str
        The type of the vehicle, e.g. a car.
    id_number: int
        The vehicle identification number.
    is_autonomous: bool
        self-driving -> True, not self-driving -> False


    Methods:
    --------
    report_location(lon=45.00, lat=90.00)
        Print the vehicle id number and its current location.
        (default longitude=45.00, default latitude=90.00)
    """

    def __init__(self, vehicle_type, id_number, is_autonomous=True):
        """
        Parameters:
        -----------
        vehicle_type: str
            The type of the vehicle, e.g. a car.
        id_number: int
            The vehicle identification number.
        is_autonomous: bool, optional
            self-driving -> True (default), not self-driving -> False
        """

        self.vehicle_type = vehicle_type
        self.id_number = id_number
        self.is_autonomous = is_autonomous

    def report_location(self, id_number, lon=45.00, lat=90.00):
        """
        Print the vehicle id number and its current location.

        Parameters:
        -----------
        id_number: int
            The vehicle identification number.
        lon: float, optional
            The vehicle's current longitude (default is 45.00)
        lat: float, optional
            The vehicle's current latitude (default is 90.00)
        """

    ...
    ...
    ...


# Docstring formatting types
# You may have noticed that we have used two different docstring formats for documenting the king_creator() function
# and the Vehicle class. The first type of formatting is called reStructuredText, and it's the official Python ' \
#         'documentation standard explained and described in PEP 287. The second example uses the NumPy/SciPy docstrings' \
#         ' format (for details, click here, which is a combination of the Google docstrings format and the ' \
#         'reStructuredText format.
#
# Both formatting types are good for the purposes of creating formal documentation, and both of them are supported
# by Sphinx, one of the most popular Python documentation generators.
#
# Sphinx is a great tool for creating documentation for software development projects. It uses reStructuredText as
# its markup language, and has a lot of useful features, such as supporting the HTML output format, automatic testing
# of code snippets, extensive cross-references, and a hierarchical structure, which lets you define a document tree.
# Check it out.

# Generally, a project should contain the following documentation elements:
#
# a readme, which provides a brief summary of the project, its purpose, and possibly some installation guidelines;
# an examples.py file, which is a script that demonstrates a few examples of how to utilize the project;
# a license in the form of a txt file (particularly important for Open Source and Public Domain projects)
# a how to contribute file which provides information about the possible ways of contributing to the project
# (shared, open source, and public domain projects).


# ----------------------------------------------------------------------

# Right. But what is a linter? Well, it's a tool that helps you write your code, because it analyzes it for any
# stylistic anomalies and programming errors against a set of pre-defined rules. ' \
#                                      'In other words, it's a program that analyzes your code and reports such
# issues as structural and syntax errors, consistency breakups, and a lack of compatibility with best practices or
# code style guidelines such as PEP 8. The most popular linters are: Flake8, Pylint, Pyflakes, Pychecker, Mypy, and
# Pycodestyle (formerly Pep8) – the official linter tool to check Python code against PEP 8 conventions.
#
# A fixer, on the other hand, is a program that helps you fix these issues and format your code to be consistent with
#     the adopted standards. The most popular fixers are: Black, YAPF, and autopep8.

# https://pypi.org/project/black/
# https://github.com/PyCQA/pycodestyle
# https://flake8.pycqa.org/en/latest/


def my_fun(a, b):
    """The summary line goes here.

    A more elaborate description of the function.

    Parameters:
    a: int (description)
    b: int (description)

    Returns:
    int: Description of the return value.
    """
    return a*b

print(my_fun.__doc__)
help(my_fun)