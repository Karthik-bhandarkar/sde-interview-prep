"""
===============================================================================
               GeeksforGeeks - If Conditional Statement
===============================================================================

Problem Statement:

You are familiar with the basics of input/output and conditional statements in
Python.

There are two friends, John and Smith, represented by the boolean values:
- j_angry
- s_angry

Return True if:
- Both John and Smith are angry, or
- Neither John nor Smith is angry.

Otherwise, return False.

Example 1:
Input:
j_angry = True
s_angry = True

Output:
True

Example 2:
Input:
j_angry = True
s_angry = False

Output:
False

===============================================================================
"""

class Solution:
    def friends_in_trouble(self, j_angry, s_angry):
        if (j_angry and s_angry) or (not j_angry and not s_angry):
            return True
        else:
            return False