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