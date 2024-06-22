import pytest
from activity import Activity
from test.test_data.test_constants import (
    CATEGORY_LEARNING,
    CATEGORY_READING,
    CATEGORY_WORKING,
    DATE,
    LOGGED_IN_HOURS_1,
    LOGGED_IN_HOURS_2,
    LOGGED_IN_HOURS_3,
    NUMBER_OF_ACTIVITIES,
    TARGET_HOURS_2,
    TARGET_HOURS_3,
    TARGET_HOURS_5,
)


def test_activity_init():
    activity = Activity(
        DATE, CATEGORY_LEARNING, TARGET_HOURS_5, True, LOGGED_IN_HOURS_2
    )
    assert activity.activity_date == DATE
    assert activity.category_name == CATEGORY_LEARNING
    assert activity.target_hours == TARGET_HOURS_5
    assert activity.is_weekly == True
    assert activity.logged_in_hours == LOGGED_IN_HOURS_2


def test_incorrect_category_name_type():
    with pytest.raises(ValueError) as e:
        Activity(DATE, 123, TARGET_HOURS_5, True, LOGGED_IN_HOURS_2)
    assert str(e.value) == "Category name must be a string"


def test_get_number_of_activities():
    activity = [
        Activity(DATE, CATEGORY_LEARNING, TARGET_HOURS_5, True, LOGGED_IN_HOURS_2),
        Activity(DATE, CATEGORY_READING, TARGET_HOURS_3, False, LOGGED_IN_HOURS_1),
        Activity(DATE, CATEGORY_WORKING, TARGET_HOURS_2, True, LOGGED_IN_HOURS_3),
    ]
    number_of_activities = Activity.get_number_of_activities(activity)
    assert number_of_activities == NUMBER_OF_ACTIVITIES
