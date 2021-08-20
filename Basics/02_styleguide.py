# General Style Guide:
# Based on Python PEP 8 @ https://www.python.org/dev/peps/pep-0008/


# Indentation: 4 spaces per level
"""This is a general recommendation for coding. 4 spaces is popular.
VSCode (and most editors) can insert 4 spaces for you if you press the tab key,
and do that by default anyway."""


# Stay below 80 characters per line.  
# Python recommends using max. 79 characters, or 72 for docstrings.
"""This has more historic value than anything.
In the early days of computing,
punch cards were used to program large mainframes.
Those things had a limit of 80 characters per card.
Likewise, some computer terminals are limited to a width of 80 characters.

While a lot of programmers argue about the 80 character limit,
it would be good to get used to it anyway, simply for consistency's sake.

And while it's true that word wrap exists for most editors these days,
it's always better to manually control the flow of text or code.

Remember: You will always read code more often than you write it.

Bonus fact: Books also generally try to stay below 80 characters per line.
In fact, the ideal character limit per line for books is considered 66.

Bonus Tip: Most code editors let you set rulers (even VIM does that).
In VS Code, go to File -> Preferences -> Settings.
Search for "ruler", you should find it. Set a general ruler for 80:
"editor.rulers": [80]
Set a python specific ruler for 79:
"[python]": {"editor.rulers": [79]}

if you love customizing your editor,
you can change the color of the ruler with:
"workbench.colorCustomizations": {
    "editorRuler.foreground": "#ff4081"
}"""


# How to line breaks within a function:  
# Use parentheses () to write continued code over multiple lines if possible.  
# print(foo
#     .bar())
"""This is pretty self explanatory, but on that note I want to add that,
while backslashes also work to break your code,
you should avoid them as best as you can.

print("Hello, " \
    + "World!")
    
works, (It prints Hello, World!) but

print("Hello, " \ 
    + "World!")
    
does not (It gives you an error).

The difference is a single space after the backslash.
Easy bug/oversight that can cost you hours. But also avoidable."""


# Line breaks and operators:  
# If you have to break, use line breaks before operators:  
# sum = (a  
#       + b  
#       + c  
#       - d  
#       + e)
"""This is also pretty self explanatory. For a long time,
it was the convention to break after operators, so it would be

sum = (a +
       b +
       c -
       d +
       e)

but because that's not as easy to read,
it's now generally recommended to break before operators.
I'm sure you can see the difference right away."""


# Blank lines / Whitespace and Imports:  
# two blank lines for top level functions and class definitions  
# single blank lines between methods inside classes  
# use blank lines sparingly in your code to group logical sections  
# imports/includes: blank lines between groups.  
# group by: 1. standard libraries, 2. related third party, 3. local specific
"""
#This code highlights blank space usage:
#Standard system imports
import wolf
import dog

#Related third party imports
import fox
import more_dog
from pandas import RedPanda

#Local application/library specific imports
from my_local_function import Foo0, Bar1


def top_level_function1():
    pass


class TestClass(object):
    
    def class_method1():
        pass

    def class_method2():
        pass


"""


# Module Level Dunders (names with double underscores around them)  
# like __all__, __author__, __version__  
# should be placed after module docstrings but before imports
"""
The exception to this is the from __future__ import.
[method docstring]

from __future__ import this_thing

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Some smelly dog'

import wolf
import dog
"""


# Whitespace General Good Practice:  
# Avoid excessive whitespace before commas. DO: x, y NOT: x , y  
# Also avoid this in brackets. DO: (x[1], x[2],) NOT: ( x[ 1 ], x[ 2 ], )  
# Keep brackets connected to functions. DO: print() NOT: print ()  
# Avoid trailing whitespaces as best as possible.  
# You can use whitespace to help with math:  
# (x*y + z) is easier to read than (x * y + z)  
# single spaces around binary operators like =, <, >, !+, +=, and, or,...  
# do not use spaces when defining unannounced function parameters:  
# DO: def sum(input: a = 0, b=0) NOT: def sum(input: a = 0 b = 0)


# Redundant Parentheses and trailing commas:  
# You have a lot of space, so it's best to use redundant parentheses  
# and redundant trailing commas.  
# It's also good convention to put items in their own lines.
"""
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )

You can also use trailing commas to create tuples like FILES = ('setup.cfg',)

Bonus Tip:
If you're programming in another language than python, like C++,
while people have different coding styles, do yourself a favor,
and give every {} their own line, and put them on the same indentation.
Even without knowing C you should be able to tell which of the two following
is more readable:

DO:
#include <stdio.h>

int main(void)
{
    for(int i = 10; i > 0; i--)
    {
        if(i < 4)
        {
            printf("3\n");
        }
        else
        {
            printf("%d\n", i);
        }
    }
    printf("Liftoff!\n");
    return 0;
}

NOT:
#include <stdio.h>

int main(void) {
    for(int i = 10; i > 0; i--) {
        if(i < 4) printf("3\n");
        else printf("%d\n", i);
    }
    printf("Liftoff!\n");
    return 0;
}

"""


# Comments  
# Yes.  
# Swear a lot, this is your outlet to scream at the computer, 
# without the computer screaming back at you.  
# Seriously though: 
# Use complete sentences, and be clear with yourself.
# Remember, you're talking to someone who has no idea what the code does.
# That someone might be your future you.
# 
# PEP8 says to use Inline comments sparingly,
# and when you use them, do not to repeat the code:
# DO: x = x + 1 # Compensate for starting from 0
# NOT: x = x + 1 # Increment x
# 
# PEP8 recommends using two spaces after each sentence in a comment.  
# I guess this is for readability.  Apparently this is easier to read than:
# I guess this is for readability. Apparently this. That being said,
# not even all standard libraries seem to follow this guideline, so, really,
# just do whatever you want.
"""My first thought when reading about the double spacing within comments 
was that maybe it would be used to indicate new lines for markdown. 
But after every sentence? Seems to be some readability thing.
I prefer single spaces, and I think I'll stick to that."""


# Docstrings:
# For consistency, always use triple double quotes aka """this"""
# Also don't use blank lines before or after docstrings.
#
# For One-Liner Docstrings, keep the opening and closing tags in one line.
# def foo_this():
#     """Return a foobar"""
#     return foobar
#
# For multi-line docstrings:
# def foo_this(bizbang=0):
#     """Return a foobang
#     
#     Keyword arguments:
#     bizbang -- the thing that does bazoing (default 0)
#     """
#     return foobar + bizbang


# Naming Convention:

# packages/modules: snake_case
"""Preferrably short and all lowercase names"""
# classes/exceptions: CamelCase
"""For errors, use suffix Error, if it's an error."""
# functions/methods: snake_case()
"""Make class methods non-public unless needed"""
# function/method arguments: snake_case
"""If a name clashes with a reserved keyword, use a trailing underscore like
class (reserved keyword) -> class_ (good) instead of an abbreviation like
clss (not so good). Try to avoid clashes in the first place if possible.
"""
# constants: CAP_SNAKE_CASE
# variables: snake_case
# type variables: CamelCase

# If used internally, add a underscore before the name
# Avoid using I (capital i), l (lowercase L), or O (capital o)
# as single character variables if possible