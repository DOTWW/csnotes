# How to use python in a console:
# python can be executed directly from the command line using "py" or "python"
# when wanting to exit python, use exit()

# How to run python programs:
# py "PATH TO PROGRAM.py"

# How Python works:
# Python is an Interpreter based language.
# Python Code -> Interpreter -> Machine Code

# Indentation:
# The number of spaces depends on the programmer but has to be at least 1.
# It also has to be consistent throughout the same block of code to make
# Python happy.
# Or if you want to keep your sanity, use the same Indentation
# throughout your whole program, and always use 4 spaces.
print("Python uses Indentation to indicate a block of code")
if (True):
 print("Hi") # This is an Indentation of 1 space
if (True):
    print("Hi again") # 4 spaces Indentation
    if (True == True):
        print("True is true")
    elif (True == False):
        print("True is false?!")
    else:
        print("Neither true nor false?!")

# Comments:
# Python lets you write comments with #
# Comments can be used to explain a program or they can be used to prevent
# code from executing.
print("Hello World")
# print("Hello Wolf")

# Variables:
# Naming a variable must follow some rules:
# 1. variables have to start with a letter or an underscore character
# 2. variables can only contain A-z, 0-9 and underscores _
# According to PEP8, which is a popular collection of guidelines to make code
# more readable, and which is followed by many programmers worldwide,
# variables should be in snake_case (all lowercase letters with underscores).
# In Python, variables are created when you assign a value to them.
# Python internally does two things: create an object (everything in python
# is an object) with a value, and assign the variable to reference the ID
# where the object is (similar to a pointer in C/C++).
# Unlike in C or other languages, you can not declare a variable without
# a value.
# Python automatically determines the type of the variable.
# Variables are case sensitive, meaning x != X (!= means does not equal)
x = 5
X = 6
print(x, X) # Output: 5 6
# Multiple variables can be declared in one line
a, b, c = 1, 2, 3
print(a, b, c)
# Or multiple variables with the same value can be created
d = e = f = 4
print(d, e, f)
# Good to know: Python caches numbers between -5 and 256 to prevent those
# numbers from being generated over and over again. TLDR:
# python identity "is" means pointing to the same object,
# but python equality "==" means same value, but it does not need to be the
# same object.
a = b = 557
if a is b:
    print("Same ID for a and b")
c = 556
c += 1
if c is b:
    print("c is also the same ID")
elif c == b:
    print("c is not the same object as b, but has the same value")
else:
    print("Wait, this shouldn't happen, oops.")
# Unpacking a collection of values in a list, touple, etc.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z, sep=", ")
# While we're at it:
# Touples touple_ = ('v1', 'v2', 'v3')
# Lists list_ = ['v1', 'v2', 'v3']
# But more later.
# Variables can change their type after they have been set
print("For x = 5, x is:", x, "and of type:", type(x))
x = "now in HD"
print("For x = \"now in HD\", x is:", x, "and of type:", type(x))
# Variable Casting means changing the type of a variable and can be done with
# <type>(<variable>). You can get the type of a variable with type(<var>).
x = 2
print("For x = 2, x is:", x, "and of type:", type(x))
x = str(2)
print("For x = str(2), x is:", x, "and of type:", type(x))
print("When casting without assigning a new value to x with int(x),\n",
    "int(x) is:", int(x), "and of type:", type(int(x)))
print("But x is still:", x, "and of type:", type(x))
# Single or double quotes both work for strings.
# You can use the + operator to concatenate (connect) strings the same way you
# can use operators to do calculations with numbers:
a, b, c = "Hello", ", ", "World!"
print(a + b + c)
a = a + b + c
print(a)
# Output for both: Hello, World!
# But you can't use the - operator to remove a part of a string.
# And you can not add a number to a string.

# Global vs Local Space:
# Variables that are created outside of functions are global.
# This means they are accessible by all functions
# Whereas local variables override global variables but only inside
# the function where they are called.
x = 1


def func1():
    """Set the value of a local variable x to 2 and print x"""
    x = 10
    print(x)


def func2():
    """Print the global variable x if it exists"""
    if 'x' in globals():
        print(x)
    else:
        print("Could not find a global variable x")


#another solution:
def func3():
    """Print a variable x without checking if it exists but catch the error
    to prevent the program from crashing and create a global variable x.
    """
    try:
        print(x)
    except BaseException as e:
        print(e)
        

func1()


func2()


func3()


del(x)


func1()


func2()


func3()


# you can change global variables inside functions:

x = 1


def func4():
    """Change the value of the global variable x"""
    global x
    x = 2


func2() # 1


func4() # change x to 2 globally


func2() # 2


# Datatypes:

# Python has a few built-in datatypes:

# Text:

#     str
# Anything between single or double quotes
"""strings in python are arrays of bytes representing unicode characters,
like in C or other popular programming languages. Strings end with \0 (NULL).
Therefore the string hello which has four letters, actually has a length of 5.
"""
s = "hello"
s = 'hello'
mults = """Multiline strings can also be created using triple quotes.
In this case the line breaks are at the same position as the line breaks
in the code."""


# Numeric:

#     int
# Any whole number, positive or negative
"""The default type of int depends on your processor architecture.
Python automatically converts the integer type in the background
to prevent overflow errors.
32bit architecture: Int32
64bit architecture: Int64

Here's a recap for min and max values for different integer types:
Int8: [
    -128,
    127]
Int16: [
    -32768,
    32767]
Int32: [
    -2147483648,
    2147483647]
Int64: [
    -9223372036854775808,
    9223372036854775807]
Int128: [
    -170141183460469231731687303715884105728,
    170141183460469231731687303715884105727]

And the unsigned integers:
UInt8: [
    0,
    255]
UInt16: [
    0,
    65535]
UInt32: [
    0,
    4294967295]
UInt64: [
    0,
    18446744073709551615]
UInt128: [
    0,
    340282366920938463463374607431768211455]

the command type() will always return "int" however.

In other languages you can use:
Int16 = short
Int32 = int
Int64 = long
Int128 = long long
"""
i = 1
i = 2

#     float
# Any number with a decimal point or written in scientific notation
# scientific notation: e = power of 10, example: 2e2 = 2 * (10*10) = 200
"""
Python also handles floats differently than some other programming languages.
What Python calls float would be a double in C or Java.
More specifically, this is called float64.

But unlike int64, float64 does not mean you get 64 bits to play with.
float64: 11 bits exponent + 52 bits mantissa + 1 bit sign = 64 bit

BUUUUT things get weird and complicated fast beyond that.
And with that I mean I don't understand it much.
Here's what I found:

float = 4 byte = 32bit
double = 8 byte = 64bit = float64 in Python
long double = 10 byte = 80bit = float96/float128 in Python
long doubles are also called extended doubles, and are not always standard.

For example, float128 does not exist on some Windows machines.
There seem to be some errors that some people run into regarding this.
Best to keep this in mind to stick with regular floats,
don't try to typecast (convert the type) manually to float128,
and let Python handle the rest automatically.

Bonus fact to make things even more weird and confusing with floats:
This is more along the lines of processor architecture, so you definitely
don't need to know this, but sometimes, not always, in the mantissa of a float,
the leading first bit is dropped because it's a 1 for any non-zero value.
This increases the precision because it gives you a whole extra bit
to work with, but you have to keep in mind that there should be a 1
before the number. x87 extended precision does not follow this.
"""
f = 1.0
f = 2e2

#     complex
# complex numbers with two parts: real and imaginary.
# the j indicates the imaginary part of the number.
# will not explain complex numbers here. See Math part for specifics.
c = 1j
c = 2+1j

# For all numeric data types, +, -, * and / work.
# You can typecast (convert) between the data types and also do operations
# across different data types. Python will then use the stronger data type
# for the output to prevent loss of precision.
# For example: 1 + 2 = 3 (type int) but 1 + 2.0 = 3.0 (type float)
"""
There are many more operations you can do of course. You can round floats,
truncate (aka. "cut") them, use advanced math functions,
or you could print a formatted version while keeping the precision of a float.
All of this will be handled later.
"""


# Sequence:

#     list
list_ = [1, 2.0, "apple"]
#     touple
touple_ = ("1", "2",)
#     range
range_ = range(0,6,2)
# Mapping:
#     dict
dictionary_ = {"name": "John", "age": 36}
# Set:
#     set
set_ = {"name", "age", "number"}
#     frozenset
frozenset_ = frozenset({"name", "age", "number"})
# Boolean:
#     bool
true_ = True
# Binary:
#     bytes
bytes_ = b"hello"
#     bytearray
bytearray_ = bytearray(5)
#     memoryview
memoryview_ = memoryview(bytes(5))

# As mentioned previously, the data type can be viewed with type(<var>)

# Something to note:
# Python defaults to lists over arrays, but lists require more space than
# C arrays, because objects need to be constructed for each included item.
list1 = [1,2,3]
print(type(list1))
# Because there's more than enough space and lists are nicer to work with
# than arrays, I'll leave it at this note. But there's a thin wrapper that
# can create a C-style array if it's really necessary, but needs to be imported
# before use.
# In C, an array is a consecutive block of memory assigned/allocated for easy
# data access and manipulation. C arrays are not dynamic,
# but they can be dynamically allocated and reallocated using functions.

# String operations:

# Strings are arrays 