# Python

## Python Keywords

Keyswords are reserved words in python. We can't use a keyword as a variable, function name or any other identifier. Keywords are case sensitive.

```python
# Get all the keywords in python
import keyword

print(keyword.kwlist)
# Output -> ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print("\nTotal number of keywords: ", len(keyword.kwlist))
# Output -> 35
```

## Identifiers

It is the name given to the entities like class, functions, variables, etc. in Python.

Rules for writing Identifiers:-

1. Combination of letters in lowercase or uppercase or digits or an underscore
2. Cannot start with a digit.
3. Keywords cannot be used as an identifier.

```python
variable_1 = 123
variable1 = 12
_variable = 1234
1variable = 1234 #invalid syntax
global = 1 #invalid syntax
```

## Variables

A variable is a location in memory used to store some data (value).

### Variable Assignments
```python
a = 10
b = 5.5
c = "Machine Learning"
```

### Multiple Assignments
```pyhton
a, b, c = 10, 5.5, "Machine Learning"
a = b = c = "ML"
```

### Storage Locations
```python
x = 3
print(id(x))    #print address of varibale x
```

## Data Types

Every value in Python has a data type. Since everything is an object in python, data types are actually classes and variables are instance (object) of these classes.

### Numbers

Integers, floating point numbers and complex numbers falls under numbers category. They are defined as int, float and complex class.

We can use the type() function to know which class a variable or a value belongs to and the instance() function to check if an object belongs to particular class.

```python
a = 5
print(a, " is of type", type(a))    #5 is of type <class 'int'>
```

```python
a = 1 + 2j
print(type(a))    #<class 'complex'>
print(isinstance(a, complex))   #true
```

### Boolean

Boolean represents the truth value true and false

```python
a = True
print(type(a))    #<class 'bool'>
```

### Strings

String is a sequence of Unicode characters. We can use single or double quotes to represent strings. Multiline strings can be denoted using triple quotes, ''' or """.

The first character of the string has the index 0.

```python
a = "We are learning Python"
print(type(a))    #<class 'str'>

s = '''This is multiline
      string'''

print(s[1])   #'h'
print(s[-1])    #'g'

#slicing
print(s[5:])  #'is multiline string'
```

### List

List is an ordered sequence of items. All the item in a list do not need to of the same type.

Lists are mutable, meaning, value of the element of a list can be altered.

```python
a = [10, 20, 30, "World"]
print(a[2])   #30

a[2] = "Hello"
print(a)    #[10, 20, "Hello", "World"]
```

### Tuple

Tuple is an ordered sequence of items same as list. The only difference is that tuples are immutable. Tuples once created cannot be modified.

```python
a = (1, 2, "ML")
print(a[1])   #2

a[1] = "DL"   #TypeError
```

### Set

Set is an unordered collection of unique items. Items in a set are not ordered.

We can perform set operations like union, intersection on two sets. Sets have unique value

```python
a = {10, 20, 30, 5, 23}
print(type(a))    #<class 'set'>

s = {1, 2, 2, 3, 4}
print(S)    #{1, 2, 3, 4}

print(s[1])   #TypeError, as sets are unordered
```

### Dictionary

It is an unordered collection of key-value pairs.

```python
d = {"a": "apple", "b": "bat"}
print(d["a"])   #'apple'
```

### Conversion between Datatypes

Conversion to and from string must contain compatible values.

```python
float(5)    #convert integer to float - 5.0

int(5.1)    #convert float to int - 5

str(20)   #convert integer to string - "20"
```

We can convert one sequence to other
```python
a = [1, 2, 3]
print(type(a)) #<class 'list'>
s = set(a)  #convert list to set
print(type(s)) #<class 'set'>

#convert string to list
list("Hello")     #['H', 'e', 'l', 'l', 'o']
```