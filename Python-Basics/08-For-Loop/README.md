# For Loop

A `for` loop iterates over any iterable — a list, string, range, tuple, dictionary,
or any object that implements `__iter__`. It processes each element in sequence and
is the preferred loop when the number of iterations is known or you're traversing a collection.

---

## What is it?

`for` binds a target variable to each element in an iterable, executing the body
once per element. The built-in `range()` function is the standard way to loop a
fixed number of times. An optional `else` clause runs after all iterations complete
(skipped if the loop exits via `break`).

---

## Why do we use it?

- Traverse collections (lists, strings, dicts, sets) cleanly without manual index management.
- Generate numeric sequences with `range()`.
- Cleaner and less error-prone than equivalent `while` loops for fixed-length iteration.

---

## Syntax

```python
for item in iterable:
    # body

# with else
for item in iterable:
    # body
else:
    # runs after loop completes (skipped on break)

# using range()
for i in range(stop):                  # 0 to stop-1
for i in range(start, stop):           # start to stop-1
for i in range(start, stop, step):     # start to stop-1, stepping by step
```

---

## Parameters

### `range(start=0, stop, step=1)`

| Parameter | Default | Description |
|---|---|---|
| `start` | `0` | First value (inclusive) |
| `stop` | required | Upper bound (exclusive) |
| `step` | `1` | Increment per iteration (can be negative) |

`range()` returns a lazy sequence — it does not create a list in memory.

---

## Return Value

`for` is a statement — no return value. `range()` returns a `range` object (iterable).

---

## Example

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Numeric range
for i in range(1, 6):
    print(i, end=" ")
print()

# Enumerate (index + value)
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")

# Nested for (multiplication table)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()
```

---

## Output

```
apple
banana
cherry
1 2 3 4 5
0: apple
1: banana
2: cherry
1x1=1  1x2=2  1x3=3
2x1=2  2x2=4  2x3=6
3x1=3  3x2=6  3x3=9
```

---

## Key Points

- `for` works on any **iterable** — list, string, tuple, set, dict, file, generator.
- `range()` is lazy — it generates values on demand, using O(1) memory regardless of size.
- `enumerate(iterable, start=0)` gives both index and value — preferred over manual `i += 1`.
- `zip(a, b)` iterates two iterables in parallel.
- Iterating a `dict` gives keys by default; use `.items()` for key-value pairs.
- `break` exits the loop; `continue` skips to the next iteration; `pass` is a no-op placeholder.
- `else` on a `for` loop runs only when the loop completes without `break` — useful for search patterns.

---

## Common Mistakes

```python
# Mistake 1 — modifying a list while iterating it
for item in my_list:
    if condition:
        my_list.remove(item)   # skips elements — iterate a copy instead
for item in my_list[:]:        # Correct: iterate a copy

# Mistake 2 — range stop is exclusive
for i in range(5):             # 0,1,2,3,4 — NOT 5
for i in range(1, 6):          # 1,2,3,4,5

# Mistake 3 — using index manually when enumerate is cleaner
for i in range(len(lst)):
    print(i, lst[i])           # works, but verbose
for i, v in enumerate(lst):
    print(i, v)                # Pythonic

# Mistake 4 — expecting else to run after break
for i in range(5):
    if i == 3:
        break
else:
    print("never runs")        # skipped because of break

# Mistake 5 — nested loop variable collision
for i in range(3):
    for i in range(3):         # inner i overwrites outer i
        pass
```

---

## Interview Notes

- **When to use:** Iterating over sequences, applying transformations, accumulating results.
- **When NOT to use:** When the termination condition is dynamic — use `while` instead.
- **List comprehension alternative:** `[x*2 for x in range(5)]` — concise for simple transformations, but use a `for` loop for complex multi-step logic.
- **`enumerate` vs manual index:** Always prefer `enumerate` — avoids off-by-one errors and is more readable.
- **Complexity:** O(n) where n = number of elements; each iteration runs in O(1) for range-based loops.

---

## Practice Problems

```
01_counter_pattern.py
02_reverse_counter_pattern.py
03_even_numbers.py
04_odd_numbers.py
05_multiples_of_5.py
06_sum_1_to_10.py
07_sum_even_numbers.py
08_factorial.py
09_multiplication_table.py
```

---

## Quick Revision

```python
# Basic for
for item in [1, 2, 3]:
    print(item)             # 1 2 3

# range
for i in range(5):          # 0 1 2 3 4
for i in range(1, 6):       # 1 2 3 4 5
for i in range(0, 10, 2):   # 0 2 4 6 8
for i in range(5, 0, -1):   # 5 4 3 2 1

# enumerate
for i, v in enumerate(["a", "b"]):
    print(i, v)             # 0 a, 1 b

# zip
for a, b in zip([1, 2], ["x", "y"]):
    print(a, b)             # 1 x, 2 y

# dict iteration
d = {"k1": 1, "k2": 2}
for k, v in d.items():
    print(k, v)

# break / continue / pass
for i in range(10):
    if i == 5: break        # stop at 5
    if i % 2 == 0: continue # skip even
    pass                    # no-op placeholder
```
