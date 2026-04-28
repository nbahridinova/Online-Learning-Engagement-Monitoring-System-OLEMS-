"""
This is analyzer module for the system
It stores and analyzes a class list of StudentRecord object
Loads student's data from CSV file and creates StudentRecord objects
Calculates and returns the average engagement score and returns the student with highest engagement score
Counts how many students are in each in category
"""
import pandas as pd
import matplotlib.pyplot as plt

from student import StudentRecord
from utils import validate_columns, clean_numeric_data, calculate_summary


class ClassAnalyzer:

    def __init__(self):
        self.students = []

    def load_csv(self, filename):
        try:
            data = pd.read_csv(filename)
        except FileNotFoundError:
            print("Error: CSV file not found")
            return False

        required_columns = [
            "student_id",
            "name",
            "login_count",
            "video_minutes",
            "assignments_completed",
            "quiz_average"
        ]

        numeric_columns = [
            "student_id",
            "login_count",
            "video_minutes",
            "assignments_completed",
            "quiz_average"
        ]

        validate_columns(data, required_columns)
        data = clean_numeric_data(data, numeric_columns)

        for index, row in data.iterrows():
            student = StudentRecord(
                row["student_id"],
                row["name"],
                row["login_count"],
                row["video_minutes"],
                row["assignments_completed"],
                row["quiz_average"]
            )

            student.calculate_score()
            student.assign_category()
            self.students.append(student)

        return True

    def average_score(self):
        scores = [student.engagement_score for student in self.students]
        summary = calculate_summary(scores)
        return summary["average"]

    def highest_student(self):
        if len(self.students) == 0:
            return None

        highest = self.students[0]

        for student in self.students:
            if student.engagement_score > highest.engagement_score:
                highest = student

        return highest

    def category_counts(self):
        counts = {
            "High": 0,
            "Medium": 0,
            "Low": 0
        }

        for student in self.students:
            counts[student.category] = counts[student.category] + 1

        return counts

    def low_engagement_students(self):
        low_students = [ ]

        for student in self.students:
            if student.category == "Low":
                low_students.append(student)

        return low_students

    def display_students(self):
        for number, student in enumerate(self.students, start=1):
            print(number, student)

    def plot_scores(self):
        names = [student.name for student in self.students]
        scores = [student.engagement_score for student in self.students]

        plt.figure(figsize=(10, 5))
        plt.bar(names, scores)
        plt.xlabel("Student Name")
        plt.ylabel("Engagement Score")
        plt.title("Student Engagement Scores")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def __len__(self):
        return len(self.students)
