rand_list = ["string", 1.234, 3]

# make list using range
range_list = list(range(11))

rand_list = rand_list + range_list
print(rand_list)

multd_list = [[j * i for j in range(1, 10)] for i in range(1, 10)]
for row in multd_list:
    print(row)

# Program to generate unique random list between 1-9
import random
num_list = []
for i in range(5):
    rand_num = random.randrange(1, 9)
    while num_list.count(rand_num) > 0:
        rand_num = random.randrange(1, 9)
    num_list.append(rand_num)

for i in num_list:
    print(i)