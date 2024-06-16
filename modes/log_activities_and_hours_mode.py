import datetime

from utils import clear_screen, print_heading


def log_activities_and_hours():
    print_heading("Log Activities And Hours Spent on Them")
    print("⬅️ To go back to the main menu, press Ctrl+C or Ctrl+D. To close the program, press Ctrl+Z.\n")
    logged_date = enter_activity_date()

def enter_activity_date():
    while True:
        try:
            date = input("Enter a date to log your activity (YYYY-MM-DD format): ")
            year, month, day = map(int, date.split("-"))

            return datetime.date(year, month, day)

        except ValueError as e:
            print(
                f"{str(e).capitalize()}. You can only enter date in YYYY-MM-DD format. Please try again"
            )
        except (KeyboardInterrupt, EOFError):
            clear_screen()
            break
