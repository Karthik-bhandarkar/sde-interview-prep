"""
------------------------------------------------------------
Problem No : 09
Topic      : Strings
Problem    : Find Character
Difficulty : Easy

Question:
Take a string and a character as input, then find the index at
which the character first appears using find().

Example Input:
Python
t

Example Output:
Character found at index: 2
------------------------------------------------------------
"""

# Solution
text = input("Enter a string: ")
char = input("Enter a character to search: ")
position = text.find(char)
print("Character found at index:", position)
