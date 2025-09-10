"""
Question 1 Positive or Negative
Write a program to check whether a given number is positive, negative, or zero
"""

def check_positive_negative(num):
    if num>0:
         print("Entered Number is Positive")
    elif num<0:
         print("Entered Number is Negative")
    else:
        print("Entered Number is Zero")

number1 = int(input("Enter a number:"))
check_positive_negative(number1)

number2 = int(input("Enter a number:"))
check_positive_negative(number2)
