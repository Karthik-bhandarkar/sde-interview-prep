"""
------------------------------------------------------------
Problem No : 10
Topic      : Strings
Problem    : Replace Word
Difficulty : Easy

Question:
Take a sentence as input along with a word to replace and its
replacement, then print the updated sentence.

Example Input:
I love Java
Java
Python

Example Output:
Updated sentence: I love Python
------------------------------------------------------------
"""

# Solution
sentence = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
updated_sentence = sentence.replace(old_word, new_word)
print("Updated sentence:", updated_sentence)
