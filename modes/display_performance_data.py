import csv
from datetime import datetime, timedelta
from tabulate import tabulate
from activity import Activity
from category import Category
from utils import print_heading

WEEKLY_PERFORMANCE_DATA_PATH = "data/weekly_performance.csv"
DAILY_PERFORMANCE_DATA_PATH = "data/daily_performance.csv"


def display_total_logged_in_hours_for_each_category() -> None:
    print_heading("Weekly and daily performace data for each category")

    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    start_of_week_str, start_of_week, end_of_week_str, end_of_week = (
        get_current_week_dates(today)
    )
    categories = Category.get_all_categories()
    Activity.calculate_logged_in_hours_for_category(
        categories,
        datetime.strptime(start_of_week_str, "%Y-%m-%d"),
        datetime.strptime(end_of_week_str, "%Y-%m-%d"),
    )

    activities = Activity.get_all_activities()

    weekly_table = prepare_weekly_table(categories)
    daily_table = prepare_daily_table(activities, start_of_week, end_of_week)
    display_daily_and_weekly_tables(weekly_table, daily_table)
    write_to_file(
        WEEKLY_PERFORMANCE_DATA_PATH,
        ["Category Name", "Is Weekly", "Weekly Target Hours", "Logged In Hours"],
        weekly_table,
    )
    write_to_file(
        DAILY_PERFORMANCE_DATA_PATH,
        ["Category Name", "Is Weekly", "Date", "Daily Target Hours", "Logged In Hours"],
        daily_table,
    )


def get_current_week_dates(today: datetime) -> tuple:
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    start_of_week_str = start_of_week.strftime("%Y-%m-%d")
    end_of_week_str = end_of_week.strftime("%Y-%m-%d")
    return start_of_week_str, start_of_week, end_of_week_str, end_of_week


def prepare_weekly_table(categories: list) -> list:
    weekly_table = []
    for category in categories:
        if category.is_weekly:
            weekly_row = [
                category.category_name,
                category.is_weekly,
                category.target_hours,
                category.logged_in_hours,
            ]
            weekly_table.append(weekly_row)
    return weekly_table


def prepare_daily_table(
    activities: list, start_of_week: datetime, end_of_week: datetime
) -> list:
    daily_table = []
    for activity in activities:
        activity_date = datetime.strptime(activity.activity_date, "%Y-%m-%d")
        if start_of_week <= activity_date <= end_of_week and not activity.is_weekly:
            daily_goals_row = [
                activity.category_name,
                activity.is_weekly,
                activity.activity_date,
                activity.target_hours,
                activity.logged_in_hours,
            ]
            daily_table.append(daily_goals_row)
    return daily_table


def display_daily_and_weekly_tables(weekly_table: list, daily_table: list) -> None:
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
    print(tabulate(daily_table, headers=daily_goals_headers, tablefmt="grid"))


def write_to_file(path: str, headers: list, table: list) -> None:
    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(table)
