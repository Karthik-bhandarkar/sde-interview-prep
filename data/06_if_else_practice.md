# Topic 06: If-Else — Practice Set (15 Problems)

**How to use this file:** Read the question, think using the hints, write your own
attempt in the blank code block, then click the "Solution + Why" section to check
yourself and understand *why* that approach was used — not just what the code does.

---

### Problem 01: Positive, Negative, or Zero
**Question:** Take a number as input and check whether it is positive, negative, or zero.

**Think about it:**
- There are 3 possible outcomes, not 2 — what structure handles more than two branches?
- Compare the number against 0.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```
**Why if-elif-else:** Three mutually exclusive outcomes → an elif ladder checks each
condition in order and stops at the first match. Using three separate `if` statements
would work but is wasteful — Python would still check all three even after finding a match.
</details>

---

### Problem 02: Even or Odd
**Question:** Take a number and check if it's even or odd.

**Think about it:**
- Only 2 outcomes → what's the simplest structure for exactly 2 branches?
- Which operator tells you the remainder after division?

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```
**Why if-else (not elif):** Exactly 2 outcomes that cover every case → plain if-else is
enough. Reaching for elif when there are only two options adds unnecessary complexity.
</details>

---

### Problem 03: Voting Eligibility
**Question:** Take age as input and print whether the person is eligible to vote (18+).

**Think about it:**
- Only one condition to check — do you need an else at all, or just an if?

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```
**Why >=, not >:** 18 itself should count as eligible, so the boundary must be inclusive.
Off-by-one boundary mistakes (`>` vs `>=`) are one of the most common real bugs.
</details>

---

### Problem 04: Largest of Two Numbers
**Question:** Take two numbers and print the larger one.

**Think about it:**
- What if they're equal? Decide how you want to handle a tie before coding.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both numbers are equal")
```
**Why three branches:** Handling the tie explicitly avoids silently picking a "wrong"
largest — this habit of thinking about edge cases (ties, empty input, zero) is exactly
what interviewers probe for.
</details>

---

### Problem 05: Largest of Three Numbers
**Question:** Take three numbers and print the largest.

**Think about it:**
- Can you compare all three with nested if, or fewer conditions using `and`?

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
```
**Why `and`:** A number is only "largest" if it beats BOTH others at once — that's a
compound condition, which is exactly what `and` is for (both sides must be true).
</details>

---

### Problem 06: Leap Year Check
**Question:** Take a year and check whether it's a leap year. Rule: divisible by 4,
but if divisible by 100 it must also be divisible by 400.

**Think about it:**
- This is a compound rule with an exception to an exception — combine `and`/`or` carefully.
- Try writing the rule in plain English first, then translate to code.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
```
**Why this structure:** A year is a leap year if EITHER (divisible by 4 but not 100)
OR (divisible by 400). This is the classic "and inside or" pattern — parentheses
matter here, since precedence rules can silently change the result.
</details>

---

### Problem 07: Grade Calculator
**Question:** Take marks (0-100) and print a grade: A (90+), B (75-89), C (60-74),
D (40-59), F (below 40).

**Think about it:**
- Ranges that don't overlap and cover every case → order matters in an elif ladder.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")
```
**Why order matters:** Checking `>= 90` first means anything lower automatically falls
through to the next check. If you checked `>= 40` first, everything above 40 would
wrongly get "D" — always order range checks from most restrictive to least.
</details>

---

### Problem 08: Password Length Validator
**Question:** Take a password and check it's at least 8 characters AND contains no spaces.

**Think about it:**
- Two conditions must BOTH hold true — which operator connects them?
- `len()` and the `in` keyword will help.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
password = input("Enter a password: ")
if len(password) >= 8 and " " not in password:
    print("Valid password")
else:
    print("Invalid password")
```
**Why `and`:** Both rules are non-negotiable requirements — if either fails, the whole
password is invalid. This is the difference between "must satisfy all" (`and`) and
"must satisfy at least one" (`or`).
</details>

---

### Problem 09: Simple Login System
**Question:** Store a correct username and password. Take user input and check both match.

**Think about it:**
- Same logic as above — both checks must pass together.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
correct_username = "karthik"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Login failed")
```
**Why not two separate if blocks:** If you checked username and password in separate
if-statements, you couldn't cleanly say "both must match" — combining them into one
condition keeps the success case a single, unambiguous branch.
</details>

---

### Problem 10: Traffic Signal Action
**Question:** Take a color ("red"/"yellow"/"green") and print the action: Stop, Slow Down, Go.

**Think about it:**
- More than 2 discrete, unrelated options → elif ladder, not and/or chaining.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
color = input("Enter signal color: ").lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Slow Down")
elif color == "green":
    print("Go")
else:
    print("Invalid color")
```
**Why `.lower()` first:** Normalizing input before comparing avoids bugs where "Red"
or "RED" wouldn't match "red" — a very common real-world gotcha with string comparisons.
</details>

---

### Problem 11: BMI Category
**Question:** Take BMI value and print category: Underweight (<18.5), Normal (18.5-24.9),
Overweight (25-29.9), Obese (30+).

**Think about it:**
- Same range-ladder pattern as the grade calculator — order from highest to lowest.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
bmi = float(input("Enter your BMI: "))
if bmi >= 30:
    print("Obese")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")
```
**Why start from the top this time:** Either direction works as long as you're
consistent and non-overlapping — starting from the highest boundary here reads more
naturally with real BMI charts, which is a style choice, not a rule.
</details>

---

### Problem 12: Divisible by Both 3 and 5
**Question:** Take a number and check if it's divisible by both 3 and 5.

**Think about it:**
- "Both" is the keyword — which operator?

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")
```
**Why this matters:** This exact `and`-of-two-modulus pattern is the core of the
classic "FizzBuzz" interview question — recognize it now, you'll see it again.
</details>

---

### Problem 13: Ticket Price by Age
**Question:** Take age and print ticket price: Child (<12) ₹100, Adult (12-59) ₹250,
Senior (60+) ₹150.

**Think about it:**
- 3 non-overlapping ranges — elif ladder again, decide the cleanest boundary order.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
age = int(input("Enter age: "))
if age < 12:
    print("Ticket Price: Rs.100")
elif age < 60:
    print("Ticket Price: Rs.250")
else:
    print("Ticket Price: Rs.150")
```
**Why this reads cleaner:** Once age < 12 is ruled out, checking `age < 60` alone is
enough to mean "between 12 and 59" — you don't need `age >= 12 and age < 60` because
the elif already guarantees age is not < 12.
</details>

---

### Problem 14: Vowel or Consonant
**Question:** Take a single letter and check if it's a vowel or a consonant.

**Think about it:**
- Checking against 5 letters one by one with `or` works but is repetitive — is there
  a shorter way using `in`?

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
letter = input("Enter a letter: ").lower()
if letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")
```
**Why `in` beats `or`:** `letter == 'a' or letter == 'e' or ...` is 5 comparisons;
`letter in "aeiou"` is one readable check. Whenever you're comparing one value
against several options, reach for `in` over a chain of `or`.
</details>

---

### Problem 15: Ternary Operator — Max of Two Numbers
**Question:** Take two numbers and print the larger one using a one-line if-else
(ternary) expression instead of a full if-else block.

**Think about it:**
- Syntax: `value_if_true if condition else value_if_false`

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
larger = a if a > b else b
print("Larger number:", larger)
```
**When to use ternary vs full if-else:** Use ternary only for simple, single-value
decisions that fit on one line — it's about assigning a value, not running multiple
statements. If you need more than one action per branch, go back to a full if-else;
forcing complex logic into a ternary hurts readability.
</details>
