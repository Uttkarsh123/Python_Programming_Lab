"""
Question 10. Discount Calculator
Write a program that calculates the discount:
- If purchase amount is greater than or equal to 1000, apply a 10% discount.
- Otherwise, no discount.
Finally, print the final bill amount
"""

def discount_calculator(purchase_amnt):
    if purchase_amnt >1000:
        return 0.1*purchase_amnt
    else:
        return 0.0

amount = float(input("Enter the Purchase Amount:"))
discount = discount_calculator(amount)

print(format(" BILL ","*^30"))
print("Purchase Amount :", amount)
print("Discount :",discount)
print("Total Amount:", amount-discount)