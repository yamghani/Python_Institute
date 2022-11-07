# The following function arguments say more about our views for the future:
#
# socket.SHUT_RD - we aren't going to read the server's messages anymore (we declare ourselves deaf)
# socket.SHUT_WR - we won't say a word (actually, we'll be dumb)
# socket.SHUT_RDWR - specifies the conjunction of the two previous options.

# Note: socket.gaierror covers more than one possible reason for the failure.
# ----------------------------------------------------------------------
import socket

server_addr = input("What server do you want to connect?")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 80))
sock.send(b"GET / HTTP/1.1\r\nHost: test_img[ ]= ["+
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")
# sock.settimeout()
reply = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(repr(reply))

# ----------------------------------------------------------------------
# The socket.timeout exception

# The connect function throws exception named socket.gaierror and its name comes from the name of a low-level function
# (usually provided not by Python but by the OS kernel) named getaddrinfo(). The function tries - among others - to find
# the full address information regarding the received argument.
#
# This exception is raised when the server's reaction doesn't occur in a reasonable time - the length of our patience
# can be set using a method named settimeout(), but we don't want to go into details.

# ----------------------------------------------------------------------

# https://edube.org/learn/pcpp1-working-with-restful-apis/json-our-new-friend-7

import json

comics = '"The Meaning of Lifetest_img = ["by Monty Python\'s Flying Circus'
print(json.dumps(comics))


import json

my_list = [1, 2.34, True, "False", None, ['a', 0]]
print(json.dumps(my_list))


import json

my_dict = {'me': "Python", 'pi': 3.141592653589, 'data': (1, 2, 4, 8), 'set': None}
print(json.dumps(my_dict))

# https://edube.org/learn/pcpp1-working-with-restful-apis/talking-to-json-in-python-6

import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


some_man = Who('John Doe', 42)
print(json.dumps(some_man))

import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')


some_man = Who('John Doe', 42)
print(json.dumps(some_man, default=encode_who))


# ----------------------------------------------------------------------

import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, w)


some_man = Who('John Doe', 42)
print(json.dumps(some_man, cls=MyEncoder))


# ----------------------------------------------------------------------

import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, z)


some_man = Who('John Doe', 42)
print(json.dumps(some_man, cls=MyEncoder))




# ----------------------------------------------------------------------

import json


class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + 'is not JSON serializable')


def decode_who(w):
    return Who(w['name'], w['age'])


old_man = Who("Jane Doe", 23)
json_str = json.dumps(old_man, default=encode_who)
new_man = json.loads(json_str, object_hook=decode_who)
print(type(new_man))
print(new_man.__dict__)

# ----------------------------------------------------------------------

import json

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, z)


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)


some_man = Who('Jane Doe', 23)
json_str = json.dumps(some_man, cls=MyEncoder)
new_man = json.loads(json_str, cls=MyDecoder)

print(type(new_man))
print(new_man.__dict__)


# ----------------------------------------------------------------------

# xml is a language. Anyway, this is what it thinks about itself. Note – it isnt a programming language, and although
# it is possible to build a real programming language on top of xml, it wasn't (and still isn't) its native niche.
# xml is – like JSON – a universal and transparent carrier of any type of data.

import xml.etree.ElementTree

path = 'C:/Personal/Python_Institute/xml/cars.xml'

cars_for_sale = xml.etree.ElementTree.parse(path).getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
    print(' =', prop.text)


# ----------------------------------------------------------------------

import xml.etree.ElementTree

path = 'C:/Personal/Python_Institute/xml/cars.xml'

# tree = xml.etree.ElementTree.parse('Python Institute/xml/cars.xml')
tree = xml.etree.ElementTree.parse(path)
cars_for_sale = tree.getroot()
for car in cars_for_sale.findall('car'):
    if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
        cars_for_sale.remove(car)
        break
new_car = xml.etree.ElementTree.Element('car')
xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
cars_for_sale.append(new_car)
save_path = "C:/Personal/Python_Institute/xml/newcars.xml"
tree.write(save_path, method='')
# tree.write('Python Institute/xml/newcars.xml', method='')

# ----------------------------------------------------------------------
# npm install -g json-server
#
# json-server --watch cars.json

# in the folder where cars.json exists, create a subfolder named public;
# inside the public folder, create a file named index.html, fill it with some text, and save.

# https://edube.org/learn/pcpp1-working-with-restful-apis/making-life-easier-with-the-requests-module-10

import requests

reply = requests.get('http://localhost:3000')
print(reply.status_code)

print(requests.codes.__dict__)

if reply.status_code == requests.codes.ok:
    print('ok')


import requests

reply = requests.get('http://localhost:3000')
print(reply.headers)
print(reply.text)


import requests

try:
    reply = requests.get('http://localhost:3000', timeout=1)
except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you didn\'t get your data')
else:
    print('Here is your data, my Master!')



import requests

try:
    reply = requests.get('http://localhost:3001', timeout=1)
except requests.exceptions.ConnectionError:
    print('Nobody\'s home, sorry!')
else:
    print('Everything fine!')




import requests

try:
    reply = requests.get('http:////////////')
except requests.exceptions.InvalidURL:
    print('Recipient unknown!')
else:
    print('Everything fine!')


# RequestException
# |___HTTPError
# |___ConnectionError
# |   |___ProxyError
# |   |___SSLError
# |___Timeout
# |   |___ConnectTimeout
# |   |___ReadTimeout
# |___URLRequired
# |___TooManyRedirects
# |___MissingSchema
# |___InvalidSchema
# |___InvalidURL
# |   |___InvalidProxyURL
# |___InvalidHeader
# |___ChunkedEncodingError
# |___ContentDecodingError
# |___StreamConsumedError
# |___RetryError
# |___UnrewindableBodyError


# ----------------------------------------------------------------------

import requests

try:
    reply = requests.get("http://localhost:3000/cars")
except requests.RequestException:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.text)
    else:
        print("Server error")

# ----------------------------------------------------------------------

import requests

try:
    reply = requests.get("http://localhost:3000/cars")
except:
    print("Communication error")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.headers['Content-Type'])
        print(reply.json())
    else:
        print("Server error")



import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
kay_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, kay_widths):
        print(n.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, kay_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    for car in json:
        show_car(car)


try:
    reply = requests.get('http://localhost:3000/cars')
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    else:
        print('Server error')

# ----------------------------------------------------------------------

import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


try:
    reply = requests.get('http://localhost:3000/cars/2')
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')





# ----------------------------------------------------------------------

import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


try:
    reply = requests.get('http://localhost:3000/cars?_sort=production_year')
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')


# ----------------------------------------------------------------------
# order desc
import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


try:
    reply = requests.get('http://localhost:3000/cars?_sort=production_year&_order=desc')
except requests.RequestException:
    print('Communication error')
else:
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')


# ----------------------------------------------------------------------

# By default, a server implementing HTTP version 1.1 works in the following manner:
#
# - it waits for the client's connection;
#
# - it reads the client's request;
#
# - it sends its response;
#
# - it keeps the connection alive, waiting for the client's next request;
#
# - if the client is inactive for some time, the server silently closes the connection; this means that the client is
# obliged to set up a new connection again if it wants to send another request.

import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


try:
    reply = requests.get('http://localhost:3000/cars')
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')




# ----------------------------------------------------------------------

# DELETE

import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


headers = {'Connection': 'Close'}
try:
    reply = requests.delete('http://localhost:3000/cars/1')
    print("res=" + str(reply.status_code))
    reply = requests.get('http://localhost:3000/cars/', headers=headers)
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')




# ----------------------------------------------------------------------

# POST

import json
import requests

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


h_close = {'Connection': 'Close'}
h_content = {'Content-Type': 'application/json'}
new_car = {'id': 7,
           'brand': 'Porsche',
           'model': '911',
           'production_year': 1963,
           'convertible': False}
print(json.dumps(new_car))
try:
    reply = requests.post('http://localhost:3000/cars', headers=h_content, data=json.dumps(new_car))
    print("reply=" + str(reply.status_code))
    reply = requests.get('http://localhost:3000/cars/', headers=h_close)
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')


# ----------------------------------------------------------------------
# UPDATE  / PUT

import requests, json

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


h_close = {'Connection': 'Close'}
h_content = {'Content-Type': 'application/json'}
car = {'id': 6,
       'brand': 'Mercedes Benz',
       'model': '300SL',
       'production_year': 1967,
       'convertible': True}
try:
    reply = requests.put('http://localhost:3000/cars/6', headers=h_content, data=json.dumps(car))
    print("res=" + str(reply.status_code))
    reply = requests.get('http://localhost:3000/cars/', headers=h_close)
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')


# ----------------------------------------------------------------------
# Last LAB exam

# import requests
# import json
#
# def check_server(cid=None):
# # returns True or False;
# # when invoked without arguments simply checks if server responds;
# # invoked with car ID checks if the ID is present in the database;
#
#
# def print_menu():
# # prints user menu - nothing else happens here;
#
# def read_user_choice():
# # reads user choice and checks if it's valid;
# # returns '0', '1', '2', '3' or '4'
#
#
# def print_header():
# # prints elegant cars table header;
#
# def print_car(car):
# # prints one car's data in a way that fits the header;
#
# def list_cars():
# # gets all cars' data from server and prints it;
# # if the database is empty prints diagnostic message instead;
#
#
# def name_is_valid(name):
# # checks if name (brand or model) is valid;
# # valid name is non-empty string containing
# # digits, letters and spaces;
# # returns True or False;
#
# def enter_id():
# # allows user to enter car's ID and checks if it's valid;
# # valid ID consists of digits only;
# # returns int or None (if user enters an empty line);
#
#
# def enter_production_year():
# # allows user to enter car's production year and checks if it's valid;
# # valid production year is an int from range 1900..2000;
# # returns int or None  (if user enters an empty line);
#
#
# def enter_name(what):
# # allows user to enter car's name (brand or model) and checks if it's valid;
# # uses name_is_valid() to check the entered name;
# # returns string or None  (if user enters an empty line);
# # argument describes which of two names is entered currently ('brand' or 'model');
#
# def enter_convertible():
# # allows user to enter Yes/No answer determining if the car is convertible;
# # returns True, False or None  (if user enters an empty line);
#
# def delete_car():
# # asks user for car's ID and tries to delete it from database;
#
#
# def input_car_data(with_id):
# # lets user enter car data;
# # argument determines if the car's ID is entered (True) or not (False);
# # returns None if user cancels the operation or a dictionary of the following structure:
# # {'id': int, 'brand': str, 'model': str, 'production_year': int, 'convertible': bool }
#
#
# def add_car():
# # invokes input_car_data(True) to gather car's info and adds it to the database;
#
#
# def update_car():
# # invokes enter_id() to get car's ID if the ID is present in the database;
# # invokes input_car_data(False) to gather new car's info and updates the database;
#
#
# while True:
#     if not check_server():
#         print("Server is not responding - quitting!")
#         exit(1)
#     print_menu()
#     choice = read_user_choice()
#     if choice == '0':
#         print("Bye!")
#         exit(0)
#     elif choice == '1':
#         list_cars()
#     elif choice == '2':
#         add_car()
#     elif choice == '3':
#         delete_car()
#     elif choice == '4':
#         update_car()






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------

