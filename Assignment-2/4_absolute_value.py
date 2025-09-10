"""
Question 4. Absolute Value
Write a program to find the absolute value of a given number without using the abs() 
function.
"""

def absolute_value(num):
    #Checking if the number is smaller than zero (negative) then we return the negative of it
    if num < 0:
        return -num
    #if number is positive then we retrun it as it is
    else:
        return num

print("Example 1")
number1 = int(input("Enter a number: "))
print("Absolute value:", absolute_value(number1))

print("\nExample 2")
number2 = int(input("Enter another number: "))
print("Absolute value:", absolute_value(number2))
