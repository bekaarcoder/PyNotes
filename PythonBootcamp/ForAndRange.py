# 1. Have the user enter their investment amount and expected interest
investment, interest = input("Enter you investment amount and expected interest: ").split()
investment = float(investment)
interest = float(interest)/100

# 2. Each year their investment will increase by their investment + their investment * interest rate
total = investment
for i in range(1, 11):
    total = total + (investment * interest)
    print(f"Amount after {i} year: {total}")

# 3. Print out their earnings after a 10 year period
print(f"You total earning after 10 yrs is {total - investment}")
print(f"You total amount of money after 10 years is {total}")