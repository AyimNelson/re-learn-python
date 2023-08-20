age = 6
name = "Jarvis"
print(age)
print(name)

"""
Casting

If you want to specify the data type of a variable, this can be done with casting.

In Python, casting refers to the process of converting a value from one data type to another.

This is sometimes necessary when you want to perform operations that require data of a specific type or when you want to ensure that data is in the correct format for a particular use case

Examples:

int(x): Converts x to an integer.

float(x): Converts x to a floating-point number.

str(x): Converts x to a string.

bool(x): Converts x to a boolean (True or False).

list(iterable): Converts an iterable (e.g., a list, tuple, or string) to a list.

tuple(iterable): Converts an iterable to a tuple.

set(iterable): Converts an iterable to a set, removing duplicate elements.

dict(iterable): Converts an iterable of key-value pairs (e.g., a list of tuples) to a dictionary.

chr(x): Converts an ASCII value x to its corresponding character.

ord(x): Converts a character x to its corresponding ASCII value.

hex(x): Converts an integer x to a hexadecimal string.

oct(x): Converts an integer x to an octal string.

complex(real, imag): Creates a complex number with real and imaginary parts.

"""

# Python is case sensitive
a=5
A=5

# The above are two different assignments...

# Variables naming

"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.


-- Python Keywords --

Python has a set of keywords that are reserved words that cannot be used as variable names, function names, or any other identifiers

"""

# Multi Words Variable Names

"""
Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

-- Camel Case --
Each word, except the first, starts with a capital letter:

myVariableName = "Jarvis"

-- Pascal Case--
Each word starts with a capital letter:

MyVariableName = "Jarvis"

-- Snake Case --
Each word is separated by an underscore character:

my_variable_name = "Jarvis"

"""

# Python Variables - Assign Multiple Values

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Note: Make sure the number of variables matches the number of values, or else you will get an error.


# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "Python is awesome"
print(x)


# Multiple output with a single print
# In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "great"
print(x, y, z)

# concatenation
# String concatenation is the process of combining two or more strings into a single string. In Python, you can concatenate strings using the + operator or by using string formatting techniques.

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

# Adding two different data types will result in an error

# print(6 +"Jarvis")
# The above code will result in a error

# -- Global Variables --


def myfunc():
  print("Python is " + hi)

hi="Awesome"

myfunc()

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# use the global keyword if you want to change a global variable inside a function.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

