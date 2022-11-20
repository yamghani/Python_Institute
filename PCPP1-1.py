# class — an idea, blueprint, or recipe for an instance;
# instance — an instantiation of the class; very often used interchangeably with the term 'object';
# object — Python's representation of data and methods; objects could be aggregates of instances;
# attribute — any object or class trait; could be a variable or method;
# method — a function built into a class that is executed on behalf of the class or object; some say that it’s a
# 'callable attribute';
# type — refers to the class that was used to instantiate the object.


# creation and use of decorators;
# implementation of core syntax;
# class and static methods;
# abstract methods;
# comparison of inheritance and composition;
# attribute encapsulation;
# exception chaining;
# object persistence;
# metaprogramming.

# ----------------------------------------------------------------------

# A class expresses an idea; it’s a blueprint or recipe for an instance.
# A class is a place which binds data with the code.

class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')


# An instance is one particular physical instantiation of a class that occupies memory and has data elements.

# An attribute is a capacious term that can refer to two major kinds of class traits:
#
# variables, containing information about the class itself or a class instance; classes and class instances can own
# many variables;
# methods, formulated as Python functions; they represent a behavior that could be applied to the object.


class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')


duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

drake.quack()
print(duckling.height)

# Information about an object’s class is contained in __class__.

print(Duck.__class__)
print(duckling.__class__)
print(duckling.sex.__class__)
print(duckling.quack.__class__)


# <class 'type'>
# <class '__main__.Duck'>
# <class 'str'>
# <class 'method'>

# ----------------------------------------------------------------------
# Instance variables
#
# This kind of variable exists when and only when it is explicitly created and added to an object.

class Demo:
    def __init__(self, value):
        self.instance_var = value


d1 = Demo(100)
d2 = Demo(200)

print("d1's instance variable is equal to:", d1.instance_var)
print("d2's instance variable is equal to:", d2.instance_var)


# it lists the contents of each object, using the built-in __dict__ property that is present for every Python object.

class Demo:
    def __init__(self, value):
        self.instance_var = value


d1 = Demo(100)
d2 = Demo(200)

d1.another_var = 'another variable in the object'

print('contents of d1:', d1.__dict__)
print('contents of d2:', d2.__dict__)


# Class variables are defined within the class construction, so these variables are available before any
# class instance is created.
# To get access to a class variable, simply access it using the class name
# it is used :
# fixed information like description, configuration, or identification values;
# mutable information like the number of instances created

class Demo:
    class_var = 'shared variable'


print(Demo.class_var)
print(Demo.__dict__)


# as the class variable is defined outside the object, it is not listed in the object's __dict__

class Demo:
    class_var = 'shared variable'


d1 = Demo()
d2 = Demo()

print(Demo.class_var)
print(d1.class_var)
print(d2.class_var)

print('contents of d1:', d1.__dict__)


class Demo:
    class_var = 'shared variable'


d1 = Demo()
d2 = Demo()

# both instances allow access to the class variable
print(d1.class_var)
print(d2.class_var)
print('.' * 20)

# d1 object has no instance variable
print('contents of d1:', d1.__dict__)
print('.' * 20)

# d1 object receives an instance variable named 'class_var'
d1.class_var = "I'm messing with the class variable"


# d1 object owns the variable named 'class_var' which holds a different value than the
# class variable named in the same way
print('contents of d1:', d1.__dict__)
print(d1.class_var)
print('.' * 20)

# d2 object variables were not influenced
print('contents of d2:', d2.__dict__)

# d2 object variables were not influenced
print('contents of class variable accessed via d2:', d2.class_var)


# ----------------------------------------------------------------------
# each class owns information that helps identify the class instance origins. Similar functionality could be
# achieved with the isinstance() function

class Duck:
    counter = 0
    species = 'duck'

    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex
        Duck.counter += 1

    def walk(self):
        pass

    def quack(self):
        print('quacks')


class Chicken:
    species = 'chicken'

    def walk(self):
        pass

    def cluck(self):
        print('clucks')


duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

chicken = Chicken()

print('So many ducks were born:', Duck.counter)

for poultry in duckling, drake, hen, chicken:
    print(poultry.species, end=' ')
    if poultry.species == 'duck':
        poultry.quack()
    elif poultry.species == 'chicken':
        poultry.cluck()


# Another example shows that a class variable of a super class can be used to count the number of all objects created
# from the descendant classes (subclasses).

class Phone:
    counter = 0

    def __init__(self, number):
        self.number = number
        Phone.counter += 1

    def call(self, number):
        message = 'Calling {} using own number {}'.format(number, self.number)
        return message


class FixedPhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        FixedPhone.last_SN += 1
        self.SN = 'FP-{}'.format(FixedPhone.last_SN)


class MobilePhone(Phone):
    last_SN = 0

    def __init__(self, number):
        super().__init__(number)
        MobilePhone.last_SN += 1
        self.SN = 'MP-{}'.format(MobilePhone.last_SN)


print('Total number of phone devices created:', Phone.counter)
print('Creating 2 devices')
fphone = FixedPhone('555-2368')
mphone = MobilePhone('01632-960004')

print('Total number of phone devices created:', Phone.counter)
print('Total number of mobile phones created:', MobilePhone.last_SN)

print(fphone.call('01632-960004'))
print('Fixed phone received "{}" serial number'.format(fphone.SN))
print('Mobile phone received "{}" serial number'.format(mphone.SN))

# ----------------------------------------------------------------------

# This is Python core syntax – an ability to perform specific operations on different data types, when operations are
# formulated using the same operators or instructions, or even functions.
#
#
# Python core syntax covers:
#
# operators like '+', '-', '*', '/', '%' and many others;
# operators like '==', '<', '>', '<=', 'in' and many others;
# indexing, slicing, subscripting;
# built-in functions like str(), len()
# reflexion – isinstance(), issubclass()

# The name of each magic method is surrounded by double underscores (Pythonistas would say
# “dunder” for double underscores
# , as it’s a shorter and more convenient phrase). Dunders indicate that such methods are not called directly,
# but called in a process of expression evaluation, according to Python core syntax rules.

number = 10
print(number + 20)

number = 10
print(number.__add__(20))


# Error in adding two objects in the following

class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, other):
        return self.weight + other.weight


p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

print(p1 + p2)


# __add__() method does not change any object attribute values – it just returns a value that is the result of adding
# the appropriate attribute values.

class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, other):
        return self.weight + other.weight


p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

print(p1 + p2)


# ----------------------------------------------------------------------

# The dir() function gives you a quick glance at an object’s capabilities and returns a list of the attributes and
# methods of the object. When you call dir() on integer 10, you'll get:
#
# >>> dir(10)
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__',
# '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
# '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__',
# '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__',
# '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__',
# '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
# '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__',
#  '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate',
#  'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

# To get more help on each attribute and method, issue the help() function on an object, as below:

# >>> help(10)
# Help on int object:
#
# class int(object)
#  |  int([x]) -> integer
#  |  int(x, base=10) -> integer
#  |...

# ----------------------------------------------------------------------
# Python core syntax expressions

# The following tables help you in situations where you like to implement a custom method for a Python core operation

# Comparison methods
# Function or operator	Magic method	Implementation meaning or purpose
# ==	__eq__(self, other)	equality operator
# !=	__ne__(self, other)	inequality operator
# <	    __lt__(self, other)	less-than operator
# >	    __gt__(self, other)	greater-than operator
# <=	__le__(self, other)	less-than-or-equal-to operator
# >=	__ge__(self, other)	greater-than-or-equal-to operator
# Numeric methods
# Unary operators and functions
# Function or operator	Magic method	Implementation meaning or purpose
# +	            __pos__(self)	unary positive, like a = +b
# -	            __neg__(self)	unary negative, like a = -b
# abs()	        __abs__(self)	behavior for abs() function
# round(a, b)	__round__(self, b)	behavior for round() function
#
# Common, binary operators and functions
# Function or operator	Magic method	Implementation meaning or purpose
# +	    __add__(self, other)	addition operator
# -	    __sub__(self, other)	subtraction operator
# *	    __mul__(self, other)	multiplication operator
# //	__floordiv__(self, other)	integer division operator
# /	    __div__(self, other)	division operator
# %	    __mod__(self, other)	modulo operator
# **	__pow__(self, other)	exponential (power) operator
# Augmented operators and functions
# By augmented assignment we should understand a sequence of unary operators and assignments like a += 20
#
# Function or operator	Magic method	Implementation meaning or purpose
# +=	__iadd__(self, other)	addition and assignment operator
# -=	__isub__(self, other)	subtraction and assignment operator
# *=	__imul__(self, other)	multiplication and assignment operator
# //=	__ifloordiv__(self, other)	integer division and assignment operator
# /=	__idiv__(self, other)	division and assignment operator
# %=	__imod__(self, other)	modulo and assignment operator
# **=	__ipow__(self, other)	exponential (power) and assignment operator


# Type conversion methods
# Python offers a set of methods responsible for the conversion of built-in data types.
#
# Function	Magic method	Implementation meaning or purpose
# int()	    __int__(self)	conversion to integer type
# float()	__float__(self)	conversion to float type
# oct()	    __oct__(self)	conversion to string, containing an octal representation
# hex()	    __hex__(self)	conversion to string, containing a hexadecimal representation
# Object introspection
# Python offers a set of methods responsible for representing object details using ordinary strings.
#
# Function	Magic method	Implementation meaning or purpose
# str()	    __str__(self)	responsible for handling str() function calls
# repr()	__repr__(self)	responsible for handling repr() function calls
# format()	__format__(self, formatstr)	called when new-style string formatting is applied to an object
# hash()	__hash__(self)	responsible for handling hash() function calls
# dir()	    __dir__(self)	responsible for handling dir() function calls
# bool()	__nonzero__(self)	responsible for handling bool() function calls
# Object retrospection
# Following the topic of object introspection, there are methods responsible for object reflection.
#
# Function	Magic method	Implementation meaning or purpose
# isinstance(object, class)	    __instancecheck__(self, object)	responsible for handling isinstance() function calls
# issubclass(subclass, class)	__subclasscheck__(self, subclass)	responsible for handling issubclass() function calls
#
# Object attribute access
# Access to object attributes can be controlled via the following magic methods
#
# Expression example	Magic method	Implementation meaning or purpose
# object.attribute	        __getattr__(self, attribute)	responsible for handling access to a non-existing attribute
# object.attribute	        __getattribute__(self, attribute)	responsible for handling access to an existing attribute
# object.attribute = value	__setattr__(self, attribute, value)	responsible for setting an attribute value
# del object.attribute	    __delattr__(self, attribute)	responsible for deleting an attribute
# Methods allowing access to containers
# Containers are any object that holds an arbitrary number of other objects; containers provide a way to access the
# contained objects and to iterate over them. Container examples: list, dictionary, tuple, and set.
#
# Expression example	Magic method	Implementation meaning or purpose
# len(container)	        __len__(self)	returns the length (number of elements) of the container
# container[key             __getitem__(self, key)	responsible for accessing (fetching) an element identified by
#                                                   the key argument
# container[key] = value	__setitem__(self, key, value)	responsible for setting a value to an element identified by
# the key argument
# del container[key]	    __delitem__(self, key)	responsible for deleting an element identified by the key argument
# for element in container	__iter__(self)	returns an iterator for the container
# item in container	        __contains__(self, item)	responds to the question: does the container contain the
#                                                       selected item?
# The list of special methods built-in in Python contains more entities.
#
# For more information, refer to https://docs.python.org/3/reference/datamodel.html#special-method-names.

# ----------------------------------------------------------------------
# class and static methods;

# Inheritance creates a class hierarchy. Any object bound to a specific level of class hierarchy inherits all the
# traits (methods and attributes) defined inside any of the superclasses.

# Each subclass is more specialized (or more specific) than its superclass. Conversely,
# each superclass is more general (more abstract) than any of its subclasses.

# a single inheritance class is always simpler, safer, and easier to understand and maintain;
# multiple inheritance may make method overriding tricky; moreover, using the super() function can lead to ambiguity;
# it is highly probable that by implementing multiple inheritance you are violating the single responsibility principle;


# MRO — Method Resolution Order
# diamond problem, or  the deadly diamond of death

#        A
#    /        \
# B             C
#     \      /
#        D

# In the multiple inheritance scenario, any specified attribute is searched for first in the current class.
# If it is not found, the search continues into the direct parent classes in depth-first level (the first level above),
# from the left to the right, according to the class definition. This is the result of the MRO algorithm.

class A:
    def info(self):
        print('Class A')


class B(A):
    def info(self):
        print('Class B')


class C(A):
    def info(self):
        print('Class C')


class D(B, C):
    pass


D().info()


# Python finds the requested method in the class B definition and stops searching;


# MRO can report definition inconsistencies when a subtle change in the class D definition is introduced

class D(A, C):
    pass


# This message informs us that the MRO algorithm had problems determining which method
# (originating from the A or C classes) should be called.


class D(B, C):
    pass


class E(C, B):
    pass


E().info()

# As a result, those classes can behave totally differently, because the order of the superclasses is different.

# ----------------------------------------------------------------------
# Polymorphism

# In Python, polymorphism is the provision of a single interface to objects of different types. In other words,
# it is the ability to create abstract methods from specific types in order to treat those types in a uniform way.


# >>> dir(1)
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', ...
# >>> dir('a')
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', ...

# there are many attributes available for the string and integer types, many of them carrying the same names.
# The first name common to both lists is __add__, which is a special method responsible for handling addition

a = 10
print(a.__add__(20))
b = 'abc'
print(b.__add__('def'))


# By the way, if you look for a method that is used when you print a value associated with an object,
# the __str__ method is called to prepare a string that is used in turn for printing.


# One way to carry out polymorphism is inheritance, when subclasses make use of base class methods, or override them

# inheritance: class Radio inherits the turn_on() method from its superclass —
# that is why we see The device was turned on string twice. Other subclasses override that method
# and as a result we see different lines being printed;
#
# polymorphism: all class instances allow the calling of the turn_on() method, even when you refer to the objects
# using the arbitrary variable element.


# Duck Typing

# Duck typing is another way of achieving polymorphism, and represents a more general approach than polymorphism
# achieved by inheritance. When we talk about inheritance, all subclasses are equipped with methods named the same way
# as the methods present in the superclass.

# In duck typing, we believe that objects own the methods that are called. If they do not own them, then we should be
# prepared to handle exceptions.

class Wax:
    def melt(self):
        print("Wax can be used to form a tool")


class Cheese:
    def melt(self):
        print("Cheese can be eaten")


class Wood:
    def fire(self):
        print("A fire has been started!")


for element in Wax(), Cheese(), Wood():
    try:
        element.melt()
    except AttributeError:
        print('No melt() method')

# Unfortunately, the Wood class is not equipped with this method, so an AttributeError exception occurs.

# ----------------------------------------------------------------------
# we can pass arguments in any order if we are assigning keywords to all argument values,
# otherwise positional ones are the first ones on the arguments list.

# functions that can accept any arbitrary number of positional arguments and keyword arguments
# The most basic example is a print() function:

# print
print()
print(3)
print(1, 20, 10)
print('--', '++')

# list
a_list = list()
b_list = list(10, 20, 43, 54, 23, 23, 34, 23, 2)
b_list = list((10, 20, 43, 54, 23, 23, 34, 23, 2))

print(a_list)
print(b_list)


# Python functions deal with a variable number of arguments : *args and **kwargs

# These two special identifiers (named *args and **kwargs) should be put as the last two parameters in a function
# definition. Their names could be changed because it is just a convention to name them 'args' and 'kwargs',
# but it’s more important to sustain the order of the parameters and leading asterisks.

# *args refers to a tuple of all additional, not explicitly expected positional arguments, so arguments passed without
# keywords and passed next after the expected arguments.
# collects all unmatched positional arguments;

# **kwargs refers to a dictionary of all unexpected arguments that were passed in the form of keyword=value pairs.
# Likewise, **kwargs collects all unmatched keyword arguments.


def combiner(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    # print(args[0])
    print(kwargs, type(kwargs))
    # print(kwargs['argument1'])


combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')


# To forward arguments


def combiner(a, b, *args, **kwargs):
    super_combiner(*args, **kwargs)
    # if we remove asteriks all is captured by my_args
    print(args)
    print(kwargs)
    super_combiner(args, kwargs)


def super_combiner(*my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_kwargs', my_kwargs)


combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')


# how to combine *args, a key word, and **kwargs in one definition:


def combiner(a, b, *args, c=20, **kwargs):
    super_combiner(c, *args, **kwargs)


def super_combiner(my_c, *my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_c:', my_c)
    print('my_kwargs', my_kwargs)


combiner(1, '1', 1, 1, c=2, argument1=1, argument2='1')


# ----------------------------------------------------------------------
# Decorating

# A decorator is one of the design patterns that describes the structure of related objects. Python is able to decorate
# functions, methods, and classes.
#
# The decorator's operation is based on wrapping the original function with a new "decorating" function (or class), ' \
# hence the name "decoration". This is done by passing the original function (i.e., the decorated function) as a
# parameter to the decorating function so that the decorating function can call the passed function.
# The decorating function returns a function that can be called later.
#
# Of course, the decorating function does more, because it can take the parameters of the decorated function and
# perform additional actions and that make it a real decorating function.

# The same principle is applied when we decorate classes.

# Decorators are used to perform operations before and after a call to wrapped object or even to prevent its execution,
# depending on the circumstances. As a result, we can change the operation of the packaged object without directly
# modifying it.
#
# Decorators are used in:
#
# the validation of arguments;
# the modification of arguments;
# the modification of returned objects;
# the measurement of execution time;
# message logging;
# thread synchronization;
# code re-factorization;
# caching.

# First sample


def simple_hello():
    print("Hello from simple function!")


def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    # print(function.__class__)
    return function


decorated = simple_decorator(simple_hello)
decorated()


# ---------------------------------------------------------------------


def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function


@simple_decorator
def simple_hello():
    print("Hello from simple function!")


simple_hello()


# Decorators, which should be universal, must support any function, regardless of the number and type of arguments
# passed. In such a situation, we can use the *args and **kwargs concepts. We can also employ a closure technique
# to persist arguments.


def simple_decorator(own_function):
    def internal_wrapper(*args, **kwargs):
        print('"{}" was called with the following arguments'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        own_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_wrapper


@simple_decorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)


combiner('a', 'b', exec='yes')


# Decorators can accept their own attributes
# In Python, we can create a decorator with arguments.

# the warehouse_decorator('kraft') function will return the wrapper function;
# the returned wrapper function will take the function it is supposed to decorate as an argument;
# the wrapper function will return the internal_wrapper function, which adds new functionality (material display) and
# runs the decorated function.

def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()

        return internal_wrapper

    return wrapper


@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')


# Python allows you to apply multiple decorators to a callable object (function, method or class).

# @outer_decorator
# @inner_decorator
# def function():
#     pass
#
# abcd = subject_matter_function()

# the outer_decorator is called to call the inner_decorator, then the inner_decorator calls your function;
# when your function ends it execution, the inner_decorator takes over control, and after it finishes its execution,
# the outer_decorator is able to finish its job.

# This routing mimics the classic stack concept.

# subject_matter_function = outer_decorator(inner_decorator(subject_matter_function())))
# abcd = subject_matter_function()


def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> The whole order would be packed with', collective_material)
            # our_function(*args)
            print()

        return internal_wrapper

    return wrapper


def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            # our_function(*args)
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)

        return internal_wrapper

    return wrapper


@big_container('plain cardboard')
@warehouse_decorator('bubble foil')
def pack_books(*args):
    print("We'll pack books:", args)


@big_container('colourful cardboard')
@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@big_container('strong cardboard')
@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')


# Decorating functions with classes
# We can define a decorator as a class, and in order to do that, we have to use a __call__ special class method.

# the __init__ method assigns a decorated function reference to the self.attribute for later use;
# the __call__ method, which is responsible for supporting a case when an object is called,
# calls a previously referenced function.


class SimpleDecorator:
    def __init__(self, own_function):
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print('"{}" was called with the following arguments'.format(self.func.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        self.func(*args, **kwargs)
        print('Decorator is still operating')


@SimpleDecorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)


combiner('a', 'b', exec='yes')


# Decorators with arguments

# the reference to function to be decorated is passed to __call__ method which is called only once during
# decoration process,
# the decorator arguments are passed to __init__ method

class WarehouseDecorator:
    def __init__(self, material):
        self.material = material

    def __call__(self, own_function):
        def internal_wrapper(*args, **kwargs):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(own_function.__name__, self.material))
            own_function(*args, **kwargs)
            print()

        return internal_wrapper


@WarehouseDecorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@WarehouseDecorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@WarehouseDecorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')


# Class decorators

# class decorators appear just before the 'class' instructions that begin the class definition

# @my_decorator
# class MyClass:
#
# obj = MyClass()

# def my_decorator(A):
#    ...
#
# class MyClass:
#    ...
#
# MyClass = my_decorator(MyClass())
#
# obj = MyClass()

# The original class named 'MyClass' is no longer available in your name space. The callable object returned by the
# class decorator creates and returns a new instance of the original class,


# When you’re debugging your code or optimizing it, you might be curious how many times the object attributes
# are accessed. In such a situation, a class decorator might be handy.

def object_counter(class_):
    class_.__getattr__orig = class_.__getattribute__

    def new_getattr(self, name):
        if name == 'mileage':
            print('We noticed that the mileage attribute was read')
        return class_.__getattr__orig(self, name)

    class_.__getattribute__ = new_getattr
    return class_


@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN


car = Car('ABC123')
print('The mileage is', car.mileage)
print('The VIN is', car.VIN)


# Decorators allow us to wrap another callable object in order to extend its behavior.
# Decorators rely heavily on closures and *args and **kwargs.

# the idea of decorators was described in two documents – PEP 318 and PEP 3129.
# Don't be discouraged that the first PEP was prepared for Python 2, because what matters here is the idea,' \
#    ' not the implementation in a specific Python.


# ----------------------------------------------------------------------
# Different faces of Python methods

# The instance methods, as the first parameter, take the self parameter, which is their hallmark.
# It’s worth emphasizing and remembering that self allows you to refer to the instance.

# The name of the parameter self was chosen arbitrarily, and you can use a different word,
# but you must do it consistently in your code.

class Example:
    def __init__(selfie, value):
        selfie.__internal = value

    def get_internal(selfie):
        return selfie.__internal


example1 = Example(10)
example2 = Example(99)
print(example1.get_internal())
print(example2.get_internal())


# Class methods

# They are bound to the class, not to the object

# Convention
#
# To be able to distinguish a class method from an instance method, the programmer signals it with the
# @classmethod decorator preceding the class method definition.
# Additionally, the first parameter of the class method is cls, which is used to refer to the class methods and
# class attributes.

# As with self, cls was chosen arbitrarily (i.e., you can use a different name, but you must do it consistently).

class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter += 1

    @classmethod
    def get_internal(cls):
        return '# of objects created: {}'.format(cls.__internal_counter)


print(Example.get_internal())

example1 = Example(10)
print(Example.get_internal())

example2 = Example(99)
print(Example.get_internal())


# The code presented in the editor shows how to use the class method as an alternative constructor,
# allowing you to handle an additional argument.


class Car:
    def __init__(self, vin):
        print('Ordinary __init__ was called for', vin)
        self.vin = vin
        self.brand = ''

    @classmethod
    def including_brand(cls, vin, brand):
        print('Class method was called')
        _car = cls(vin)
        _car.brand = brand
        return _car


car1 = Car('ABCD1234')
car2 = Car.including_brand('DEF567', 'NewBrand')

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)


# ----------------------------------------------------------------------
# Static methods

# Static methods are methods that do not require (and do not expect!) a parameter indicating the class object or
# the class itself in order to execute their code.

# @staticmethod decorator

# 1. When you need a utility method that comes in a class because it is semantically related,
# but does not require an object of that class to execute its code;
# 2. consequently, when the static method does not need to know the state of the objects or classes.


class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban

    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False


account_numbers = ['8' * 20, '7' * 4, '2222']

for element in account_numbers:
    if Bank_Account.validate(element):
        print('We can use', element, ' to create a bank account')
    else:
        print('The account number', element, 'is invalid')

# Using static and class methods - comparison
# The time has come to compare the use of class and static methods:
#
# a class method requires 'cls' as the first parameter and a static method does not;
# a class method has the ability to access the state or methods of the class, and a static method does not;
# a class method is decorated by '@classmethod' and a static method by '@staticmethod';
# a class method can be used as an alternative way to create objects, and a static method is only a utility method.

# ----------------------------------------------------------------------
# Abstract classes

# An abstract class should be considered a blueprint for other classes,
# a kind of contract between a class designer and a programmer:

# the class designer sets requirements regarding methods that must be implemented by just declaring them,
# but not defining them in detail. Such methods are called abstract methods.

# The programmer delivers the method definitions by overriding the method declarations received from the class designer.

# Python has come up with a module which provides the helper class for defining Abstract Base Classes (ABC) and
# that module name is abc.
# A method becomes abstract by being decorated with an @abstractmethod decorator.

import abc


class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass


class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field!')


class RedField(BluePrint):
    def yellow(self):
        pass


gf = GreenField()
gf.hello()

bp = BluePrint()

rf = RedField()


# Summary:
# Abstract Base Class (ABC) is a class that cannot be instantiated. Such a class is a base class for concrete classes;
# ABC can only be inherited from;
# we are forced to override all abstract methods by delivering concrete method implementations.


# ----------------------------------------------------------------------
# Attribute encapsulation

# Encapsulation is used to hide the attributes inside a class like in a capsule, preventing unauthorized parties
# direct access to them. Publicly accessible methods are provided in the class to access the values,
# and other objects call those methods to retrieve and modify the values within the object.

# Python introduces the concept of properties that act like proxies to encapsulated attributes.


class TankError(Exception):
    pass


class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, amount):
        if amount > 0:
            # fueling
            if amount <= self.capacity:
                self.__level = amount
            else:
                raise TankError('Too much liquid in the tank')
        elif amount < 0:
            raise TankError('Not possible to set negative liquid level')

    @level.deleter
    def level(self):
        if self.__level > 0:
            print('It is good to remember to sanitize the remains from the tank!')
        self.__level = None

    # @level.getter
    # def level(self):
    #     if self.__level > 0:
    #         return self.__level + 2
    #     else:
    #         return 0


# our_tank object has a capacity of 20 units
our_tank = Tank(20)

# our_tank's current liquid level is set to 10 units
our_tank.level = 10
print('Current liquid level:', our_tank.level)

# adding additional 3 units (setting liquid level to 13)
our_tank.level += 3
print('Current liquid level:', our_tank.level)

# let's try to set the current level to 21 units
# this should be rejected as the tank's capacity is 20 units
try:
    our_tank.level = 21
except TankError as e:
    print('Trying to set liquid level to 21 units, result:', e)

# similar example - let's try to add an additional 15 units
# this should be rejected as the total capacity is 20 units
try:
    our_tank.level += 15
except TankError as e:
    print('Trying to add an additional 15 units, result:', e)

# let's try to set the liquid level to a negative amount
# this should be rejected as it is senseless
try:
    our_tank.level = -3
except TankError as e:
    print('Trying to set liquid level to -3 units, result:', e)

print('Current liquid level:', our_tank.level)

del our_tank.level


# Composition vs Inheritance - two ways to the same destination: Inheritance

# inheritance extends a class s capabilities by adding new components and modifying existing ones; in other words,
# the complete recipe is contained inside the class itself and all its ancestors; the object takes all the class s
# belongings and makes use of them;
#
# composition projects a class as a container (called a composite) able to store and use other objects
# (derived from other classes) where each of the objects implements a part of a desired class s behavior.
# Its worth mentioning that blocks are loosely coupled with the composite, and those blocks could be exchanged any time,
# even during program runtime.


# The “Car” class is loosely coupled with the “engine” component. It’s a composite object.
#
# The main advantages are:
#
# whenever a change is applied to the engine object, it does not influence the “Car” class object structure;
# you can decide what your car should be equipped with.


class Car:
    def __init__(self, engine):
        self.engine = engine


class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))


class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))


my_car = Car(GasEngine(4))
my_car.engine.start()
my_car.engine = DieselEngine(2)
my_car.engine.start()


# In fact, with the composition approach you can more easily respond to the requirement changes regarding classes,
# as it does not require deep dependency investigations which you would spot while implementing code with
# the inheritance approach.
#
#
# On the other hand, there is a clear drawback: composition transfers additional responsibilities to the developer.
# The developer should assure that all component classes that are used to build the composite should implement
# the methods named in the same manner to provide a common interface.

# In the case of inheritance, if the developer forgets to implement a specific method, the inherited method with
# the same name will be called. Additionally, in the case of inheritance, the developer has to re-implement only
# the specific methods, not all of them, to gain a common interface.


# inheritance and composition are not mutually exclusive. Real-life problems are hardly every pure
# “is a” or “has a” cases;
# treat both inheritance and composition as supplementary means for solving problems

class Base_Computer:
    def __init__(self, serial_number):
        self.serial_number = serial_number


class Personal_Computer(Base_Computer):
    def __init__(self, sn, connection):
        super().__init__(sn)
        self.connection = connection
        print('The computer costs $1000')


class Connection:
    def __init__(self, speed):
        self.speed = speed

    def download(self):
        print('Downloading at {}'.format(self.speed))


class DialUp(Connection):
    def __init__(self):
        super().__init__('9600bit/s')

    def download(self):
        print('Dialling the access number ... '.ljust(40), end='')
        super().download()


class ADSL(Connection):
    def __init__(self):
        super().__init__('2Mbit/s')

    def download(self):
        print('Waking up modem  ... '.ljust(40), end='')
        super().download()


class Ethernet(Connection):
    def __init__(self):
        super().__init__('10Mbit/s')

    def download(self):
        print('Constantly connected... '.ljust(40), end='')
        super().download()


class TestConnection(Connection):
    def __init__(self):
        super().__init__('1000Mbit/s')


# I started my IT adventure with an old-school dial-up connection
my_computer = Personal_Computer('1995', DialUp())
my_computer.connection.download()

# then it came year 1999 with ADSL
my_computer.connection = ADSL()
my_computer.connection.download()

# finally I upgraded to Ethernet
my_computer.connection = Ethernet()
my_computer.connection.download()

# It uses the default download method in Connection class
my_computer.connection = TestConnection()
my_computer.connection.download()


# Inheriting properties from built-in classes
# Python gives you the ability to create a class that inherits properties from any Python built-in class in order to get
# a new class that can enrich the parents attributes or methods. As a result, your newly-created class has the advantage
#  of all of the well-known functionalities inherited from its parent or even parents and you can still access those
# attributes and methods.

# a static, dedicated method for checking argument types. As we have delegated this responsibility to only one method,
# the code will be shorter, cleaner and easier to maintain. Well make use of this method a few times. In case the
# argument's type is not an integer, a ValueError exception is raised

class IntegerList(list):

    @staticmethod
    def check_value_type(value):
        if type(value) is not int:
            raise ValueError('Not an integer type')

    def __setitem__(self, index, value):
        IntegerList.check_value_type(value)
        list.__setitem__(self, index, value)

    def append(self, value):
        IntegerList.check_value_type(value)
        list.append(self, value)

    def extend(self, iterable):
        for element in iterable:
            IntegerList.check_value_type(element)

        list.extend(self, iterable)

    def __add__(self, value):
        IntegerList.check_value_type(value)
        list.__add__(value)

    def insert(self, index, value):
        IntegerList.check_value_type(value)
        list.insert(index, value)


int_list = IntegerList()

int_list.append(66)
int_list.append(22)
print('Appending int elements succeed:', int_list)

int_list[0] = 49
print('Inserting int element succeed:', int_list)

int_list.extend([2, 3])
print('Extending with int elements succeed:', int_list)

try:
    int_list.append('8-10')
except ValueError:
    print('Appending string failed')

try:
    int_list[0] = '10/11'
except ValueError:
    print('Inserting string failed')

try:
    int_list.extend([997, '10/11'])
except ValueError:
    print('Extending with ineligible element failed')

print('Final result:', int_list)

# we’ll create a class based on Python’s built-in dictionary, which will be equipped with logging mechanisms for details
# of writing and reading operations performed on the elements of our dictionary.

# In other words, we are arming a Python dictionary with the ability to log details (time and operation type) of:
#
# class instantiation;
# read access;
# new element creation or update.


from datetime import datetime


class MonitoredDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.log_timestamp('MonitoredDict created')

    def __getitem__(self, key):
        val = super().__getitem__(key)
        self.log_timestamp('value for key [{}] retrieved'.format(key))
        return val

    def __setitem__(self, key, val):
        super().__setitem__(key, val)
        self.log_timestamp('value for key [{}] set'.format(key))

    def log_timestamp(self, message):
        timestampStr = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        self.log.append('{} {}'.format(timestampStr, message))


kk = MonitoredDict()
kk[10] = 15
kk[20] = 5

print('Element kk[10]:', kk[10])
print('Whole dictionary:', kk)
print('Our log book:\n')
print('\n'.join(kk.log))


# IBAN is an algorithm used by European banks to specify account numbers. The standard name IBAN
# (International Bank Account Number) provides a simple and fairly reliable method of validating the account numbers
# against simple typos that can occur during rewriting of the number, e.g., from paper documents, like invoices or bills,
# into computers.
#
# You can find more details here: https://en.wikipedia.org/wiki/International_Bank_Account_Number.

# IBAN Validator

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")

# Now, lets add a new exception class and wrap the previous IBAN validating snippet into a function, reformulate the
# last condition, and use it as a helper function.


class IBANValidationError(Exception):
    pass


def validateIBAN(iban):
    iban = iban.replace(' ', '')

    if not iban.isalnum():
        raise IBANValidationError("You have entered invalid characters.")

    elif len(iban) < 15:
        raise IBANValidationError("IBAN entered is too short.")

    elif len(iban) > 31:
        raise IBANValidationError("IBAN entered is too long.")

    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        ibann = int(iban2)

        if ibann % 97 != 1:
            raise IBANValidationError("IBAN entered is invalid.")

        return True


test_keys = ['GB72 HBZU 7006 7212 1253 01', 'FR76 30003 03620 00020216907 50', 'DE02100100100152517108' ]

for key in test_keys:
    try:
        print('Status of "{}" validation: '.format(key))
        validateIBAN(key)
    except IBANValidationError as e:
        print("\t{}".format(e))
    else:
        print("\tcorrect")

# Having a validateIBAN() function in place, we can write our own class that inherits after a built-in dict class.

import random


class IBANValidationError(Exception):
    pass


class IBANDict(dict):
    def __setitem__(self, _key, _val):
        if validateIBAN(_key):
            super().__setitem__(_key, _val)

    def update(self, *args, **kwargs):
        for _key, _val in dict(*args, **kwargs).items():
            print(_key)
            print("\t{}".format(_val))
            self.__setitem__(_key, _val)


def validateIBAN(iban):
    iban = iban.replace(' ', '')

    if not iban.isalnum():
        raise IBANValidationError("You have entered invalid characters.")

    elif len(iban) < 15:
        raise IBANValidationError("IBAN entered is too short.")

    elif len(iban) > 31:
        raise IBANValidationError("IBAN entered is too long.")

    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        ibann = int(iban2)

        if ibann % 97 != 1:
            raise IBANValidationError("IBAN entered is invalid.")

        return True


my_dict = IBANDict()
keys = ['GB72 HBZU 7006 7212 1253 00', 'FR76 30003 03620 00020216907 50', 'DE02100100100152517108']

for key in keys:
    my_dict[key] = random.randint(0, 1000)

print('The my_dict dictionary contains:')
for key, value in my_dict.items():
    print("\t{} -> {}".format(key, value))

try:
    my_dict.update({'dummy_account': 100})
except IBANValidationError:
    print('IBANDict has protected your dictionary against incorrect data insertion')


# ----------------------------------------------------------------------
# Advanced Exceptions

# name – represents the name of the module that was attempted to be imported;
# path – represents the path to any file which triggered the exception, respectively. Could be None.

try:
    import abcdefghijk


except ImportError as e:
    print(e.args)
    print(e.name)
    print(e.path)

# encoding – the name of the encoding that raised the error.
# reason – a string describing the specific codec error.
# object – the object the codec was attempting to encode or decode.
# start – the first index of invalid data in the object.
# end – the index after the last invalid data in the object.

try:
    b'\x80'.decode("utf-8")
except UnicodeError as e:
    print(e)
    print(e.encoding)
    print(e.reason)
    print(e.object)
    print(e.start)
    print(e.end)

# Exception chaining

# This chaining concept introduces two attributes of exception instances:
#
# the __context__ attribute, which is inherent for implicitly chained exceptions;
# the __cause__ attribute, which is inherent for explicitly chained exceptions.


# The result of the code execution contains a message that joins the subsequent tracebacks:
# During handling of the above exception, another exception occurred:

a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    print(0 / 0)


# The original exception object e is now being referenced by the __context__ attribute of the following exception f.
# The except Exception clause is a wide one and normally
# should be used as a last resort to catch all unhandled exceptions

a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print progress as 1/10	but wrote 1/0
        print(1 / 0)
    except ZeroDivisionError as f:
        print('Inner exception (f):', f)
        print('Outer exception (e):', e)
        print('Outer exception referenced:', f.__context__)
        print('Is it the same object:', f.__context__ is e)
        print(f.__cause__)


# Advanced exceptions - explicitly chained exceptions
# This time wed like to convert an explicit type of exception object to another type of exception object at the moment
# when the second exception is occurring


class RocketNotReadyError(Exception):
    print("inner exception:", Exception.__name__)
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


crew = ['John', 'Mary', 'Mike']
print('Final check procedure')

personnel_check()

# To catch the cause of the RocketNotReadyError exception, you should access
# the __cause__ attribute of the RocketNotReadyError object.


class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


crew = ['John', 'Mary', 'Mike']
print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print('General exception: "{}", caused by "{}"'.format(f, f.__cause__))


# Pay attention to the fact that thanks to polymorphism and explicit chaining, our approach has become more generic:
# we are able to run two different checks, each returning a different exception type.

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100 / 0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e


crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))


# Advanced exceptions - the traceback attribute
# Each exception object owns a __traceback__ attribute.
#
# Python allows us to operate on the traceback details because each exception object
# (not only chained ones) owns a __traceback__ attribute.


class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


crew = ['John', 'Mary', 'Mike']

print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))


# To achieve this, we could use the format_tb() method delivered by the built-in traceback module to get
# a list of strings describing the traceback.
#
# We could use the print_tb() method, also delivered by the traceback module, to print strings directly to the
# standard output.
#
# The corresponding output reveals the sequence of exceptions and proves that the execution was not interrupted by
# the exceptions because we see the final wording Final check is over.

import traceback


class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


crew = ['John', 'Mary', 'Mike']

print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))
    print('\nTraceback details')
    details = traceback.format_tb(f.__traceback__)
    print("\n".join(details))

print('Final check is over')


# ----------------------------------------------------------------------
# object persistence;

# object: label vs. identity vs. value;
# the id() function and the is operand;
# shallow and deep copies of the objects.

# The built-in id() function returns the 'identity' of an object.
# This is an integer which is guaranteed to be unique and constant for this object during its lifetime.
# Two objects with non-overlapping lifetimes may have the same id() value.

# CPython implementation detail: This is the address of the object in the memory.
# Don’t treat it as an absolute memory address.

# a variable called id shadows the genuine function and makes it
# unreachable in the scope in which the variable has been defined.

a_string = '10 days to departure'
b_string = '20 days to departure'

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))


# When you have two variables referring to the same object, the return values of the id() function must be the same.

a_string = '10 days to departure'
b_string = a_string

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))

# In order to compare two objects, you should start with the '==' operator as usual.
# This operator compares the values of both operands and checks for value equality.

# To check whether both operands refer to the same object or not, you should use the 'is' operator. In other words,
# it responds to the question: “Are both variables referring to the same identity?”

a_string = ['10', 'days', 'to', 'departure']
b_string = a_string

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
print('The result of the value comparison:', a_string == b_string)
print('The result of the identity comparison:', a_string is b_string)

print()

a_string = ['10', 'days', 'to', 'departure']
b_string = ['10', 'days', 'to', 'departure']

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))
print('The result of the value comparison:', a_string == b_string)
print('The result of the identity comparison:', a_string is b_string)


# When you process the data, you’ll come to the point where you may want to have distinct copies of objects that
# you can modify without automatically modifying the original at the same time.

# So, despite the fact that b_list is a copy of a_list, modifying b_list results in a modification of the a_list object.

print("Part 1")
print("Let's make a copy")
a_list = [10, "banana", [997, 123]]
b_list = a_list[:]
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

print()
print("Part 2")
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)


# the 'a_list' object is a compound object;
# we’ve run a shallow copy that constructs a new compound object, b_list in our example, and
# then populated it with references to the objects found in the original;

# deepcopy
# If you want to make an independent copy of a compound object (list, dictionary, custom class instance)
# you should make use of deep copy,

import copy

print("Let's make a deep copy")
a_list = [10, "banana", [997, 123]]
b_list = copy.deepcopy(a_list)
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)

print()
print("Let's modify b_list[2]")
b_list[2][0] = 112
print("a_list contents:", a_list)
print("b_list contents:", b_list)
print("Is it the same object?", a_list is b_list)


# The 'copy' module contains a function for shallow copying: copy(). Of course, you could say that for
# copying lists there is already
# the [:] notation, or
# a_list=list(b_list), and
# for dictionaries you could use a_dict = dict(b_dict)

# a universal function to copy any type object : copy()


# The first approach is a simple reference copy. This is done very quickly, as there’s nearly nothing to be done
# by the CPU – just a copy of a reference to 'a_list'.
#
# The second approach is a shallow copy. This is slower than the previous code, as there are 1,000,000 references
# (not objects) created.
#
# The third approach is a deep copy. This is the most comprehensive operation, as there are 3,000,000 objects created.

import copy
import time

a_list = [(1, 2, 3) for x in range(1_000_000)]

print('Single reference copy')
time_start = time.time()
b_list = a_list
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:', id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)

print()

print('Shallow copy')
time_start = time.time()
b_list = a_list[:]
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:', id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)

print()

print('Deep copy')
time_start = time.time()
b_list = copy.deepcopy(a_list)
print('Execution time:', round(time.time() - time_start, 3))
print('Memory chunks:', id(a_list), id(b_list))
print('Same memory chunk?', a_list is b_list)


# The same deepcopy() method could be utilized when you want to copy dictionaries or custom class objects.

import copy

a_dict = {
    'first name': 'James',
    'last name': 'Bond',
    'movies': ['Goldfinger (1964)', 'You Only Live Twice']
    }
b_dict = copy.deepcopy(a_dict)
print('Memory chunks:', id(a_dict), id(b_dict))
print('Same memory chunk?', a_dict is b_dict)
print("Let's modify the movies list")
a_dict['movies'].append('Diamonds Are Forever (1971)')
print('a_dict movies:', a_dict['movies'])
print('b_dict movies:', b_dict['movies'])


# Pay attention to the fact that the __init__() method is executed only once, despite the fact we own two
# instances of the example class.

# This method is not executed for the b_example object as the deepcopy function copies an already initialized object.


import copy


class Example:
    def __init__(self):
        self.properties = ["112", "997"]
        print("Hello from __init__()")


a_example = Example()
b_example = copy.deepcopy(a_example)
print("Memory chunks:", id(a_example), id(b_example))
print("Same memory chunk?", a_example is b_example)
print()
print("Let's modify the movies list")
b_example.properties.append("911")
print('a_example.properties:', a_example.properties)
print('b_example.properties:', b_example.properties)

# Section summary
# Important things to remember:
#
# the deepcopy() method creates and persists new instances of source objects, whereas any shallow copy operation only
# stores references to the original memory address;
# a deep copy operation takes significantly more time than any shallow copy operation;
# the deepcopy() method copies the whole object, including all nested objects; it’s an example of practical recursion
# taking place;
# deep copy might cause problems when there are cyclic references in the structure to be
#
#


# ----------------------------------------------------------------------
# Serialization of Python objects using the pickle module

# In Python, object serialization is the process of converting an object structure into a stream of bytes to store the
# object in a file or database, or to transmit it via a network. This byte stream contains all the information necessary
# to reconstruct the object in another Python script.
#
# This reverse process is called deserialization.
#
# Python objects can also be serialized using a module called 'pickle', and using this module, you can 'pickle'
# your Python objects for later use.
#
# The 'pickle' module is a very popular and convenient module for data serialization in the world of Pythonistas.
#
# So, what can be pickled and then unpickled?
#
# The following types can be pickled:
#
# None, booleans;
# integers, floating-point numbers, complex numbers;
# strings, bytes, bytearrays;
# tuples, lists, sets, and dictionaries containing pickleable objects;
# objects, including objects with references to other objects (remember to avoid cycles!)
# references to functions and classes, but not their definitions.

# It’s important to open the file in binary mode as we are dumping data as a stream of bytes.

# dump() function. This function expects an object to be persisted and a file handle.

# In this result, we have created a file that retains the pickled objects.

import pickle

a_dict = dict()
a_dict['EUR'] = {'code':'Euro', 'symbol': '€'}
a_dict['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
a_dict['USD'] = {'code':'US dollar', 'symbol': '$'}
a_dict['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

a_list = ['a', 123, [10, 100, 1000]]

with open('multidata.pckl', 'wb') as file_out:
    pickle.dump(a_dict, file_out)
    pickle.dump(a_list, file_out)


# ------------------------------------------------------------------
# UnPickle the objects

import pickle

with open('multidata.pckl', 'rb') as file_in:
    data1 = pickle.load(file_in)
    data2 = pickle.load(file_in)

print(type(data1))
print(data1)
print(type(data2))
print(data2)

# ------------------------------------------------------------------
# pickle.dumps(object_to_be_pickled) – expects an initial object, returns a byte object. This byte object should be
# passed to a database or network driver to persist the data;
# pickle.loads(bytes_object) – expects the bytes object, returns the initial object.


import pickle

a_list = ['a', 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print('Intermediate object type, used to preserve data:', type(bytes))

# now pass 'bytes' to appropriate driver

# therefore when you receive a bytes object from an appropriate driver you can deserialize it
b_list = pickle.loads(bytes)
print('A type of deserialized object:', type(b_list))
print('Contents:', b_list)

# ------------------------------------------------------------------
# Remember that attempts to pickle non-pickleable objects will raise the PicklingError exception.
#
# Trying to pickle a highly recursive data structure (mind the cycles) may exceed the maximum recursion depth, and
# a RecursionError exception will be raised in such cases.

# Note that functions (both built-in and user-defined) are pickled by their name reference, not by any value.
# This means that only the function name is pickled; neither the function’s code, nor any of its function attributes,
# are pickled.

# This is done on purpose, so you can fix bugs in a class or add methods to the class, and still load objects that were
# created with an earlier version of the class.

# Similarly, classes are pickled by named reference, so the same restrictions in the unpickling environment apply.
# Note that none of the class’s code or data are pickled.

# Hence, your role is to ensure that the environment where the class or function is unpickled is able to import
# the class or function definition. In other words, the function or class must be available in the namespace of your
# code reading the pickle file.
# Otherwise, an AtrributeError exception will be raised.

import pickle


def f1():
    print('Hello from the jar!')


with open('function.pckl', 'wb') as file_out:
    pickle.dump(f1, file_out)

with open('function.pckl', 'rb') as file_in:
    data = pickle.load(file_in)

print(type(data))
print(data)
data()


# ------------------------------------------------------------------
import pickle


class Cucumber:
    def __init__(self):
        self.size = 'small'

    def get_size(self):
        return self.size


cucu = Cucumber()

with open('cucumber.pckl', 'wb') as file_out:
    pickle.dump(cucu, file_out)


with open('cucumber.pckl', 'rb') as file_in:
    data = pickle.load(file_in)

print(type(data))
print(data)
print(data.size)
print(data.get_size())


# ------------------------------------------------------------------
# There is another handy module, called shelve, that is built on top of pickle,and implements a serialization dictionary
# where objects are pickled and associated with a key. The keys must be ordinary strings,because the underlying database
# (dbm) requires strings.

# Value	Meaning
# 'r'	Open existing database for reading only
# 'w'	Open existing database for reading and writing
# 'c'	Open database for reading and writing, creating it if it doesn’t exist (this is a default value)
# 'n'	Always create a new, empty database, open for reading and writing

import shelve

shelve_name = 'first_shelve.shlv'

my_shelve = shelve.open(shelve_name, flag='c')
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()

new_shelve = shelve.open(shelve_name)
print(new_shelve['USD'])
new_shelve.close()

# You should treat a shelve object as a Python dictionary, with a few additional notes:
#
# the keys must be strings;
# Python puts the changes in a buffer which is periodically flushed to the disk. To enforce an immediate flush, call
# the sync() method on your shelve object;
# when you call the close() method on an shelve object, it also flushes the buffers.
# When you treat a shelve object like a Python dictionary, you can make use of the dictionary utilities:
#
# the len() function;
# the in operator;
# the keys() and items() methods;
# the update operation, which works the same as when applied to a Python dictionary;
# the del instruction, used to delete a key-value pair.


# because the shelve module is backed by pickle, it isn’t safe to load a shelve from an untrusted source.
# As with pickle, loading a shelve can execute arbitrary code.

# ----------------------------------------------------------------------
# metaprogramming.

# Metaprogramming is a programming technique in which computer programs have the ability to modify their own or
# other programs’ codes.

# For Python, code modifications can occur while the code is being executed, and you might have already experienced it
# while implementing decorators, overriding operators, or even implementing the properties' protocol.

# 1 ) this technique could be used for tool preparation; those tools could be applied to your code to make it follow
# specific programming patterns,
# or to help you create a coherent API (Application Programming Interface).

# 2 ) metaclass
#
# Tim Peters, the Python guru who authored the Zen of Python, expressed his feelings about metaclasses in the comp.lang.
#     python newsgroup on 12/22/2002:
#
# [meta-classes] are deeper magic than 99% of users should ever worry about. If you wonder whether you need
# them,  don't (the people who actually need them know with certainty that they need them, and don't need an explanation
# about why).

# In Python, a metaclass is a class whose instances are classes. Just as an ordinary class defines the behavior of
# certain objects, a metaclass allows for the customization of class instantiation.
#
# The functionality of the metaclass partly coincides with that of class decorators, but metaclasses act in a different
# way than decorators:
#
# decorators bind the names of decorated functions or classes to new callable objects. Class decorators are applied
# when classes are instantiated;
# metaclasses redirect class instantiations to dedicated logic, contained in meta-classes. Meta-classes are applied
# when class definitions are read to create classes, well before classes are instantiated.

# Metaclasses usually enter the game when we program advanced modules or frameworks, where a lot of precise automation
# must be provided.
#
# The typical use cases for metaclasses:
#
# logging;
# registering classes at creation time;
# interface checking;
# automatically adding new methods;
# automatically adding new variables.

# ------------------------------------------------------------------
class Dog:
    pass


age = 10
codes = [33, 92]
dog = Dog()

print(type(age))
print(type(codes))
print(type(dog))
print(type(Dog))


for t in (int, list, type):
    print(type(t))

# ------------------------------------------------------------------
# metaclasses are used to create classes;
# classes are used to create objects;
# the type of the metaclass type is type – no, that is not a typo.
#
# type is a class that generates classes defined by a programmer;
# metaclasses are subclasses of the type class.

# __name__ – inherent for classes; contains the name of the class;
# __class__ – inherent for both classes and instances; contains information about the class to which a class
# instance belongs;
# __bases__ – inherent for classes; it’s a tuple and contains information about the base classes of a class;
# __dict__ – inherent for both classes and instances; contains a dictionary (or other type mapping object) of
# the object's attributes.


class Dog:
    pass

dog = Dog()
print('"dog" is an object of class named:', Dog.__name__)
print()
print('class "Dog" is an instance of:', Dog.__class__)
print('instance "dog" is an instance of:', dog.__class__)
print()
print('class "Dog" is  ', Dog.__bases__)
print()
print('class "Dog" attributes:', Dog.__dict__)
print('object "dog" attributes:', dog.__dict__)

# ------------------------------------------------------------------
# The same information stored in __class__could be retrieved by calling a type() function with one argument:
for element in (1, 'a', True):
    print(element, 'is', element.__class__, type(element))


# ------------------------------------------------------------------

# When the type() function is called with three arguments, then it dynamically creates a new class.
#
# For the invocation of type(, , ):
#
# the argument specifies the class name; this value becomes the __name__ attribute of the class;
# the argument specifies a tuple of the base classes from which the newly created class is inherited; this argument
# becomes the __bases__ attribute of the class;
# the argument specifies a dictionary containing method definitions and variables for the class body; the elements of
# this argument become the __dict__ attribute of the class and state the class namespace.

Dog = type('Dog', (), {})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

# ------------------------------------------------------------------
# after the class instruction has been identified and the class body has been executed, the class = type(, , )
# code is executed;
# the type is responsible for calling the __call__ method upon class instance creation; this method calls two
# other methods:
# __new__(), responsible for creating the class instance in the computer memory; this method is run before __init__();
# __init__(), responsible for object initialization.
# Metaclasses usually implement these two methods (__init__, __new__), taking control of the procedure of
# creating and initializing a new class instance. Classes receive a new layer of logic.


def bark(self):
    print('Woof, woof')


class Animal:
    def feed(self):
        print('It is feeding time!')


Dog = type('Dog', (Animal, ), {'age':0, 'bark':bark})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()

# ------------------------------------------------------------------
# It’s important to remember that metaclasses are classes that are instantiated to get classes.


class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.custom_attribute = 'Added by My_Meta'
        return obj


class My_Object(metaclass=My_Meta):
    pass


print(My_Object.__dict__)


# ------------------------------------------------------------------
def greetings(self):
    print('Just a greeting function, but it could be something more serious like a check sum')


class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        if 'greetings' not in dictionary:
            dictionary['greetings'] = greetings
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj


class My_Class1(metaclass=My_Meta):
    pass


class My_Class2(metaclass=My_Meta):
    def greetings(self):
        print('We are ready to greet you!')

myobj1 = My_Class1()
myobj1.greetings()
myobj2 = My_Class2()
myobj2.greetings()


# ------------------------------------------------------------------

class test:
    def __init__(self) -> None:
        self.__numbers = 0


t = test()
print(t._test__numbers)

# ----------------------------------------------------------------------


# ----------------------------------------------------------------------


