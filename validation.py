def get_valid_score(skill_name):
    """Get a valid skill score between 0 and 10."""

    while True:
        try:
            score = float(input(f"Enter {skill_name} score (0-10): "))

            if 0 <= score <= 10:
                return score

            print("Error: Score must be between 0 and 10.")

        except ValueError:
            print("Error: Please enter a valid number.")


def get_non_empty_input(message):
    """Get input that cannot be empty."""

    while True:
        value = input(message).strip()

        if value:
            return value

        print("Error: This field cannot be empty.")