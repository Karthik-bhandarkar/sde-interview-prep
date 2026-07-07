"""
------------------------------------------------------------
Problem No : 09
Topic      : Input & Type Conversion
Problem    : Currency Converter
Difficulty : Easy

Question:
Take an amount in US Dollars as input and convert it to Indian
Rupees using a fixed rate of 1 USD = 83.0 INR.

Example Input:
10

Example Output:
Amount in INR: 830.0
------------------------------------------------------------
"""

# Solution
usd = float(input("Enter amount in USD: "))
conversion_rate = 83.0
inr = usd * conversion_rate
print("Amount in INR:", round(inr, 2))
