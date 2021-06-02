import random
num_list = []
for i in range(5):
    rand_num = random.randrange(1, 9)
    while num_list.count(rand_num) > 0:
        rand_num = random.randrange(1, 9)
    num_list.append(rand_num)

for num in num_list:
    print(num, end="")
print()

i = len(num_list) - 1
while i > 1:
    j = 0
    while j < i:
        print(f"\nIs {num_list[j]} > {num_list[j+1]}")
        print()
        if num_list[j] > num_list[j+1]:
            print("Swap")
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp
        else:
            print("Don't swap")
        j += 1
        for k in num_list:
            print(k, end="")
        print()
    print("End of round")
    i -= 1

    for k in num_list:
        print(k, end="")
    print()
