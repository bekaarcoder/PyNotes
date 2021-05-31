# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# == : Equal to
# != : Not equal to

# Calculator
calculation = input("Enter Calculation (ex: 5 + 4): ")
user_input = calculation.split()
num_1 = int(user_input[0])
num_2 = int(user_input[2])
operator = user_input[1]

result = 0

if operator == '+':
    result = num_1 + num_2
elif operator == '-':
    result = num_1 - num_2
elif operator == '*':
    result = num_1 * num_2
elif operator == '/':
    result = num_1 / num_2
else:
    print("Use valid operators: +,-,*,/")
    quit()

print(f"{calculation} = {result}")