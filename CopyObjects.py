# The built-in id() function returns the 'identity' of an object. This is an integer which is guaranteed to be
# unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the
# same id() value.

a_string = '10 days to departure'
b_string = '20 days to departure'

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))

# -----------------------------------------------------------
a_string = '10 days to departure'
b_string = a_string

print('a_string identity:', id(a_string))
print('b_string identity:', id(b_string))

# -----------------------------------------------------------
# == This operator compares the values of both operands and checks for value equality
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


# -----------------------------------------------------------
# Using[:], which is an array slice syntax, we get a fresh copy

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

# So, despite the fact that b_list is a copy of a_list, modifying b_list results in a modification of the a_list object.

# we’ve run a shallow copy that constructs a new compound object, b_list in our example, and then populated it with
# references to the objects found in the original;
# as you can see, a shallow copy is only one level deep. The copying process does not recurse and therefore does not
# create copies of the child objects, but instead populates b_list with references to the already existing objects.

# -----------------------------------------------------------


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

# The 'copy' module contains a function for shallow copying: copy(). Of course, you could say that for copying lists
# there is already the [:] notation, or a_list=list(b_list), and for dictionaries you could use a_dict = dict(b_dict).

# -----------------------------------------------------------
# In the following example, we'll compare the performance of three ways of copying a large compound object ' \
# (a million three-element tuples).
#
# The first approach is a simple reference copy. This is done very quickly, as there’s nearly nothing to be done
# by the CPU – just a copy of a reference to 'a_list'.
#
# The second approach is a shallow copy. This is slower than the previous code, as there are 1,000,000 references
# (not objects) created.
#
# The third approach is a deep copy. This is the most comprehensive operation, as there are 3,000,000 objects created.


import copy
import time

a_list = [(1,2,3) for x in range(1_000_000)]

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


# -----------------------------------------------------------
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

# the deepcopy() method creates and persists new instances of source objects, whereas any shallow copy operation only
# stores references to the original memory address;
# a deep copy operation takes significantly more time than any shallow copy operation;
# the deepcopy() method copies the whole object, including all nested objects; it’s an example of practical recursion
# taking place;
# deep copy might cause problems when there are cyclic references in the structure to be copied.
# -----------------------------------------------------------






# -----------------------------------------------------------






# -----------------------------------------------------------







# -----------------------------------------------------------





# -----------------------------------------------------------