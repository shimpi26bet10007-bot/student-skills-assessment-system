def print_header(title):
    print("\n" + "=" * 55)
    print(f"{title:^55}")
    print("=" * 55)


def pause():
    input("\nPress Enter to continue...")


def display_menu():
    print_header("STUDENT SKILL ASSESSMENT SYSTEM")
    print("1. Assess Student")
    print("2. View Saved Records")
    print("3. Exit")
    print("-" * 55)