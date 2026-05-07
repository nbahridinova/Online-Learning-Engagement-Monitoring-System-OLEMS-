# Online-Learning-Engagement-Monitoring-System-OLEMS-
## Project Overview
The Online Learning Engagement Monitoring System (OLEMS) is a Python-based data analyzer program designed for monitoring and evaluating student engagement in an online learning platform, like Canvas. Functionally speaking, the system will read student activity data from a csv file and calculate engagement scores using different academic activity indicators, such as quiz averages, assignment completion, etc.
 
The program was developed using concepts learned throughout the course, including object-oriented programming (OOP), data analysis, exception handling, testing, and modular programming
 
---
 
## Features
- Load student engagement data from a CSV file
- Create StudentRecord objects for each student in the CSV
- Calculate engagement scores
- Categorize students into engagement levels
- Calculate average engagement scores
- Identify the student with the highest engagement score
- Display low engagement students
- Generate engagement score visualization plot
- Perform automated pytest testing

---
 
# Technologies Used
 
- Python 3.13
 - Jupyter Notebook
 - pandas
 - matplotlib
 - pytest
 - math module
 
---

## Project Structure
```text
Online-Learning-Engagement-Monitoring-System-OLEMS-/
│── main.ipynb
│── student.py
│── analyzer.py
│── utils.py
│── README.md
│
├── data/
│   └── students.csv
│
└── tests/
    └── test_project.py
```

--- 

## Module Descriptions
### main.ipynb
Main Jupyter Notebook used to run the project.
 
### student.py
Contains the StudentRecord class, which stores student activity data and calculates each student's engagement score and category.
 
### analyzer.py
Contains the ClassAnalyzer class, which loads data, stores StudentRecord objects, analyzes engagement results, and creates graphs.
 
### utils.py
Contains helper functions for validating columns, cleaning numeric data, and calculating summary statistics.
 
### data/students.csv
Dataset containing student engagement information.
 
### tests/test_project.py
Pytest file used to test scoring, categorization, analyzer logic, and invalid data handling.
 
### README.md
Documentation file explaining the project, structure, setup, and team contributions.
 
---

# Installation and Setup
 
## Clone the Repository
```bash
 git clone https://github.com/nbahridinova/Online-Learning-Engagement-Monitoring-System-OLEMS-.git
```

 
## Navigate Into the Project Directory
```bash
 cd Online-Learning-Engagement-Monitoring-System-OLEMS-
```

 
## Launch Jupyter Notebook
```bash
 jupyter notebook
```

Open:
```text
  main.ipynb
```
 
---
 
# Running the Project
 
Run all cells in `main.ipynb` from top to bottom.
 
This notebook will:
 - Load the CSV dataset
 - Create StudentRecord objects
 - Calculate engagement scores
 - Categorize students
 - Display analytics
 - Generate visualizations
 
---
 
# Running Tests

Run the following command in Terminal:

```bash
PYTHONPATH=. pytest
```
 
Expected output:
```text
5 passed
```
---


# Team Members

| Name | Email | Stevens ID |
|------|------|------|
| Sebastian Castano | scastan2@stevens.edu | 20007319 |
| Nozanin Bahridinova | nbahridi@stevens.edu | 10468113 |
| Clarkston Stith | cstith@stevens.edu | 20045914 |

---
 
# Team Contributions
## Nozanin Bahridinova
- Created the main Jupyter Notebook workflow
- Developed the StudentRecord class
- Created the dataset
- Added notebook visualizations
- Managed GitHub integration and execution flow
- Added README project documentation and structure

 
## Sebastian Castano
- Developed pytest test cases
- Improved the testing effectiveness
- Added exceptions to testing
- Added setup and test documentation
- Added README project documentation and structure

 
## Clarkston Stith
- Developed the ClassAnalyzer module
- Added the exception handling with utility validation
- Enhanced the helper functions & calculations
- Added README project documentation and project structure

---

# Satisfied Requirements

## Part 1 Requirements
- Two meaningful classes with composition relationship
- Multiple modules & functions
- Matplotlib and pandas usage
- Exception handling scenarios
- Input/Output CSV file
- Loops & condition statements
- Mutable & immutable type of data
- Overloading operator with “__str__()” and “__len__()”
- Pytest test
- Docstrings & meaningful comments
 

## Part 2 Requirements
- Enumerate
- List comprehensions
- Built-in math module
- generator expression
