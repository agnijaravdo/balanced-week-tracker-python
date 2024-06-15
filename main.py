from category import Category
from modes.mode_selection import show_mode_selection_menu
from utils import print_heading


def main():
    print_heading("WEEKLY BALANCE TRACKER")
    show_mode_selection_menu()
    print(Category.get_number_of_categories())

if __name__ == "__main__":
    main()
