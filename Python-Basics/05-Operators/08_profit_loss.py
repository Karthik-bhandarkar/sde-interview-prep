"""
------------------------------------------------------------
Problem No : 08
Topic      : Operators
Problem    : Profit / Loss
Difficulty : Easy

Question:
Take the cost price and selling price of an item as input and
calculate the profit or loss amount using operators only
(positive = profit, negative = loss).

Example Input:
500
650

Example Output:
Profit/Loss amount: 150.0
(Positive = Profit, Negative = Loss)
------------------------------------------------------------
"""

# Solution
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))
difference = selling_price - cost_price
print("Profit/Loss amount:", difference)
print("(Positive = Profit, Negative = Loss)")
