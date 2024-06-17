import csv
from datetime import datetime, timedelta
from tabulate import tabulate
from category import Category
from utils import print_heading

WEEKLY_PERFORMANCE_DATA_PATH = "data/weekly_performance.csv"
DAILY_PERFORMANCE_DATA_PATH = "data/daily_performance.csv"


def display_total_logged_in_hours_for_each_category():
    print_heading("Display performance for each category")

    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    start_of_week_str = start_of_week.strftime("%Y-%m-%d")
    end_of_week_str = end_of_week.strftime("%Y-%m-%d")

    categories = Category.get_all_categories()
    Category.calculate_logged_in_hours_for_category(
        categories,
        datetime.strptime(start_of_week_str, "%Y-%m-%d"),
        datetime.strptime(end_of_week_str, "%Y-%m-%d"),
    )

    activities = Category.get_all_activities()
    weekly_table = []
    daily_goals_table = []

    for category in categories:
        if category.is_weekly:
            weekly_row = [
                category.category_name,
                category.is_weekly,
                category.target_hours,
                category.logged_in_hours,
            ]
            weekly_table.append(weekly_row)

    for activity in activities:
        activity_date = datetime.strptime(activity.activity_date, "%Y-%m-%d")
        if (
            activity_date >= start_of_week
            and activity_date <= end_of_week
            and not activity.is_weekly
        ):
            daily_goals_row = [
                activity.category_name,
                activity.is_weekly,
                activity.activity_date,
                activity.target_hours,
                activity.logged_in_hours,
            ]
            daily_goals_table.append(daily_goals_row)

    weekly_headers = [
        "Category Name",
        "Is Weekly",
        "Weekly Target Hours",
        "Logged In Hours",
    ]
    daily_goals_headers = [
        "Category Name",
        "Is Weekly",
        "Date",
        "Daily Target Hours",
        "Logged In Hours",
    ]

    print("\nWeekly Goals Table:")
    print(tabulate(weekly_table, headers=weekly_headers, tablefmt="grid"))

    print("\nDaily Goals Table:")
    print(tabulate(daily_goals_table, headers=daily_goals_headers, tablefmt="grid"))

    with open(WEEKLY_PERFORMANCE_DATA_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(weekly_headers)
        writer.writerows(weekly_table)

    with open(DAILY_PERFORMANCE_DATA_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(daily_goals_headers)
        writer.writerows(daily_goals_table)
