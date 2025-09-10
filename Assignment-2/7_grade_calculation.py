"""
Question 7. Grade Calculation
Write a program that takes marks as input and prints: 
- 'Pass' if marks are 40 or above 
- 'Fail' if marks are less than 40
"""

def grade_calculation(marks):
    #Pass if marks are greater than or equal to 40 otherwise fail
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

# Take input and check for two examples
marks = float(input(f"Enter marks for student #1: "))
print(grade_calculation(marks))

marks = float(input(f"Enter marks for student #2: "))
print(grade_calculation(marks))
