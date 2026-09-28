import unittest

from assessment import Assessment


class TestAssessment(unittest.TestCase):

    def setUp(self):
        self.assessment = Assessment("TEST001")

        self.assessment.add_skill("Programming", 8)
        self.assessment.add_skill("Communication", 7)
        self.assessment.add_skill("Problem Solving", 9)
        self.assessment.add_skill("Technical/Subject", 8)

    def test_total_marks(self):
        self.assertEqual(
            self.assessment.calculate_total(),
            32
        )

    def test_percentage(self):
        self.assertEqual(
            self.assessment.calculate_percentage(),
            80.0
        )

    def test_strongest_skill(self):
        strongest = self.assessment.find_strongest_skill()

        self.assertEqual(
            strongest.skill_name,
            "Problem Solving"
        )

    def test_weakest_skill(self):
        weakest = self.assessment.find_weakest_skill()

        self.assertEqual(
            weakest.skill_name,
            "Communication"
        )

    def test_performance_level(self):
        self.assertEqual(
            self.assessment.get_performance_level(),
            "Excellent"
        )


if __name__ == "__main__":
    unittest.main()