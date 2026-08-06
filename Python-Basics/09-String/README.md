# Strings — Traversal, Slicing & Indexing

This topic covers strings as a **sequence** — how to traverse them character by
character, index into them, extract substrings with slicing, and apply the step
parameter for patterns like reversal. It builds on the basics covered in topic 04.

---

## What is it?

String traversal means visiting each character in order — typically with a `for` loop
or by index. String slicing (`s[start:stop:step]`) extracts a contiguous (or stepped)
subsequence from a string without modifying the original.

---

## Why do we use it?

- Parse and search text character by character (palindrome check, vowel count, first non-repeating char).
- Extract substrings for parsing (URLs, file paths, log lines).
- Reverse a string (`[::-1]`) — a classic interview pattern.
- Validate or transform strings one character at a time.

---

## Syntax

```python
# Indexing
s[i]          # character at index i (positive: left-to-right, negative: right-to-left)
s[-1]         # last character
s[-n]         # nth from the end

# Slicing
s[start:stop]          # characters from start up to (not including) stop
s[start:stop:step]     # every 'step'-th character in range

# Traversal with for
for char in s:
    print(char)

# Traversal with index
for i in range(len(s)):
    print(i, s[i])

# Enumerate (index + char together)
for i, char in enumerate(s):
    print(i, char)
```

---

## Parameters

### Slicing `s[start:stop:step]`

| Parameter | Default | Description |
|---|---|---|
| `start` | `0` | Start index (inclusive); negative counts from end |
| `stop` | `len(s)` | End index (exclusive); negative counts from end |
| `step` | `1` | Interval between characters; negative reverses direction |

---

## Return Value

- **Indexing** (`s[i]`) → single-character `str`.
- **Slicing** (`s[a:b]`) → new `str` (empty string if range is invalid).
- **`for` traversal** → no return value; yields one `str` character per iteration.

---

## Example

```python
text = "Python"

# Indexing
print(text[0])        # P
print(text[-1])       # n
print(text[-2])       # o

# Slicing
print(text[0:3])      # Pyt
print(text[:3])       # Pyt
print(text[3:])       # hon
print(text[::-1])     # nohtyP  (reverse)
print(text[::2])      # Pto    (every other char)

# Traversal
for char in text:
    print(char, end=" ")  # P y t h o n
print()

# Count vowels
vowels = sum(1 for c in text.lower() if c in "aeiou")
print(f"Vowels in '{text}': {vowels}")
```

---

## Output

```
P
n
o
Pyt
Pyt
hon
nohtyP
Pto
P y t h o n
Vowels in 'Python': 1
```

---

## Key Points

- Positive indices count left-to-right from `0`; negative count right-to-left from `-1`.
- Slicing never raises `IndexError` — an out-of-range slice returns an empty string.
- `s[::-1]` is the idiomatic Python way to reverse a string — O(n) time and space.
- `step` can be negative to traverse in reverse: `s[5:1:-1]` iterates indices 5, 4, 3, 2.
- `for char in string` is the cleanest traversal — Python handles index management.
- Strings are immutable — slicing creates a new string; you can't assign to a slice.
- `enumerate(s)` gives `(index, character)` pairs — cleaner than `range(len(s))`.

---

## Common Mistakes

```python
# Mistake 1 — IndexError on direct access
s = "abc"
print(s[5])           # IndexError: string index out of range
print(s[5:10])        # "" — slicing never errors

# Mistake 2 — stop index is exclusive
print(s[0:3])         # "abc" (all 3 chars) — NOT s[0], s[1], s[2], s[3]

# Mistake 3 — forgetting negative step reverses start/stop meaning
s = "Python"
print(s[5:0:-1])      # "nohty" — not the full reverse
print(s[::-1])        # "nohtyP" — correct full reverse

# Mistake 4 — trying to mutate via index
s = "hello"
s[0] = "H"            # TypeError — strings are immutable
s = "H" + s[1:]       # Correct

# Mistake 5 — comparing character to multi-char string
for c in s:
    if c == "vowel":  # always False — c is a single char
        pass
if c in "aeiou":      # Correct membership check
    pass
```

---

## Interview Notes

- **Palindrome check:** `s == s[::-1]` — O(n).
- **Reverse a string:** `s[::-1]` — always the expected answer in Python.
- **First non-repeating character:** traverse with `s.count(c) == 1` or a frequency dict.
- **When to use index vs `for`:** Use `for char in s` when you only need the character; use `range(len(s))` or `enumerate` when you need the index too.
- **Complexity:**
  - Indexing: O(1)
  - Slicing `s[a:b]`: O(b-a) — creates a copy
  - Full traversal: O(n)

---

## Practice Problems

```
01_string_traversal.py
02_reverse_string.py
03_direct_traversal.py
04_string_indexing.py
05_count_vowels.py
06_first_non_vowel.py
```

---

## Quick Revision

```python
s = "Python"

# Index
s[0]          # 'P'
s[-1]         # 'n'

# Slice (stop is exclusive)
s[0:3]        # 'Pyt'
s[:3]         # 'Pyt'
s[3:]         # 'hon'
s[::-1]       # 'nohtyP'   reverse
s[::2]        # 'Pto'      every 2nd char

# Traversal
for c in s:   print(c)              # P y t h o n
for i, c in enumerate(s): print(i, c)

# Palindrome
s == s[::-1]   # True / False

# Vowel count
sum(1 for c in s.lower() if c in "aeiou")
```
