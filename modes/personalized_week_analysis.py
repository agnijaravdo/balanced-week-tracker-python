import csv
import os
from utils import print_heading

WEEKLY_PERFORMANCE_DATA_PATH = "data/weekly_performance.csv"
DAILY_PERFORMANCE_DATA_PATH = "data/daily_performance.csv"


def show_personalised_week_analysis():
    display_weekly_goals_performance()
    display_daily_goals_performance()


def display_weekly_goals_performance():
    if (
        not os.path.exists(WEEKLY_PERFORMANCE_DATA_PATH)
        or os.path.getsize(WEEKLY_PERFORMANCE_DATA_PATH) == 0
    ):
        print(
            f"\nNo data available in {WEEKLY_PERFORMANCE_DATA_PATH} or file not exist. Select 'Generate weekly and daily performance data' menu option first\n"
        )
        return

    print_heading("Weekly Goals Performance")
    with open(WEEKLY_PERFORMANCE_DATA_PATH, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            target_hours = float(row["Weekly Target Hours"])
            logged_in_hours = float(row["Logged In Hours"])

            print(f"Category: {row['Category Name']}")
            print(
                f"Weekly Target Hours: {target_hours}, Logged In Hours: {logged_in_hours}"
            )

            if target_hours == logged_in_hours:
                print(
                    "GOAL ACHIEVED ✅: Bravo! You've balanced your time perfectly for this week"
                )
            elif target_hours > logged_in_hours:
                difference = target_hours - logged_in_hours
                print(
                    f"GOAL NOT ACHIEVED ❌: You are {difference:.2f} hours below your target. Try to have a more balanced week for overall well-being"
                )
            elif target_hours < logged_in_hours:
                difference = logged_in_hours - target_hours
                print(
                    f"OVERACHIEVED 💡: You logged in {difference:.2f} extra hours. Great job, but remember to also take care of your well-being and avoid burning out or not sticking to your planned tasks"
                )

            print("")


def display_daily_goals_performance():
    if (
        not os.path.exists(DAILY_PERFORMANCE_DATA_PATH)
        or os.path.getsize(DAILY_PERFORMANCE_DATA_PATH) == 0
    ):
        print(
            f"No data available in {DAILY_PERFORMANCE_DATA_PATH} or file not exist. Select 'Generate weekly and daily performance data' menu option first"
        )
        return

    print_heading("Daily Goals Performance")
    with open(DAILY_PERFORMANCE_DATA_PATH, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            target_hours = float(row["Daily Target Hours"])
            logged_in_hours = float(row["Logged In Hours"])

            print(f"Category: {row['Category Name']}")
            print(
                f"Daily Target Hours: {target_hours}, Logged In Hours: {logged_in_hours}"
            )

            if target_hours == logged_in_hours:
                print(
                    "GOAL ACHIEVED ✅: Bravo! You've balanced your time perfectly for today"
                )
            elif target_hours > logged_in_hours:
                difference = target_hours - logged_in_hours
                print(
                    f"GOAL NOT ACHIEVED ❌: You are {difference:.2f} hours below your target. Try to have a more balanced day for overall well-being"
                )
            elif target_hours < logged_in_hours:
                difference = logged_in_hours - target_hours
                print(
                    f"OVERACHIEVED 💡: You logged in {difference:.2f} extra hours. Great job, but remember to also take care of your well-being and avoid burning out or not sticking to your planned tasks"
                )

            print("")
