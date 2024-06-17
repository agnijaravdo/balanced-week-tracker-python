import csv
import os

CATEGORIES_AND_GOALS_DATA_PATH = "data/categories_and_goals.csv"


class Category:
    def __init__(
        self,
        category_name: str,
        target_hours: float,
        is_weekly: bool,
        logged_in_hours=0.0,
    ):
        self.category_name = category_name
        self.target_hours = target_hours
        self.is_weekly = is_weekly
        self.logged_in_hours = logged_in_hours

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Category name must be a string")
        self._category_name = value

    @property
    def target_hours(self):
        return self._target_hours

    @target_hours.setter
    def target_hours(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Target hours must be a number")
        if value < 0:
            raise ValueError("Target hours cannot be negative")
        self._target_hours = value

    @property
    def is_weekly(self):
        return self._is_weekly

    @is_weekly.setter
    def is_weekly(self, value):
        if not isinstance(value, bool):
            raise ValueError("is_weekly must be a boolean value")
        self._is_weekly = value

    @property
    def logged_in_hours(self):
        return self._logged_in_hours

    @logged_in_hours.setter
    def logged_in_hours(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Logged in hours must be a number")
        if value < 0:
            raise ValueError("Logged in hours cannot be negative")
        self._logged_in_hours = value

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
            header = ["id", "category", "is_weekly", "target_hours"]
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
    def get_number_of_categories(categories: list) -> int:
        return len(categories)

    @staticmethod
    def get_category_names(categories: list) -> list:
        category_names = []
        for category in categories:
            category_names.append(category.category_name)

        return category_names
