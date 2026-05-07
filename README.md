# Online-Learning-Engagement-Monitoring-System-OLEMS-
## Project Overview
The Online Learning Engagement Monitoring System (OLEMS) is a Python-based data analyzer program designed for monitoring and evaluating student engagement in an online learning platform, like Canvas. Functionally speaking, the system will read student activity data from a csv file and calculate engagement scores using different academicy activity indicators, such as quiz averages, assignment completion, etc.
 
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
