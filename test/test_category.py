import pytest
from category import Category
from test.test_data.test_constants import (
    CATEGORY_LEARNING,
    CATEGORY_READING,
    CATEGORY_WORKING,
    NUMBER_OF_CATEGORIES,
    TARGET_HOURS_2,
    TARGET_HOURS_3,
    TARGET_HOURS_5,
)


def test_category_init():
    category = Category(CATEGORY_LEARNING, TARGET_HOURS_5, True)
    assert category.category_name == CATEGORY_LEARNING
    assert category.target_hours == TARGET_HOURS_5
    assert category.is_weekly == True
    assert category.logged_in_hours == 0.0


def test_incorrect_category_name_type():
    with pytest.raises(ValueError) as e:
        Category(123, TARGET_HOURS_5, True)
    assert str(e.value) == "Category name must be a string"


def test_incorrect_target_hours_type():
    with pytest.raises(ValueError) as e:
        Category(CATEGORY_LEARNING, "Number", True)
    assert str(e.value) == "Target hours must be a number"


def test_incorrect_target_hours_negative():
    with pytest.raises(ValueError) as e:
        Category(CATEGORY_LEARNING, -TARGET_HOURS_5, True)
    assert str(e.value) == "Target hours cannot be negative"


def test_get_categories_names():
    category = [Category(CATEGORY_LEARNING, TARGET_HOURS_5, True)]
    category_name = Category.get_category_names(category)
    assert category_name == [CATEGORY_LEARNING]


def test_get_number_of_categories():
    category = [
        Category(CATEGORY_LEARNING, TARGET_HOURS_5, True),
        Category(CATEGORY_READING, TARGET_HOURS_3, False),
        Category(CATEGORY_WORKING, TARGET_HOURS_2, True),
    ]
    number_of_categories = Category.get_number_of_categories(category)
    assert number_of_categories == NUMBER_OF_CATEGORIES
