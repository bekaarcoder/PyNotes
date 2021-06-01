# [condition_true] if [condition] else [condition_false]

# Example 1
age = int(input("Enter you age: "))
can_vote = True if age >= 18 else False
if can_vote:
    print("Great! You can vote.")
else:
    print("Sorry! You can't vote.")

# Example 2
a, b = 10, 20
print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")
