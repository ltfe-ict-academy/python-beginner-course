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
        # TODO: implement

    def show_full_menu(self) -> None:
        """Print the menu to the screen."""
        # TODO: implement


def main() -> None:
    """Run ordering system."""
    goveja_juha = MenuItem("Goveja Juha", 4.5, "juha")
    gobova_juha = MenuItem("Gobova Juha", 4.7, "juha")
    mesna_lazanija = MenuItem("Mesna Lazanija", 11.7, "glavna")
    pizza = MenuItem("Pizza", 10.8, "glavna")
    zelenjavna_rizota = MenuItem("Zelenjavna rizota", 13.4, "glavna")
    # TODO: initilize Menu and add items
    # TODO: Show full menu
