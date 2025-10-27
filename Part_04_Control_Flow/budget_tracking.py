"""Budget tracking app."""

print("Welcome to budget tracking app!")
print("Enter your expenses!")

total_expenses = 0
total_budget = float(input("Enter your total budget for today (€): "))

while True:
    expense_name = input("Enter first expense name: ")
    expense_category = input("-> Category: ")
    expense_price = float(input("-> Price: "))
    total_expenses += expense_price
    print("\n ############# \n")
    if input("Enter another one? [y]").lower() != "y":
        break

print(f"Total expenses: {round(total_expenses, 2)}€")
print(f"Budget exceeded? {total_expenses > total_budget}")
