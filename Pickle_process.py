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
#
# Similarly, classes are pickled by named reference, so the same restrictions in the unpickling environment apply.
# Note that none of the class’s code or data are pickled.

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
# There is another handy module, called shelve, that is built on top of pickle, and implements a serialization dictionary
# where objects are pickled and associated with a key. The keys must be ordinary strings, because the underlying database
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
# the keys() anditems() methods;
# the update operation, which works the same as when applied to a Python dictionary;
# the del instruction, used to delete a key-value pair.



# ------------------------------------------------------------------




# ------------------------------------------------------------------




# ------------------------------------------------------------------




# ------------------------------------------------------------------




# ------------------------------------------------------------------




# ------------------------------------------------------------------




# ------------------------------------------------------------------

