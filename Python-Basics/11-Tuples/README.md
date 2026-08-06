# Tuples & Tuple Methods

Tuples are ordered, immutable collections of items. They are similar to lists, but
once created, they cannot be modified (no adding, removing, or changing elements).
They are typically used for grouped, related data that should not change throughout
the program's lifecycle.

---

## What is it?

A `tuple` is a fixed-size sequence of elements defined by a comma-separated list of values,
typically enclosed in parentheses `()`. Because they are immutable, they are hashable,
which means they can be used as keys in dictionaries or elements in sets (unlike lists).

---

## Why do we use it?

- **Safety:** Prevent accidental modification of data (e.g., configurations, coordinates).
- **Performance:** Iteration and creation are slightly faster than lists due to fixed size and memory efficiency.
- **Dictionary Keys:** Serve as composite keys (e.g., `{(x, y): value}`).
- **Multiple Returns:** Used by functions to return multiple values.

---

## Syntax

```python
# Creation
empty = ()
single_element = (5,)          # comma is required!
coordinates = (10.0, 20.0)
mixed = (1, "hello", 3.14)

# Without parentheses (Tuple packing)
packed = 1, 2, 3

# Unpacking
a, b, c = packed

# Indexing & Slicing (same as lists)
first = coordinates[0]
subset = mixed[1:3]
```

---

## Parameters

### Common Tuple Methods

Since tuples are immutable, they only have two methods:

| Method | Signature | Description |
|---|---|---|
| `.count(x)` | — | Returns the number of times `x` appears in the tuple |
| `.index(x)` | — | Returns the index of the first occurrence of `x` (raises ValueError if not found) |

### Built-in Functions on Tuples

| Function | Description |
|---|---|
| `len(t)` | Number of elements |
| `sum(t)` | Sum of numeric elements |
| `min(t)` / `max(t)` | Minimum / maximum element |
| `sorted(t)` | Returns a new **list** of sorted elements |
| `tuple(iterable)` | Converts an iterable (like a list) into a tuple |

---

## Return Value

- `.count(x)` → `int`
- `.index(x)` → `int`
- Unpacking a tuple assigns individual values to the target variables.

---

## Example

```python
# Tuple creation and packing
point = 10, 20, 30
print(type(point))       # <class 'tuple'>

# Unpacking
x, y, z = point
print(f"x: {x}, y: {y}, z: {z}")

# Tuple methods
nums = (1, 2, 2, 3, 4, 2)
print(nums.count(2))     # 3
print(nums.index(4))     # 4

# Function returning multiple values (returns a tuple)
def get_user():
    return "Alice", 25

name, age = get_user()
print(f"{name} is {age}")
```

---

## Output

```
<class 'tuple'>
x: 10, y: 20, z: 30
3
4
Alice is 25
```

---

## Key Points

- A trailing comma is mandatory for a single-element tuple: `(5,)` is a tuple, `(5)` is just an integer in parentheses.
- Tuples can contain mutable objects (like lists). The tuple itself can't be resized or re-assigned, but the inner mutable object *can* be modified: `t = (1, [2, 3])`, `t[1].append(4)` is valid.
- Parentheses are optional for tuple packing: `a = 1, 2, 3` is perfectly valid.
- Function returns with multiple comma-separated values are automatically packed into a tuple.

---

## Common Mistakes

```python
# Mistake 1 — forgetting the comma for a single-element tuple
t = ("apple")
print(type(t))         # <class 'str'>
t = ("apple",)
print(type(t))         # <class 'tuple'>

# Mistake 2 — trying to mutate a tuple
t = (1, 2, 3)
t[0] = 99              # TypeError: 'tuple' object does not support item assignment

# Mistake 3 — unpacking mismatch
t = (1, 2, 3)
a, b = t               # ValueError: too many values to unpack (expected 2)
a, b, c, d = t         # ValueError: not enough values to unpack (expected 4, got 3)

# Fix: Use * to gather remaining items
a, *rest = t           # a=1, rest=[2, 3]
```

---

## Interview Notes

- **List vs Tuple:** Expect this question. Key differences: Mutability (List=Mutable, Tuple=Immutable), syntax (`[]` vs `()`), and use-cases (dynamic collections vs static configurations/records).
- **Hashability:** Tuples can be used in `set`s or as `dict` keys *only if* all their elements are hashable. `(1, 2)` works as a key, `(1, [2])` does not.
- **Memory:** `sys.getsizeof(tuple)` is smaller than `sys.getsizeof(list)` for the same elements.
- **Complexity:** Indexing `t[i]` is O(1), same as lists.

---

## Practice Problems

*No practice problems currently available in this folder.*

---

## Quick Revision

```python
# Single element
t = (5,)

# Packing / Unpacking
t = 1, 2, 3
a, b, c = t

# Methods
t.count(2)
t.index(1)

# Immutability
# t[0] = 5  -> TypeError

# Swap idiom (uses tuple packing/unpacking)
a, b = b, a
```
