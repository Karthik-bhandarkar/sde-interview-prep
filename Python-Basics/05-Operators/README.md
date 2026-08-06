# Operators

Operators are symbols that perform operations on values and variables. Python
provides six categories: arithmetic, comparison, logical, assignment, membership,
and identity. Understanding operator precedence and short-circuit evaluation is
essential for writing correct, predictable code.

---

## What is it?

An operator takes one or more operands and produces a result. Python operators
are built into the language — no import required — and work across all core types
(`int`, `float`, `str`, `bool`, `list`, etc.) with type-specific behavior.

---

## Why do we use it?

- Perform calculations, comparisons, and logical decisions in a single expression.
- Assignment operators (`+=`, `*=`, etc.) make update operations concise.
- `in` and `is` answer the two most common runtime questions: membership and identity.

---

## Syntax

```python
# Arithmetic
+   -   *   /   //   %   **

# Comparison  (always return bool)
==  !=  >   <   >=  <=

# Logical
and   or   not

# Assignment (augmented)
=   +=  -=  *=  /=  //=  %=  **=

# Membership
in    not in

# Identity
is    is not
```

---

## Parameters

### Arithmetic Operators

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` (float) |
| `//` | Floor Division | `10 // 3` | `3` (int) |
| `%` | Modulus | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 10` | `1024` |

### Comparison Operators

| Operator | Meaning |
|---|---|
| `==` | Equal in value |
| `!=` | Not equal |
| `>` / `<` | Greater / Less than |
| `>=` / `<=` | Greater or equal / Less or equal |

### Logical Operators

| Operator | Behaviour |
|---|---|
| `and` | `True` if both operands are truthy |
| `or` | `True` if at least one operand is truthy |
| `not` | Inverts the boolean value |

### Membership & Identity

| Operator | Use |
|---|---|
| `in` / `not in` | Check if item exists in a sequence |
| `is` / `is not` | Check if two variables point to the same object |

---

## Return Value

| Category | Returns |
|---|---|
| Arithmetic | `int` or `float` (division `/` always returns `float`) |
| Comparison | `bool` |
| Logical | The actual operand value (truthy/falsy), not always `bool` |
| Assignment | No return value (statement) |
| Membership | `bool` |
| Identity | `bool` |

---

## Example

```python
# Arithmetic
print(10 // 3)          # 3      (floor division)
print(10 % 3)           # 1      (remainder)
print(2 ** 8)           # 256    (exponentiation)

# Comparison
print(10 > 5)           # True
print(10 == 10.0)       # True   (value equality)

# Logical (short-circuit)
print(True and False)   # False
print(False or True)    # True
print(not True)         # False

# Augmented assignment
x = 10
x += 5
print(x)                # 15

# Membership
fruits = ["apple", "banana"]
print("apple" in fruits)   # True

# Identity
a = [1, 2]
b = a
print(a is b)              # True  (same object)
print(a is [1, 2])         # False (different object, equal value)
```

---

## Output

```
3
1
256
True
True
False
True
False
15
True
True
False
```

---

## Key Points

- `/` always returns a `float`; use `//` for integer division.
- `==` checks **value equality**; `is` checks **object identity** (memory address).
- `and` / `or` **short-circuit**: `and` stops at the first falsy value, `or` stops at the first truthy value.
- `and` / `or` return the **deciding operand**, not necessarily `True`/`False`: `0 or "default"` → `"default"`.
- Operator precedence (high → low): `**` → unary `- +` → `* / // %` → `+ -` → comparisons → `not` → `and` → `or`.
- `x < y < z` is valid Python — it chains comparisons.
- Augmented assignment (`+=`) modifies the variable in place for mutable types but creates a new object for immutables like `int` and `str`.

---

## Common Mistakes

```python
# Mistake 1 — using = instead of ==
if x = 10:            # SyntaxError
if x == 10:           # Correct

# Mistake 2 — is vs ==
a = 256
b = 256
a is b                # True — CPython caches small ints (-5 to 256)
a = 1000
b = 1000
a is b                # False (may vary) — don't use is for value comparison

# Mistake 3 — integer vs float division
print(7 / 2)          # 3.5 (not 3)
print(7 // 2)         # 3

# Mistake 4 — misreading short-circuit return
print(0 or "hello")   # 'hello' — not True
print(1 and "hello")  # 'hello' — not True

# Mistake 5 — precedence surprise
print(2 + 3 * 4)      # 14, not 20 — * binds tighter than +
```

---

## Interview Notes

- **When to use `//` over `/`:** Anytime you need an integer result — array indexing, binary search midpoints, etc.
- **`%` (modulus) patterns:** Even/odd check `n % 2 == 0`, cyclic wrap `i % n`, last digit `n % 10`.
- **`is` rule:** Only use `is` to check `None`, `True`, `False` — never for integers or strings.
- **Short-circuit idiom:** `value = user_input or "default"` is idiomatic Python for defaults.
- **Complexity:** All basic operators are O(1) except `**` which is O(log exponent) for large integers.

---

## Practice Problems

```
01_addition.py
02_arithmetic_operations.py
03_operator_precedence.py
04_augmented_assignment.py
05_math_functions.py
06_calculator.py
07_discount.py
08_profit_loss.py
09_percentage.py
10_power_calculator.py
```

---

## Quick Revision

```python
# Arithmetic
10 + 3    # 13     10 - 3    # 7
10 * 3    # 30     10 / 3    # 3.333 (float)
10 // 3   # 3      10 % 3    # 1
2 ** 8    # 256

# Augmented
x = 5; x += 3   # x = 8

# Comparison → bool
10 > 5    # True    10 == 10.0  # True

# Logical (short-circuit)
True and False   # False
False or True    # True
not True         # False

# Membership / Identity
"a" in "abc"     # True
x is None        # use is only for None/True/False
```
