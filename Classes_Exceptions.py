vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]

my_list = [1, 2, 3, 4]
print(my_list[-3:-1])

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])

i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")


def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return


fun(fun(2)) + 1

my_tuple = tuple()

my_tuple[1] = my_tuple[1] + my_tuple[2]


# try:
#     # value = 0
#     # print(int(value)/len(value))
#     print(5/0)
#     break
# except:
#     print("sorry")
# except (ValueError, ZeroDivisionError):
#     print("Too bad")
#
# except ValueError:
#     print("Bad input!")
# except ZeroDivisionError:
#     print("Very bad input!")
# except TypeError:
#     print("Very very bad input!")
# except:
#     print("Boooo!")


def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c


for x in I():
    print(x)

import calendar

c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday)

import os

os.mkdir('th1')
os.chdir('th1')

sizes = ['small', 'medium', 'large']

for size in sizes:
    os.mkdir(size)

print(os.listdir())


def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in fun(2):
    print(x)

my_tuple = (0, 1, 2, 3, 4, 5, 6)
foo = list(filter(lambda x: x - 0 and x - 1, my_tuple))
print(foo)

import random

random.choice((0, 100, 3))

x = "\\\\"
len(x)


class A:
    def __init__(self):
        pass


a = A(1)
print(hasattr(a, 'A'))


class A:
    A = 1

    def __init__(self):
        self.a = 0


s = A()
print(hasattr(s, 'a'))

float("1.3")

import math

dir(math)

from datetime import timedelta

delta = timedelta(weeks=1, days=7, hours=11)
print(delta * 2)

# try:
#     raise Exception
# except:
#     print("c")
# except BaseException:
#     print("a")
# except Exception:
#     print("b")


from datetime import datetime

datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)

print(datetime_1 - datetime_2)


class MyZeroDivisionError(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')


class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

t = (1,)
t = t[0] + t[0]
print(t)


def fun(par2, par1):
    return par2 + par1


# print(fun(par2=1, 2))

my_list = [[c for c in range(r)] for r in range(3)]

for element in my_list:
    if len(element) < 2:
        print('l')

x, y, z = 3, 2, 1
z, y, x = x, y, z
print(x, y, z)

x = """
"""

print(len(x))

d = {'one': 1, 'three': 3, 'two': 2}

for k in sorted(d.values()):
    print(k)

t = (1, 2, 3, 4)
t = t[-2:-1]
t = t[-1]
print(t)

[i for i in range(0, -2)]


class A:
    def __init__(self):
        pass

    def f(self):
        return 1

    def g(self):
        return self.f()


a = A()
print(a.g())


class A:
    def __init__(self, name):
        self.name = name


a = A("Class")
print(a)


def fun(d, k, v):
    d[k] = v


my_dic = {}
print(fun(my_dic, '1', 'v'))

i = 4

while i > 0:
    i -= 2
    print("*")
    if i == 2:
        break
else:
    print("*")

z = 2
y = 1

x = y < z or z > y and y > z or z < y

my_string = 'abcdef'


def fun(s):
    del s[2]
    return s


print(fun(my_string))

str_1 = 'string'
str_2 = str_1[:]

str1 = (',,,').join(('apple', 'orange'))
str1 = str1.split(',')
print(str1)


class mobile_phone:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        output_str = "mobile phone {mobile_number} is turned on".format(mobile_number=self.number)
        return (output_str)

    def turn_off(self):
        output_str = "mobile phone is turned off"
        return (output_str)

    def call(self, number):
        output_str = "calling {mobile_number}".format(mobile_number=number)
        return (output_str)


mobile1 = mobile_phone("555-3145624")
mobile2 = mobile_phone("289-3652445")

print(mobile1.turn_on())
print(mobile2.turn_on())

print(mobile1.call(mobile2.number))

print(mobile1.turn_off())
print(mobile2.turn_off())

output_srt = "mobile phone {mobile_number} is turned on".format(mobile_number="65245555")

num = 10
print(num.__add__(20))

print(num + 20)


def simple_decorator(own_function):
    def internal_wrapper(*args, **kwargs):
        print('"{}" was called with the following arguments'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        own_function(*args, **kwargs)
        print('Decorator is still operating')

    return internal_wrapper


# ---------------------------------------------------


@simple_decorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)


combiner('a', 'b', exec='yes')


# ---------------------------------------------------


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


# ---------------------------------------------------

def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> The whole order would be packed with', collective_material)
            print()

        return internal_wrapper

    return wrapper


def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))

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


# ---------------------------------------------------

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


# ---------------------------------------------------

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


# ---------------------------------------------------


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

car.mileage += 10


# ---------------------------------------------------

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


# ---------------------------------------------------

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


# ---------------------------------------------------
# Using static and class methods - comparison
# The time has come to compare the use of class and static methods:
#
# a class method requires 'cls' as the first parameter and a static method does not;
# a class method has the ability to access the state or methods of the class, and a static method does not;
# a class method is decorated by '@classmethod' and a static method by '@staticmethod';
# a class method can be used as an alternative way to create objects, and a static method is only a utility method.

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

# ---------------------------------------------------
# An abstract class should be considered a blueprint for other classes, a kind of contract between a class designer
#  and a programmer:
# the class designer sets requirements regarding methods that must be implemented by just declaring them, but not
# defining them in detail. Such methods are called abstract methods.
# The programmer has to deliver all method definitions and the completeness would be validated by another, dedicated
# module. The programmer delivers the method definitions by overriding the method declarations received from the
# class designer.

# Why do we want to use abstract classes?
# The very important reason is: we want our code to be polymorphic, so all subclasses have to deliver a set of their
# own method implementations in order to call them by using common method names.
#
# Furthermore, a class which contains one or more abstract methods is called an abstract class. This means that abstract
# classes are not limited to containing only abstract methods – some of the methods can already be defined, but if any
# of the methods is an abstract one, then the class becomes abstract.
#
# What is an abstract method?
# An abstract method is a method that has a declaration, but does not have any implementation.
# We'll give some examples of such methods to emphasize their abstract nature.


import abc


class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass


class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field!')


gf = GreenField()
gf.hello()

bp = BluePrint()
# ---------------------------------------------------
# Abstract Base Class (ABC) is a class that cannot be instantiated. Such a class is a base class for concrete classes;
# ABC can only be inherited from;
# we are forced to override all abstract methods by delivering concrete method implementations.

# A note:
#
# It’s tempting to call a module “abc” and then try to import it, but by doing so Python imports the module containing
# the ABC class instead of your local file. This could cause some confusion – why does such a common name as “abc”
# conflict with my simple module “abc”?
#
# Run your own experiment to become familiar with the error messages you would encounter in such a situation.
import abc


class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MFD1(Scanner, Printer):
    def scan_document(self):
        print("Document is scanned")

    def get_scanner_status(self):
        print("Scan resolution is low")

    def print_document(self):
        print("Document is printed!")

    def get_printer_status(self):
        print("the printer resolution is low!")


mfd1 = MFD1()

mfd1.scan_document()
mfd1.print_document()

mfd1.get_scanner_status()
mfd1.get_printer_status()

# ---------------------------------------------------
# Encapsulation is used to hide the attributes inside a class like in a capsule, preventing unauthorized
# parties' direct access to them. Publicly accessible methods are provided in the class to access the values, and
# other objects call those methods to retrieve and modify the values within the object. This can be a way to
# enforce a certain amount of privacy for the attributes.

# Python introduces the concept of properties that act like proxies to encapsulated attributes.
#
# This concept has some interesting features:
#
# the code calling the proxy methods might not realize if it is "talking" to the real attributes or to the methods
# controlling access to the attributes;

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

# ---------------------------------------------------

# On the other hand, there is a clear drawback: composition transfers additional responsibilities to the developer.
# The developer should assure that all component classes that are used to build the composite should implement the
# methods named in the same manner to provide a common interface.
#
# In the case of inheritance, if the developer forgets to implement a specific method, the inherited method with the
# same name will be called. Additionally, in the case of inheritance, the developer has to re-implement only the
# specific methods, not all of them, to gain a common interface.

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

# ---------------------------------------------------
# combination of composition and inheritance


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

# I started my IT adventure with an old-school dial up connection
my_computer = Personal_Computer('1995', DialUp())
my_computer.connection.download()

# then it came year 1999 with ADSL
my_computer.connection = ADSL()
my_computer.connection.download()

# finally I upgraded to Ethernet
my_computer.connection = Ethernet()
my_computer.connection.download()
# ---------------------------------------------------
# inherit from built in class like list of integers
# to check the sold tickets nuber only for example

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

# ---------------------------------------------------

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

# ---------------------------------------------------
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

# ---------------------------------------------------


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



# ---------------------------------------------------

import random


class IBANValidationError(Exception):
    pass


class IBANDict(dict):
    def __setitem__(self, _key, _val):
        if validateIBAN(_key):
            super().__setitem__(_key, _val)

    def update(self, *args, **kwargs):
        for _key, _val in dict(*args, **kwargs).items():
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

# ---------------------------------------------------
# Exception

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

# This chaining concept introduces two attributes of exception instances:
#
# the __context__ attribute, which is inherent for implicitly chained exceptions;
# the __cause__ attribute, which is inherent for explicitly chained exceptions.

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

# ---------------------------------------------------
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

# ---------------------------------------------------
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
        print('Fuel tank is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

def batteries_check():
    # add your own implentation
    pass

def circuits_check():
    # add your own implentation
    pass


crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))
        print(f.__traceback__)
        print(type(f.__traceback__))

# ---------------------------------------------------

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

# ---------------------------------------------------







# ---------------------------------------------------







# ---------------------------------------------------







# ---------------------------------------------------






# ---------------------------------------------------







# ---------------------------------------------------






# ---------------------------------------------------














