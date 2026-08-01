"""
Problem: First Non-Vowel Character

Difficulty: Easy

Problem Statement:
Given a string s, print the first character that is NOT a vowel.
If every character is a vowel, print "Not Found".

Example 1:
Input:
apple

Output:
p

Example 2:
Input:
aeiou

Output:
Not Found

Concepts Used:
- Direct Traversal
- if statement
- String Membership (in)

Pattern:
- Search Pattern

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

s = input()

# Write your code here


for ch in s:

    if ch not in "aeiouAEIOU":
        
        print(ch)
        break
