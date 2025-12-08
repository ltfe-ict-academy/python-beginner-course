from .menu import MenuItem
from .order import Order
from .waiter import Waiter


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
