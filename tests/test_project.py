import pandas as pd
import pytest

from student import StudentRecord
from analyzer import ClassAnalyzer
from utils import clean_numeric_data


def test_calculated_score():
    """
    Test that engagement score is calculated correctly
    """

    # Create a sample student record using fixed test values
    # These values are used so the expected engagement score can be checked
    student = StudentRecord(1, "Testing the student", 10, 100, 5, 80)

    # Call the calculate_score method to calculate the student's engagement score
    score = student.calculate_score()

    # Check that the calculated score matches the expected result
    # If the score is not 120.0, this test will fail
    assert score == 120.0


def test_category_high():
    """
    Test that a high score is assigned to the appropriate High category
    """

    # Create a sample student record with values that should produce a high score
    student = StudentRecord(1, "Test the student", 10, 100, 5, 80)

    # Calculate the score first because the category depends on the student's score
    student.calculate_score()

    # Assign a category based on the calculated engagement score
    category = student.assign_category()

    # Check that the student's category is classified as High
    assert category == "High"


def test_category_counts():
    """
    Test that category counts return a dictionary with all expected categories
    """

    # Create a ClassAnalyzer object to load and analyze the class data
    system = ClassAnalyzer()

    # Load the student data from the CSV file before calculating category counts
    system.load_csv("data/students.csv")

    # Count how many students fall into each engagement category
    counts = system.category_counts()

    # Check that the results include all three expected category labels
    # These checks help confirm that the dictionary has the required keys
    assert "High" in counts
    assert "Medium" in counts
    assert "Low" in counts


def test_average_score():
    """
    Test that average score is greater than zero after loading data
    """

    # Create a ClassAnalyzer object to work with the student data file
    system = ClassAnalyzer()

    # Load the CSV file so the analyzer has student records to calculate from
    system.load_csv("data/students.csv")

    # Check that the average engagement score is greater than zero
    # This confirms that the data loaded and the average calculation returned a valid value
    assert system.average_score() > 0

def test_the_invalid_numeric_data():
    """
    Test that in the event there is invalid numeric data, it raises a ValueError
    """
    # Create a sample DataFrame with text in a column that should be numeric
    data = pd.DataFrame({
        "login_count": ["wrong_data"]
    })

    # Check that clean_numeric_data raises a ValueError for invalid numeric input
    with pytest.raises(ValueError):    
        clean_numeric_data(data, ["login_count"])