"""
------------------------------------------------------------
Problem No : 07
Topic      : Operators
Problem    : Discount
Difficulty : Easy

Question:
Take the price of an item and a discount percentage as input,
then calculate and print the discount amount and the final price.

Example Input:
1000
10

Example Output:
Discount Amount: 100.0
Final Price: 900.0
------------------------------------------------------------
"""

# Solution
price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter discount percentage: "))
discount_amount = (price * discount_percent) / 100
final_price = price - discount_amount
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)
