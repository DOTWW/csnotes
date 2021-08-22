# Everything in Python is an object
# Here's a demonstration of immutable objects:

x = 2
print("The value of x BEFORE x = x + 1 is:", x)
print("The id(x) of x BEFORE x = x + 1 is:", id(x))
x = x + 1
print("The value of x AFTER x = x + 1 is:", x)
print("The id(x) of x AFTER x = x + 1 is:", id(x))

# variable x references to an int object with the value of 2.
# the reference points to an object location. That pointer stores the ID of 2.
# Now, the int object value can not be changed. This is what immutable means.
# When x = x + 1 executes, python creates a new int object with the value of 3.
# x will point to the new int object with the value of 3.
# In this case, the old int object of 2 does not have any pointers associated,
# and will be handled by Python's garbage collector automatically.
"""
Note: some languages do not handle pointers automatically, aka. free memory 
automatically. In C for example, for each pointer location that has memory 
reserved with malloc(size) (short for memory allocate), the memory must be freed 
again with free(pointer), otherwise the memory will stay reserved.
This is called a memory leak, and if called over and over, might reserve the
entire RAM of the system and cause a crash.
"""