# Program to solve an algebric equation


def solve_equation(equation):
    variables = equation.split(' ')
    operator = variables[1]

    if operator == '+':
        return int(variables[4]) - int(variables[2])
    elif operator == '-':
        return int(variables[4]) + int(variables[2])
    elif operator == '*':
        return int(variables[4]) / int(variables[2])
    elif operator == '/':
        return int(variables[4]) * int(variables[2])


equation = input("Enter an equation to solve: (Ex:- x + 5 = 9) ")
print("x = ", solve_equation(equation))
