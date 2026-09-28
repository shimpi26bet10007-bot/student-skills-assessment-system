from student import Student
from assessment import Assessment
from validation import get_valid_score, get_non_empty_input
from database import save_student_record, display_saved_records
from report import generate_report
from utils import print_header, pause, display_menu


def assess_student():
    print_header("STUDENT DETAILS")

    name = get_non_empty_input("Enter student name: ")
    student_id = get_non_empty_input("Enter registration number: ")
    email = get_non_empty_input("Enter email: ")
    course = get_non_empty_input("Enter course: ")

    student = Student(
        student_id,
        name,
        email,
        course
    )

    assessment = Assessment(student_id)

    print("\nEnter marks out of 10 for each skill:")

    programming = get_valid_score("Programming")
    communication = get_valid_score("Communication")
    problem_solving = get_valid_score("Problem Solving")
    technical = get_valid_score("Technical/Subject")

    assessment.add_skill("Programming", programming)
    assessment.add_skill("Communication", communication)
    assessment.add_skill("Problem Solving", problem_solving)
    assessment.add_skill("Technical/Subject", technical)

    student.display_student()
    assessment.display_assessment()

    record = {
        "name": student.name,
        "student_id": student.student_id,
        "course": student.course,
        "percentage": assessment.calculate_percentage(),
        "performance": assessment.get_performance_level()
    }

    save_student_record(record)

    report_file = generate_report(student, assessment)

    print("\nAssessment record saved successfully.")
    print(f"Detailed report created: {report_file}")

    pause()


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            assess_student()

        elif choice == "2":
            display_saved_records()
            pause()

        elif choice == "3":
            print("\nThank you for using Student Skill Assessment System!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()