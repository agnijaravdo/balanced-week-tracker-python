from datetime import datetime
from activity import Activity
from modes.display_performance_data import (
    get_current_week_dates,
    prepare_daily_table,
    prepare_weekly_table,
)
from category import Category
from test.test_data.test_constants import (
    CATEGORY_LEARNING,
    CATEGORY_READING,
    CATEGORY_WORKING,
    DATE,
    LOGGED_IN_HOURS_1,
    LOGGED_IN_HOURS_2,
    LOGGED_IN_HOURS_3,
    TARGET_HOURS_2,
    TARGET_HOURS_3,
    TARGET_HOURS_5,
)


def test_prepare_weekly_table():

    categories = [
        Category(CATEGORY_LEARNING, TARGET_HOURS_5, True, LOGGED_IN_HOURS_2),
        Category(CATEGORY_READING, TARGET_HOURS_3, False, LOGGED_IN_HOURS_1),
        Category(CATEGORY_WORKING, TARGET_HOURS_2, True, LOGGED_IN_HOURS_3),
    ]
    weekly_table = prepare_weekly_table(categories)

    assert weekly_table == [
        [CATEGORY_LEARNING, True, TARGET_HOURS_5, LOGGED_IN_HOURS_2],
        [CATEGORY_WORKING, True, TARGET_HOURS_2, LOGGED_IN_HOURS_3],
    ]


def test_prepare_weekly_table_no_is_weekly_categories():

    categories = [
        Category(CATEGORY_READING, TARGET_HOURS_3, False, LOGGED_IN_HOURS_1),
    ]
    weekly_table = prepare_weekly_table(categories)

    assert weekly_table == []


def test_prepare_weekly_table_no_categories():

    categories = []
    weekly_table = prepare_weekly_table(categories)

    assert weekly_table == []


def test_prepare_daily_table():

    activities = [
        Activity(DATE, CATEGORY_LEARNING, TARGET_HOURS_5, True, LOGGED_IN_HOURS_2),
        Activity(DATE, CATEGORY_READING, TARGET_HOURS_3, False, LOGGED_IN_HOURS_1),
        Activity(DATE, CATEGORY_WORKING, TARGET_HOURS_2, True, LOGGED_IN_HOURS_3),
    ]
    start_of_week = datetime(2024, 6, 3)
    end_of_week = datetime(2024, 6, 9)
    daily_table = prepare_daily_table(activities, start_of_week, end_of_week)

    assert daily_table == [
        [CATEGORY_READING, False, DATE, TARGET_HOURS_3, LOGGED_IN_HOURS_1],
    ]


def test_get_current_week_dates():
    today = datetime(2024, 6, 7)
    start_of_week_str, start_of_week, end_of_week_str, end_of_week = (
        get_current_week_dates(today)
    )

    assert start_of_week_str == "2024-06-03"
    assert start_of_week == datetime(2024, 6, 3)
    assert end_of_week_str == "2024-06-09"
    assert end_of_week == datetime(2024, 6, 9)
