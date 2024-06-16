import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_heading(text):
    line_length = 50
    print("\n" + "-" * line_length)
    print(text.center(line_length))
    print("-" * line_length + "\n")
