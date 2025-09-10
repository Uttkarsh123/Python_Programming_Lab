"""
Question 8. Multiple of 5
Write a program to check whether a given number is a multiple of 5.
"""

def check_multiple_five(num):
    if(num%5==0):
        print(f"{num} is a multiple of 5")
    else:
        print(f"{num} is not a multiple of 5")

num1 = int(input("Enter a number"))
check_multiple_five(num1)

num2 = int(input("\nEnter a number"))
check_multiple_five(num2)