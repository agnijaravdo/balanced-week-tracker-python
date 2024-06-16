from category import Category
from tabulate import tabulate

def show_categories_and_target_hours():
    categories = Category.get_all_categories()

    table = []
    for category in categories:
        row = [
            category.id,
            category.category_name,
            category.is_weekly,
            category.target_hours,
        ]
        table.append(row)

    headers = [
        "ID",
        "Category Name",
        "Is Weekly",
        "Target Hours",
    ]
    print(
        tabulate(
            table,
            headers=headers,
            tablefmt="grid",
            maxcolwidths=[None, None, None, None],
        )
    )
