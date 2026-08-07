# Topic 08: For Loop — Practice Set (12 Problems)

---

### Problem 01: Print 1 to 10
**Question:** Print numbers 1 to 10 using a for loop and range().

**Think about it:**
- `range(a, b)` goes up to but NOT including `b` — off-by-one is the #1 range() bug.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
for i in range(1, 11):
    print(i)
```
**Why for-range beats while here:** When you know exactly how many times to loop
(1 to 10, fixed), `for i in range(...)` says that directly — no manual counter,
no manual increment, less room for bugs than a while loop.
</details>

---

### Problem 02: Even Numbers 1 to 20
**Question:** Print even numbers from 1 to 20 using range() with a step.

**Think about it:**
- `range(start, stop, step)` — what start and step give you only even numbers?

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
for i in range(2, 21, 2):
    print(i)
```
**Why step=2 beats if-checking:** You could loop 1-20 and filter with `if i % 2 == 0`,
but jumping in steps of 2 from the start skips the unwanted numbers entirely — fewer
iterations, and no filtering logic needed.
</details>

---

### Problem 03: Sum of 1 to N
**Question:** Take N as input and find the sum of numbers 1 to N using a for loop.

**Think about it:**
- Same accumulator idea as the while-loop version — does the loop itself get simpler?

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)
```
**Why `n + 1`:** Since range() stops one before its second argument, you need `n + 1`
to actually include `n` itself in the loop — always double-check your range boundary
against what you actually want included.
</details>

---

### Problem 04: Multiplication Table
**Question:** Take a number and print its multiplication table (1 to 10) using a for loop.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```
**Why it's shorter than the while version:** No manual `i = 1` and `i += 1` needed —
range() handles both. This is generally why for-loops are preferred whenever the
iteration count is known in advance.
</details>

---

### Problem 05: Right Triangle Pattern (Nested Loops)
**Question:** Print a right-angled triangle of stars with 5 rows, where row `r` has
`r` stars, using nested for loops.

**Think about it:**
- Outer loop = which row. Inner loop = how many stars in that row. What's the
  relationship between the row number and the star count?

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()
```
**Why nested loops:** Whenever a pattern's shape changes per row (or column), you
need one loop to move through rows and a second loop inside it to build each row's
content — this "outer controls structure, inner controls content" pattern applies to
almost every pattern-printing problem you'll ever see.
</details>

---

### Problem 06: Loop Through a String
**Question:** Take a string and print each character on its own line using a for loop.

**Think about it:**
- Strings are directly iterable — you don't need indexes or range() at all here.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
text = input("Enter a string: ")
for char in text:
    print(char)
```
**Why no range() needed:** `for char in text` iterates the characters directly — using
`for i in range(len(text)): print(text[i])` works too, but it's an extra unnecessary
step. Iterate the thing directly whenever you can.
</details>

---

### Problem 07: Count Vowels in a String
**Question:** Take a string and count how many vowels it contains using a for loop.

**Think about it:**
- Combine "loop through each character" with the vowel-check idea from If-Else Problem 14.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
text = input("Enter a string: ").lower()
count = 0
for char in text:
    if char in "aeiou":
        count += 1
print("Number of vowels:", count)
```
**Why combining topics matters:** Real problems rarely use just one concept — this
mixes loops (iterate), conditionals (check), and an accumulator (count). Recognizing
which small pieces to combine is the actual "problem-solving skill" you're building.
</details>

---

### Problem 08: Find Largest Number in a List
**Question:** Given a list of numbers, find the largest one using a for loop
(don't use the built-in `max()`).

**Think about it:**
- Start by assuming the first element is the largest, then compare against the rest.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = [12, 45, 3, 89, 27]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)
```
**Why start with `numbers[0]`, not 0:** If the list contains only negative numbers,
starting your "largest so far" at 0 would give a wrong answer. Always initialize a
running comparison with an actual element from the data, not an assumed value.
</details>

---

### Problem 09: Sum of List Elements
**Question:** Given a list of numbers, find their sum using a for loop (don't use `sum()`).

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num
print("Sum:", total)
```
**Why practice this even though `sum()` exists:** Interviewers often ask you to
implement built-ins yourself precisely to check you understand the loop underneath —
know both the shortcut and the manual version.
</details>

---

### Problem 10: Divisible by 3, Skip Others
**Question:** Loop from 1 to 30 and print only numbers divisible by 3, skipping the
rest using `continue`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
for i in range(1, 31):
    if i % 3 != 0:
        continue
    print(i)
```
**Why continue is safer here than in a while loop:** In a for-loop, range() still
auto-advances `i` even when `continue` fires — there's no risk of the infinite-loop
bug you saw in While Loop Problem 9. This is a genuine advantage of for over while
when the iteration count is fixed.
</details>

---

### Problem 11: Factorial Using For Loop
**Question:** Take a number and calculate its factorial using a for loop.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial:", factorial)
```
**Why the same result as the while version:** This is the same logic as While Loop
Problem 7, just written with range() — proof that for and while are often
interchangeable when the number of steps is known; the choice becomes style/clarity.
</details>

---

### Problem 12: Index and Value with enumerate()
**Question:** Given a list of fruits, print each item's index and value together.

**Think about it:**
- You could use `range(len(list))` and index in — but Python has a purpose-built tool
  for exactly this.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
fruits = ["apple", "banana", "mango", "grape"]
for index, fruit in enumerate(fruits):
    print(index, "->", fruit)
```
**Why enumerate() over range(len(...))**: `for i in range(len(fruits)): print(i,
fruits[i])` works, but `enumerate()` gives you both index and value directly, is more
readable, and is what experienced Python developers actually use — recognizing this
now saves you from a habit you'd otherwise have to unlearn later.
</details>
