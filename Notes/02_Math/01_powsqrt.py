# Powers and Square Roots
import math
import cmath

# Powers: Powers consist of a base and an exponent (sometimes called index).
# The operation for power is:  base**exponent
# Example: 2**8 = 2*2*2*2*2*2*2*2 = 256 (2 to the power of 8)

print(2**8) # Output: 256
print(-2**8) # Output: -256
print((-2)**8) # Output: 256

# As you can see, if you're using negative numbers, be careful when using
# this notation, as it can lead to easy bugs. Python first calculates 2**8,
# then adds the sign to it, unless brackets are used to change the order of
# the operation (as you know, in mathematics, brackets have the priority).

# Square Roots
# Root of X solve the question of "what to the power of what results in X?"
# Square Roots specifically solve the question of B * B = X
# In other words, the answer to the square root of X is B, because
# B to the power of 2, or B squared (B for Base), is X.
# Or generally, the N-root of X is B,
# because B to the power of N, where N is the exponent and B is the Base, is X.

print(math.sqrt(16)) # Output: 4.0

# See what Python did there?
# It's alright if you didn't, it's an easy oversight.
# But the answer you got from the square root function is absolute.
# The answer you got from python is technically |4.0|,
# but Python doesn't tell you that.
# This means that Python only tells you half the answer.
# Keep in mind that even-number roots can have two answers. For example:
# 4 * 4 = 16 but also -4 * -4 = 16
# Whereas uneven-number roots (3-root) only have one answer based on the sign.

print("4 * 4 = ", 4**2) # Output: 16
print("-4 * -4 = ", (-4)**2) # Output: 16

# Also, you might have noted that the output is a floating point value.

# Complex numbers
# In the above example, real numbers were handled. After all,
# when dealing with square roots, there are no negative square roots.
# Negative times Negative is always Positive. You learned that in school.
# BUT WHAT IF THERE WERE?
# Introducing: Imaginary numbers, or complex numbers if you will.
# But we have a problem:

# print(math.sqrt(-16)) # Output: ValueError: math domain error.
# print(math.sqrt(-16j)) # Output: TypeError: can't convert complex to float

# As you can see, Python does not like that either way.
# That's because complex numbers are outside of the scope of basic math
# functions. For complex numbers, a whole own library exists: cmath

print(cmath.sqrt(-16)) # Output: 4j

# Not that also here, the output is absolute.

# Combining square root and power
# If you were wondering how you could use a root that wasn't just the square,
# say, you wanted a cubic root, what would you do then?
# The answer is probably simple to those who remember mathematics from school,
# but could be puzzling for the rest of us.
# Technically, root functions are just exponents that look like 1/n to a base.
# Or X to the power of 1/n.
# So if you wanted the square root of 16, without using the square root
# function in math or cmath, you could just write: 16**(1/2)
# 16 to the power of 1/2.

print(16**(1/2)) # Output: 4.0

# But why is it a float again? Didn't we use all integers?
# Well, thankfully Python automatically converts 1/2 to a float of 0.5
# If we used all integers the exponent would truncate after the comma,
# and the value would be 0. And 16**0 would output 1.
# But don't take my word for it. Here's a demonstration:

y = 2
print(1, ", ", type(1), ", ",
      y, ", ", type(y), ", ",
      1/y, ", ", type(1/y),
      sep="")
      # Output: 1, <class 'int'>, 2 <class 'int'>, 0.5, <class 'float'>

print(int(1/2)) # Output: 0

# However, similar to before, complex numbers behave differently:

x = (-16)**(1/2)
print(x) # Output: 2.4492935982947064e-16+4j

# Let's break this down:

print(x.real) # Output: 2.4492935982947064e-16
print(x.imag) # Output: 4.0

# The imaginary part of the square root of -16
# is 4.0 (reminder: the j only indicates it's imaginary, that's all it does)
# and the real part is... some number.
# But that's weird, why is there a real part at all?
# The answer lies within floating point imprecision.
# If you look at the number, it's extremely small: e-16 stands for "* 10^(-16)"
# which means "something * 0. 0000 0000 0000 0001"
# In our case, the real number is 0. 0000 0000 0000 0002 (rounded)
# rounded to 2 digits after the comma, our result is:

print(round(x.real, 2)) # Output: 0.0 (technically 0.00)

# Which is zero. There is no real part.
# Now we know this (at least in this simple example), but the computer doesn't.

# Floating point imprecision can be the cause to many bugs in programming.
# The only way to correct this would be to round things between calculations,
# But this could in some cases cause other imprecisions:

print("X = (-16)**(1/2) which should be (0+4j)")
print(x, "That's wrong...") # Output: 2.4492935982947064e-16+4j
print("X**2 Should equal -16, it reverses the square root from earlier")
print((x)**2, "Also wrong...") # Output: (-16+1.959434878635765e-15j)

# To round x, because x.real and x.imag are readonly, you have to redefine x
# The important part is to not forget to make sure that the imaginary part
# has to stay imaginary, and not get converted into a real number,
# so multiply the imaginary part by 1 using *1j
x = round(x.real, 2) + round(x.imag, 2)*1j
print(x) # Output: 4j (the fake real part from the float imprecision is gone!)
print("Now we can reverse the square root from earlier:")
print(x**2) # Output: -16

# or rather the output is -16+0j because it's a complex number,
# and it wants you to know, like a submissive furry at a gay pride parade.