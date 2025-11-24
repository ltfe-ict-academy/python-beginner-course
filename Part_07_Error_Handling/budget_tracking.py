"""Budget tracking app."""

categories = ("home", "car", "food", "services")
all_expenses = []


def get_expense_name() -> str:
    """Get expense name from user."""
    while True:
        expense_name = input("-->> Expense name: ")
        if not expense_name or len(expense_name) < 3:  # noqa: PLR2004
            print("Expense name should be at least 3 characters long!")
            continue
        return expense_name


def get_expense_category() -> str:
    """Get expense category from user."""
    while True:
        expense_category = input(f"-->> Expense category [{', '.join(categories)}]: ")
        if expense_category not in categories:
            print(f"Please enter a valid category: {categories}")
            continue
        return expense_category


def get_expense_price() -> float:
    """Get expense price from user."""
    while True:
        try:
            expense_price = float(input("-->> Expense price: "))
            if expense_price <= 0:
                print("Price should be bigger than 0€!")
                continue
        except ValueError:
            print("Price should be a valid number! Please enter the value again!")
        else:
            return round(expense_price, 2)


def get_new_expense_from_user() -> dict:
    """Get new expense from the user input."""
    expense_name = get_expense_name()
    expense_category = get_expense_category()
    expense_price = get_expense_price()
    return {"name": expense_name, "category": expense_category, "price": expense_price}


def print_all_expenses(expenses: list[dict]) -> None:
    """Print all expenses."""
    print("\n---------------------- All expenses ----------------------")
    for expense in expenses:
        print(f"{expense['name']:^25} | {expense['category']:^15} | {expense['price']:>10.2f}€")
    print("----------------------------------------------------------")


def summarize_expenses(expenses: list[dict]) -> None:
    """Summarize expenses by category."""
    prices = [expense["price"] for expense in expenses]
    total_expenses = sum(prices)
    print(f"\nTotal expenses: {round(total_expenses, 2)}€")


def main() -> None:
    """Run budget tracking app."""
    print("Welcome to budget tracking app!")
    try:
        while True:
            new_expense = get_new_expense_from_user()
            all_expenses.append(new_expense)
            print_all_expenses(all_expenses)
            if input("Enter another one? [y]").lower() != "y":
                break
    except KeyboardInterrupt:
        pass
    finally:
        summarize_expenses(all_expenses)


main()
