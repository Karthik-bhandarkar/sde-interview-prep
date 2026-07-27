"""
Problem No   : 18
Topic        : While Loop
Pattern      : Number Manipulation
Difficulty   : Easy
Concepts Used: While Loop, %, //, Reverse Number
Objective    : Check whether a number is a palindrome.
Author       : Karthik Bhandarkar
"""
# Take input from the user
num = int(input("Enter the number: "))

# Save the original number because 'num' will change
original = num

# Variable to store the reversed number
reverse = 0

# Reverse the number
while num > 0:

    # Get the last digit
    digit = num % 10

    # Build the reversed number
    reverse = reverse * 10 + digit

    # Remove the last digit
    num = num // 10

# Compare the original number with the reversed number
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")