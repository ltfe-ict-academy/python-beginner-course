"""Budget tracking app."""

print("Welcome to budget tracking app!")
print("Enter your 3 expenses!")

total_budget = float(input("Enter your total budget for today (€): "))

expense_name_01 = input("Enter first expense name: ")
expense_category_01 = input("-> Category: ")
expense_price_01 = float(input("-> Price: "))
print("\n ############# \n")

expense_name_02 = input("Enter second expense name: ")
expense_category_02 = input("-> Category: ")
expense_price_02 = float(input("-> Price: "))
print("\n ############# \n")

expense_name_03 = input("Enter third expense name: ")
expense_category_03 = input("-> Category: ")
expense_price_03 = float(input("-> Price: "))
print("\n ############# \n")

total_expenses = expense_price_01 + expense_price_02 + expense_price_03
print(f"Total expenses: {round(total_expenses, 2)}€")
print(f"Budget exceeded? {total_expenses > total_budget}")
