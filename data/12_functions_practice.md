# Topic 12: Functions — Practice Set (15 Problems)

---

### Problem 01: Function with No Parameters
**Question:** Write a function `greet()` that prints a fixed greeting message. Call it.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def greet():
    print("Hello! Welcome to Python.")

greet()
```
**Why wrap this in a function at all:** Even one line benefits from being a function
if you'll ever call it more than once, or if naming it (`greet`) makes the rest of
your code more readable than the raw print statement would.
</details>

---

### Problem 02: Function with a Parameter and Return Value
**Question:** Write a function `greet_user(name)` that returns (not prints) a greeting
message using the given name.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def greet_user(name):
    return f"Hello, {name}! Welcome."

message = greet_user("Karthik")
print(message)
```
**Why return instead of print inside the function:** A function that returns a value
can be reused in more places — you can print it, store it, or pass it to another
function. A function that only prints can't do any of that. Prefer return over print
inside functions as a general rule.
</details>

---

### Problem 03: Add Two Numbers
**Question:** Write a function `add(a, b)` that returns the sum of two numbers.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def add(a, b):
    return a + b

result = add(5, 7)
print("Sum:", result)
```
**Why this is the standard shape of a function:** Take input via parameters, do work,
return the output. This "input → process → output" shape applies to almost every
function you'll ever write.
</details>

---

### Problem 04: Default Parameter Value
**Question:** Write a function `power(base, exponent=2)` that returns base raised to
exponent, defaulting to squaring if exponent isn't given.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(5, 3))
```
**When to use default parameters:** Use them when a parameter has an obvious "usual"
value most callers will want, while still allowing it to be overridden — this avoids
forcing every caller to specify a value that's almost always the same.
</details>

---

### Problem 05: Keyword Arguments
**Question:** Write a function `describe_person(name, age, city)` and call it once
using positional arguments and once using keyword arguments in a different order.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person("Karthik", 21, "Bengaluru")
describe_person(city="Bengaluru", name="Karthik", age=21)
```
**Why keyword arguments matter:** With positional arguments, order must match exactly
— easy to mess up with many parameters. Keyword arguments let you specify `name=`,
`age=` explicitly, making calls clearer and order-independent.
</details>

---

### Problem 06: Even or Odd Function
**Question:** Write a function `is_even(number)` that returns True if even, False if odd.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(7))
```
**Why return the condition directly:** `number % 2 == 0` is already a True/False
expression — writing `if number % 2 == 0: return True else: return False` produces
the exact same result with unnecessary extra lines. Return boolean expressions directly.
</details>

---

### Problem 07: Factorial Function
**Question:** Write a function `factorial(n)` that returns n! using a loop inside the function.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
```
**Why wrap loop-based logic in functions:** You already wrote this exact loop in
For-Loop Problem 11 — wrapping it in a function means you can now call
`factorial(5)`, `factorial(8)`, etc. anywhere in a bigger program without repeating
the loop each time.
</details>

---

### Problem 08: Prime Number Checker
**Question:** Write a function `is_prime(n)` that returns True if n is prime, False otherwise.

**Think about it:**
- A number is prime if nothing between 2 and n-1 divides it evenly. You can `return
  False` the moment you find a divisor.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))
```
**Why return False immediately inside the loop:** The moment you find ONE divisor,
you already know the answer — no need to keep checking the rest. Returning early
inside a loop (instead of setting a flag and breaking) is a cleaner, very common
pattern.
</details>

---

### Problem 09: Sum Using *args
**Question:** Write a function `total(*args)` that returns the sum of any number of
numbers passed to it.

**Think about it:**
- `*args` collects any number of positional arguments into a tuple inside the function.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def total(*args):
    return sum(args)

print(total(1, 2, 3))
print(total(10, 20, 30, 40, 50))
```
**Why *args instead of a fixed parameter list:** A normal function like `add(a, b)`
only ever accepts exactly 2 numbers. `*args` lets the SAME function accept 2, 5, or
20 numbers — use it whenever the number of inputs isn't fixed in advance.
</details>

---

### Problem 10: Print Details Using **kwargs
**Question:** Write a function `print_details(**kwargs)` that prints each key-value
pair passed to it as named arguments.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_details(name="Karthik", age=21, city="Bengaluru")
```
**\*args vs \*\*kwargs:** `*args` collects extra POSITIONAL arguments into a tuple;
`**kwargs` collects extra NAMED (keyword) arguments into a dictionary. Use `*args`
when values don't need labels, `**kwargs` when they do.
</details>

---

### Problem 11: Simple Interest Function
**Question:** Write a function `simple_interest(principal, rate, time)` that returns
the calculated interest.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print(simple_interest(10000, 5, 2))
```
**Why this deserves to be a function:** You wrote this same formula inline back in
Variables Problem 09 and Input Problem 08 — as soon as a calculation gets reused
across your codebase, that's the signal to turn it into a function instead of
copy-pasting the formula each time.
</details>

---

### Problem 12: Recursive Factorial
**Question:** Write `factorial(n)` again, but this time using recursion instead of a loop.

**Think about it:**
- A recursive function calls itself with a smaller input, and needs a "base case"
  that stops the recursion.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```
**Why recursion works here:** `factorial(5)` = 5 × `factorial(4)` = 5 × 4 ×
`factorial(3)` ... down to `factorial(1)` = 1 (the base case, which stops the chain).
Every recursive function needs exactly this: a base case that stops it, and a step
that moves toward that base case.
</details>

---

### Problem 13: Recursive Fibonacci
**Question:** Write a recursive function `fibonacci(n)` that returns the nth Fibonacci
number (0, 1, 1, 2, 3, 5, 8, ...).

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
```
**Why two base cases here (not one):** Fibonacci needs the two PREVIOUS values to
compute the next one, so it needs both `fibonacci(0)` and `fibonacci(1)` defined
directly — one base case isn't enough to stop the recursion cleanly here.
</details>

---

### Problem 14: Return Multiple Values
**Question:** Write a function `min_max(numbers)` that returns both the minimum and
maximum of a list at once.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
def min_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = min_max([12, 45, 3, 89, 27])
print("Min:", smallest, "Max:", largest)
```
**Why this works:** `return a, b` actually returns a tuple `(a, b)` — Python lets you
unpack it directly into two variables when you call the function. This is how you
return "more than one answer" from a single function.
</details>

---

### Problem 15: Local vs Global Variable Scope
**Question:** Demonstrate the difference between a local variable (inside a function)
and a global variable (outside it), including what happens when they share a name.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
count = 10  # global variable

def show_local():
    count = 5  # local variable, separate from the global one
    print("Inside function, count =", count)

show_local()
print("Outside function, count =", count)
```
**Why the global `count` doesn't change:** The `count = 5` inside the function
creates a NEW local variable that only exists during the function call — it doesn't
touch the global one at all, even though they share a name. This is why unrelated
functions can safely reuse simple variable names like `i`, `count`, `total` without
interfering with each other.
</details>
