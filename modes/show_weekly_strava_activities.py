from datetime import datetime, timedelta
import json
import time
import os
import requests
from dotenv import load_dotenv


def show_weekly_strava_activities():
    activities_response = get_strava_activities_response()
    print_weekly_strava_activity_statistics(activities_response)


def get_strava_activities_response():

    load_dotenv()

    access_token = os.getenv("STRAVA_ACCESS_TOKEN")
    url = "https://www.strava.com/api/v3/athlete/activities"

    before = int(time.time())
    after = before - 7 * 24 * 60 * 60  # One week ago
    page = 1
    per_page = 30

    params = {"before": before, "after": after, "page": page, "per_page": per_page}

    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        activities = response.json()
        # print(json.dumps(activities, indent=2))
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

    return activities


def print_weekly_strava_activity_statistics(activities_response):
    for i, result in enumerate(activities_response, 1):
        activity_type = result["type"]
        activity_name = result["name"]
        activity_date = datetime.strptime(result["start_date"], "%Y-%m-%dT%H:%M:%SZ")
        activity_moving_time = str(timedelta(seconds=result["moving_time"]))

        print(
            f"{i}. {activity_type} activity with name: '{activity_name}' on {activity_date} and moving time: {activity_moving_time}"
        )
    print("\n")
