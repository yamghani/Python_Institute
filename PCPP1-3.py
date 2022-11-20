import tkinter
from tkinter import messagebox


def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy();


skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)
skylight.mainloop()


# ----------------------------------------------------------------------

# The most usable place() method parameters are as follows (all of them are passed as keyword arguments):
#
# height=h – the widget's desired height measured in pixels; if the parameter is omitted, the widget's height
# will be determined automatically;
# width=w – the widget's desired width measured in pixels; if the parameter is omitted, the widget's width
# will be determined automatically;
# x=x – the widget's top-left pixel's horizontal coordinate measured relative to the home window's top-left corner;
# y=y – the widget's top-left pixel's vertical coordinate measured relative to the home window's top-left corner.

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.place(x=10, y=10, width=150)
button_2.place(x=20, y=40)
button_3.place(x=30, y=70, height=50)
window.mainloop()


# ----------------------------------------------------------------------

# The most commonly used grid() method parameters are gathered below (as, previously, all of them are passed as
# keyword arguments):
#
# column=c – deploys the widget in the column number c; note: the columns' numbers start from zero, and if you omit ' \
#                                                                        'this argument, the manager will assume 0 ' \
#                                                                        '(the left-most column)
# row=r – deploys the widget in the row number r; if you omit this argument, the manager will assume the first free
# row starting from the top;
# columnspan=cs – determines how many neighboring columns the widget occupies; the parameter defaults to 1 (the
# widget won't cross a single grid's cell)
# rowspan=rs – works as columnspan but refers to rows.

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=2)
window.mainloop()


# ----------------------------------------------------------------------
import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=0, columnspan=2)
window.mainloop()


# ----------------------------------------------------------------------
# side=s – forces the manager to pack the widgets in a specified direction, where s can be specified as:
# TOP – the widget is packed toward the window's top (it's manager's default behavior)
# BOTTOM – the widget is packed toward the window's bottom;
# LEFT – toward the window's left boundary;
# RIGHT – toward the window's right boundary;
# fill=f – suggests to the manager how to expand the widget if you want it to occupy more space than the default,
# while f should be specified as:
# NONE – do not expand the widget (default behavior)
# X – expand it in the horizontal direction;
# Y – expand it in the vertical direction;
# BOTH – expand it in both directions;

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack(side=tk.RIGHT)
button_2.pack()
button_3.pack()
window.mainloop()

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack(side=tk.RIGHT, fill=tk.Y)
button_2.pack()
button_3.pack()
window.mainloop()

window = tk.Tk()
button = tk.Button(window, text="Button #1", bg="red", fg="yellow")
button.pack()
window.mainloop()

window = tk.Tk()
button = tk.Button(window, text="Button #1",
                   bg="MediumPurple",
                   fg="LightSalmon",
                   activeforeground="LavenderBlush",
                   activebackground="HotPink")
button.pack()
window.mainloop()

# When all the components are set to zero (absence of the colors), we get black as a result.
#
# When all the components are set to 255 (full presence of the colors), we get white as a result.
#
# When one of the components is set to 255 while others are set to 0, we get one of the primary colors –
# red, green or blue.

# This is how it works:
#
# #RRGGBB
#
# All three pairs (RR, GG and GG) are two-digit hexadecimal number so:
#
# #000000 is black
# #FFFFFF is white
# #FF0000 is red
# #00FF00 is green
# #0000FF is blue
# #00FFFF is turquoise
# #FF00FF is violet
# ...

window = tk.Tk()
button = tk.Button(window, text="Button #1",
                   bg="#9370DB",
                   fg="#FFA07A",
                   activeforeground="#FFF0F5",
                   activebackground="#FF69B4")
button.pack()
window.mainloop()


# ----------------------------------------------------------------------

# Objects of the IntVar class are used by tkinter to organize internal communication between different widgets.
# A regular variable can't play such a role.

import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(window, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

window.mainloop()


# ----------------------------------------------------------------------

import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(window, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(0)

checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()

entry = tk.Entry(window, width=30)
entry.pack()

window.mainloop()


import tkinter
from tkinter import messagebox


def clicked():
    messagebox.showinfo("info", "some\ninfo")


window = tkinter.Tk()
button_1 = tkinter.Button(window, text="Show info", command=clicked)
button_1.pack()
button_2 = tkinter.Button(window, text="Quit", command=window.destroy)
button_2.pack()
window.mainloop()


import tkinter as tk
from tkinter import messagebox


def click():
    tk.messagebox.showinfo("Click!", "I love clicks!")


window = tk.Tk()
label = tk.Label(window, text="Label")
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.pack()

window.mainloop()

# ----------------------------------------------------------------------

# Fortunately, you’re still able to bind a callback to any of the events it may receive (including clicks, of course)
# and this is done with a method named – it couldn’t be anything else – bind():
#
# widget.bind(event, callback)
#
# The bind() method needs two arguments:
#
# the event you want to launch your callback with;
# the callback itself.

# Events and how to handle them

# https://edube.org/learn/pcpp1-4-gui-programming/events-and-how-to-handle-them-4

import tkinter as tk
from tkinter import messagebox


def click(event=None):
    tk.messagebox.showinfo("Click!", "I love clicks!")


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)   # Line I
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-2>", click)   # Line II
frame.pack()

window.mainloop()


# ----------------------------------------------------------------------
# If you want to modify a property named prop, existing within a widget named wid, and you’re going set its value
# to val, you can use the config() method, just like here:
#
# wid.config(prop=val)
#
# This means that if you want to unbind your current callback from a Button named b1, you would use an invocation
# like this one:
#
# b1.config(command=lambda:None)
#
# This binds an empty (i.e., doing absolutely nothing) function to the widget’s callback.


import tkinter as tk
from tkinter import messagebox


def click(event=None):
    if event is None:
        tk.messagebox.showinfo("Click!", "I love clicks!")
    else:
        string = "x=" + str(event.x) + ",y=" + str(event.y) + \
                 ",num=" + str(event.num) + ",type=" + event.type
        tk.messagebox.showinfo("Click!", string)


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)
button.config(command=lambda: None)


frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)
frame.pack()

window.mainloop()

# ----------------------------------------------------------------------
#
# To unbind a callback previously bound with the bind() method invocation, you need to use the unbind() method:
#
# widget.unbind(event)
#
# The method requires one argument identifying the event being unbound.
#
# Note: the information about a previously used callback is lost. You cannot
# retrieve it automatically, and you must repeat the bind() invocation.

import tkinter as tk
from tkinter import messagebox


def on_off():
    global switch
    if switch:
        button_2.config(command=lambda: None)
        button_2.config(text="Gee!")
    else:
        button_2.config(command=peekaboo)
        button_2.config(text="Peekaboo!")
    switch = not switch


def peekaboo():
    messagebox.showinfo("", "PEEKABOO!")


def do_nothing():
    pass


switch = True
window = tk.Tk()
buton_1 = tk.Button(window, text="On/Off", command=on_off)
buton_1.pack()
button_2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
button_2.pack()
window.mainloop()


# ----------------------------------------------------------------------

import tkinter as tk


def on_off():
    global switch
    if switch:
        label.unbind("<Button-1>")
    else:
        label.bind("<Button-1>", rhyme)
    switch = not switch


def rhyme(dummy):
    global word_no, words
    word_no += 1
    label.config(text=words[word_no % len(words)])


switch = True
words = ["Old", "McDonald", "Had", "A", "Farm"]
word_no = 0
window = tk.Tk()
button = tk.Button(window, text="On/Off", command=on_off)
button.pack()
label = tk.Label(window, text=words[0])
label.bind("<Button-1>", rhyme)
label.pack()
window.mainloop()

# ----------------------------------------------------------------------
#
# The main tkinter window has a method named bind_all() which binds a callback to all currently existing widgets.
#
# There is also a method named unbind_all() which reverts the first method’s effects.

import tkinter as tk
from tkinter import messagebox


def hello(dummy):
    messagebox.showinfo("", "Hello!")


window = tk.Tk()
button = tk.Button(window, text="On/Off")
button.pack()
label = tk.Label(window, text="Label")
label.pack()
frame = tk.Frame(window, bg="yellow", width=100, height=20)
frame.pack()
window.bind_all("<Button-1>", hello)
window.mainloop()

# ----------------------------------------------------------------------

# The first method is based on using a dictionary which exists inside every widget. Assuming that a widget named Widget
# has a property named prop and you want to read its value and then set it with a new value, you can do this in
# the following way:

import tkinter as tk


def on_off():
    global button
    state = button["text"]
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button["text"] = state


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()

# ----------------------------------------------------------------------
# The second method relies on two specialized widget methods, the first named cget() designed to read the property’s
# value, and the second named config(), which allows you to set a new value to the property.

import tkinter as tk


def on_off():
    global button
    state = button.cget("text")
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button.config(text=state)


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()


# ----------------------------------------------------------------------

# One of the properties we want to tell you about is font. Every widget presenting a piece of text
# (e.g., Button and Label but not Frame) can be made to use a font different from the default.
#
# Tkinter represents fonts as tuples.


import tkinter as tk


window = tk.Tk()
label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog")
label_1.grid(column=0, row=0)
label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"))
label_2.grid(column=0, row=1)
label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"))
label_3.grid(column=0, row=2)
window.mainloop()

# ----------------------------------------------------------------------
# Every widget occupies a part of the window’s area, thus it’s obvious the widgets must have sizes. Interestingly,
# widgets have properties describing many more sizes than just width (usually specified in pixels) and height
# (which can be specified in rows of text if the widget is able to present textual information).

# List of widget property names

# https://edube.org/learn/pcpp1-4-gui-programming/visiting-widgets-properties-4

import tkinter as tk


window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button");
button_1.pack()
button_2 = tk.Button(window, text="Exceptional button")
button_2.pack()
button_2["borderwidth"] = 10
button_2["highlightthickness"] = 10
button_2["padx"] = 10
button_2["pady"] = 5
button_2["underline"] = 1
window.mainloop()


# ----------------------------------------------------------------------
# Color property names
# https://edube.org/learn/pcpp1-4-gui-programming/visiting-widgets-properties-5


import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button");
button_1.pack()
button_2 = tk.Button(window, text="Colorful button")
button_2.pack()
button_2.config(bg ="#000000")
button_2.config(fg ="yellow")
button_2.config(activeforeground ="#FF0000")
button_2.config(activebackground ="green")
window.mainloop()

# ----------------------------------------------------------------------
# Anchor property

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Regular button");
button_1["anchor"] = "e"
button_1["width"] = 20  # pixels!
# button_1.config(width=20)
button_1.pack()
button_2 = tk.Button(window, text="Another button")
button_2["anchor"] = "sw"
button_2["width"] = 20
button_2["height"] = 3  # rows
button_2.pack()
window.mainloop()

# ----------------------------------------------------------------------
# Cursor

# https://www.tcl.tk/man/tcl8.4/TkCmd/cursors.html

import tkinter as tk

window = tk.Tk()
label_1 = tk.Label(window, height=3, text="arrow", cursor="arrow")
label_1.pack()
label_2 = tk.Label(window, height=3, text="clock", cursor="clock")
label_2.pack()
label_3 = tk.Label(window, height=3, text="heart", cursor="heart")
label_3.pack()
window.mainloop()


# ----------------------------------------------------------------------
# Widgets have methods – you’ve met some of them already. Now we’re going to show you a few more of them,
# and we’ll start with two which seem to be very specific. We can even say that the sense of their existence is
# very closely bound to the unique features of event programming.
#
# The methods are named (assuming that Widget is an existing widget):
#
# Widget.after(time_ms, function)
#
# Widget.after_cancel(id)

# ----------------------------------------------------------------------
# The destroy() method is very destructive. It removes the widget completely, not only from your sight, but also from
# the event manager’s memory, as the widget’s object is deleted and becomes inaccessible.

import tkinter as tk


def suicide():
    frame.destroy()


window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='green')
button = tk.Button(frame, text="I'm a frame's child")
button.place(x=10, y=10)
frame.after(5000, suicide)
frame.pack()
window.mainloop()

# ----------------------------------------------------------------------
# the focus_get() method returns a reference to the currently focused widget, or None when no widget owns the focus
# (note: you can invoke the method from any widget, including the main window)
# the focus_set() method focuses the widget from the method which was invoked, so you have to choose it carefully.


import tkinter as tk


def flip_focus():
    if window.focus_get() is button_1:
        button_2.focus_set()
    else:
        button_1.focus_set()
    window.after(1000, flip_focus)


window = tk.Tk()
button_1 = tk.Button(window, text="First")
button_1.pack()
button_2 = tk.Button(window, text="Second")
button_2.pack()
window.after(1000, flip_focus)
window.mainloop()

# ----------------------------------------------------------------------
# Variables
# To implement some of its functions, Tkinter uses a very special kind of variable called an observable variable.
# This variable works like a regular variable (i.e., it’s able to store values which are accessible to the outside world
# but there is something more – any change of the variable’s state can be observed by a number of external agents.
# For example, the Entry widget can use its own observable variable to inform other objects that the contents of the
# input field have been changed.
#
# From a technical point of view, such a variable is an object of the container class. This means that a variable of
# that kind has to be explicitly created and initialized.

# There is another important difference – these variables are typed. You have to be aware of what type of value you
# want to store in them, and don’t change your mind during the variable’s life.
#
# Note: you can only create an observable variable after the main window initialization. Don’t forget this –
# you’ve been warned!

# There are four kinds (types) of observable variable used by tkinter:
#
# BooleanVar
# DoubleVar
# IntVar
# StringVar
#
# Note: the newly created variables are set to:
#
# integer 0 for IntVar;
# float 0.0 for DoubleVar;
# Boolean False for BooleanVar;
# string "" for StringVar.

# Each observable variable can be enriched with a number of observers. An observer is a function (a kind of callback)
# which will be invoked automatically each time a specified event occurs in the variable’s life.

# obsid = variable.trace(trace_mode, observer)


# The method takes two arguments:
#
# a string describing which events should trigger an observer – the possible values are:
# "r" – if you want to be aware of the variable reads (accessing its value through get())
# "w" – if you want to be aware of the variable writes (changing its value through set())
# "u" – if you want to be aware of the variable’s annihilation (removing the object through del)
# a reference to a function which will be invoked when the specified event occurs.
# The function returns a string which is a unique observer identifier. Don’t try to interpret its contents.
# You don’t want to know its meaning.

# ----------------------------------------------------------------------
# The observer should be declared as a three-parameter function:
#
# def observer(id, ix, act):
# :
# :
#
#
# id – an internal observable variable identifier (unusable for us);
# ix – an empty string (always – don’t ask us why, it’s tkinter’s business)
# act – a string informing us what happened to the variable or, in other words, what reason triggered
# the observer ('r', 'w' or 'u')
# If you don’t need any of the arguments, you can declare the observer as: def obs(*):
#
# Removing the observer is done with a method named trace_vdelete():
#
# variable.trace_vdelete(trace_mode,obsid)
#
# Its arguments’ meanings are as follows:
#
# trace_mode – the mode in which the observer has been created;
# obsid – the observer’s identifier obtained from the previous trace() invocation.

import tkinter as tk


def r_observer(*args):
    print("Reading")


def w_observer(*args):
    print("Writing")


dummy = tk.Tk()    # we need this although we won't display any windows
variable = tk.StringVar()
variable.set("abc")
r_obsid = variable.trace("r", r_observer)
w_obsid = variable.trace("w", w_observer)
variable.set(variable.get() + 'd')  # read followed by write
variable.trace_vdelete("r", r_obsid)
variable.set(variable.get() + 'e')
variable.trace_vdelete("w", w_obsid)
variable.set(variable.get() + 'f')
print(variable.get())

# ----------------------------------------------------------------------
# Lexicon

# Check button
# https://edube.org/learn/pcpp1-4-gui-programming/a-small-lexicon-of-widgets-part-1-2

import tkinter as tk


def switch():
    if button_1.cget('state') == tk.DISABLED:
        button_1.config(state=tk.NORMAL)
        button_1.flash()
    else:
        button_1.flash()
        button_1.config(state=tk.DISABLED)


def mouseover(ev):
    button_1['bg'] = 'green'


def mouseout(ev):
    button_1['bg'] = 'red'


window = tk.Tk()
button_1 = tk.Button(window, text="Enabled", bg="red")
button_1.bind("<Enter>", mouseover)
button_1.bind("<Leave>", mouseout)
button_1.pack()
button_2 = tk.Button(window, text="Enable/Disable", command=switch)
button_2.pack()
window.mainloop()

# ----------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox


def count():
    global counter
    counter += 1


def show():
    messagebox.showinfo("", "counter=" + str(counter) + ",state=" + str(switch.get()))


window = tk.Tk()
switch = tk.IntVar()
counter = 0
button = tk.Button(window, text="Show", command=show)
button.pack()
checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
checkbutton.pack()
window.mainloop()

# ----------------------------------------------------------------------

# https://edube.org/learn/pcpp1-4-gui-programming/a-small-lexicon-of-widgets-part-1-10

import tkinter as tk
from tkinter import messagebox


def show():
    messagebox.showinfo("", "radio_1=" + str(radio_1_var.get()) +
                        ",radio_2=" + str(radio_2_var.get()))


def command_1():
    radio_2_var.set(radio_1_var.get())


def command_2():
    radio_1_var.set(radio_2_var.get())


window = tk.Tk()
button = tk.Button(window, text="Show", command=show)
button.pack()
radio_1_var = tk.IntVar()
radio_1_1 = tk.Radiobutton(window, text="pizza", variable=radio_1_var, value=1, command=command_1)
radio_1_1.select()
radio_1_1.pack()
radio_1_2 = tk.Radiobutton(window, text="clams", variable=radio_1_var, value=2, command=command_1)
radio_1_2.pack()
radio_2_var = tk.IntVar()
radio_2_1 = tk.Radiobutton(window, text="FR", variable=radio_2_var, value=2, command=command_2)
radio_2_1.pack()
radio_2_2 = tk.Radiobutton(window, text="IT", variable=radio_2_var, value=1, command=command_2)
radio_2_2.select()
radio_2_2.pack()
window.mainloop()


# ----------------------------------------------------------------------

import tkinter as tk


def to_string(x):
    return "Current counter\nvalue is:\n" + str(x)


def plus():
    global counter
    counter += 1
    text.set(to_string(counter))


counter = 0
window = tk.Tk()
button = tk.Button(window, text="Go on!", command=plus)
button.pack()
text = tk.StringVar()
label = tk.Label(window, textvariable=text, height=4)
text.set(to_string(counter))
label.pack()
window.mainloop()

# ----------------------------------------------------------------------

import tkinter as tk


def do_it_again():
    text.set(text.get() + "and again...")


window = tk.Tk()
button = tk.Button(window, text="Go ahead!", command=do_it_again)
button.pack()
text = tk.StringVar()
message = tk.Message(window, textvariable=text, width=400)
text.set("You did it again... ")
message.pack()
window.mainloop()


# ----------------------------------------------------------------------

import tkinter as tk

window = tk.Tk()

frame_1 = tk.Frame(window, width=200, height=100, bg='white')
frame_2 = tk.Frame(window, width=200, height=100, bg='yellow')

button_1_1 = tk.Button(frame_1, text="Button #1 inside Frame #1")
button_1_2 = tk.Button(frame_1, text="Button #2 inside Frame #1")
button_2_1 = tk.Button(frame_2, text="Button #1 inside Frame #2")
button_2_2 = tk.Button(frame_2, text="Button #2 inside Frame #2")

button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=50)
button_2_1.grid(column=0, row=0)
button_2_2.grid(column=1, row=1)

frame_1.pack()
frame_2.pack()

window.mainloop()


# ----------------------------------------------------------------------

import tkinter as tk

window = tk.Tk()
label_frame_1 = tk.LabelFrame(window, text="Frame #1",
                              width=200, height=100, bg='white')
label_frame_2 = tk.LabelFrame(window, text="Frame #2",
                              labelanchor='sw', width=200, height=100, bg='yellow')

button_1_1 = tk.Button(label_frame_1, text="Button #1 inside Frame #1")
button_1_2 = tk.Button(label_frame_1, text="Button #2 inside Frame #1")
button_2_1 = tk.Button(label_frame_2, text="Button #1 inside Frame #2")
button_2_2 = tk.Button(label_frame_2, text="Button #2 inside Frame #2")

button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=50)
button_2_1.grid(column=0, row=0)
button_2_2.grid(column=1, row=1)

label_frame_1.pack()
label_frame_2.pack()
window.mainloop()


# ----------------------------------------------------------------------

import tkinter as tk


def digits_only(*args):
    global last_string
    string = text.get()
    if string == '' or string.isdigit():  # Field's content is valid.
        last_string = string
    else:
        text.set(last_string)


last_string = ''
window = tk.Tk()
text = tk.StringVar()
entry = tk.Entry(window, textvariable=text)
text.set(last_string)
text.trace('w', digits_only)
entry.pack()
entry.focus_set()
window.mainloop()


# ----------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")


window = tk.Tk()

# main menu creation
main_menu = tk.Menu(window)
window.config(menu=main_menu)

# 1st main menu item: an empty (as far) submenu
sub_menu_file = tk.Menu(main_menu)
main_menu.add_cascade(label="File", menu=sub_menu_file)

# 2nd main menu item: a simple callback
sub_menu_help = tk.Menu(main_menu)
main_menu.add_command(label="About...", command=about_app)

window.mainloop()

# Using underline
# ----------------------------------------

import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")


window = tk.Tk()

main_menu = tk.Menu(window)
window.config(menu=main_menu)
sub_menu_file = tk.Menu(main_menu)
# setting the hotkey to "Alt-F"
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
sub_menu_help = tk.Menu(main_menu)
# setting the hotkey to "Alt-B"
main_menu.add_command(label="About...", command=about_app, underline=1)

window.mainloop()

# ----------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")


def are_you_sure():
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()


def open_file():
    messagebox.showinfo("Open doc", "We'll open a file here...")


window = tk.Tk()

main_menu = tk.Menu(window)
window.config(menu=main_menu)
sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# add the QUIT action to the submenu
# a new submenu item is here!
sub_menu_file.add_command(label="Open...", underline=0, command=open_file)

sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

for i in range(8):
    number = str(i + 1)
    sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)

# separator is here!
sub_menu_file.add_separator()
sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
sub_menu_help = tk.Menu(main_menu)
main_menu.add_command(label="About...", command=about_app, underline=1)

window.mainloop()

# ----------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")


def are_you_sure(event=None):
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()


def open_file():
    messagebox.showinfo("Open doc", "We'll open a file here...")


window = tk.Tk()

main_menu = tk.Menu(window)
window.config(menu=main_menu)
sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

for i in range(8):
    number = str(i + 1)
    sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)

sub_menu_file.add_separator()
sub_menu_file.add_command(label="Quit", accelerator="Ctrl-Q",
                          underline=0, command=are_you_sure)
sub_menu_help = tk.Menu(main_menu)
main_menu.add_command(label="About...", command=about_app, underline=1)

window.bind_all("<Control-q>", are_you_sure)
# window.bind_all("q", are_you_sure)
window.mainloop()


# ----------------------------------------------------------------------
# Note: you cannot modify any of the (sub)menu item by using the standard config() method invocation, because from
# tkinter's point of view, the item is not a widget – it’s only a very specific widget component.
#
# If you want to manipulate a menu’s item, you should use a dedicated method named entryconfigure(). The method accepts
# two parameters:
#
# item.entryconfigure(i, prop=value)
#
#
# the first is an integer index of the modified item (entry)
# the second is a keyworded argument pointing to the modified property.

# https://edube.org/learn/pcpp1-4-gui-programming/a-small-lexicon-of-widgets-part-3-23


import tkinter as tk


def on_off():
    global accessible
    if accessible == tk.DISABLED:
        accessible = tk.ACTIVE
    else:
        accessible = tk.DISABLED
    sub_menu.entryconfigure(1, state=accessible)


accessible = tk.DISABLED
window = tk.Tk()
menu = tk.Menu(window)
window.config(menu=menu)
sub_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=sub_menu)
sub_menu.add_command(label="On/Off", command=on_off)
sub_menu.add_command(label="Switch", state=tk.DISABLED)
window.mainloop()

# ----------------------------------------------------------------------
# Window config

# title

import tkinter as tk


def click(*args):
    global counter
    if counter > 0:
        counter -= 1
    window.title(str(counter))


counter = 10
window = tk.Tk()
window.title(str(counter))
window.bind("<Button-1>", click)
window.mainloop()

# prepare an icon as a PNG image;
# put the image in the same directory where the application resides;
# use a PhotoImage class constructor to convert the PNG file into an internal tkinter representation
# (PhotoImage() is a part of tkinter, and we’re going to tell you more about it soon)

import tkinter as tk

window = tk.Tk()
window.title('Icon?')
window.tk.call('wm', 'iconphoto', window._w, tkinter.PhotoImage(file='logo.png'))
window.bind("&lt;Button-1&gt;", lambda e: window.destroy())
window.mainloop()

# ----------------------------------------------------------------------

import tkinter as tk


def click(*args):
    global size, grows
    if grows:
        size += 50
        if size >= 500:
            grows = False
    else:
        size -= 50
        if size <= 100:
            grows = True
    window.geometry(str(size) + "x" + str(size))


size = 100
grows = True
window = tk.Tk()
window.geometry("100x100")
window.bind("<Button-1>", click)
# window.bind("&lt;Button-1&gt;", click)
window.mainloop()

# ----------------------------------------------------------------------
# Min/max size of window

import tkinter as tk

window = tk.Tk()
window.minsize(width=250, height=200)
window.geometry("500x500")
window.mainloop()


import tkinter as tk

window = tk.Tk()
window.maxsize(width=500, height=300)
window.geometry("200x200")
window.mainloop()


import tkinter as tk

window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry("400x200")
window.mainloop()


import tkinter as tk
from tkinter import messagebox


def really():
    if messagebox.askyesno("?", "Wilt thou be gone?"):
        window.destroy()


window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", really)
window.mainloop()


import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askyesno("?", "To be or not to be?")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="Ask the question!", command=question)
button.pack()
window.mainloop()


import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="What are your plans?", command=question)
button.pack()
window.mainloop()


import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askretrycancel("?", "I'm going to format your hard drive")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="What are your plans?", command=question)
button.pack()
window.mainloop()


import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askquestion("?", "I'm going to format your hard drive")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="What are your plans?", command=question)
button.pack()
window.mainloop()


import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.showerror("!", "Your code does nothing!")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="Alarming message", command=question)
button.pack()
window.mainloop()



import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.showwarning("Be careful!", "Big Brother is watching you!")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="What's going on?", command=question)
button.pack()
window.mainloop()

# ----------------------------------------------------------------------

# Canvas
# Our last meeting is devoted to the Canvas – a widget that behaves like a... canvas. It’s a flat, rectangular surface
# that you can cover with drawings, text, frames, and other widgets. Please treat this story as a basic introduction to
# the Canvas facilities

import tkinter as tk


window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()


import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380, arrow=tk.BOTH, fill='red', smooth=True, width=3)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='black')
canvas.create_rectangle(200, 100, 300, 300, outline='white', width=5, fill='red')
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()

# ----------------------------------------------------------------------

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='black')
canvas.create_polygon(20, 380, 200, 68, 380, 380, outline='red', width=5, fill='yellow')
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()




import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='blue')
canvas.create_oval(100, 100, 300, 200, outline='red', width=20, fill='white')
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()



import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas.create_arc(10, 100, 380, 300, outline='red', width=5)
canvas.create_arc(10, 100, 380, 300, outline='blue', width=5,
                  style=tk.CHORD, start=90, fill='white')
canvas.create_arc(10, 100, 380, 300, outline='green', width=5,
                  style=tk.ARC, start=180, extent=180)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()



import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='blue')
canvas.create_text(200, 200, text="Mary\nhad\na\nlittle\nlamb",
                   font=("Arial", "40", "bold"),
                   justify=tk.CENTER,
                   fill='white')
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()


import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
image = tk.PhotoImage(file='C:/Personal/Python_Institute/logo.png')
canvas.create_image(200, 200, image=image)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()


# ----------------------------------------------------------------------

# If you want to use a JPEG bitmap, some additional steps are required – you need to:
#
# import the Image and ImageTk classes from the PIL (Python Image Library) module;
# build an object of the Image() class and use its open() method to fetch the bitmap from the file
# (the argument should specify the file’s path)
# convert this object into a PhotoImage class object using an ImageTk function of the same name;
# continue as usual.


import tkinter as tk
import PIL
from PIL import  Image
from PIL import  ImageTk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='red')
jpg = PIL.Image.open('C:/Personal/Python_Institute/logo.jpg')
image = PIL.ImageTk.PhotoImage(jpg)
canvas.create_image(200, 200, image=image)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()

# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------






# ----------------------------------------------------------------------
