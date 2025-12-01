# MENU ITEM (name, price, category)
# MENU (items-> list[MENU ITEM]), add_item, find_item, show_all
# WAITER (name, waiter_id)
# TABLE (number, seats, waiter, order), assign_waiter, open_order, close_order
# ORDER ITEM (menu_item_id, quantity), subtotal
# ORDER (table_number, waiter, items, is_closed), add_item, total, close


class MenuItem:
    """Single item on the menu."""

    def __init__(self, name: str, price: float, category: str) -> None:
        """Initialize the MenuItem."""
        self.name = name
        self.price = price
        self.category = category

    def __str__(self) -> str:
        """Create string representation of the object."""
        return f"{self.name} ({self.category}) => {self.price:.2f}€"


class Menu:
    """Collection of MenuItem."""

    def __init__(self, menu_name: str) -> None:
        """Initialize the Menu."""
        self.menu_name = menu_name
        self.items: list[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        """Add a new MenuItem to the Menu."""
        self.items.append(item)

    def find_item(self, name: str) -> MenuItem | None:
        """Search for the menu item by name."""
        name = name.lower()
        for item in self.items:
            if item.name.lower() == name:
                return item
        return None

    def show_full_menu(self) -> None:
        """Print the menu to the screen."""
        print(f"===== MENU ({self.menu_name}) =====")
        for item in self.items:
            print(item)
        print("================================")


class Waiter:
    """Waiter is serving tables."""

    def __init__(self, waiter_id: int, name: str) -> None:
        """Initialize the Waiter."""
        self.waiter_id = waiter_id
        self.name = name

    def __str__(self) -> str:
        """Create string representation of the object."""
        return f"Waiter {self.name} (id={self.waiter_id})"


class OrderItem:
    """Number of ordered menu items."""

    def __init__(self, menu_item: MenuItem, quantity: int) -> None:
        """Initialize the OrderItem."""
        self.menu_item = menu_item
        self.quantity = quantity

    def __str__(self) -> str:
        """Create string representation of the object."""
        return f"{self.quantity} x {self.menu_item.name} = {self.compute_subtotal():.2f}€"

    def compute_subtotal(self) -> float:
        """Compute item value."""
        return self.quantity * self.menu_item.price


class Order:
    """An order for a specific table, taken by a waiter."""

    def __init__(self, table_number: int, waiter: Waiter) -> None:
        """Initialize the Order."""
        self.table_number = table_number
        self.waiter = waiter
        self.items: list[OrderItem] = []
        self.is_closed: bool = False

    def add_item(self, menu_item: MenuItem, quantity: int = 1) -> None:
        """Add a new MenuItem to the Order."""
        if self.is_closed:
            raise ValueError("Cannot add items to a closed order.")

        # Check if the item is already in the items list
        for item in self.items:
            if item.menu_item.name == menu_item.name:
                item.quantity += quantity
                return

        self.items.append(OrderItem(menu_item, quantity))

    def close_order(self) -> None:
        """Close the order."""
        self.is_closed = True

    def compute_total(self) -> float:
        """Compute the total order value."""
        return sum([item.compute_subtotal() for item in self.items])

    def create_receipt(self) -> None:
        """Create a receipt for the current order."""
        print(f"\n======= RECEIPT - TABLE {self.table_number} =======")
        print(f"Served by: {self.waiter.name}")
        print("--------------")
        for item in self.items:
            print(f"--> {item}")
        print(f"\nTotal: {self.compute_total():.2f}€")
        print("===================================\n")


class Table:
    """Table can have one active order."""

    def __init__(self, table_number: int, seats: int) -> None:
        """Initialize the Table."""
        self.table_number: int = table_number
        self.seats: int = seats
        self.waiter: Waiter | None = None
        self.current_order: Order | None = None

    def assign_waiter(self, waiter: Waiter) -> None:
        """Assign waiter to the table."""
        self.waiter = waiter

    def add_order(self, menu_item: MenuItem | None, quantity: int = 1) -> None:
        """Add order for the table."""
        if self.waiter is None:
            raise ValueError("Cannot add order if no waiter is selected.")

        if menu_item is None:
            print("Menu item is None, skipping adding to order")
            return

        # When adding an element for the first time
        if self.current_order is None:
            self.current_order = Order(self.table_number, self.waiter)

        self.current_order.add_item(menu_item, quantity)

    def finalize_table(self) -> None:
        """Create payment and close the order."""
        if self.current_order is None:
            raise ValueError("No order to close.")
        self.current_order.create_receipt()
        self.current_order.close_order()


def generate_summer_menu() -> Menu:
    """Generate summer menu."""
    summer_menu = Menu(menu_name="Summer Menu")
    summer_menu.add_item(MenuItem("Goveja Juha", 4.5, "juha"))
    summer_menu.add_item(MenuItem("Gobova Juha", 4.7, "juha"))
    summer_menu.add_item(MenuItem("Mesna Lazanija", 11.7, "glavna"))
    summer_menu.add_item(MenuItem("Pizza", 10.8, "glavna"))
    summer_menu.add_item(MenuItem("Zelenjavna rizota", 13.4, "glavna"))
    return summer_menu


def main() -> None:
    """Run ordering system."""
    # 1.step: Generate a new menu
    summer_menu = generate_summer_menu()
    summer_menu.show_full_menu()
    # 2.step: Generate active waiters
    waiter_john = Waiter(waiter_id=1, name="John")
    waiter_ben = Waiter(waiter_id=2, name="Ben")
    print(waiter_john)
    print(waiter_ben)
    # 3.step: Generate Tables and assign the waiters
    table_01 = Table(table_number=1, seats=5)
    table_02 = Table(table_number=2, seats=2)
    table_03 = Table(table_number=3, seats=8)
    table_04 = Table(table_number=4, seats=4)
    table_05 = Table(table_number=5, seats=4)
    table_01.assign_waiter(waiter_john)
    table_02.assign_waiter(waiter_john)
    table_03.assign_waiter(waiter_john)
    table_04.assign_waiter(waiter_ben)
    table_05.assign_waiter(waiter_ben)
    # 4.step: Open orders for occupied tables
    table_01.add_order(summer_menu.find_item("Goveja Juha"), 6)
    table_01.add_order(summer_menu.find_item("Zelenjavna rizota"), 3)
    table_01.add_order(summer_menu.find_item("Zelenjavna rizota"), 3)
    table_01.add_order(summer_menu.find_item("Zelenjavna rizota11"), 3)
    table_01.finalize_table()


main()
