class Skill:
    def __init__(self, skill_name, score):
        self.skill_name = skill_name
        self.score = score

    def display_skill(self):
        print(f"{self.skill_name:<20} : {self.score}/100")

    def get_skill_data(self):
        return {
            "skill_name": self.skill_name,
            "score": self.score
        }

