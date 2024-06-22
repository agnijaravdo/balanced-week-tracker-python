from simple_term_menu import TerminalMenu
from category import Category
from utils import clear_screen, print_heading


def enter_categories_and_target_hours() -> None:
    print_heading("Set Categories and Target Hours")
    print(
        "⬅️ To go back to the main menu, press Ctrl+C or Ctrl+D. To close the program, press Ctrl+Z.\n"
    )

    while True:
        try:
            category_name = enter_category_name()
            if category_name.lower() == "done":
                clear_screen()
                break
            is_weekly = is_target_weekly()
            if is_weekly == None:
                break
            frequency = "weekly" if is_weekly else "daily"
            target_hours = get_correct_target_hours_input(frequency, category_name)
            category = Category(category_name, target_hours, is_weekly)
            category.write_category_and_target_hours_to_file(category)
        except (KeyboardInterrupt, EOFError):
            clear_screen()
            break


def enter_category_name() -> str:
    while True:
        category_name = input(
            "Enter category like 'Sleep', 'Work', 'Move', etc. name (or 'done' to finish): "
        ).strip()
        if not is_category_name_valid(category_name):
            print(
                "Please enter a valid category name. It cannot be empty, consist only of numbers or be already logged in"
            )
            continue
        return category_name


def is_target_weekly() -> bool:
    options = ["Weekly", "Daily"]
    terminal_menu = TerminalMenu(
        options,
        title="\nℹ️ Select whether category hours goal is weekly or daily: \n",
        menu_cursor_style=("fg_green", "bold"),
        quit_keys=(),
    )
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == None:
        return

    selected_mode = options[menu_entry_index]

    is_weekly = selected_mode.lower() == "weekly"

    return is_weekly


def is_category_name_valid(category_name: str) -> bool:
    existing_categories = Category.get_all_categories()
    existing_category_names = Category.get_category_names(existing_categories)
    if not category_name:
        return False
    elif category_name.isnumeric():
        return False
    if category_name.lower() in (name.lower() for name in existing_category_names):
        return False
    else:
        return True


def get_correct_target_hours_input(frequency: str, category_name: str) -> float:
    while True:
        try:
            target_hours = float(
                input(f"Enter target {frequency} hours for {category_name}: ").strip()
            )
            if frequency == "daily" and target_hours > float(24):
                print("You cannot exceed daily hours maximum 24h. Try again")
                continue
            elif frequency == "weekly" and target_hours > float(168):
                print("You cannot exceed daily hours maximum 168h. Try again")
                continue
            else:
                return target_hours
        except ValueError:
            print("Please enter target hours in numbers format")
            continue
