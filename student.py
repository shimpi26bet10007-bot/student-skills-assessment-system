class Student:
    def __init__(self, student_id, name, email, course):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.course = course

    def display_student(self):
        print("\n---------- STUDENT DETAILS ----------")
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Email      : {self.email}")
        print(f"Course     : {self.course}")
        print("-------------------------------------")

    def update_student(self, name=None, email=None, course=None):
        if name:
            self.name = name

        if email:
            self.email = email

        if course:
            self.course = course

    def get_student_data(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "course": self.course
        }