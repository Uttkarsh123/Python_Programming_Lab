"""
Question 6. Leap Year Check
Write a program to check whether a given year is a leap year or not. (Hint: A leap year is 
divisible by 4, but not by 100 unless also divisible by 400)
"""

def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400 -> leap year
            else:
                return False  # Divisible by 100 but not 400 -> not leap year
        else:
            return True  # Divisible by 4 but not by 100 -> leap year
    else:
        return False 

year1 = int(input("Enter first year: "))
print(f"{year1} is a leap year: {check_leap_year(year1)}")

year2 = int(input("\nEnter second year: "))
print(f"{year2} is a leap year: {check_leap_year(year2)}")

        