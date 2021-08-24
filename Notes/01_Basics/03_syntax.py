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
like in C or other popular programming languages.
Python does not have a NULL character to terminate the string. In fact,
string objects in python are immutable (meaning they can not be changed),
so in order to do anything, a new object needs to be created.
PYTHON IS WEIRD.
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

# Strings are arrays and can be accessed as such
s = "abc"
print(s[0], s[1], s[2])

# You can loop through a string with:
for char_ in s:
    print(char_, end='')
print() # new line

# the length of a string can be accessed with len():
print(len(s))

# or calculated manually using the above method:
s_count = 0
for char_ in s:
    s_count += 1
print(s_count)

# to check if something is contained in a string we can use the keyword "in":
if "d" in s:
    print("yup, there's a \"d\" in the string s:", s)
elif "a" in s:
    print("yup, there's an \"a\" in the string s, but no \"d\":", s)
else:
    print("This shouldn't happen")

# you can also use the keyword not to check for something not being present:
if "d" not in s:
    print("Told you there was no \"d\"")
else:
    print("Where did that \"d\" come from?")

# Note: at this point I'm starting to get really frustrated from constantly
# having to escape my double quotes and I'm seriously considering switching to
# single quotes for my strings because those would be a lot faster anyway.
# EITHER WAY:

# string slicing:

# you can return or check a range of characters by using a range:
# [start:end(not included):step]
s = 'hello, world!'
print(s[0:5])
# you can do silly things with this:
s = 'tacocat'
print(s) # print s
print(s[::-1]) # print s backwards
print(s[::2]) # only print every second character of s
# You can use negative indexing to start counting from the back:
print(s[:4], s[4:], 'backwards is spelled', s[:-4:-1], s[-4::-1])
s = '1234567'
print(s[:4], s[4:], 'backwards is spelled', s[:-4:-1], s[-4::-1])

# note this only works for strings so:
# i = 1234567
# print(i[0:3])
# does not execute, but typecasting might work in some cases for this:
i = 1234567
print(str(i)[0:3])

a = '        hi hoLLO'
print(a)

# strip removes leading and trailing whitespace
a = a.strip()
print(a)

# uppercase and lowercase operations are built into python:
# along with a whole array of other string related operations:
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.casefold())

# replace replaces something in a string:
a = a.replace("hi", "Hello,")
a = a.replace("hoLLO", "World!")
print(a)

# split string returns a list with a specified separator:
a1, a2 = a.split()
print(a.split())
print("a1:", a1, "a2:", a2)

# strings can be concatenated (think i mentioned that before)
b = a1 + " " + a2
print(b)


# String formatting:

# as mentioned somewhere before, strings and numbers can't be concatenated.
# another method than typecasting is to format something into a string:

age = 30 # or any user input
txt = 'Hello, I am {} years old'
# do things
print(txt.format(age))

# this can also take multiple inputs:
item_ = {"id": 122, "name": "Valve Index", "price": 999.00, "instock": 2}
quantity_ = 3
order_ = "Hello, I want to buy {0} of the item {1} for the total price of {2}"
print(order_.format(quantity_, item_["name"], (quantity_*item_["price"])))

if(item_["instock"] >= quantity_):
    print("Your order can be completed.",
        "Proceed to checkout or continue shopping?")
else:
    print(("We can only offer {0} of the item {1} for a total price of {2}")
        .format(item_["instock"], item_["name"],
            (item_["instock"]*item_["price"])))
    print("Would you like to change your order?")

# you can use numbers for the positions or you can use identifiers,
# or you can just use empty placeholders.
amt = 5
txt = "{amount} Pcs For Only ${price:.2f}! {}!"
print(txt.format("What a steal", price = 2.990, amount = amt))

# you can also use funny little smiley faces to format the placeholders
# https://www.w3schools.com/python/ref_string_format.asp for more information.

txt = ("{:<8}\n" # left aligned with a space of 8
    + "{:>8}\n" # right aligned with a space of 8
    + "{:^8}\n" # centered with a space of 8
    + "{:=8}\n" # places sign on the left
    + "{:+8}\n" # uses a +/- sign for positive/negative
    + "{:-8}\n" # uses a - sign for negative only (positive without sign)
    + "{: 8}\n" # uses a space for pos or minus for negative
    + "{:,}\n" # uses a comma for thousand separator
    + "{:_}\n" # uses a underscore for thousand spearator
    + "{:b}\n" # binary format
    + "{:c}\n" # converts value to corresponding unicode character
    + "{:d}\n" # decimal format
    + "{:e}\n" # scientific format, lowercase e
    + "{:E}\n" # scientific format, uppercase E
    + "{:f}\n" # fix/float point number, in lowercase (inf/nan)
    + "{:F}\n" # fix/float point number, but in uppercase (INF/NAN)
    + "{:g}\n" # general format
    + "{:G}\n" # general format, uppercase for scientific notation E
    + "{:o}\n" # octal format
    + "{:x}\n" # hex format, lowercase
    + "{:X}\n" # hex format, uppercase
    + "{:n}\n" # number format
    + "{:%}" # percentage format
    )
print(txt.format(100,200,300,-400,500,600,700,800,900,1000,
                1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,
                2100,2200,2300))


# Escape characters:
# The backslash is used to escape some characters with special functions
# for example an escaped \" is considered as a string character instead of
# part of the code (to close the string).
# \n = new line
# \r = carriage return
# \t = tab
# \b = backspace
# \f = form feed
# \ooo = octal value
# \xhh = hex value

# string operations should have their own chapter, i should have known
# that this gets complicated.
# a number of string operations can be found 
# at https://www.w3schools.com/python/python_strings_methods.asp

