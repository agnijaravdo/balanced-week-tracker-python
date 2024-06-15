from simple_term_menu import TerminalMenu
from category import Category
from utils import clear_screen, print_heading


def enter_categories_and_target_hours():
    print_heading("Set Categories and Target Hours")
    while True:
        category_name = input("Enter category like 'Sleep', 'Work', 'Move', etc. name (or 'done' to finish): ").strip()
        if category_name.lower() == 'done':
            clear_screen()
            break
        is_weekly = is_target_weekly()
        frequency = "weekly" if is_weekly else "daily"
        target_hours = float(input(f"Enter target {frequency} hours for {category_name}: ").strip())
        category = Category(category_name, target_hours, is_weekly)
        category.writeCategoryAndTargetHoursToFile(category)
   

    
def is_target_weekly() -> bool:
    options = ["Weekly", "Daily"]
    terminal_menu = TerminalMenu(
            options,
            title="\nℹ️ Select whether category hours goal is weekly or daily: \n",
            menu_cursor_style=("fg_green", "bold"),
            quit_keys=("escape", "q", "ctrl-g", "ctrl-c", "ctrl-d")
        )
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == None:
        return

    selected_mode = (options[menu_entry_index])

    is_weekly = selected_mode.lower() == "weekly"

    return is_weekly
