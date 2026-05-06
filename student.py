"""This class shows one student and stores their online activity data
    Every StudentRecord object will keep track of the students ID, Name, # of logins, video minutes  that was watched, assigments completed, average of quizes, engagement score and engagement category level
"""
class StudentRecord:  #this class stores info for student and calculates the engagemnet level based on activity   
    def __init__(self, student_id, name, login_count, video_minutes, assignments_completed, quiz_average):                        #this code initializes StudentRecord with student's activity info
        self.student_id = int(student_id)  #converts student ID to integer
        self.name = name    #students name will be stored as text
        self.login_count = int(login_count)    #converts login count to integer
        self.assignments_completed = int(assignments_completed)  #converts # of assignments done to integer
        self.video_minutes = float(video_minutes)   #converts the minutes to float since they have decimals 
        self.quiz_average = float(quiz_average)   #converts the quiz average to float as well since grades can have decimals 
        self.engagement_score = 0   #will begin the score at 0 & will calc. later
        self.category = "Not assigned yet" #begins with actegory of not assigned yet & get updated later
    
    def calculate_score(self): 
        """This code calculates and returns the weighted engagement score
        each login is given worth of 2 points
        each video min worth 0.10 points
        each completed assignment is worth 10 points
        and lastly the quiz average will be multiplied by 0.50
        and finally will return the engagement score rounded to 2 decimal places
        """
        self.engagement_score = (
            self.login_count * 2  
            + self.video_minutes * 0.10
            + self.assignments_completed * 10
            + self.quiz_average * 0.50
        )
        return round(self.engagement_score, 2)

    def assign_category(self):           
        """This code assigns the students to the levels of their engagement category
        there is three categories- High - 120 or higher , Medium - 80 to 119.99 , Low - below 80
        lastly it will return the students' engagement catgory in text format
        """
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