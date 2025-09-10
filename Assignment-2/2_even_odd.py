"""
Question 2 Even or Odd
Write a program to check whether a given integer is even or odd. 
"""

def even_odd(num):
    if(num%2==0):
        print(f"{num} is Even")
    else:
         print(f"{num} is Odd")

number1 = int(input("Enter a number:"))
even_odd(number1)

number2 = int(input("Enter a number:"))
even_odd(number2)