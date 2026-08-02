# 09 - String Traversal & Manipulation

Practice problems covering string iteration patterns (index-based traversal, reverse traversal, direct character iteration), indexing, vowel counting, and search algorithms in Python. Part of the [SDE Interview Prep](https://github.com/Karthik-bhandarkar/sde-interview-prep) series under `Python-Basics`.

## 📋 Problems

| # | Problem | File | Difficulty | Concepts |
|---|---------|------|------------|----------|
| 01 | String Traversal | [`01_string_traversal.py`](./01_string_traversal.py) | Easy ⭐ | `for i in range(len(s))`, Indexing |
| 02 | Reverse String | [`02_reverse_string.py`](./02_reverse_string.py) | Easy ⭐ | Reverse index iteration `range(len-1, -1, -1)` |
| 03 | Direct Traversal | [`03_direct_traversal.py`](./03_direct_traversal.py) | Easy ⭐ | `for ch in s` direct iteration |
| 04 | String Indexing | [`04_string_indexing.py`](./04_string_indexing.py) | Easy ⭐ | Positive & negative indexing (`s[0]`, `s[-1]`, `s[-2]`) |
| 05 | Count Vowels | [`05_count_vowels.py`](./05_count_vowels.py) | Easy ⭐⭐ | Membership test `ch in "aeiouAEIOU"`, Counter |
| 06 | First Non-Vowel | [`06_first_non_vowel.py`](./06_first_non_vowel.py) | Easy ⭐⭐ | Linear search, Early exit with `break` |

---

## 📝 Problem Details

### 01. String Traversal
Print each character of a string on a new line using index-based loop (`range(len(s))`).

```python
s = input()

for i in range(len(s)):
    print(s[i])
```

- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$

---

### 02. Reverse String
Print string characters in reverse order without modifying the original string.

```python
s = input()
last_index = len(s) - 1

for i in range(last_index, -1, -1):
    print(s[i], end="")
```

- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$

---

### 03. Direct Traversal
Print each character of a string directly using `for ch in s` without `len()` or indexing.

```python
s = input()

for ch in s:
    print(ch)
```

- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$

---

### 04. String Indexing
Extract specific boundary characters (first, last, second, second last) using positive and negative indices.

```python
s = input()

print(s[0])   # First character
print(s[-1])  # Last character
print(s[1])   # Second character
print(s[-2])  # Second last character
```

- **Time Complexity:** $O(1)$
- **Space Complexity:** $O(1)$

---

### 05. Count Vowels
Count total uppercase and lowercase vowels in a string using membership test.

```python
s = input()
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print(count)
```

- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$

---

### 06. First Non-Vowel
Find and print the first non-vowel character in a string using linear search with early termination (`break`).

```python
s = input()

for ch in s:
    if ch not in "aeiouAEIOU":
        print(ch)
        break
```

- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$

---

## ▶️ How to Run

```bash
python 01_string_traversal.py
```

---

## 🎯 Key Takeaways

- **Direct Traversal (`for ch in s`)** is cleaner when index positions are not needed.
- **Index Traversal (`range(len(s))`)** is necessary when index positions matter during iteration.
- **Reverse Indexing (`range(len-1, -1, -1)`)** provides linear reverse scanning.
- The `in` operator combined with a vowel set (`"aeiouAEIOU"`) performs efficient $O(1)$ membership checks per character.

---

*Author: Karthik Bhandarkar*
