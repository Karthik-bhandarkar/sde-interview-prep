# Topic 10: Tuples — Practice Set (10 Problems)

---

### Problem 01: Create and Print a Tuple
**Question:** Create a tuple with your name, age, and city, then print it.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
person = ("Karthik", 21, "Bengaluru")
print(person)
```
**Why a tuple instead of a list here:** This data represents a fixed record that
shouldn't change once created (a person's name/age/city snapshot) — tuples signal
"this shouldn't be modified," which is useful documentation for anyone reading your code.
</details>

---

### Problem 02: Indexing and Slicing
**Question:** From a tuple of numbers, print the first element, last element, and a slice.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = (10, 20, 30, 40, 50)
print("First:", numbers[0])
print("Last:", numbers[-1])
print("Slice:", numbers[1:4])
```
**Why indexing/slicing looks identical to lists:** Tuples and lists are both
"sequences" in Python, so read access works the same way — the difference only shows
up when you try to CHANGE them (see next problem).
</details>

---

### Problem 03: Immutability Check
**Question:** Try to change an element of a tuple and observe what happens. Write a
comment explaining the error.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = (10, 20, 30)
# numbers[0] = 99  # This line would raise: TypeError: 'tuple' object does not support item assignment
print("Tuples cannot be modified after creation — this is what 'immutable' means.")
```
**Why immutability is a feature, not a limitation:** Because tuples can't change,
Python can use them as dictionary keys and store them more efficiently than lists.
Use a tuple exactly when you want a guarantee that the data won't be accidentally
modified elsewhere in your program.
</details>

---

### Problem 04: Unpacking a Tuple
**Question:** Unpack a tuple containing name, age, and city directly into three variables.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
person = ("Karthik", 21, "Bengaluru")
name, age, city = person
print("Name:", name)
print("Age:", age)
print("City:", city)
```
**Why unpacking beats indexing:** `person[0]`, `person[1]`, `person[2]` works but
tells you nothing about what each index MEANS. Unpacking into named variables
(`name, age, city`) makes the code self-documenting.
</details>

---

### Problem 05: Count Occurrences
**Question:** Given a tuple with repeated values, count how many times a value appears.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = (1, 2, 2, 3, 2, 4)
print("Count of 2:", numbers.count(2))
```
**Why tuples still have some methods:** Even though tuples are immutable, read-only
operations like `.count()` and `.index()` are still available — immutability only
blocks methods that would CHANGE the tuple's contents.
</details>

---

### Problem 06: Find Index of an Element
**Question:** Given a tuple, find the index of a specific value using `.index()`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
fruits = ("apple", "banana", "mango", "grape")
print("Index of mango:", fruits.index("mango"))
```
**Note:** `.index()` raises a `ValueError` if the value isn't found at all — worth
knowing before you use it on data you're not 100% sure contains the value.
</details>

---

### Problem 07: Convert List to Tuple and Back
**Question:** Convert a list into a tuple, then convert that tuple back into a list.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print("As tuple:", my_tuple)

back_to_list = list(my_tuple)
print("Back to list:", back_to_list)
```
**When you'd actually do this:** A common real pattern is receiving data as a tuple
(e.g., from a database row or function return), converting to a list to modify it,
then converting back to a tuple if you need to "lock" it again afterward.
</details>

---

### Problem 08: Concatenate Two Tuples
**Question:** Combine two tuples into one using `+`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)
```
**Why this creates a new tuple:** Just like lists, `+` never modifies either
original — it builds a brand new tuple. Since tuples can't be modified in place
anyway, this is actually the ONLY way to "combine" them.
</details>

---

### Problem 09: Max, Min, Sum of a Tuple
**Question:** Given a tuple of numbers, find the max, min, and sum.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = (23, 67, 12, 89, 45)
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
```
**Why these built-ins work on tuples too:** `max()`, `min()`, and `sum()` work on any
iterable, not just lists — this is a good sign you're starting to see lists and
tuples as "two flavors of the same idea" (ordered collections) rather than unrelated things.
</details>

---

### Problem 10: Nested Tuple Access
**Question:** Given a tuple of tuples (each representing a student's name and marks),
print each student's name and marks.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
students = (("Karthik", 88), ("Raj", 76), ("Priya", 92))
for name, marks in students:
    print(name, "scored", marks)
```
**Why unpacking works directly in the for-loop:** `for name, marks in students`
unpacks each inner tuple automatically as it loops — this pattern (looping over
tuples of pairs) is exactly how you'll later loop over dictionary `.items()`.
</details>
