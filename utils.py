"""Utility functions module contains helper functions that validate and clean student engagement data
"""
def validate_columns(dataframe, required_columns):
    missing_columns = [ ]

    for column in required_columns:
        if column not in dataframe.columns:
            missing_columns.append(column)

    if len(missing_columns) > 0:
        raise ValueError(f"Missing required columns: {missing_columns}")

    return True

def clean_numeric_data(dataframe, numeric_columns):
    for column in numeric_columns:
        dataframe[column] = dataframe[column].fillna(0)
        dataframe[column] = dataframe[column].astype(float)

    return dataframe


def calculate_summary(scores):
    if len(scores) == 0:
        raise ValueError("Score list cannot be empty.")

    total = 0

    for score in scores:
        total = total + score

    average = total / len(scores)

    summary = {
        "minimum": min(scores),
        "maximum": max(scores),
        "average": round(average, 2)
    }

    return summary