from ordering_system import menu_generator
from ordering_system.utils.table import Table
from ordering_system.utils.waiter import Waiter


def main() -> None:
    """Run ordering system."""
    # 1.step: Generate a new menu
    summer_menu = menu_generator.generate_summer_menu()
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


if __name__ == "__main__":
    main()
