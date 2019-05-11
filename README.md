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

## Python Input and Output

### Output Formatting

```python
a = 10; b = 20
print("The value of a is {} and b is {}".format(a, b))
# 'The value of a is 10 and b is 20'
```

```python
a = 10; b = 20
print("The value of b is {1} and a is {0}".format(a, b))
# 'The value of b is 20 and a is 10'
```

```python
print("Hello {name}, {greeting}!",format(name="Shashank", greeting="Whats Up"));
# 'Hell0 Shashank, Whats Up!'
```

```python
print("Hello {0}, {1}!",format(name="Shashank", greeting="Whats Up"));
# 'Hell0 Shashank, Whats Up!'
```

### Python Input

```python
num = input("Enter a number: ") #gives a textbox
print(num)
```

## Operators

Operators are special symbols in python that can carry out arithmetic and logical computation. The value that the operator operates on is called the operand.

### Operator Types

1. **Arithmetic**
    ```python
    #addition (+)
    #subtraction (-)
    #multiplication (*)
    #division (/)
    #modulo division (%)
    #Floor Division (//)
    #Exponent (**)
    ```
2. **Comparison**
    > <, >, ==, !=, >=, <=
3. **Logical (Boolean)**
    > and, or and not
4. **Bitwise**
    > &, |, ~, ^, >>, <<
5. **Assignment**
    ```python
    #Add AND (+=)
    #subtract AND (-=)
    #Multiply AND (*=)
    #Divide AND (/=)
    #Modulus AND (%=)
    #Floor division AND (//=)
    #Exponent AND (*=)
    ```
6. **Special**
    - **Identity Operator** - **is and is not** are identity operators. They are used to check if two values are located on the same part of the memory.
        ```python
        a = 5; b = 5
        print(a is b) #true

        L1 = [1, 2, 3]
        L2 = [1, 2, 3]
        print(L1 is L2) #false

        s1 = "ABCD"
        s2 = "ABCD"
        print(s1 is not s2) #false
        ```
    - **Membership Operators** - **in and in not** are membership operators. They are used to test weather a value or variable is found in a sequence (string, list, tuple, set or dictionary).
        ```python
        l = [1, 2, 3, 4]
        print(1 in l) #true

        d = {1: "a", 2: "b"}
        print(2 in d) #true
        ```

## Control Flow

### if Statement

```python
num = 10
if num > 0:
  print("Number is positive")
print("Number is Negative")

#'Number is positive'
```

### if...else Statement

```python
num = 10
if num > 0:
  print("Number is positive")
else:
  print("Number is Negative")

#'Number is positive'
```

### if...elif...else Statement

```python
num = 10
if num > 0:
  print("Number is positive")
elif num == 0:
  print("ZERO")
else:
  print("Number is Negative")

#'Number is positive'
```

### while Loop

The while loop is used to iterate over a block of code as long as the condition is true.

```python
lst = [10, 20, 30, 40, 50, 60]
product = 1
index = 0
while index < len(lst):
    product = product * lst[index]
    index = index + 1
print("The product of list is {}".format(product))

#'The product of list is 720000000'
```

### while loop with else

```python
numbers = [1, 2, 3]

index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1
else:
    print("No numbers left in the list.")

# 1
# 2
# 3
# No numbers left in the list.
```

```python
# Program to find a prime number

num = int(input("Enter a number: "))
print(num)

isDivisible = False

i = 2;
while i < num:
    if(num % i == 0):
        isDivisible = True
        print("{} is divisible by {}".format(num, i))
    i += 1;
        
if isDivisible:
    print("{} is not a Prime number".format(num))
else:
    print("{} is a Prime number".format(num))
```

### for Loop

```python
itm = [10, 12, 13, 14, 15]

product = 1
for el in itm:
    product *= el
    
print("The product of all the items in the list is {}".format(product))

# The product of all the items in the list is 327600
```

> **range() function** - We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).

```python
for i in range(10):
  print(i)

# print range of numbers from 1 to 20 with step size of 2
for i in range(1, 20 , 2):
    print(i)
```

```python
# Program to find the prime numbers within an interval

index1 = 1
index2 = 10

print("Prime numbers between {} and {} are:".format(index1, index2))

for num in range(index1, index2+1):
    if num > 1:
        isDivisible = False
        for i in range(2, num):
            if(num % i == 0):
                isDivisible = True
        if not isDivisible:
            print(num)
```

### break Statement

```python
lst1 = [2, 3, 4, 6, 7]

for el in lst1:
    if(el % 2 != 0):
        break
    print(el)
else:
    print("inside the for loop")
print("outside the for loop")

# 2
# outside the for loop
```

### continue statement

```python
lst1 = [2, 4, 6, 7, 8]

for el in lst1:
    if(el % 2 != 0):
        continue
    print(el)
else:
    print("inside the for loop")
print("outside the for loop")

# 2
# 4
# 6
# 8
# inside the for loop
# outside the for loop
```

## List

List is one of the sequence data-structure. List are the collection of items (Strings, integers or even other lists). List are enclosed in []. Each item in the list have assigned index. 

>Lists are mutable, which means they can be changed.

### List Creation
```python
emptyList = []
lst = ['one', 'two', 'three'] # list of strings
lst2 = [1, 2, 3, 4] # list of integers
lst3 = [[1, 2], [3, 4]] #list of lists
lst4 = [1, 'two', 3.45 ] #list of different data types 
```

### List Length
```python
len(lst)
```

### List Append
```python
lst.append('four')
# will add 'four' at the end of the list
```

### List Insert
```python
lst.insert(2, "three")
# will add 'three' at index 2
```

### List Remove
```python
lst.remove('three')
# will remove the first occurance of 'three' from the list
```

### List Append & Extend
```python
lst = [1, 2, 3, 4]
lst2 = [5, 6]

lst.append(lst2) # [1, 2, 3, 4, [5, 6]]

lst.extend(lst2) # [1, 2, 3, 4, 5, 6]
# extend will join the lst2 with lst
```

### List Delete
```python
del lst[1] # removes the element at index 1

# or we can use pop() method
a = pop(1)
```

### List related keywords in Python
```python
# keyword 'in' is used to test if an element is in a list
lst = [1, 2, 3, 4]
if 2 in lst:
    print("True")

#keyword 'not' can be combined with 'in;
if 4 not in lst:
    print("False")
```

### List Reverse
```python
lst.reverse()
```

### List Sorting

The easiest way to sort a List is to use sorted(list) function. That takes a list and returns a new list in sorted order. The original list is not changed.
>The sorted() optional argument, reverse=True, nakes it sort backwards

```python
numbers = [3, 2, 5, 4, 1]

sorted_lst = sorted(numbers)
print(sorted_lst) # 1, 2, 3, 4, 5

reverse_lst = sorted(numbers, reverse=True)
print(reverse_lst) # 5, 4, 3, 2, 1
```

