import csv
from datetime import datetime

LOGGED_IN_ACTIVITIES_DATA_PATH = "data/logged_in_activities.csv"


class Activity:
    def __init__(
        self,
        activity_date,
        category_name: str,
        target_hours: float,
        is_weekly: bool,
        logged_in_hours: float,
    ):
        self.activity_date = activity_date
        self.category_name = category_name
        self.target_hours = target_hours
        self.is_weekly = is_weekly
        self._logged_in_hours = logged_in_hours

    @property
    def category_name(self):
        return self._category_name

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
            raise ValueError("is_weekly must be a boolean")
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
    def update_or_create_log_entry(
        categories, activity_date, activity_category, logged_in_hours
    ):
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
            with open(LOGGED_IN_ACTIVITIES_DATA_PATH, "r") as file:
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

        with open(LOGGED_IN_ACTIVITIES_DATA_PATH, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(temp_rows)
        print(
            f"\nLog entry for date '{activity_date}' and category '{activity_category}' was successfully updated or created.\n"
        )

    @staticmethod
    def calculate_logged_in_hours_for_category(
        categories, start_date=None, end_date=None
    ):
        with open(LOGGED_IN_ACTIVITIES_DATA_PATH, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                activity_date = datetime.strptime(row["date"], "%Y-%m-%d")
                if (
                    start_date
                    and end_date
                    and (activity_date < start_date or activity_date > end_date)
                ):
                    continue
                category_name = row["category"]
                logged_in_hours = float(row["logged_in_hours"])
                for category in categories:
                    if category.category_name == category_name:
                        category.logged_in_hours += logged_in_hours

    @staticmethod
    def get_all_activities() -> list:
        activities = []
        with open(LOGGED_IN_ACTIVITIES_DATA_PATH, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                activity = Activity(
                    activity_date=row["date"],
                    category_name=row["category"],
                    target_hours=row["target_hours"],
                    is_weekly=row["is_weekly"] == "True",
                    logged_in_hours=row["logged_in_hours"],
                )
                activity.id = int(row["id"])
                activities.append(activity)
        return activities

    @staticmethod
    def get_number_of_activities(activities) -> int:
        categories_count = len(activities)
        return categories_count
