import pytest
from category import Category


def test_category_init():
    category = Category("Learning", 5.0, True)
    assert category.category_name == "Learning"
    assert category.target_hours == 5.0
    assert category.is_weekly == True
    assert category.logged_in_hours == 0.0


def test_incorect_category_name_type():
    with pytest.raises(ValueError) as e:
        Category(123, 5.0, True)
    assert str(e.value) == "Category name must be a string"


def test_incorect_target_hours_type():
    with pytest.raises(ValueError) as e:
        Category("Learning", "Number", True)
    assert str(e.value) == "Target hours must be a number"


def test_incorect_target_hours_negative():
    with pytest.raises(ValueError) as e:
        Category("Learning", -5.0, True)
    assert str(e.value) == "Target hours cannot be negative"


def test_get_caegories_names():
    category = [Category("Learning", 5.0, True)]
    category_name = Category.get_category_names(category)
    assert category_name == ["Learning"]


def test_get_number_of_categories():
    category = [
        Category("Learning", 5.0, True),
        Category("Reading", 3.0, False),
        Category("Working", 2.0, True),
    ]
    number_of_categories = Category.get_number_of_categories(category)
    assert number_of_categories == 3
