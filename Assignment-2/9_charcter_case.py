"""
Question 9. Character Case Check
Write a program to input a character and check whether it is an uppercase letter, 
lowercase letter, or not a letter.
"""

def check_charcter_case(ch):
    if ch.isalpha():
        if ch.isupper():
            result ="Uppercase"
        else :
            result = "Lowercase"
    else:
        result=" Not a Character"

    return result

ch1 = input("Enter a Character")
print(f"{ch1} is in : {check_charcter_case(ch1)}")

ch2 = input("\nEnter a Character")
print(f"{ch1} is in : {check_charcter_case(ch2)}")

ch3 = input("\nEnter a Character")
print(f"{ch1} is in : {check_charcter_case(ch3)}")