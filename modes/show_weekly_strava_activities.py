from datetime import datetime, timedelta
from simple_term_menu import TerminalMenu
import json
import time
import os
import requests
from dotenv import load_dotenv
from activity import Activity
from category import Category
from modes.log_activities_and_hours_mode import select_activity_category
from utils import clear_screen, print_heading


def show_weekly_strava_activities():
    print_heading("Weekly Strava Activities")
    print(
        "⬅️ To go back to the main menu - press Ctrl+C or Ctrl+D. To close the program, press Ctrl+Z.\n"
    )
    try:
        activities_response = get_strava_activities_response()
        activities_details = return_and_print_weekly_strava_activities_details(
            activities_response
        )
        response = select_whether_to_log_activities_from_strava()
        log_activities_based_on_response(response, activities_details)
    except (KeyboardInterrupt, EOFError):
        clear_screen()
        return


def get_strava_activities_response():

    load_dotenv()

    STRAVA_ACCESS_TOKEN = os.getenv("STRAVA_ACCESS_TOKEN")

    url = "https://www.strava.com/api/v3/athlete/activities"

    before = int(time.time())
    after = before - 7 * 24 * 60 * 60  # One week ago
    page = 1
    per_page = 30

    params = {"before": before, "after": after, "page": page, "per_page": per_page}

    headers = {"Authorization": f"Bearer {STRAVA_ACCESS_TOKEN}"}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        activities = response.json()
        # print(json.dumps(activities, indent=2))
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

    return activities


def return_and_print_weekly_strava_activities_details(activities_response):
    activities_details = []

    for i, result in enumerate(activities_response, 1):
        activity_type = result["type"]
        activity_name = result["name"]
        activity_date = datetime.strptime(result["start_date"], "%Y-%m-%dT%H:%M:%SZ")
        activity_moving_time = str(timedelta(seconds=result["moving_time"]))

        print(
            f"{i}. {activity_type} activity with name: '{activity_name}' on {activity_date} and moving time: {activity_moving_time}"
        )

        activities_details.append(
            {
                "name": activity_name,
                "type": activity_type,
                "date": activity_date,
                "moving_time": activity_moving_time,
            }
        )

    return activities_details


def select_whether_to_log_activities_from_strava():
    options = ["Yes", "No"]
    terminal_menu = TerminalMenu(
        options,
        title="\nℹ️ Would you like to log any of these activities into your weekly tracker?: \n",
        menu_cursor_style=("fg_green", "bold"),
        quit_keys=(),
    )

    try:
        menu_entry_index = terminal_menu.show()
    except (KeyboardInterrupt, EOFError):
        return None

    if menu_entry_index == None:
        return

    selected_mode = options[menu_entry_index]

    return selected_mode


def select_whether_to_log_individual_activity_from_strava(activity_info):
    options = ["Yes", "No"]
    terminal_menu = TerminalMenu(
        options,
        title=f"\nℹ️ Would you like to log '{activity_info}': \n",
        menu_cursor_style=("fg_green", "bold"),
        quit_keys=(),
    )

    try:
        menu_entry_index = terminal_menu.show()
    except (KeyboardInterrupt, EOFError):
        return None

    if menu_entry_index == None:
        return

    selected_mode = options[menu_entry_index]

    return selected_mode


def log_activities_based_on_response(response, activities_details):
    if response == "No":
        clear_screen()
        return
    elif response == "Yes":
        category = select_activity_category()
        if category is None:
            clear_screen()
            return
        for activity in activities_details:
            name, activity_type, date, moving_time = (
                activity["name"],
                activity["type"],
                activity["date"],
                activity["moving_time"],
            )
            activity_info = f"{activity_type} activity with name: '{name}' on {date} and moving time: {moving_time}"
            parsed_date = date.strftime("%Y-%m-%d")
            parsed_moving_time = time_string_to_float(moving_time)
            activity_to_log_response = (
                select_whether_to_log_individual_activity_from_strava(activity_info)
            )
            if activity_to_log_response is None:
                clear_screen()
                return
            if activity_to_log_response.lower() == "yes":
                categories = Category.get_all_categories()
                Activity.update_or_create_log_entry(
                    categories, parsed_date, category, parsed_moving_time
                )
            elif activity_to_log_response.lower() == "no":
                return

        clear_screen()


def time_string_to_float(time_string):
    time_parts = time_string.split(":")
    hours, minutes, seconds = map(int, time_parts)
    total_hours = hours + minutes / 60 + seconds / 3600

    total_hours_rounded = round(total_hours, 2)

    return total_hours_rounded
