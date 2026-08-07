# Topic 07: While Loop — Practice Set (12 Problems)

---

### Problem 01: Print 1 to 10
**Question:** Print numbers from 1 to 10 using a while loop.

**Think about it:**
- A while loop needs 3 things: a starting value, a condition, and something that
  changes each time. Which line updates the counter, and where does it go?

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
i = 1
while i <= 10:
    print(i)
    i += 1
```
**Why while (not for) here:** Either works, but while makes the "condition-driven"
nature explicit — useful once you move to loops where the number of iterations isn't
known ahead of time (which for-range can't naturally express).
</details>

---

### Problem 02: Sum of First N Natural Numbers
**Question:** Take N as input and find the sum of numbers from 1 to N using a while loop.

**Think about it:**
- You need an accumulator variable to keep a running total, separate from the counter.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
n = int(input("Enter N: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum:", total)
```
**Why two variables:** `i` tracks position (where the loop is), `total` tracks the
accumulated result. Mixing these into one variable is a very common beginner bug —
keep "what changes to control the loop" separate from "what you're computing".
</details>

---

### Problem 03: Countdown from N to 1
**Question:** Take N as input and print numbers from N down to 1.

**Think about it:**
- The counter should decrease, not increase — update the condition to match.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
n = int(input("Enter N: "))
while n >= 1:
    print(n)
    n -= 1
```
**Why `-=` and `>=`:** Direction of the counter and direction of the condition must
match, or you get an infinite loop (if n only increases but the condition wants it
decreasing) or zero iterations (wrong direction check).
</details>

---

### Problem 04: Multiplication Table
**Question:** Take a number and print its multiplication table from 1 to 10 using while.

**Think about it:**
- What varies from row to row? Multiply the fixed number by the changing counter.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
```
**Why this pattern generalizes:** "fixed value x changing counter" is the backbone of
almost every table/grid-printing problem you'll see later — recognize the shape, not
just this specific case.
</details>

---

### Problem 05: Reverse a Number
**Question:** Take a number and reverse its digits using a while loop (no string conversion).

**Think about it:**
- `% 10` gives the last digit. `// 10` removes the last digit. Build the reversed
  number one digit at a time.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
print("Reversed number:", reversed_num)
```
**Why `% 10` and `// 10` together:** This pair is the standard way to peel digits off
a number one at a time — you'll reuse this exact combo for sum-of-digits, palindrome
checks, and digit-counting problems.
</details>

---

### Problem 06: Sum of Digits
**Question:** Take a number and find the sum of its digits using a while loop.

**Think about it:**
- Same digit-extraction trick as above, but accumulate a sum instead of rebuilding a number.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
num = int(input("Enter a number: "))
digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num = num // 10
print("Sum of digits:", digit_sum)
```
**Why recognizing patterns matters:** Once you see "digit extraction" as a reusable
building block, new problems (reverse, sum, count, palindrome) become variations of
the same 3 lines instead of separate things to memorize.
</details>

---

### Problem 07: Factorial Using While
**Question:** Take a number and calculate its factorial (n!) using a while loop.

**Think about it:**
- Factorial multiplies, so your accumulator should start at 1, not 0.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
num = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print("Factorial:", factorial)
```
**Why start at 1, not 0:** For sums, the "empty" starting value is 0 (adding 0 changes
nothing). For products, it's 1 (multiplying by 0 would zero out everything). Match
your starting value to the operation.
</details>

---

### Problem 08: Guess the Number (Fixed Target)
**Question:** Store a secret number. Keep asking the user to guess until they get it
right, telling them if they're too high or too low.

**Think about it:**
- This needs `while True` with a `break` when correct — you don't know in advance
  how many guesses it'll take.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
secret = 7
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
```
**Why `while True` + `break` here:** The number of attempts isn't known upfront, so
there's no clean condition to put in the while line itself. `while True` means "loop
forever," and `break` is the explicit exit — this pattern is the standard way to
write "keep going until something specific happens."
</details>

---

### Problem 09: Print Even Numbers 1 to N (skip odd with continue)
**Question:** Print only even numbers from 1 to N using a while loop and `continue`.

**Think about it:**
- `continue` skips the rest of the current iteration and jumps back to the condition.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
n = int(input("Enter N: "))
i = 1
while i <= n:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1
```
**Why continue needs care:** Notice `i += 1` appears in BOTH the skip path and the
normal path — a classic while-loop bug is forgetting to update the counter before
`continue`, which causes an infinite loop. This is one reason for-loops (next topic)
are often safer for simple counting.
</details>

---

### Problem 10: Count Digits in a Number
**Question:** Take a number and count how many digits it has using a while loop.

**Think about it:**
- Same digit-stripping idea, but count iterations instead of summing values.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num = num // 10
print("Number of digits:", count)
```
**Why this is the same skeleton as Problems 5 & 6:** Reverse, sum-of-digits, and
count-digits all share the exact same `while num > 0: ... num //= 10` frame — only
what happens inside the loop changes. Once you see the skeleton, new problems get
much faster to solve.
</details>

---

### Problem 11: Palindrome Number Check
**Question:** Take a number and check if it reads the same forwards and backwards
(e.g., 121) using a while loop.

**Think about it:**
- Reuse Problem 5's reverse logic, then compare the reversed number to the original.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
num = int(input("Enter a number: "))
original = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
if original == reversed_num:
    print("Palindrome")
else:
    print("Not a Palindrome")
```
**Why save `original` first:** The while loop destroys `num` as it processes it
(that's how `// 10` works), so you must save a copy before the loop to compare
against afterward. Forgetting to copy a value before mutating it is a very common
source of bugs.
</details>

---

### Problem 12: Sum Until User Enters 0 (Sentinel Loop)
**Question:** Keep asking the user for numbers and add them up. Stop when they enter 0,
then print the total.

**Think about it:**
- 0 is a "sentinel" value — a special input that signals "stop." The loop condition
  itself can check for it directly.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
total = 0
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter a number (0 to stop): "))
print("Total:", total)
```
**Why input is taken twice:** You need one input BEFORE the loop starts (to have
something to check in the while condition) and one INSIDE the loop (to get the next
value). This "prime the loop, then repeat" shape is the standard way to write
sentinel-controlled input loops.
</details>
