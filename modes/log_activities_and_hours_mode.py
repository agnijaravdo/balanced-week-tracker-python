import datetime
from simple_term_menu import TerminalMenu
from activity import Activity
from category import Category
from utils import clear_screen, print_heading


def log_activities_and_hours():
    print_heading("Log Activities And Hours Spent on Them")
    print(
        "⬅️ To go back to the main menu or finish entering activities - press Ctrl+C or Ctrl+D. To close the program, press Ctrl+Z.\n"
    )

    try:
        logged_date = enter_activity_date()
    except (KeyboardInterrupt, EOFError):
        clear_screen()
        return

    while True:
        try:
            activity_category = select_activity_category()
            if activity_category == None:
                break
            hours_spent_on_activity = enter_hours_spent_on_activity(logged_date)
            categories = Category.get_all_categories()
            Activity.update_or_create_log_entry(
                categories, logged_date, activity_category, hours_spent_on_activity
            )
            while True:
                enter_for_the_same_date = input(
                    f"Do you want to input next activities for the same date {logged_date}? y/n: "
                ).lower()
                if enter_for_the_same_date == "y":
                    break
                elif enter_for_the_same_date == "n":
                    logged_date = enter_activity_date()
                    break
                elif not enter_for_the_same_date in ["y", "n"]:
                    print("Invalid input. Please enter 'y' or 'n'.")
                    continue

        except (KeyboardInterrupt, EOFError):
            clear_screen()
            break


def enter_activity_date():
    while True:
        try:
            date = input("Enter a date to log your activity (YYYY-MM-DD format).: ")
            year, month, day = map(int, date.split("-"))

            return datetime.date(year, month, day)

        except ValueError as e:
            print(
                f"{str(e).capitalize()}. You can only enter date in YYYY-MM-DD format. Please try again"
            )


def select_activity_category():
    categories = Category.get_all_categories()
    categories_names = Category.get_category_names(categories)
    terminal_menu = TerminalMenu(
        categories_names,
        title="\nℹ️ Select a category for your activity among the current ones: \n",
        menu_cursor_style=("fg_green", "bold"),
        quit_keys=(),
    )
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == None:
        return

    selected_mode = categories_names[menu_entry_index]

    return selected_mode


def enter_hours_spent_on_activity(date):
    while True:
        try:
            logged_daily_hours = float(
                input(
                    f"Enter how many hours you spent on this activity on {date}: "
                ).strip()
            )
            if logged_daily_hours > float(24):
                print("You cannot exceet daily hours maximum 24h. Try again")
                continue
            else:
                return logged_daily_hours

        except ValueError as e:
            print(f"{str(e).capitalize()}. You can only enter numeric type of hours")
