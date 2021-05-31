# Logical Operators
# and : If both are true it returns true
# or : If either are true it returns true
# not : Converts true into false and vice versa

age = int(input("Enter age: "))

if age < 5:
    print("Stay at Home")
elif age == 5:
    print("Go to Kindergarten")
elif (age > 5) and (age < 18):
    print(f"Go to Grade {age - 5}")
else:
    print("Go to College")