"""This class represents one student and stores their online activity data
"""
class StudentRecord:
    def __init__(self, student_id, name, login_count, video_minutes, assignments_completed, quiz_average):                        #this code initializes StudentRecord with student's activity info
        self.student_id = int(student_id)
        self.name = name
        self.login_count = int(login_count)
        self.assignments_completed = int(assignments_completed)
        self.video_minutes = float(video_minutes)
        self.quiz_average = float(quiz_average)
        self.engagement_score = 0
        self.category = "Not assigned yet"
    
    def calculate_score(self):         # this code calculates and returns the weighted engagement score
        self.engagement_score = (
            self.login_count * 2
            + self.video_minutes * 0.10
            + self.assignments_completed * 10
            + self.quiz_average * 0.50
        )
        return round(self.engagement_score, 2)

    def assign_category(self):           #this code assigns the students to the levels of engagement
        if self.engagement_score >= 120:
            self.category = "High"
        elif self.engagement_score >= 80:
            self.category = "Medium"
        else:
            self.category = "Low"
        return self.category

    def __str__(self):                     #returns a readable string for student object
        return f"{self.name}: Score = {self.engagement_score}, Category = {self.category}"

    def __len__(self):                  #returns the number of main egagement fields tracked
        return 4 