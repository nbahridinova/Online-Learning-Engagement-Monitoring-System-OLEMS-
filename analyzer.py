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
    """
    This class contains methods for analyzing a collection of StudentRecord objects
    """
    def __init__(self):
        """
        This function is needed to initialze a ClassAnalyzer object when it's created
        """
        self.students = []

    def load_csv(self, filename):
        """
        This function loads student data from a csv file to populate StudentRecord objects
        Parameters:
            filename: A string containing the path to the csv file
        Returns:
            True if loading succeeds
            False if file not found exception is thrown
        """
        try:
            data = pd.read_csv(filename)
        except FileNotFoundError:
            print("Error: CSV file not found")
            return False

        # These are the required columns that must exist in the csv
        required_columns = [
            "student_id",
            "name",
            "login_count",
            "video_minutes",
            "assignments_completed",
            "quiz_average"
        ]

        # These are the columns expected to contain numeric data in the csv
        numeric_columns = [
            "student_id",
            "login_count",
            "video_minutes",
            "assignments_completed",
            "quiz_average"
        ]

        # We must validate and clean the data before we create StudentRecord objects
        validate_columns(data, required_columns)
        data = clean_numeric_data(data, numeric_columns)

        # We can convert each row into a StudentRecord object using a for loop
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
        """
        This function calculates the average engagement score acorss all students
        Returns:
            The average engagement score (float)
        """
        # Here we extract all of the engagement scores
        scores = list(student.engagement_score for student in self.students)

        summary = calculate_summary(scores)
        return summary["average"]

    def highest_student(self):
        """
        This function finds the student with the highest engagement score
        Returns:
            StudentRecord with the highest score
            None if there are no students
        """
        # We must first check that we have a sufficient number of students
        if len(self.students) == 0:
            return None

        highest = self.students[0]
        for student in self.students:
            if student.engagement_score > highest.engagement_score:
                highest = student

        return highest

    def category_counts(self):
        """
        This function counts how many students fall into each engagement category
        "High", "Medium", or "Low"
        Returns:
            A dictionary of each category with a number of corresponding students
        """
        counts = {
            "High": 0,
            "Medium": 0,
            "Low": 0
        }

        for student in self.students:
            counts[student.category] = counts[student.category] + 1

        return counts

    def low_engagement_students(self):
        """
        This function retrieves all students categorized as low engagement
        Returns:
            A list of low engagement scoring students
        """
        low_students = [ ]

        for student in self.students:
            if student.category == "Low":
                low_students.append(student)

        return low_students

    def display_students(self):
        """
        This function prints all students with their index in the list
        """
        for number, student in enumerate(self.students, start=1):
            print(number, student)

    def plot_scores(self):
        """
        This function creates a bar chart of student engagement scores
        """
        # This is the x-axis of the plot
        names = [student.name for student in self.students]
        # This is the y-axis of the plot
        scores = [student.engagement_score for student in self.students]

        # These lines will create the bar chart and show it 
        plt.figure(figsize=(10, 5))
        plt.bar(names, scores)
        plt.xlabel("Student Name")
        plt.ylabel("Engagement Score")
        plt.title("Student Engagement Scores")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def __len__(self):
        """
        This function returns the number of current StudentRecord objects in ClassAnalyzer
        Returns:
            Number of StudentRecord objects
        """
        return len(self.students)
