"""
------------------------------------------------------------
Problem No : 05
Topic      : Strings
Problem    : String Methods
Difficulty : Easy

Question:
Take a string and demonstrate the use of upper(), lower(),
strip(), and replace() methods on it.

Example Output:
Uppercase:   HELLO PYTHON WORLD  
Lowercase:   hello python world  
Stripped: Hello Python World
Replaced:   Hello Python Learner  
------------------------------------------------------------
"""

# Solution
text = "  Hello Python World  "
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Stripped:", text.strip())
print("Replaced:", text.replace("World", "Learner"))
