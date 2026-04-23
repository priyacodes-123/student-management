class StudentManager:
    def __init__(self, filename="data.txt"):
        self.filename = filename

    def add_student(self, name, attendance, marks):
        with open(self.filename, "a") as f:
            f.write(f"{name},{attendance},{marks}\n")

    def get_students(self):
        students = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    name, attendance, marks = line.strip().split(",")
                    students.append((name, float(attendance), float(marks)))
        except FileNotFoundError:
            pass
        return students

    def calculate_grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "Fail"

    def low_attendance(self):
        return [s for s in self.get_students() if s[1] < 75]