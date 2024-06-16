
from enum import Enum
from simple_term_menu import TerminalMenu

from category import Category
from modes.log_activities_and_hours_mode import log_activities_and_hours
from modes.set_categories_and_target_hours_mode import enter_categories_and_target_hours
from modes.show_categories_and_target_hours_mode import show_categories_and_target_hours
from utils import clear_screen


class StartMenuItem(Enum):
    SET_CATEGORIES_AND_TARGET_HOURS = "Set categories and target hours"
    SHOW_CATEGORIES_AND_TARGET_HOURS = "Show categories and target hours"
    LOG_ACTIVITIES_AND_HOURS= "Log activities and hours"
    SHOW_WEEKLY_STRAVA_ACTIVITIES = "Show weekly Strava activities"
    DISPLAY_DOWNLOAD_DATA = "Display and/or download data"
    PERSONALIZED_WEEK_ANALYSIS = "Personalized week analysis"
    EXIT_PROGRAM = "Exit program"

def show_mode_selection_menu():
    while True:
        options = [item.value for item in StartMenuItem]
        terminal_menu = TerminalMenu(
            options,
            title="ℹ️ Use ↓ or ↑ arrow keys to navigate and 'Enter' to select:\n",
            menu_cursor_style=("fg_green", "bold"),
            quit_keys=("escape", "q", "ctrl-g", "ctrl-c", "ctrl-d")
        )
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == None:
            return

        selected_mode = StartMenuItem(options[menu_entry_index])

        clear_screen()
        if selected_mode == StartMenuItem.SET_CATEGORIES_AND_TARGET_HOURS:
            enter_categories_and_target_hours()
        elif selected_mode == StartMenuItem.SHOW_CATEGORIES_AND_TARGET_HOURS:
            validate_categories_count(show_categories_and_target_hours, selected_mode)
        elif selected_mode == StartMenuItem.LOG_ACTIVITIES_AND_HOURS:
            validate_categories_count(log_activities_and_hours, selected_mode)
        elif selected_mode == StartMenuItem.SHOW_WEEKLY_STRAVA_ACTIVITIES:
            print("Validate if categories not null and show weekly strava data")
        elif selected_mode == StartMenuItem.DISPLAY_DOWNLOAD_DATA:
            print("Validate if categories and activities not null and display and/or download data")
        elif selected_mode == StartMenuItem.PERSONALIZED_WEEK_ANALYSIS:
            print("Validate if categories and activities not null and display personalized week analysis")
        elif selected_mode == StartMenuItem.EXIT_PROGRAM:
            print("Exiting program. Goodbye!👋")
            break

def validate_categories_count(
    function_name, selected_mode
):
    categories_count = Category.get_number_of_categories()
    if categories_count == 0:
        print(
            f"\n❗ To select '{selected_mode.value}' mode you need to have at least one category added. Current count of categories is {categories_count}\n"
        )
    else:
        function_name()
