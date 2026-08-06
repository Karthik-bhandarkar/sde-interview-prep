# Lists & List Methods

A list is an ordered, mutable sequence that can hold items of any type — including
mixed types and other lists. It is Python's most versatile general-purpose container
and the foundation for most algorithmic problem solving.

---

## What is it?

A `list` is a dynamic array that stores references to objects. Elements are
accessed by integer index starting at `0`. Lists can grow or shrink at runtime and
support a rich set of built-in methods for adding, removing, sorting, and searching.

---

## Why do we use it?

- Store collections of related items that may change over time.
- Build, transform, and accumulate data in algorithms and data pipelines.
- List comprehensions provide concise, readable one-line transformations.

---

## Syntax

```python
# Creation
lst = [1, 2, 3]
empty = []
mixed = [1, "hello", 3.14, True]

# Indexing & Slicing
lst[0]        # first element
lst[-1]       # last element
lst[1:3]      # sublist (stop exclusive)
lst[::-1]     # reversed copy

# List comprehension
squares = [x**2 for x in range(5)]
evens   = [x for x in range(10) if x % 2 == 0]
```

---

## Parameters

### Common List Methods

| Method | Signature | Description |
|---|---|---|
| `.append(x)` | — | Add `x` to end — O(1) amortized |
| `.insert(i, x)` | — | Insert `x` at index `i` — O(n) |
| `.remove(x)` | — | Remove first occurrence of `x`; raises `ValueError` if not found |
| `.pop(i=-1)` | `i` optional | Remove & return element at index `i` (default last) — O(1) for last, O(n) otherwise |
| `.sort(key=None, reverse=False)` | — | Sort in place — O(n log n) |
| `.reverse()` | — | Reverse in place — O(n) |
| `.index(x)` | — | Index of first `x`; raises `ValueError` if not found |
| `.count(x)` | — | Number of occurrences of `x` — O(n) |
| `.extend(iterable)` | — | Append all items from iterable — O(k) |
| `.clear()` | — | Remove all elements |
| `.copy()` | — | Shallow copy |

### Built-in functions on lists

| Function | Description |
|---|---|
| `len(lst)` | Number of elements — O(1) |
| `sum(lst)` | Sum of numeric elements |
| `min(lst)` / `max(lst)` | Minimum / maximum element |
| `sorted(lst)` | Returns a new sorted list (does not modify original) |

---

## Return Value

| Operation | Returns |
|---|---|
| `.append()`, `.insert()`, `.remove()`, `.reverse()`, `.sort()` | `None` (in-place) |
| `.pop(i)` | The removed element |
| `.index(x)` | `int` (index) |
| `.count(x)` | `int` |
| `sorted(lst)` | New sorted `list` |

---

## Example

```python
fruits = ["banana", "apple", "cherry"]

fruits.append("mango")          # ["banana", "apple", "cherry", "mango"]
fruits.insert(0, "grape")       # ["grape", "banana", "apple", "cherry", "mango"]
fruits.remove("apple")          # ["grape", "banana", "cherry", "mango"]
popped = fruits.pop()           # "mango" removed; fruits = ["grape", "banana", "cherry"]
fruits.sort()                   # ["banana", "cherry", "grape"]
fruits.reverse()                # ["grape", "cherry", "banana"]

print(fruits)
print(len(fruits), min(fruits), max(fruits))

# Comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)
```

---

## Output

```
['grape', 'cherry', 'banana']
3 banana grape
[1, 4, 9, 16, 25]
```

---

## Key Points

- Lists are **ordered** and **mutable** — elements can be changed, added, or removed after creation.
- Indexing is O(1); searching (`in`, `.index()`) is O(n).
- `.append()` is O(1) amortized; `.insert(0, x)` and `.remove()` are O(n) — avoid for performance-sensitive code.
- `.sort()` modifies the list in place; `sorted()` returns a new list.
- List comprehensions are faster than equivalent `for` loops for simple transformations.
- `lst[:]` or `lst.copy()` creates a **shallow copy** — nested mutable objects are still shared.
- `list * n` repeats elements: `[0] * 5` → `[0, 0, 0, 0, 0]`.

---

## Common Mistakes

```python
# Mistake 1 — modifying list while iterating
for item in lst:
    if item < 0:
        lst.remove(item)      # skips elements — use lst[:] or filter()
for item in lst[:]:           # Correct: iterate a copy

# Mistake 2 — sort returns None
lst = [3, 1, 2]
result = lst.sort()           # result is None — sort is in-place
result = sorted(lst)          # Correct: sorted() returns a new list

# Mistake 3 — shallow copy gotcha
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print(a)                      # [[1, 2, 99], [3, 4]] — inner list shared!
import copy
b = copy.deepcopy(a)          # Correct for nested lists

# Mistake 4 — remove raises ValueError if not found
lst.remove(99)                # ValueError — check first: if 99 in lst
# Or: use try/except ValueError

# Mistake 5 — negative indexing confusion
lst = [10, 20, 30]
print(lst[-1])                # 30 (last)
print(lst[-0])                # 10 (same as lst[0] — -0 is 0)
```

---

## Interview Notes

- **When to use:** Dynamic sequence of homogeneous or mixed items; stack (`.append()` + `.pop()`).
- **Stack pattern:** `lst.append(x)` to push, `lst.pop()` to pop — O(1) both.
- **Queue pattern:** Avoid `lst.pop(0)` — it's O(n). Use `collections.deque` for O(1) dequeue.
- **Sorting with key:** `sorted(lst, key=lambda x: x[1])` — sorts by second element of tuples.
- **Comprehension vs map/filter:** List comprehension is more readable; `map`/`filter` are marginally faster in some cases.
- **Complexity summary:**

| Operation | Complexity |
|---|---|
| Index (`lst[i]`) | O(1) |
| Append | O(1) amortized |
| Insert at arbitrary index | O(n) |
| Remove / pop(0) | O(n) |
| Pop last | O(1) |
| Search (`in`) | O(n) |
| Sort | O(n log n) |

---

## Practice Problems

```
01_print_list_elements.py
02_sum_of_list.py
03_count_even_numbers.py
04_find_largest.py
05_find_smallest.py
06_print_first_three_elements.py
07_reverse_list_using_slicing.py
08_list_operations.py
```

---

## Quick Revision

```python
lst = [3, 1, 4, 1, 5]

# Mutating methods (return None)
lst.append(9)        # add to end
lst.insert(0, 7)     # insert at index
lst.remove(1)        # remove first 1
lst.pop()            # remove & return last
lst.sort()           # sort in place
lst.reverse()        # reverse in place

# Non-mutating
sorted(lst)          # new sorted list
len(lst)             # count
sum(lst)             # total
min(lst); max(lst)   # extremes
lst.count(1)         # occurrences
lst.index(4)         # first index of 4
lst[1:3]             # slice
lst[::-1]            # reversed copy

# Comprehension
[x**2 for x in lst]               # squares
[x for x in lst if x % 2 == 0]    # filter even
```
