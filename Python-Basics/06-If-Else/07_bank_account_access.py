"""
------------------------------------------------------------
Problem No : 07

Topic : Nested If

Problem : Bank Account Access

Difficulty : Easy ⭐⭐⭐

Concepts Used :
- input()
- if
- Nested if

Objective :
Allow a user to access their bank account only if all
conditions are satisfied.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

card = input("Do you have an ATM card? (yes/no):").lower()

if card == "yes":
    atm_pin = int(input("Enter the PIN"))
    if atm_pin == 1234:
       print ("Access Granted. \n Welcome to your bank account.")
    else:
       print("Incorrect PIN.")
else:
    print("Access Denied.")