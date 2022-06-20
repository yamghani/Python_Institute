# In this course, you will learn about:
#
# sqlite - interacting with SQLite databases;
# xml - creating and processing xml files;
# csv - csv file reading and writing;
# logging - basics logging facility for Python;
# configparser - configuration file parser.


# ----------------------------------------------------------------------
# The database management system (DBMS) is the software responsible for:
#
# creating a database structure;
# inserting, updating, deleting, and searching data;
# ensuring data security;
# transaction management;
# ensuring concurrent access to data for many users;
# enabling data exchange with other database systems.

# SQLite is actually a C library which allows the user to read and write data directly to a file

# https://peps.python.org/pep-0249/

# It's also possible to use a special name, :memory:, which creates a database in RAM:

import sqlite3

conn = sqlite3.connect(':memory:')

# Remember that the connect method creates a database only if it cannot find a database in the given location.
# If a database exists, SQLite connects to it.

# SQLite generally implements the SQL-92 standard, with some exceptions that you can read about
# https://www.sqlite.org/lang.html

# ----------------------------------------------------------------------
# INSERT INTO table_name (column1, column2, column3, ..., columnN)
# VALUES (value1, value2, value3, ..., value4);

# Of course, we can define the value of the id column ourselves, but it's more convenient not to worry about it.
#
# The INSERT INTO statement also has a short form in which we can omit the column names:
#
# INSERT INTO table_name VALUES (value1, value2, value3, ..., valueN);

# The commit method confirms our changes (the current transaction). If you forget to call it,
# your changes wont be visible in the database.

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')
c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))
conn.commit()
conn.close()


# ----------------------------------------------------------------------
# The executemany method allows you to insert multiple records at once. As an argument, it accepts an SQL statement
# and an array containing any number of tuples.

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')
tasks = [
    ('My first task', 1),
    ('My second task', 5),
    ('My third task', 10),
]
c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)
conn.commit()
conn.close()


# ----------------------------------------------------------------------
# Refactoring

import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def add_task(self):
        name = input('Enter task name: ')
        priority = int(input('Enter priority: '))

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()


app = Todo()
app.add_task()


# ----------------------------------------------------------------------
# The SELECT statement allows you to read data from one or more tables. Its syntax looks like this:
#
# SELECT column FROM table_name;
#
# or
#
# SELECT column1, column2, column3, …, columnN FROM table_name;
#
# or
#
# SELECT * FROM table_name;

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM tasks'):
    print(row)
conn.close()


# ----------------------------------------------------------------------
# The fetchall method fetches all records (those not yet fetched from the query result)
# The fetchall method is less efficient than the iterator, because it reads all records into the memory and then returns
# a list of tuples.

# For small amounts of data, it doesnt matter, but if your table contains a huge number of records, this can cause
# # memory issues.

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('SELECT * FROM tasks')
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()

# ----------------------------------------------------------------------
# In addition to the iterator and the fetchall method, the Cursor object provides a very useful method called fetchone
# to retrieve the next available record

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('SELECT * FROM tasks')
row = c.fetchone()
print(row)
row = c.fetchone()
print(row)
conn.close()

# ----------------------------------------------------------------------
# The UPDATE statement is used to modify existing records in the database.

# UPDATE table_name
# SET column1 = value1, column2 = value2, column3 = value3, …, columnN = valueN
# WHERE condition;

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (20, 1))
c.commit()
c.close()

# ----------------------------------------------------------------------
# DELETE FROM table_name WHERE condition;

import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('DELETE FROM tasks WHERE id = ?', (1,))
c.commit()
c.close()

# ----------------------------------------------------------------------

# xml

# ----------------------------------------------------------------------

# xml.etree.ElementTree – has a very simple API for analyzing and creating xml data. It is an excellent choice for
# people who have never worked with the Document Object Model (DOM) before.
# xml.dom.minidom – is the minimum implementation of the Document Object Model (DOM). Using the DOM, the approach to
# an xml document is slightly different, because it is parsed into a tree structure in which each node is an object.
# xml.sax – SAX is an acronym for “Simple API for xml”. SAX is an interface in Python for event-driven xml document
# analysis. Unlike the above modules, analyzing a simple xml document using this module requires more work.

# Extensible Markup Language (xml) is a markup language intended for storing and transporting data, e.g.,
# by systems using the SOAP communication protocol.

# prolog – the first (optional) line of the document. In the prolog, you can specify character encoding, e.g.,
# <?xml version="1.0" encoding="ISO-8859-2"?> changes the default character encoding (UTF-8) to ISO-8859-2.
# root element – the xml document must have one root element that contains all other elements. In the example below,
# the main element is the data tag.
# elements – these consist of opening and closing tags. The elements include text, attributes, and other child elements.
# In the example below, we can find the book element with the title attribute and two child elements (author and year).
# attributes – these are placed in the opening tags. They consist of key-value pairs, e.g., title = "The Little Prince".

# <?xml version="1.0"?>
# <data>
#     <book title="The Little Prince">
#         <author>Antoine de Saint-Exupéry</author>
#         <year>1943</year>
#     </book>
#     <book title="Hamlet">
#         <author>William Shakespeare</author>
#         <year>1603</year>
#     </book>
# </data>

# The ElementTree object is responsible for presenting the xml document in the form of a tree on which we can move up
# or down.

import xml.etree.ElementTree as ET

tree = ET.parse('Python Institute/xml/books.xml')
root = tree.getroot()
print('The root tag is:', root.tag)
print('The root has the following children:')
for child in root:
    print(child.tag, child.attrib)

print("My books:\n")
for book in root:
    print('Title: ', book.attrib['title'])
    print('Author:', book[0].text)
    print('Year: ', book[1].text, '\n')

# In addition to the parse method, we can use the method called fromstring, which, as an argument,
# takes xml as a string:
# root = ET.fromstring(your_xml_as_string)


# ----------------------------------------------------------------------
# the Element class, provides several useful methods for finding elements in an xml document.

# The iter method returns all elements by having the tag passed as an argument.

import xml.etree.ElementTree as ET

tree = ET.parse('Python Institute/xml/books.xml')
root = tree.getroot()
for author in root.iter('author'):
    print(author.text)


# Unlike the iter method, the findall method only searches the children at the first nesting level.

import xml.etree.ElementTree as ET

tree = ET.parse('Python Institute/xml/books.xml')
root = tree.getroot()
for book in root.findall('book'):
    print(book.get('title'))
    print(book.attrib['title'])


import xml.etree.ElementTree as ET

tree = ET.parse('Python Institute/xml/books.xml')
root = tree.getroot()
for author in root.findall('author'):
    print(author.text)

# he find method returns the first child element containing the specified tag or matching XPath expression.

import xml.etree.ElementTree as ET

tree = ET.parse('Python Institute/xml/books.xml')
root = tree.getroot()
print(root.find('book').get('title'))


# ----------------------------------------------------------------------
# Let's modify the element tree and create a new xml file based on it with the following movie data:
#
# <?xml version="1.0"?>
# <data>
#     <movie title="The Little Prince" rate="5"></movie>
#     <movie title="Hamlet" rate="5"></movie>
# </data>

import xml.etree.ElementTree as ET

tree = ET.parse('Python Institute/xml/books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

# The remove method removes the child element passed as its argument, which must be an Element object.
# Note that for this purpose we use the method called find, which you're already familiar with.

import xml.etree.ElementTree as ET

tree = ET.parse('Python Institute/xml/books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'
    child.remove(child.find('author'))
    child.remove(child.find('year'))
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

# The Element object also has a method called set, which allows you to set any attribute.

import xml.etree.ElementTree as ET

tree = ET.parse('Python Institute/xml/books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'
    child.remove(child.find('author'))
    child.remove(child.find('year'))
    child.set('rate', '5')
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

# To save all the changes we’ve made to the tree, we have to use the method called write.

# To add a prolog to our document, we must pass True in the third argument.

import xml.etree.ElementTree as ET

tree = ET.parse('Python Institute/xml/books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'
    child.remove(child.find('author'))
    child.remove(child.find('year'))
    child.set('rate', '5')
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

tree.write('Python Institute/xml/movies.xml', 'UTF-8', True)


# how to build an xml document in Python.
# The Element class constructor takes two arguments. The first is the name of the tag to be created,
# while the second (optional) is the attribute dictionary

# dump method, which allows us to debug either the whole tree or a single element.

import xml.etree.ElementTree as ET

root = ET.Element('data')
ET.dump(root)

# the xml.etree.ElementTree module offers a function for creating child elements called SubElement

# The first one defines the parent element,
# the second one defines the tag name,
# and the third (optional) defines the attributes of the element

import xml.etree.ElementTree as ET

root = ET.Element('data')
movie_1 = ET.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})
ET.dump(root)


# ----------------------------------------------------------------------
# csv - csv file reading and writing;

# The reader function returns an object that allows you to iterate over each line in the csv file
# The newline='' argument added to the open function protects us from incorrect interpretation of the newline
# character on different platforms.


import csv

with open('Python Institute/csv/contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)

import csv

with open('Python Institute/csv/contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(','.join(row))

# each line is mapped to an OrderedDict object

import csv

with open('Python Institute/csv/contacts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], ':', row['Phone'])

 # If your file doesn't have a header, you must define it using the fieldnames argument

import csv

with open('Python Institute/csv/contacts.csv', newline='') as csvfile:
    fieldnames = ['Name', 'Phone']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in reader:
        print(row['Name'], row['Phone'])

# ----------------------------------------------------------------------
# Saving csv



import csv

with open('Python Institute/csv/exported_contacts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow(['Name', 'Phone'])
    writer.writerow(['mother', '222-555-101'])
    writer.writerow(['father', '222-555-102'])
    writer.writerow(['wife', '222-555-103'])
    writer.writerow(['mother-in-law', '222-555-104'])


# QUOTE_MINIMAL means that only values with special characters such as separator or quotechar will be quoted

# csv.QUOTE_ALL – quotes all values
#
# csv.QUOTE_NONNUMERIC – quotes only non-numeric values
#
# csv.QUOTE_NONE – doesn't quote any values. It's not a good idea to set this value if you have special characters
# that require quoting, because this will raise an error
#
# NOTE: The quotechar and quoting parameters can also be used in the reader function.


import csv

with open('Python Institute/csv/exported_contacts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(['Name', 'Phone'])
    writer.writerow(['mother', '222-555-101'])
    writer.writerow(['father', '222-555-102'])
    writer.writerow(['wife', '222-555-103'])
    writer.writerow(['mother-in-law', '222-555-104'])
    writer.writerow(['grandmother, grandfather', '222-555-105'])


 # In the csv module, there is an analogous class called DictWriter with which we can map dictionaries to rows.

import csv

with open('Python Institute/csv/exported_contacts.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name': 'mother', 'Phone': '222-555-101'})
    writer.writerow({'Name': 'father', 'Phone': '222-555-102'})
    writer.writerow({'Name': 'wife', 'Phone': '222-555-103'})
    writer.writerow({'Name': 'mother-in-law', 'Phone': '222-555-104'})
    writer.writerow({'Name': 'grandmother, grandfather and auntie', 'Phone': '222-555-105'})


# ----------------------------------------------------------------------
# logging - basics logging facility for Python;

# you can use the root logger. To do this, call the getLogger function without providing a name.
# The root logger is at the highest point in the hierarchy. Its place in the hierarchy is assigned based on the names
# passed to the getLogger function.

import logging

logger = logging.getLogger()
hello_logger = logging.getLogger('hello')
hello_world_logger = logging.getLogger('hello.world')
recommended_logger = logging.getLogger(__name__)

# Level name	Value
# CRITICAL	50
# ERROR	    40
# WARNING	    30
# INFO	    20
# DEBUG	    10
# NOTSET	     0

# You can also define your own level,
# You’re probably wondering why messages with INFO and DEBUG levels are not displayed.
# NOTE: The basicConfig method will be discussed later in the course. For now, remember that it is responsible for
#     the basic logging configuration.

import logging

logging.basicConfig()

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')


import logging

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')

# If the closest parent has a level set to NOTSET, the logger level is set based on the levels of subsequent parents in
# the hierarchy. Level setting ends if a parent has a level other than NOTSET. If none of the visited parents has a
# level other than NOTSET, then all messages will be processed regardless of their level.

# Calling the basicConfig method (without specifying any arguments) creates a StreamHandler object that processes the
# logs and then displays them in the console.

import logging

logging.basicConfig(level=logging.CRITICAL, filename='Python Institute/logs/prod.log', filemode='a')

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')

# The LogRecord object is automatically created by the logger during logging. It contains many attributes,
# such as the name of the logger, the logging level, or even the line number in which the logging method is called.
# A full list of all available attributes can be found here
# [https://docs.python.org/3/library/logging.html#logrecord-attributes].

import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a', format=FORMAT)

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')


# Each logger can save logs in different locations as well as in different formats.
# The logging module has the FileHandler class, which facilitates this task.
# you need to add the created handler to your logger using the addHandler method.

# NOTE: Each logger can have several handlers added. One handler can save logs to a file,
# while another can send them to an external service. In order to process messages
# with a level lower than WARNING by added handlers, it iss necessary to set this level threshold in
# the root logger.

import logging

logger = logging.getLogger(__name__)

handler = logging.FileHandler('prod.log', mode='w')
handler.setLevel(logging.CRITICAL)

logger.addHandler(handler)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')


# Adding Formatter to Handler

import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logger = logging.getLogger(__name__)

handler = logging.FileHandler('prod.log', mode='w')
handler.setLevel(logging.CRITICAL)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')


# ----------------------------------------------------------------------

# configparser - configuration file parser.

# Each service may require different data for authentication, but one thing is certain – we need to store it somewhere
# in our application. It's not a good idea to hardcode them directly in the code.
#
# A better solution is to use the configuration file, which will be read by the code.
# In Python, this is possible thanks to a module called configparser.

# The structure of the configuration file is very similar to Microsoft Windows INI files. It consists of sections
# that are identified by names enclosed in square brackets. The sections contain items consisting of key value pairs.
# Each pair is separated by a colon : or equals sign =.

# the configuration file may contain comments followed by a semicolon ; or hash #

# Sample:

# [DEFAULT]
# host = localhost # This is a comment.
#
# [mariadb]
# name = hello
# user = user
# password = password
#
# [redis]
# port = 6379
# db = 0

# Its also possible to access the values stored in the options by using the get method.
# The get method requires the section name and key to be passed. This is what it looks like in practice:

import configparser

config = configparser.ConfigParser()
print(config.read('config.ini'))

print('Sections:', config.sections(),'\n')

print('mariadb section:')
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))

# Result :
# Sections: ['mariadb', 'redis']
#
# mariadb section:
# Host: localhost
# Database: hello
# Username: user
# Password: password
#
# redis section:
# Host: localhost
# Port: 6379
# Database number: 0


# The configparser module enables configurations from various sources to be read.
# One of them is a dictionary that we can load using the read_dict


import configparser

config = configparser.ConfigParser()

dict = {
    'DEFAULT': {
        'host': 'localhost'
    },
    'mariadb': {
        'name': 'hello',
        'user': 'root',
        'password': 'password'
    },
    'redis': {
        'port': 6379,
        'db': 0
    }
}

config.read_dict(dict)

print('Sections:', config.sections(),'\n')

print('mariadb section:')
print('Host:', config['mariadb']['host'])
print('Database:', config['mariadb']['name'])
print('Username:', config['mariadb']['user'])
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'])
print('Port:', int(config['redis']['port']))
print('Database number:', int(config['redis']['db']))


# Creating Config File
# To create a configuration file, you should treat the ConfigParser object as a dictionary


import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {'host': 'localhost'}
config['mariadb'] = {'name': 'hello',
                     'user': 'root',
                     'password': 'password'}
config['redis'] = {'port': 6379,
                   'db': 0}

with open('config.ini', 'w') as configfile:
    config.write(configfile)


# ---------------------------------------------------------------------
# Interpolating values
# The big advantage of the configuration file is the possibility of using interpolation.
# It allows you to create expressions consisting of a placeholder under which the appropriate value will be substituted.


# [DEFAULT]
# host = localhost
#
# [mariadb]
# name = hello
# user = user
# password = password
#
# [redis]
# port = 6379
# db = 0
# dsn = redis://%(host)s


# The configuration file has been extended with another option called dsn.
# Its value contains the placeholder %(host)s, which needs to be replaced by an appropriate value.
#
# Placing any key between % and s informs the parser of the need to interpolate. Of course,
# all the work is done for us, and we only get the ready results.
#
# For the dsn option, it will be the following string: redis://localhost. Note that the placeholder %(host)s
# has been replaced by the value stored in the host option.











# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------








# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------

# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------

# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------



# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------

# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------

# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------

# ----------------------------------------------------------------------





