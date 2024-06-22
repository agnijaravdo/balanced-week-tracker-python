import csv
import os
from utils import print_heading

WEEKLY_PERFORMANCE_DATA_PATH = "data/weekly_performance.csv"
DAILY_PERFORMANCE_DATA_PATH = "data/daily_performance.csv"


def show_personalised_week_analysis():
    display_weekly_goals_performance()
    display_daily_goals_performance()


def check_file_exists_and_not_empty(file_path) -> bool:
    return os.path.exists(file_path) and os.path.getsize(file_path) > 0


def display_weekly_goals_performance() -> None:
    if not check_file_exists_and_not_empty(WEEKLY_PERFORMANCE_DATA_PATH):
        print(
            f"\nNo data available in {WEEKLY_PERFORMANCE_DATA_PATH} or file not exist. Select 'Generate weekly and daily performance data' menu option first\n"
        )
        return

    print_heading("Weekly Goals Performance")
    display_goals_performance(WEEKLY_PERFORMANCE_DATA_PATH, "Weekly")


def display_daily_goals_performance() -> None:
    if not check_file_exists_and_not_empty(DAILY_PERFORMANCE_DATA_PATH):
        print(
            f"No data available in {DAILY_PERFORMANCE_DATA_PATH} or file not exist. Select 'Generate weekly and daily performance data' menu option first"
        )
        return

    print_heading("Daily Goals Performance")
    display_goals_performance(DAILY_PERFORMANCE_DATA_PATH, "Daily")


def display_goals_performance(file_path: str, period: str) -> None:
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            target_hours = float(row[f"{period} Target Hours"])
            logged_in_hours = float(row["Logged In Hours"])

            print(f"Category: {row['Category Name']}")
            print(
                f"{period} Target Hours: {target_hours}, Logged In Hours: {logged_in_hours}"
            )

            evaluate_performance(target_hours, logged_in_hours, period)
            print("")


def evaluate_performance(
    target_hours: float, logged_in_hours: float, period: str
) -> None:
    if target_hours == logged_in_hours:
        print(
            f"GOAL ACHIEVED ✅: Bravo! You've balanced your time perfectly for this {period.lower()}"
        )
    elif target_hours > logged_in_hours:
        difference = target_hours - logged_in_hours
        print(
            f"GOAL NOT ACHIEVED ❌: You are {difference:.2f} hours below your target. Try to have a more balanced {period.lower()} for overall well-being"
        )
    elif target_hours < logged_in_hours:
        difference = logged_in_hours - target_hours
        print(
            f"OVERACHIEVED 💡: You logged in {difference:.2f} extra hours. \nGreat job, but remember to also take care of your well-being and avoid burning out or not sticking to your planned tasks"
        )
