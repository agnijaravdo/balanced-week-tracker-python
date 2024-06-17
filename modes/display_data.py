from datetime import datetime, timedelta
from tabulate import tabulate

from category import Category
from utils import print_heading



def display_total_logged_in_hours_for_each_category():
    print_heading("Display performance for each category")
    print(
        "⬅️ To go back to the main menu - press Ctrl+C or Ctrl+D. To close the program, press Ctrl+Z.\n"
    )
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    start_of_week_str = start_of_week.strftime("%Y-%m-%d")
    end_of_week_str = end_of_week.strftime("%Y-%m-%d")

    categories = Category.get_all_categories()
    Category.calculate_logged_in_hours_for_category(categories, datetime.strptime(start_of_week_str, "%Y-%m-%d"), datetime.strptime(end_of_week_str, "%Y-%m-%d"))

    table = []
    for category in categories:
        row = [
            category.id,
            category.category_name,
            category.is_weekly,
            category.target_hours,
            category.logged_in_hours,
        ]
        table.append(row)

    headers = [
        "ID",
        "Category Name",
        "Is Weekly",
        "Target Hours",
        "Logged In Hours",
    ]
    print(
        tabulate(
            table,
            headers=headers,
            tablefmt="grid",
            maxcolwidths=[None, None, None, None, None],
        )
    )
