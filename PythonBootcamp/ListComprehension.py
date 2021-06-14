# cities = ["London", "NY", "Paris"]


# def visit(city):
#     print(f"Welcome to {city}")


# [visit(x) for x in cities]

output_using_for = []

for x in range(1, 11):
    output_using_for.append(x ** 2)

print(f"Squares using for loop: {output_using_for}")

output_using_list_comp = [x ** 2 for x in range(1, 11)]

print(f"Squares using list comprehension: {output_using_list_comp}")