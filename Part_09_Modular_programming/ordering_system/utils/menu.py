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
