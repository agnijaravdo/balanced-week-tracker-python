from datetime import datetime
from activity import Activity
from modes.display_performance_data import (
    get_current_week_dates,
    prepare_daily_table,
    prepare_weekly_table,
)
from category import Category


def test_prepare_weekly_table():

    categories = [
        Category("Learning", 5.0, True, 2.0),
        Category("Reading", 3.0, False, 1.0),
        Category("Working", 2.0, True, 3.0),
    ]
    weekly_table = prepare_weekly_table(categories)

    assert weekly_table == [
        ["Learning", True, 5.0, 2.0],
        ["Working", True, 2.0, 3.0],
    ]


def test_prepare_weekly_table_no_is_weekly_categories():

    categories = [
        Category("Reading", 3.0, False, 1.0),
    ]
    weekly_table = prepare_weekly_table(categories)

    assert weekly_table == []


def test_prepare_weekly_table_no_categories():

    categories = []
    weekly_table = prepare_weekly_table(categories)

    assert weekly_table == []


def test_prepare_daily_table():

    activities = [
        Activity("2024-06-07", "Learning", 5.0, True, 2.0),
        Activity("2024-06-07", "Reading", 3.0, False, 1.0),
        Activity("2024-06-07", "Working", 2.0, True, 3.0),
    ]
    start_of_week = datetime(2024, 6, 3)
    end_of_week = datetime(2024, 6, 9)
    daily_table = prepare_daily_table(activities, start_of_week, end_of_week)

    assert daily_table == [
        ["Reading", False, "2024-06-07", 3.0, 1.0],
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
