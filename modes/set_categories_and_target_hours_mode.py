from simple_term_menu import TerminalMenu
from category import Category
from utils import clear_screen, print_heading


def enter_categories_and_target_hours():
    print_heading("Set Categories and Target Hours")
    while True:
        category_name = input("Enter category like 'Sleep', 'Work', 'Move', etc. name (or 'done' to finish): ").strip()
        if not is_category_name_valid(category_name):
            print("Please enter a valid category name. It cannot be empty, consist only of numbers or be already logged in")
            continue
        if category_name.lower() == 'done':
            clear_screen()
            break
        is_weekly = is_target_weekly()
        frequency = "weekly" if is_weekly else "daily"
        target_hours = get_correct_target_hours_input(frequency, category_name)
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

def is_category_name_valid(category_name):
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
    
def get_correct_target_hours_input(frequency, category_name):
    while True:
        try:
            target_hours = float(input(f"Enter target {frequency} hours for {category_name}: ").strip())
            if frequency == "daily" and target_hours > float(24):
                print("You cannot exceet daily hours maximum 24h. Try again")
                continue
            elif frequency == "weekly" and target_hours > float(168):
                print("You cannot exceet daily hours maximum 168h. Try again")
                continue
            else:
                return target_hours
        except ValueError:
            print("Please enter target hours in numbers format")
            continue
