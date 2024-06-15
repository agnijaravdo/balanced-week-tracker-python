from modes.mode_selection import show_mode_selection_menu


def main():
    print_heading()
    show_mode_selection_menu()


def print_heading():
    heading_text = "WEEKLY BALANCE TRACKER"
    line_length = 50
    print("\n" + "-" * line_length)
    print(heading_text.center(line_length))
    print("-" * line_length + "\n")


if __name__ == "__main__":
    main()
