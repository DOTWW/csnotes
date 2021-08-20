# Numeric types: int, float, complex

# int = any whole number
# 8957293
# -3298572
# 12
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

# float = any number with a decimal point
# 32905.2
# -23.0
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

# string = everything that's between single or double quotes
# 'awoo'
# "AWOOOO!"

# bool = true (1) or false (0)
# true
# 0