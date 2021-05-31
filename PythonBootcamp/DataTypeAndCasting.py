import sys

print(sys.maxsize)
print(sys.float_info.max)

# Python is Dynamically Typed
my_age = 28
my_age = "Twenty Eight"
print(my_age)

# Casting

print("Cast", type(int(2.5)))  # float to int
print("Cast", type(str(2.5)))  # float to str
print("Cast", type(chr(97)))  # int to unicode character
print("Cast", type(ord('a')))  # str to unicode code
print("Cast", type(float(2)))  # int to float
