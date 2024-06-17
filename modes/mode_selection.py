from enum import Enum
from simple_term_menu import TerminalMenu

from category import Category
from modes.display_performance_data import (
    display_total_logged_in_hours_for_each_category,
)
from modes.log_activities_and_hours_mode import log_activities_and_hours
from modes.personalized_week_analysis import show_personalised_week_analysis
from modes.set_categories_and_target_hours_mode import enter_categories_and_target_hours
from modes.show_categories_and_target_hours_mode import show_categories_and_target_hours
from modes.show_weekly_strava_activities import show_weekly_strava_activities
from utils import clear_screen


class StartMenuItem(Enum):
    SET_CATEGORIES_AND_TARGET_HOURS = "Set categories and target hours"
    SHOW_CATEGORIES_AND_TARGET_HOURS = "Show categories and target hours"
    LOG_ACTIVITIES_AND_HOURS = "Log activities and hours"
    SHOW_AND_LOG_WEEKLY_STRAVA_ACTIVITIES = "Show and log weekly Strava activities"
    GENERATE_PERFORMANCE_DATA = "Generate weekly and daily performance data"
    PERSONALIZED_WEEK_ANALYSIS = "Personalized week analysis"
    EXIT_PROGRAM = "Exit program"


def show_mode_selection_menu():
    while True:
        options = [item.value for item in StartMenuItem]
        terminal_menu = TerminalMenu(
            options,
            title="ℹ️ Use ↓ or ↑ arrow keys to navigate and 'Enter' to select:\n",
            menu_cursor_style=("fg_green", "bold"),
            quit_keys=("escape", "q", "ctrl-g", "ctrl-c", "ctrl-d"),
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
        elif selected_mode == StartMenuItem.SHOW_AND_LOG_WEEKLY_STRAVA_ACTIVITIES:
            validate_categories_count(show_weekly_strava_activities, selected_mode)
        elif selected_mode == StartMenuItem.GENERATE_PERFORMANCE_DATA:
            validate_activities_count(
                display_total_logged_in_hours_for_each_category, selected_mode
            )
        elif selected_mode == StartMenuItem.PERSONALIZED_WEEK_ANALYSIS:
            validate_activities_count(show_personalised_week_analysis, selected_mode)
        elif selected_mode == StartMenuItem.EXIT_PROGRAM:
            print("Exiting program. Goodbye!👋")
            break


def validate_categories_count(function_name, selected_mode):
    categories_count = Category.get_number_of_categories()
    if categories_count == 0:
        print(
            f"\n❗ To select '{selected_mode.value}' mode you need to have at least one category added. Current count of categories is {categories_count}\n"
        )
    else:
        function_name()


def validate_activities_count(function_name, selected_mode):
    activities_count = Category.get_number_of_activities()
    if activities_count == 0:
        print(
            f"\n❗ To select '{selected_mode.value}' mode you need to have at least one activity added. Current count of activities is {activities_count}\n"
        )
    else:
        function_name()
