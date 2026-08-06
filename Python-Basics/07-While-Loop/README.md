# While Loop

A `while` loop repeats a block of code as long as its condition evaluates to `True`.
Unlike a `for` loop that iterates over a known sequence, a `while` loop is
condition-driven and is used when the number of iterations is not known upfront.

---

## What is it?

`while` is a control-flow statement that checks a condition before every iteration.
When the condition becomes `False`, the loop exits. An optional `else` clause runs
once when the condition naturally becomes `False` (but not if the loop exits via `break`).

---

## Why do we use it?

- Repeat logic until a user provides valid input.
- Poll a resource or condition (e.g., wait for a file to appear).
- Implement counters, accumulators, or traversals where end point isn't fixed in advance.

---

## Syntax

```python
while condition:
    # body — runs as long as condition is True

# with else
while condition:
    # body
else:
    # runs once when condition becomes False (skipped on break)

# break and continue inside while
while condition:
    if early_exit:
        break          # exits the loop immediately
    if skip_this:
        continue       # skips rest of this iteration, re-checks condition
```

---

## Parameters

`while` takes a single **condition expression** — any expression Python can evaluate to truthy/falsy:

| Condition type | Example |
|---|---|
| Comparison | `count < 10` |
| Boolean literal | `while True:` (infinite loop, must `break`) |
| Function return | `while stack:` (truthy while list is non-empty) |

---

## Return Value

`while` is a statement — it produces no value. Use a variable inside the loop to accumulate results.

---

## Example

```python
count = 0
total = 0

while count < 5:
    total += count
    count += 1

print(f"Sum of 0–4: {total}")   # 10

# while-else
n = 1
while n <= 3:
    print(n)
    n += 1
else:
    print("Done")
```

---

## Output

```
Sum of 0–4: 10
1
2
3
Done
```

---

## Key Points

- The condition is evaluated **before** each iteration — if `False` from the start, the body never runs.
- Always ensure the condition will eventually become `False` — otherwise you get an infinite loop.
- `break` exits the loop immediately; `else` block is **skipped** when `break` fires.
- `continue` skips the remainder of the current iteration and jumps back to the condition check.
- `while True: ... break` is the idiomatic pattern for a do-while-like loop in Python.
- Avoid modifying the loop variable inside nested `if` blocks carelessly — it's a common source of infinite loops.

---

## Common Mistakes

```python
# Mistake 1 — forgetting to update the condition variable (infinite loop)
count = 0
while count < 5:
    print(count)       # loops forever — count never changes
    # Fix: count += 1

# Mistake 2 — off-by-one
while count <= 5:      # runs 6 times (0,1,2,3,4,5) — check if intended
    count += 1

# Mistake 3 — break skips the else clause (unexpected)
n = 0
while n < 5:
    if n == 3:
        break
    n += 1
else:
    print("This never prints")  # skipped because of break

# Mistake 4 — using while for known-length sequences (prefer for)
i = 0
while i < len(my_list):   # works, but for item in my_list: is cleaner
    print(my_list[i])
    i += 1
```

---

## Interview Notes

- **When to use:** Unknown number of iterations — input validation loops, retry logic, game loops, polling.
- **When NOT to use:** When iterating over a sequence of known length — use `for` instead.
- **`while True` pattern:** Standard for interactive menus, read-until-sentinel, or server loops — always pair with a `break`.
- **Complexity:** O(n) where n = number of iterations; each iteration's body determines actual runtime.
- **Infinite loop detection:** In interviews, showing `while count < n: count += 1` with a clear termination condition demonstrates awareness.

---

## Practice Problems

```
01_counter_pattern.py
02_reverse_counter.py
03_even_numbers.py
04_odd_numbers.py
05_sum_of_numbers.py
06_sum_of_even_numbers.py
07_product_of_numbers.py
08_factorial.py
09_count_even_numbers.py
10_largest_number.py
11_smallest_number.py
12_largest_number.py
13_smallest_number.py
14_sum_of_n_numbers.py
15_average_of_n_numbers.py
16_count_positive_negative_zero.py
17_reverse_number.py
18_palindrome_number.py
```

---

## Quick Revision

```python
# Basic while
i = 0
while i < 5:
    print(i)
    i += 1           # 0 1 2 3 4

# while-else
while condition:
    ...
else:
    ...              # runs if loop ended naturally (no break)

# do-while equivalent
while True:
    action()
    if done:
        break

# break / continue
while i < 10:
    if i == 5:
        break        # exits loop
    if i % 2 == 0:
        i += 1
        continue     # skip to next iteration
    i += 1
```
