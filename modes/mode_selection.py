
from enum import Enum
from simple_term_menu import TerminalMenu

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
        # categories_count = get_number_of_categories()
        # activities_count = get_number_of_activities()

        clear_screen()
        if selected_mode == StartMenuItem.SET_CATEGORIES_AND_TARGET_HOURS:
            print("Set target")
        elif selected_mode == StartMenuItem.SHOW_CATEGORIES_AND_TARGET_HOURS:
            print("Validate if categories not null and show categories and times data")
        elif selected_mode == StartMenuItem.LOG_ACTIVITIES_AND_HOURS:
            print("Validate if categories not null and log activities and hours")
        elif selected_mode == StartMenuItem.SHOW_WEEKLY_STRAVA_ACTIVITIES:
            print("Validate if categories not null and show weekly strava data")
        elif selected_mode == StartMenuItem.DISPLAY_DOWNLOAD_DATA:
            print("Validate if categories and activities not null and display and/or download data")
        elif selected_mode == StartMenuItem.PERSONALIZED_WEEK_ANALYSIS:
            print("Validate if categories and activities not null and display personalized week analysis")
        elif selected_mode == StartMenuItem.EXIT_PROGRAM:
            print("Exiting program. Goodbye!👋")
            break
