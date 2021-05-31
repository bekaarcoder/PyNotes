# [condition_true] if [condition] else [condition_false]

age = int(input("Enter you age: "))
can_vote = True if age >= 18 else False
if can_vote:
    print("Great! You can vote.")
else:
    print("Sorry! You can't vote.")

