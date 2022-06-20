
# Metaprogramming is a programming technique in which computer programs have the ability to modify their own or
# other programs’ codes.

# For Python, code modifications can occure while the code is being executed, and you might have already experienced it
# while implementing decorators, overriding operators, or even implementing the properties protocol.

# 1 ) this technique could be used for tool preparation; those tools could be applied to your code to make it follow
# specific programming patterns,
# or to help you create a coherent API (Application Programming Interface).

# 2 ) metaclass
#
# Tim Peters, the Python guru who authored the Zen of Python, expressed his feelings about metaclasses in the comp.lang.
#     python newsgroup on 12/22/2002:
#
# [metaclasses] are deeper magic than 99% of users should ever worry about. If you wonder whether you need
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
# metaclasses redirect class instantiations to dedicated logic, contained in metaclasses. Metaclasses are applied
# when class definitions are read to create classes, well before classes are instantiated.

# Metaclasses usually enter the game when we program advanced modules or frameworks, where a lot of precise automation must be provided.
#
# The typical use cases for metaclasses:
#
# logging;
# registering classes at creation time;
# interface checking;
# automatically adding new methods;
# automatically adding new variables.

#------------------------------------------------------------------
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

# ------------------------------------------------------------------


# ------------------------------------------------------------------








# ------------------------------------------------------------------



















