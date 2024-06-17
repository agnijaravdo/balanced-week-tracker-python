from datetime import datetime
import pytest
from activity import Activity
from category import Category


def test_activity_init():
    activity = Activity("2024-06-07", "Learning", 5.0, True, 2.0)
    assert activity.activity_date == "2024-06-07"
    assert activity.category_name == "Learning"
    assert activity.target_hours == 5.0
    assert activity.is_weekly == True
    assert activity.logged_in_hours == 2.0


def test_incorect_category_name_type():
    with pytest.raises(ValueError) as e:
        Activity("2024-06-07", 123, 5.0, True, 2.0)
    assert str(e.value) == "Category name must be a string"


def test_get_number_of_activities():
    activity = [
        Activity("2024-06-07", "Learning", 5.0, True, 2.0),
        Activity("2024-06-07", "Reading", 3.0, False, 1.0),
        Activity("2024-06-07", "Working", 2.0, True, 3.0),
    ]
    number_of_activities = Activity.get_number_of_activities(activity)
    assert number_of_activities == 3
