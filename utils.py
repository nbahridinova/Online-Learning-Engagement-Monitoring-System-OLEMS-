"""
Utility functions module contains helper functions that validate and clean student engagement data
"""
def validate_columns(dataframe, required_columns):
    # Create an empty list to store any required columns that are not found
    # in the dataframe.
    missing_columns = [ ]

    # Check each required column name against the dataframe's existing columns.
    for column in required_columns:
        if column not in dataframe.columns:
            # If a required column is missing, add it to the missing_columns list
            # so all missing columns can be reported together.
            missing_columns.append(column)

    # If one or more required columns are missing, stop the program and show
    # which columns need to be fixed before continuing.
    if len(missing_columns) > 0:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Return True only when all required columns are present in the dataframe.
    return True

def clean_numeric_data(dataframe, numeric_columns):
    """
    This function will convert numeric columns to numbers and fill missing values with 0
    
    Parameters:
        dataframe: any pandas dataframe to be cleaned
        numeric_columns: a list of columns expected to contain numberic data
    """
    # Loop through each column that is expected to contain numeric data.
    for column in numeric_columns:
        # Replace missing values with 0 so calculations will not fail because
        # of blank or NaN values.
        # Convert the column values to floats so mathematical operations can
        # be performed consistently.
        # We wrap this in a try/except to ensure the value becomes  afloat
        try:
            dataframe[column] = dataframe[column].fillna(0)
            dataframe[column] = dataframe[column].astype(float)
        except ValueError:
            raise ValueError(f"Wrong numeric data found in the column: {column}")

    # Return the cleaned dataframe so it can be used later in the program.
    return dataframe


def calculate_summary(scores):
    # Do not allow an empty list because min, max, and avg values
    # cannot be calculated without at least one score.
    if len(scores) == 0:
        raise ValueError("Score list cannot be empty.")

    # Start the total at 0 before adding each score.
    total = 0

    # Add each score to the running total.
    for score in scores:
        total = total + score

    # Calculate the average by dividing the total score by the number of scores.
    average = total / len(scores)

    # Store the main summary statistics in a dictionary so the results
    # are clearly labeled and easy to access later.
    summary = {
        "minimum": min(scores),
        "maximum": max(scores),
        "average": round(average, 2)
    }

    # Return the summary dictionary containing the min, max, and avg.
    return summary
