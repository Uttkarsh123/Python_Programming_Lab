"""
Question 3. Largest of Two Numbers
Write a program to input two numbers and print which one is larger.
"""

# Function to find the largest of two numbers
def find_largest(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal"

print("Example 1")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result1 = find_largest(a, b)
print("Larger Number:", result1)

print("\nExample 2")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
result2 = find_largest(x, y)
print("Larger Number:", result2)