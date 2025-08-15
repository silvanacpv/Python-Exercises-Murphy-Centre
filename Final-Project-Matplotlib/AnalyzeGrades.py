#Project Two
#Analyze Students Grades
#By:   Silvana Paredes
#Date: 22/02/2025

import pandas as pd

#Read the CSV file
df = pd.read_csv("Grades_Short.csv", sep=",")

#Calculate the final score
df["Final_score"] = df.iloc[:, 2:8].mean(axis=1).round(2)

#Determine the letter grade
def determine_grade(score):
    if score > 90:
        return "A+"
    elif score > 80:
        return "A"
    elif score > 70:
        return "B"
    elif score > 60:
        return "C"
    elif score > 55:
        return "D"
    else:
        return "F"

df["Letter_grade"] = df["Final_score"].apply(determine_grade)

#Generate a new CSV file with the calculated values 
df.to_csv("Grades_Short_new.csv", index=False)



    
  










