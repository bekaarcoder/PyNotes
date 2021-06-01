import random

rand_num = random.randrange(1, 51)
i = 1
while i != rand_num:
    i += 1
print(f"The random value is {rand_num}")
print(f"Loop iterated {i} times")

# Program to print a tree based on a given height

tree_height = input("How tall is your tree? ")
tree_height = int(tree_height)
spaces = tree_height - 1
hashes = 1
stump_spaces = tree_height - 1

while tree_height != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print("#", end="")
    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1
for i in range(stump_spaces):
    print(" ", end="")
print("#")

# Guessing Game

secret_num = 7
while True:
    try:
        guess = int(input("Guess the number: "))
        if guess == secret_num:
            print("You guessed it!")
            break
    except ValueError:
        print("Please enter a number.")
