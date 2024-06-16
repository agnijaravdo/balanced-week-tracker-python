import csv
import os


CATEGORIES_AND_GOALS_DATA_PATH = "data/categories_and_goals.csv"

class Category:
    def __init__(self, category_name, target_hours, is_weekly):
        self.category_name = category_name
        self.target_hours = target_hours
        self.is_weekly = is_weekly
        
    def __repr__(self) -> str:
        return f"Category {self.category_name} with target hours {self.target_hours}"

    @staticmethod
    def writeCategoryAndTargetHoursToFile(category):
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

            if not is_file_exists or os.path.getsize(CATEGORIES_AND_GOALS_DATA_PATH) == 0:
                writer.writeheader()

            writer.writerow(
                {
                    "id": max_id + 1,
                    "category": category.category_name,
                    "is_weekly": category.is_weekly,
                    "target_hours": category.target_hours,
                }
            )
            
            print(f"\nCategory '{category.category_name}' with target hours '{category.target_hours}' was added successfully\n")


    @staticmethod
    def get_all_categories():
        categories = []
        with open(CATEGORIES_AND_GOALS_DATA_PATH, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                question = Category(
                    category_name=row["category"],
                    target_hours=row["target_hours"],
                    is_weekly=row["is_weekly"]
                )
                categories.append(question)
        return categories


    @staticmethod
    def get_number_of_categories():
        categories = Category.get_all_categories()
        categories_count = len(categories)
        return categories_count
    
    @staticmethod
    def get_category_names(categories):
        category_names = []
        for category in categories:
            category_names.append(category.category_name)
        
        return category_names
