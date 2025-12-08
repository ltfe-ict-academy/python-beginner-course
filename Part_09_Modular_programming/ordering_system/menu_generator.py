from .utils.menu import Menu, MenuItem


def generate_summer_menu() -> Menu:
    """Generate summer menu."""
    summer_menu = Menu(menu_name="Summer Menu")
    summer_menu.add_item(MenuItem("Goveja Juha", 4.5, "juha"))
    summer_menu.add_item(MenuItem("Gobova Juha", 4.7, "juha"))
    summer_menu.add_item(MenuItem("Mesna Lazanija", 11.7, "glavna"))
    summer_menu.add_item(MenuItem("Pizza", 10.8, "glavna"))
    summer_menu.add_item(MenuItem("Zelenjavna rizota", 13.4, "glavna"))
    return summer_menu
