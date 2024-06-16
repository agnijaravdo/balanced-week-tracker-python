import csv
import os


CATEGORIES_AND_GOALS_DATA_PATH = "data/categories_and_goals.csv"
LOGGED_IN_DATA_PATH = "data/logged_in_data.csv"


class Category:
    def __init__(self, category_name, target_hours, is_weekly) -> None:
        self.category_name = category_name
        self.target_hours = target_hours
        self.is_weekly = is_weekly

    def __repr__(self) -> str:
        return f"Category {self.category_name} with target hours {self.target_hours}"

    @staticmethod
    def write_category_and_target_hours_to_file(category) -> None:
        is_file_exists = os.path.isfile(CATEGORIES_AND_GOALS_DATA_PATH)

        max_id = 0
        if is_file_exists:
            with open(CATEGORIES_AND_GOALS_DATA_PATH, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row_id = int(row["id"])
                    if row_id > max_id:
                        max_id = row_id

        with open(CATEGORIES_AND_GOALS_DATA_PATH, "a") as file:
            header = [
                "id",
                "category",
                "is_weekly",
                "target_hours",
            ]
            writer = csv.DictWriter(file, fieldnames=header)

            if (
                not is_file_exists
                or os.path.getsize(CATEGORIES_AND_GOALS_DATA_PATH) == 0
            ):
                writer.writeheader()

            writer.writerow(
                {
                    "id": max_id + 1,
                    "category": category.category_name,
                    "is_weekly": category.is_weekly,
                    "target_hours": category.target_hours,
                }
            )

            print(
                f"\nCategory '{category.category_name}' with target hours '{category.target_hours}' was added successfully\n"
            )

    @staticmethod
    def get_all_categories() -> list:
        categories = []
        with open(CATEGORIES_AND_GOALS_DATA_PATH, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = Category(
                    category_name=row["category"],
                    target_hours=row["target_hours"],
                    is_weekly=row["is_weekly"] == "True",
                )
                category.id = int(row["id"])
                categories.append(category)
        return categories

    @staticmethod
    def get_number_of_categories() -> int:
        categories = Category.get_all_categories()
        categories_count = len(categories)
        return categories_count

    @staticmethod
    def get_category_names(categories) -> list:
        category_names = []
        for category in categories:
            category_names.append(category.category_name)

        return category_names

    @staticmethod
    def get_frequency_based_on_category(category_name):
        categories = Category.get_all_categories()

        category = None
        for cat in categories:
            if cat.category_name == category_name:
                category = cat
                break

        if category is None:
            return "Category was not found"

        return "weekly" if category.is_weekly else "daily"

    @staticmethod
    def update_or_create_log_entry(activity_date, activity_category, logged_in_hours):
        categories = Category.get_all_categories()
        category = next(
            (
                cat
                for cat in categories
                if cat.category_name.strip().lower()
                == activity_category.strip().lower()
            ),
            None,
        )

        temp_rows = []

        try:
            with open(LOGGED_IN_DATA_PATH, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    temp_rows.append(row)
        except FileNotFoundError:
            pass

        entry_found = False
        for row in temp_rows:
            if (
                row["date"] == activity_date
                and row["category"].strip().lower() == activity_category.strip().lower()
            ):
                row["logged_in_hours"] = float(row["logged_in_hours"]) + float(
                    logged_in_hours
                )
                entry_found = True
                break

        if not entry_found:
            temp_rows.append(
                {
                    "id": len(temp_rows) + 1,
                    "date": activity_date,
                    "category": activity_category,
                    "is_weekly": str(category.is_weekly).capitalize(),
                    "target_hours": category.target_hours,
                    "logged_in_hours": logged_in_hours,
                }
            )

        fieldnames = [
            "id",
            "date",
            "category",
            "is_weekly",
            "target_hours",
            "logged_in_hours",
        ]

        with open(LOGGED_IN_DATA_PATH, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(temp_rows)
        print(
            f"\nLog entry for date '{activity_date}' and category '{activity_category}' was successfully updated or created.\n"
        )
