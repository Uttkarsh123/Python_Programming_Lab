"""
Question 5. Eligibility for Voting
Write a program to check whether a person is eligible to vote or not. (A person is 
eligible if their age is 18 or above). 
"""

def check_voting_eligibility(age):
    if age >=18:
        return "Eligible to vote"
    else:
        return "Not Eligible to vote"

age1 = int(input("Enter your age:"))
print(check_voting_eligibility(age1))

age2 = int(input("Enter your age:"))
print(check_voting_eligibility(age2))
    