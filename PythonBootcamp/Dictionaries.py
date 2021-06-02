dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
new_dic = {k: v * v for k, v in dic.items() if v > 2}
for k, v in new_dic.items():
    print(k, v)

customers = []
while True:
    res = input("Enter Customer (Y/N): ")
    res = res.upper()
    if res == "N":
        break
    else:
        f_name, l_name = input("Enter Customer Name: ").split()
        customers.append({"f_name": f_name, "l_name": l_name})

for customer in customers:
    print(customer['f_name'], customer['l_name'])
