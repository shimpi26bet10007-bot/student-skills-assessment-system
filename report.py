import os


def generate_report(student, assessment):
    """Generate a detailed assessment report."""

    os.makedirs("data", exist_ok=True)

    filename = f"data/report_{student.student_id}.txt"

    strongest = assessment.find_strongest_skill()
    weakest = assessment.find_weakest_skill()

    with open(filename, "w") as file:
        file.write("=" * 55 + "\n")
        file.write("           STUDENT SKILL ASSESSMENT REPORT\n")
        file.write("=" * 55 + "\n\n")

        file.write("STUDENT DETAILS\n")
        file.write("-" * 55 + "\n")
        file.write(f"Student Name     : {student.name}\n")
        file.write(f"Registration No. : {student.student_id}\n")
        file.write(f"Email            : {student.email}\n")
        file.write(f"Course           : {student.course}\n\n")

        file.write("SKILL ASSESSMENT\n")
        file.write("-" * 55 + "\n")

        for skill in assessment.skills:
            file.write(
                f"{skill.skill_name:<25}: {skill.score}/10\n"
            )

        file.write("\n")
        file.write("PERFORMANCE ANALYSIS\n")
        file.write("-" * 55 + "\n")
        file.write(
            f"Total Marks      : "
            f"{assessment.calculate_total()}/40\n"
        )
        file.write(
            f"Percentage       : "
            f"{assessment.calculate_percentage():.2f}%\n"
        )
        file.write(
            f"Performance      : "
            f"{assessment.get_performance_level()}\n"
        )

        if strongest:
            file.write(
                f"Strongest Skill  : {strongest.skill_name}\n"
            )

        if weakest:
            file.write(
                f"Skill to Improve : {weakest.skill_name}\n"
            )

        file.write("\n")
        file.write("=" * 55 + "\n")
        file.write("Thank you for using Student Skill Assessment System!\n")
        file.write("=" * 55 + "\n")

    return filename