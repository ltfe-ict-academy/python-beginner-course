"""Budget tracking app."""

print("Welcome to budget tracking app!")
print("Enter your expenses!")

categories = ("home", "car", "food", "services")
all_expenses = []
total_budget = float(input("Enter your total budget for today (€): "))

while True:
    expense_name = input("Enter first expense name: ")
    expense_category = input("-> Category: ")
    if expense_category not in categories:
        print(f"Please enter a valid category: {categories}")
        continue
    expense_price = float(input("-> Price: "))
    all_expenses.append(expense_price)
    print("\n ############# \n")
    if input("Enter another one? [y]").lower() != "y":
        break

print(f"All expenses: {all_expenses}")
total_expenses = sum(all_expenses)
print(f"Total expenses: {round(total_expenses, 2)}€")
print(f"Budget exceeded? {total_expenses > total_budget}")
