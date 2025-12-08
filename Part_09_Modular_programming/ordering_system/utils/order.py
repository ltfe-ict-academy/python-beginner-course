from .menu import MenuItem
from .waiter import Waiter


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
