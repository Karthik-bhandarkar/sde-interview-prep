# ANTIGRAVITY BUILD INSTRUCTIONS — PASTE THIS ENTIRE FILE AS THE PROMPT

## GOAL (fixed — do not change)
Create a local VS Code Python practice workspace covering exactly five topics, in this order: **Print Statements → Variables → Input & Type Conversion → Strings → Operators**. Each problem file must show the **question first (in a docstring), then the solution code below it**, LeetCode-style. This workspace will later be pushed to GitHub as a visible, chronological learning portfolio for recruiters. Do **not** invent new questions, do **not** change any code, do **not** add functions/loops/if-else (not learned yet), and do **not** create any folder beyond `05-Operators`. The user will add `06-If-Else` and everything after it manually as they practice it themselves starting today.

## INSTRUCTIONS FOR THE AGENT
1. Create the folder structure exactly as shown below.
2. Create every file listed with the **exact content** given in this document — copy it verbatim, don't regenerate it.
3. Do not add comments, functions, loops, or conditionals beyond what's already in the code.
4. Do not create a `06-If-Else` folder or any topic after Operators.
5. After creation, do nothing else (no git init, no push — user will do that manually).

---

## FOLDER STRUCTURE

```text
Python-Basics-Portfolio/
├── README.md
├── 01-Print-Statements/
│   ├── README.md
│   ├── 01_hello_world.py
│   ├── 02_print_multiple_lines.py
│   ├── 03_escape_characters.py
│   ├── 04_quotes.py
│   ├── 05_print_shapes.py
│   ├── 06_print_personal_info.py
│   ├── 07_print_formatted_text.py
│   ├── 08_print_special_characters.py
│   ├── 09_print_pattern.py
│   └── 10_mini_profile.py
├── 02-Variables/
│   ├── README.md
│   ├── 01_store_name.py
│   ├── 02_store_age.py
│   ├── 03_multiple_variables.py
│   ├── 04_swap_variables.py
│   ├── 05_update_variable.py
│   ├── 06_student_information.py
│   ├── 07_employee_details.py
│   ├── 08_calculate_birth_year.py
│   ├── 09_simple_interest.py
│   └── 10_area_of_rectangle.py
├── 03-Input-TypeConversion/
│   ├── README.md
│   ├── 01_name_input.py
│   ├── 02_age_input.py
│   ├── 03_birth_year.py
│   ├── 04_bmi_input.py
│   ├── 05_temperature_converter.py
│   ├── 06_add_two_numbers.py
│   ├── 07_area_circle.py
│   ├── 08_simple_interest.py
│   ├── 09_currency_converter.py
│   └── 10_percentage_calculator.py
├── 04-Strings/
│   ├── README.md
│   ├── 01_string_basics.py
│   ├── 02_string_indexing.py
│   ├── 03_string_slicing.py
│   ├── 04_formatted_strings.py
│   ├── 05_string_methods.py
│   ├── 06_full_name.py
│   ├── 07_reverse_name.py
│   ├── 08_count_characters.py
│   ├── 09_find_character.py
│   └── 10_replace_word.py
└── 05-Operators/
    ├── README.md
    ├── 01_addition.py
    ├── 02_arithmetic_operations.py
    ├── 03_operator_precedence.py
    ├── 04_augmented_assignment.py
    ├── 05_math_functions.py
    ├── 06_calculator.py
    ├── 07_discount.py
    ├── 08_profit_loss.py
    ├── 09_percentage.py
    └── 10_power_calculator.py
```

---

## FILE: README.md (root)

```markdown
# Python Basics Portfolio

This repository shows my Python learning journey **in the exact order I learned it** —
starting from `print()` statements and building up topic by topic. Each folder is a topic,
and each file has the question first, then my solution — similar to how problems are
shown on LeetCode.

## Progress

- [x] 01. Print Statements
- [x] 02. Variables
- [x] 03. Input & Type Conversion
- [x] 04. Strings
- [x] 05. Operators
- [ ] 06. If-Else (in progress)
- [ ] 07. Loops
- [ ] 08. Lists / Tuples / Dictionaries
- [ ] 09. Functions
- [ ] 10. OOP

## Why this structure?

Most beginner repositories are just a pile of `test.py` / `practice.py` files with no story.
This one is organized so anyone browsing it — recruiter or otherwise — can follow the exact
order concepts were learned, see steady daily practice, and find any concept quickly for revision.

## Tools used
Practiced and written in **VS Code**, then pushed here to GitHub. Problem-solving practice
(HackerRank / GeeksforGeeks / LeetCode) will be tracked separately once fundamentals are complete.
```

---

## FILE: 01-Print-Statements/README.md

```markdown
# Topic: Print Statements

## Concepts Covered
- print() basics
- Printing multiple lines
- Escape characters (\n, \t, \\)
- Single vs double quotes
- Printing patterns/shapes
- f-strings (intro)

## Problems
01. Hello World
02. Print Multiple Lines
03. Escape Characters
04. Quotes Inside Strings
05. Print Shapes
06. Print Personal Info
07. Print Formatted Text
08. Print Special Characters
09. Print Pattern
10. Mini Profile Card

## Learning Outcome
By completing these problems you should be able to:
- Use print() confidently for single and multiple lines
- Handle escape characters and quotes correctly
- Format simple output using f-strings
```

## FILE: 01-Print-Statements/01_hello_world.py

```python
"""
------------------------------------------------------------
Problem No : 01
Topic      : Print Statements
Problem    : Hello World
Difficulty : Easy

Question:
Print "Hello, World!" to the console.

Example Output:
Hello, World!
------------------------------------------------------------
"""

# Solution
print("Hello, World!")
```

## FILE: 01-Print-Statements/02_print_multiple_lines.py

```python
"""
------------------------------------------------------------
Problem No : 02
Topic      : Print Statements
Problem    : Print Multiple Lines
Difficulty : Easy

Question:
Using a single print() statement, print the following three lines:
I love Python.
I am learning to code.
I will build great projects.

Example Output:
I love Python.
I am learning to code.
I will build great projects.
------------------------------------------------------------
"""

# Solution
print("I love Python.\nI am learning to code.\nI will build great projects.")
```

## FILE: 01-Print-Statements/03_escape_characters.py

```python
"""
------------------------------------------------------------
Problem No : 03
Topic      : Print Statements
Problem    : Escape Characters
Difficulty : Easy

Question:
Print a sentence that demonstrates a tab space (\t), a new line (\n),
and a backslash (\\) all in one print() statement.

Example Output:
Name:	Karthik
Path:	C:\Users\Karthik
------------------------------------------------------------
"""

# Solution
print("Name:\tKarthik\nPath:\tC:\\Users\\Karthik")
```

## FILE: 01-Print-Statements/04_quotes.py

```python
"""
------------------------------------------------------------
Problem No : 04
Topic      : Print Statements
Problem    : Quotes Inside Strings
Difficulty : Easy

Question:
Print a sentence containing both single and double quotes, e.g.:
He said, "Python's syntax is clean."

Example Output:
He said, "Python's syntax is clean."
------------------------------------------------------------
"""

# Solution
print('He said, "Python\'s syntax is clean."')
```

## FILE: 01-Print-Statements/05_print_shapes.py

```python
"""
------------------------------------------------------------
Problem No : 05
Topic      : Print Statements
Problem    : Print Shapes
Difficulty : Easy

Question:
Print a right-angled triangle made of stars, 5 rows tall,
using separate print() statements (no loops yet).

Example Output:
*
**
***
****
*****
------------------------------------------------------------
"""

# Solution
print("*")
print("**")
print("***")
print("****")
print("*****")
```

## FILE: 01-Print-Statements/06_print_personal_info.py

```python
"""
------------------------------------------------------------
Problem No : 06
Topic      : Print Statements
Problem    : Print Personal Info
Difficulty : Easy

Question:
Print your name, age, city, and hobby using separate print() statements.

Example Output:
Name: Karthik Bhandarkar
Age: 21
City: Bengaluru
Hobby: Coding
------------------------------------------------------------
"""

# Solution
print("Name: Karthik Bhandarkar")
print("Age: 21")
print("City: Bengaluru")
print("Hobby: Coding")
```

## FILE: 01-Print-Statements/07_print_formatted_text.py

```python
"""
------------------------------------------------------------
Problem No : 07
Topic      : Print Statements
Problem    : Print Formatted Text
Difficulty : Easy

Question:
Using an f-string, print a sentence that combines a name variable
and an age variable into one message.

Example Output:
My name is Karthik and I am 21 years old.
------------------------------------------------------------
"""

# Solution
name = "Karthik"
age = 21
print(f"My name is {name} and I am {age} years old.")
```

## FILE: 01-Print-Statements/08_print_special_characters.py

```python
"""
------------------------------------------------------------
Problem No : 08
Topic      : Print Statements
Problem    : Print Special Characters
Difficulty : Easy

Question:
Print a line containing the special characters: @ # $ % & *

Example Output:
Special Characters: @ # $ % & *
------------------------------------------------------------
"""

# Solution
print("Special Characters: @ # $ % & *")
```

## FILE: 01-Print-Statements/09_print_pattern.py

```python
"""
------------------------------------------------------------
Problem No : 09
Topic      : Print Statements
Problem    : Print Pattern
Difficulty : Easy

Question:
Print a 5x5 square pattern made of the '#' character
using separate print() statements (no loops yet).

Example Output:
#####
#####
#####
#####
#####
------------------------------------------------------------
"""

# Solution
print("#####")
print("#####")
print("#####")
print("#####")
print("#####")
```

## FILE: 01-Print-Statements/10_mini_profile.py

```python
"""
------------------------------------------------------------
Problem No : 10
Topic      : Print Statements
Problem    : Mini Profile Card
Difficulty : Easy

Question:
Combine everything learned so far to print a small "profile card"
using print() statements and border characters (- and |).

Example Output:
-----------------------------
| Name : Karthik Bhandarkar |
| Role : Python Learner     |
| Goal : Product-Based Job  |
-----------------------------
------------------------------------------------------------
"""

# Solution
print("-----------------------------")
print("| Name : Karthik Bhandarkar |")
print("| Role : Python Learner     |")
print("| Goal : Product-Based Job  |")
print("-----------------------------")
```

---

## FILE: 02-Variables/README.md

```markdown
# Topic: Variables

## Concepts Covered
- Declaring and printing variables
- Multiple variables at once
- Swapping variables
- Updating a variable's value
- Using variables in simple real-world calculations

## Problems
01. Store Name
02. Store Age
03. Multiple Variables
04. Swap Variables
05. Update Variable
06. Student Information
07. Employee Details
08. Calculate Birth Year
09. Simple Interest
10. Area of Rectangle

## Learning Outcome
By completing these problems you should be able to:
- Create, update, and swap variables
- Use variables to solve small real-world numeric problems
```

## FILE: 02-Variables/01_store_name.py

```python
"""
------------------------------------------------------------
Problem No : 01
Topic      : Variables
Problem    : Store Name
Difficulty : Easy

Question:
Store your name in a variable and print it.

Example Output:
Karthik
------------------------------------------------------------
"""

# Solution
name = "Karthik"
print(name)
```

## FILE: 02-Variables/02_store_age.py

```python
"""
------------------------------------------------------------
Problem No : 02
Topic      : Variables
Problem    : Store Age
Difficulty : Easy

Question:
Store your age in a variable and print it along with a message.

Example Output:
My age is: 21
------------------------------------------------------------
"""

# Solution
age = 21
print("My age is:", age)
```

## FILE: 02-Variables/03_multiple_variables.py

```python
"""
------------------------------------------------------------
Problem No : 03
Topic      : Variables
Problem    : Multiple Variables
Difficulty : Easy

Question:
Store your name, age, and city in three variables and print
all of them in a single print() statement.

Example Output:
Karthik 21 Bengaluru
------------------------------------------------------------
"""

# Solution
name = "Karthik"
age = 21
city = "Bengaluru"
print(name, age, city)
```

## FILE: 02-Variables/04_swap_variables.py

```python
"""
------------------------------------------------------------
Problem No : 04
Topic      : Variables
Problem    : Swap Variables
Difficulty : Easy

Question:
Swap the values of two variables a and b WITHOUT using a third
variable, and print both before and after swapping.

Example Output:
Before swap -> a: 5 , b: 10
After swap  -> a: 10 , b: 5
------------------------------------------------------------
"""

# Solution
a = 5
b = 10
print("Before swap -> a:", a, ", b:", b)
a, b = b, a
print("After swap  -> a:", a, ", b:", b)
```

## FILE: 02-Variables/05_update_variable.py

```python
"""
------------------------------------------------------------
Problem No : 05
Topic      : Variables
Problem    : Update Variable
Difficulty : Easy

Question:
Store a variable 'score' with an initial value, then update it
and print the value before and after updating.

Example Output:
Initial score: 50
Updated score: 70
------------------------------------------------------------
"""

# Solution
score = 50
print("Initial score:", score)
score = score + 20
print("Updated score:", score)
```

## FILE: 02-Variables/06_student_information.py

```python
"""
------------------------------------------------------------
Problem No : 06
Topic      : Variables
Problem    : Student Information
Difficulty : Easy

Question:
Store a student's name, roll number, and marks in three variables
and print them in a readable format.

Example Output:
Student Name: Karthik
Roll Number: 21
Marks: 88
------------------------------------------------------------
"""

# Solution
student_name = "Karthik"
roll_number = 21
marks = 88
print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Marks:", marks)
```

## FILE: 02-Variables/07_employee_details.py

```python
"""
------------------------------------------------------------
Problem No : 07
Topic      : Variables
Problem    : Employee Details
Difficulty : Easy

Question:
Store an employee's name, employee ID, and salary in variables,
then print a formatted summary using an f-string.

Example Output:
Employee Karthik (ID: 101) earns Rs.45000 per month.
------------------------------------------------------------
"""

# Solution
emp_name = "Karthik"
emp_id = 101
salary = 45000
print(f"Employee {emp_name} (ID: {emp_id}) earns Rs.{salary} per month.")
```

## FILE: 02-Variables/08_calculate_birth_year.py

```python
"""
------------------------------------------------------------
Problem No : 08
Topic      : Variables
Problem    : Calculate Birth Year
Difficulty : Easy

Question:
Store the current year and your age in variables, calculate your
birth year, and print it.

Example Output:
Your birth year is: 2005
------------------------------------------------------------
"""

# Solution
current_year = 2026
age = 21
birth_year = current_year - age
print("Your birth year is:", birth_year)
```

## FILE: 02-Variables/09_simple_interest.py

```python
"""
------------------------------------------------------------
Problem No : 09
Topic      : Variables
Problem    : Simple Interest
Difficulty : Easy

Question:
Store principal, rate, and time in variables. Calculate simple
interest using the formula (P * R * T) / 100 and print it.

Example Output:
Simple Interest: 1000.0
------------------------------------------------------------
"""

# Solution
principal = 10000
rate = 5
time = 2
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)
```

## FILE: 02-Variables/10_area_of_rectangle.py

```python
"""
------------------------------------------------------------
Problem No : 10
Topic      : Variables
Problem    : Area of Rectangle
Difficulty : Easy

Question:
Store the length and breadth of a rectangle in variables,
calculate its area, and print the result.

Example Output:
Area of Rectangle: 60
------------------------------------------------------------
"""

# Solution
length = 12
breadth = 5
area = length * breadth
print("Area of Rectangle:", area)
```

---

## FILE: 03-Input-TypeConversion/README.md

```markdown
# Topic: Input & Type Conversion

## Concepts Covered
- input() basics
- Converting input using int(), float()
- Combining input with variables and calculations
- Rounding results with round()

## Problems
01. Name Input
02. Age Input
03. Birth Year
04. BMI Input
05. Temperature Converter
06. Add Two Numbers
07. Area of Circle
08. Simple Interest
09. Currency Converter
10. Percentage Calculator

## Learning Outcome
By completing these problems you should be able to:
- Take input from the user and convert it to the correct type
- Use converted input inside real calculations
```

## FILE: 03-Input-TypeConversion/01_name_input.py

```python
"""
------------------------------------------------------------
Problem No : 01
Topic      : Input & Type Conversion
Problem    : Name Input
Difficulty : Easy

Question:
Take the user's name as input and print a greeting using it.

Example Input:
Karthik

Example Output:
Hello, Karthik! Welcome to Python.
------------------------------------------------------------
"""

# Solution
name = input("Enter your name: ")
print("Hello,", name + "! Welcome to Python.")
```

## FILE: 03-Input-TypeConversion/02_age_input.py

```python
"""
------------------------------------------------------------
Problem No : 02
Topic      : Input & Type Conversion
Problem    : Age Input
Difficulty : Easy

Question:
Take the user's age as input (input() always returns a string),
convert it to an integer, and print their age 10 years from now.

Example Input:
21

Example Output:
In 10 years, you will be 31 years old.
------------------------------------------------------------
"""

# Solution
age = int(input("Enter your age: "))
print("In 10 years, you will be", age + 10, "years old.")
```

## FILE: 03-Input-TypeConversion/03_birth_year.py

```python
"""
------------------------------------------------------------
Problem No : 03
Topic      : Input & Type Conversion
Problem    : Birth Year
Difficulty : Easy

Question:
Take the current year and the user's age as input, then
calculate and print the user's birth year.

Example Input:
2026
21

Example Output:
Your birth year is: 2005
------------------------------------------------------------
"""

# Solution
current_year = int(input("Enter the current year: "))
age = int(input("Enter your age: "))
birth_year = current_year - age
print("Your birth year is:", birth_year)
```

## FILE: 03-Input-TypeConversion/04_bmi_input.py

```python
"""
------------------------------------------------------------
Problem No : 04
Topic      : Input & Type Conversion
Problem    : BMI Input
Difficulty : Easy

Question:
Take weight (kg) and height (m) as input and calculate BMI
using the formula: weight / (height ** 2).

Example Input:
70
1.75

Example Output:
Your BMI is: 22.86
------------------------------------------------------------
"""

# Solution
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))
```

## FILE: 03-Input-TypeConversion/05_temperature_converter.py

```python
"""
------------------------------------------------------------
Problem No : 05
Topic      : Input & Type Conversion
Problem    : Temperature Converter
Difficulty : Easy

Question:
Take temperature in Celsius as input and convert it to
Fahrenheit using the formula: (C * 9/5) + 32.

Example Input:
37

Example Output:
Temperature in Fahrenheit: 98.6
------------------------------------------------------------
"""

# Solution
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
```

## FILE: 03-Input-TypeConversion/06_add_two_numbers.py

```python
"""
------------------------------------------------------------
Problem No : 06
Topic      : Input & Type Conversion
Problem    : Add Two Numbers
Difficulty : Easy

Question:
Take two numbers as input from the user and print their sum.

Example Input:
5
7

Example Output:
Sum: 12.0
------------------------------------------------------------
"""

# Solution
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)
```

## FILE: 03-Input-TypeConversion/07_area_circle.py

```python
"""
------------------------------------------------------------
Problem No : 07
Topic      : Input & Type Conversion
Problem    : Area of Circle
Difficulty : Easy

Question:
Take the radius of a circle as input and calculate its area
using the formula: pi * r^2 (use 3.14159 for pi).

Example Input:
7

Example Output:
Area of Circle: 153.94
------------------------------------------------------------
"""

# Solution
radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * (radius ** 2)
print("Area of Circle:", round(area, 2))
```

## FILE: 03-Input-TypeConversion/08_simple_interest.py

```python
"""
------------------------------------------------------------
Problem No : 08
Topic      : Input & Type Conversion
Problem    : Simple Interest
Difficulty : Easy

Question:
Take principal, rate, and time as input and calculate the
simple interest.

Example Input:
10000
5
2

Example Output:
Simple Interest: 1000.0
------------------------------------------------------------
"""

# Solution
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)
```

## FILE: 03-Input-TypeConversion/09_currency_converter.py

```python
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
```

## FILE: 03-Input-TypeConversion/10_percentage_calculator.py

```python
"""
------------------------------------------------------------
Problem No : 10
Topic      : Input & Type Conversion
Problem    : Percentage Calculator
Difficulty : Easy

Question:
Take marks obtained in 5 subjects (out of 100 each) as input
and calculate the total and percentage.

Example Input:
80
90
75
85
95

Example Output:
Total Marks: 425.0
Percentage: 85.0
------------------------------------------------------------
"""

# Solution
m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))
m4 = float(input("Enter marks in subject 4: "))
m5 = float(input("Enter marks in subject 5: "))
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100
print("Total Marks:", total)
print("Percentage:", round(percentage, 2))
```

---

## FILE: 04-Strings/README.md

```markdown
# Topic: Strings

## Concepts Covered
- String creation and length
- Indexing
- Slicing
- f-strings
- String methods (upper, lower, strip, replace, find)

## Problems
01. String Basics
02. String Indexing
03. String Slicing
04. Formatted Strings
05. String Methods
06. Full Name
07. Reverse Name
08. Count Characters
09. Find Character
10. Replace Word

## Learning Outcome
By completing these problems you should be able to:
- Store, access, and manipulate strings
- Use indexing, slicing, and built-in string methods confidently
```

## FILE: 04-Strings/01_string_basics.py

```python
"""
------------------------------------------------------------
Problem No : 01
Topic      : Strings
Problem    : String Basics
Difficulty : Easy

Question:
Create a string variable with your favorite quote and print its
length using len().

Example Output:
Quote: Code every day, improve every day.
Length: 35
------------------------------------------------------------
"""

# Solution
quote = "Code every day, improve every day."
print("Quote:", quote)
print("Length:", len(quote))
```

## FILE: 04-Strings/02_string_indexing.py

```python
"""
------------------------------------------------------------
Problem No : 02
Topic      : Strings
Problem    : String Indexing
Difficulty : Easy

Question:
Create a string with your name and print the first character,
the last character, and the character at index 2.

Example Output:
First character: K
Last character: k
Character at index 2: r
------------------------------------------------------------
"""

# Solution
name = "Karthik"
print("First character:", name[0])
print("Last character:", name[-1])
print("Character at index 2:", name[2])
```

## FILE: 04-Strings/03_string_slicing.py

```python
"""
------------------------------------------------------------
Problem No : 03
Topic      : Strings
Problem    : String Slicing
Difficulty : Easy

Question:
Create a string and print the first 3 characters, the last 3
characters, and a fully reversed version of it using slicing.

Example Output:
First 3 characters: Pyt
Last 3 characters: ing
Reversed string: gnimmargorP nohtyP
------------------------------------------------------------
"""

# Solution
text = "Python Programming"
print("First 3 characters:", text[:3])
print("Last 3 characters:", text[-3:])
print("Reversed string:", text[::-1])
```

## FILE: 04-Strings/04_formatted_strings.py

```python
"""
------------------------------------------------------------
Problem No : 04
Topic      : Strings
Problem    : Formatted Strings
Difficulty : Easy

Question:
Using an f-string, create a sentence that combines a name
variable and a course name variable into one message.

Example Output:
Karthik is learning Python Programming to become a great developer.
------------------------------------------------------------
"""

# Solution
name = "Karthik"
course = "Python Programming"
print(f"{name} is learning {course} to become a great developer.")
```

## FILE: 04-Strings/05_string_methods.py

```python
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
```

## FILE: 04-Strings/06_full_name.py

```python
"""
------------------------------------------------------------
Problem No : 06
Topic      : Strings
Problem    : Full Name
Difficulty : Easy

Question:
Take first name and last name as input and combine them into
a full name using string concatenation.

Example Input:
Karthik
Bhandarkar

Example Output:
Full Name: Karthik Bhandarkar
------------------------------------------------------------
"""

# Solution
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print("Full Name:", full_name)
```

## FILE: 04-Strings/07_reverse_name.py

```python
"""
------------------------------------------------------------
Problem No : 07
Topic      : Strings
Problem    : Reverse Name
Difficulty : Easy

Question:
Take a name as input and print it in reverse order using slicing.

Example Input:
Karthik

Example Output:
Reversed name: kihtraK
------------------------------------------------------------
"""

# Solution
name = input("Enter your name: ")
print("Reversed name:", name[::-1])
```

## FILE: 04-Strings/08_count_characters.py

```python
"""
------------------------------------------------------------
Problem No : 08
Topic      : Strings
Problem    : Count Characters
Difficulty : Easy

Question:
Take a string as input and print the total number of characters
in it using len().

Example Input:
Python

Example Output:
Number of characters: 6
------------------------------------------------------------
"""

# Solution
text = input("Enter a string: ")
print("Number of characters:", len(text))
```

## FILE: 04-Strings/09_find_character.py

```python
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
```

## FILE: 04-Strings/10_replace_word.py

```python
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
```

---

## FILE: 05-Operators/README.md

```markdown
# Topic: Operators

## Concepts Covered
- Arithmetic operators (+, -, *, /, //, %, **)
- Operator precedence
- Augmented assignment operators (+=, -=, *=, /=)
- Built-in math functions (abs, sqrt)
- Applying operators to real-world calculations

## Problems
01. Addition
02. Arithmetic Operations
03. Operator Precedence
04. Augmented Assignment
05. Math Functions
06. Calculator
07. Discount
08. Profit/Loss
09. Percentage
10. Power Calculator

## Learning Outcome
By completing these problems you should be able to:
- Use all arithmetic and augmented assignment operators correctly
- Understand operator precedence
- Apply operators to solve real-world numeric problems
```

## FILE: 05-Operators/01_addition.py

```python
"""
------------------------------------------------------------
Problem No : 01
Topic      : Operators
Problem    : Addition
Difficulty : Easy

Question:
Take two numbers as input and print their sum using the + operator.

Example Input:
4
6

Example Output:
Sum: 10.0
------------------------------------------------------------
"""

# Solution
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
```

## FILE: 05-Operators/02_arithmetic_operations.py

```python
"""
------------------------------------------------------------
Problem No : 02
Topic      : Operators
Problem    : Arithmetic Operations
Difficulty : Easy

Question:
Take two numbers as input and print the result of addition,
subtraction, multiplication, division, floor division, modulus,
and exponentiation.

Example Input:
10
3

Example Output:
Addition: 13.0
Subtraction: 7.0
Multiplication: 30.0
Division: 3.3333333333333335
Floor Division: 3.0
Modulus: 1.0
Exponentiation: 1000.0
------------------------------------------------------------
"""

# Solution
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
```

## FILE: 05-Operators/03_operator_precedence.py

```python
"""
------------------------------------------------------------
Problem No : 03
Topic      : Operators
Problem    : Operator Precedence
Difficulty : Easy

Question:
Evaluate the expression 10 + 2 * 3 - (4 / 2) and print the result.

Example Output:
Result: 14.0
------------------------------------------------------------
"""

# Solution
result = 10 + 2 * 3 - (4 / 2)
print("Result:", result)
# Order of evaluation: Parentheses -> Multiplication/Division -> Addition/Subtraction
```

## FILE: 05-Operators/04_augmented_assignment.py

```python
"""
------------------------------------------------------------
Problem No : 04
Topic      : Operators
Problem    : Augmented Assignment
Difficulty : Easy

Question:
Start with a variable value = 10 and demonstrate +=, -=, *=, /=
by updating and printing the value after each operation.

Example Output:
Initial value: 10
After += 5: 15
After -= 3: 12
After *= 2: 24
After /= 4: 6.0
------------------------------------------------------------
"""

# Solution
value = 10
print("Initial value:", value)
value += 5
print("After += 5:", value)
value -= 3
print("After -= 3:", value)
value *= 2
print("After *= 2:", value)
value /= 4
print("After /= 4:", value)
```

## FILE: 05-Operators/05_math_functions.py

```python
"""
------------------------------------------------------------
Problem No : 05
Topic      : Operators
Problem    : Math Functions
Difficulty : Easy

Question:
Take a number as input and print its absolute value, square root,
and its power of 2 using built-in math functions.

Example Input:
-16

Example Output:
Absolute value: 16.0
Square root: 4.0
Power of 2: 256.0
------------------------------------------------------------
"""

# Solution
import math
num = float(input("Enter a number: "))
print("Absolute value:", abs(num))
print("Square root:", math.sqrt(abs(num)))
print("Power of 2:", num ** 2)
```

## FILE: 05-Operators/06_calculator.py

```python
"""
------------------------------------------------------------
Problem No : 06
Topic      : Operators
Problem    : Calculator
Difficulty : Easy

Question:
Take two numbers as input and print the result of all four basic
operations on them (+, -, *, /). No if-else yet, so all results
are shown together.

Example Input:
20
4

Example Output:
Addition Result: 24.0
Subtraction Result: 16.0
Multiplication Result: 80.0
Division Result: 5.0
------------------------------------------------------------
"""

# Solution
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition Result:", num1 + num2)
print("Subtraction Result:", num1 - num2)
print("Multiplication Result:", num1 * num2)
print("Division Result:", num1 / num2)
```

## FILE: 05-Operators/07_discount.py

```python
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
```

## FILE: 05-Operators/08_profit_loss.py

```python
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
```

## FILE: 05-Operators/09_percentage.py

```python
"""
------------------------------------------------------------
Problem No : 09
Topic      : Operators
Problem    : Percentage
Difficulty : Easy

Question:
Take marks obtained and total marks as input, then calculate
and print the percentage using operators.

Example Input:
450
500

Example Output:
Percentage: 90.0
------------------------------------------------------------
"""

# Solution
marks_obtained = float(input("Enter marks obtained: "))
total_marks = float(input("Enter total marks: "))
percentage = (marks_obtained / total_marks) * 100
print("Percentage:", round(percentage, 2))
```

## FILE: 05-Operators/10_power_calculator.py

```python
"""
------------------------------------------------------------
Problem No : 10
Topic      : Operators
Problem    : Power Calculator
Difficulty : Easy

Question:
Take a base number and an exponent as input and calculate the
result using the exponentiation operator (**).

Example Input:
2
10

Example Output:
Result: 1024.0
------------------------------------------------------------
"""

# Solution
base = float(input("Enter base number: "))
exponent = float(input("Enter exponent: "))
result = base ** exponent
print("Result:", result)
```

---

## END OF BUILD INSTRUCTIONS
Total files to create: 1 root README + 5 topic READMEs + 50 Python files = 56 files.
Stop here. Do not create `06-If-Else` — that topic starts today, and the user will add it themselves.
