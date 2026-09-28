from skill import Skill


class Assessment:
    def __init__(self, student_id):
        self.student_id = student_id
        self.skills = []

    def add_skill(self, skill_name, score):
        skill = Skill(skill_name, score)
        self.skills.append(skill)

    def calculate_total(self):
        return sum(skill.score for skill in self.skills)

    def calculate_percentage(self):
        if not self.skills:
            return 0

        total = self.calculate_total()
        maximum = len(self.skills) * 10

        return (total / maximum) * 100

    def find_strongest_skill(self):
        if not self.skills:
            return None

        return max(self.skills, key=lambda skill: skill.score)

    def find_weakest_skill(self):
        if not self.skills:
            return None

        return min(self.skills, key=lambda skill: skill.score)

    def get_performance_level(self):
        percentage = self.calculate_percentage()

        if percentage >= 80:
            return "Excellent"
        elif percentage >= 60:
            return "Good"
        elif percentage >= 40:
            return "Average"
        else:
            return "Needs Improvement"

    def display_assessment(self):
        print("\n" + "=" * 50)
        print("             ASSESSMENT RESULT")
        print("=" * 50)

        for skill in self.skills:
            print(f"{skill.skill_name:<20}: {skill.score}/10")

        print("-" * 50)
        print(f"Total Marks       : {self.calculate_total()}/40")
        print(f"Percentage        : {self.calculate_percentage():.2f}%")
        print(f"Performance       : {self.get_performance_level()}")

        strongest = self.find_strongest_skill()
        weakest = self.find_weakest_skill()

        if strongest:
            print(f"Strongest Skill   : {strongest.skill_name}")

        if weakest:
            print(f"Skill to Improve  : {weakest.skill_name}")

        print("=" * 50)