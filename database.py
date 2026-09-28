import json
import os


DATA_FILE = os.path.join("data", "students.json")


def save_student_record(record):
    """Save a student assessment record."""

    os.makedirs("data", exist_ok=True)

    records = []

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                records = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            records = []

    records.append(record)

    with open(DATA_FILE, "w") as file:
        json.dump(records, file, indent=4)


def load_student_records():
    """Load all saved student records."""

    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def display_saved_records():
    """Display all saved student records."""

    records = load_student_records()

    if not records:
        print("\nNo student records found.")
        return

    print("\n" + "=" * 60)
    print("              SAVED STUDENT RECORDS")
    print("=" * 60)

    for record in records:
        print(f"\nStudent Name     : {record['name']}")
        print(f"Registration No. : {record['student_id']}")
        print(f"Course           : {record['course']}")
        print(f"Percentage       : {record['percentage']:.2f}%")
        print(f"Performance      : {record['performance']}")

    print("=" * 60)