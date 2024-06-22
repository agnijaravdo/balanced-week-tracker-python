from modes.mode_selection import show_mode_selection_menu
from utils import print_heading


def main() -> None:
    print_heading("WEEKLY BALANCE TRACKER")
    show_mode_selection_menu()


if __name__ == "__main__":
    main()
