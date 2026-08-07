# Topic 09: Lists — Practice Set (15 Problems)

---

### Problem 01: Create and Print a List
**Question:** Create a list of 5 favorite movies and print it.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
movies = ["Inception", "Interstellar", "Titanic", "Avatar", "Gladiator"]
print(movies)
```
**Why lists over separate variables:** Once you have a *collection* of related items,
a list lets you loop, sort, search, and modify them together — five separate
variables `movie1, movie2, ...` can't do any of that.
</details>

---

### Problem 02: Indexing and Slicing
**Question:** From a list of numbers, print the first element, the last element, and
a slice of the middle 3 elements.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = [10, 20, 30, 40, 50, 60, 70]
print("First:", numbers[0])
print("Last:", numbers[-1])
print("Middle 3:", numbers[2:5])
```
**Why `-1` for last:** Negative indexing counts from the end, so you never need to
know the list's length just to grab the last item — this avoids `numbers[len(numbers)-1]`.
</details>

---

### Problem 03: Add Elements
**Question:** Start with a list of 3 fruits. Add one fruit to the end, and insert
another at position 1.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
fruits.insert(1, "grape")
print(fruits)
```
**Append vs insert:** `append()` always adds to the end (fast, O(1)); `insert()` puts
it at a specific position but has to shift every element after it (slower, O(n)).
Use insert only when position genuinely matters.
</details>

---

### Problem 04: Remove Elements
**Question:** From a list, remove one element by value using `remove()`, and another
by position using `pop()`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
numbers.pop(0)
print(numbers)
```
**remove() vs pop():** `remove(value)` searches for and deletes the first match by
VALUE (errors if not found); `pop(index)` deletes by POSITION and also returns the
removed item. Choose based on whether you know the value or the position.
</details>

---

### Problem 05: Sort Ascending and Descending
**Question:** Sort a list of numbers in ascending order, then descending order.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = [45, 12, 89, 3, 27]
numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)
```
**Why `sort(reverse=True)` over reversing after sorting:** Passing `reverse=True`
sorts descending directly in one pass — calling `.sort()` then `.reverse()`
separately works but does two operations for something one argument handles.
</details>

---

### Problem 06: Reverse a List
**Question:** Reverse a list two ways: using `.reverse()` and using slicing `[::-1]`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print("Using reverse():", numbers)

original = [1, 2, 3, 4, 5]
print("Using slicing:", original[::-1])
```
**Key difference:** `.reverse()` mutates the original list in place; `[::-1]` returns
a NEW reversed list and leaves the original untouched. Choose based on whether you
need to keep the original order elsewhere.
</details>

---

### Problem 07: Find Max and Min
**Question:** Given a list of numbers, find the maximum and minimum using built-in functions.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = [34, 12, 89, 5, 67]
print("Max:", max(numbers))
print("Min:", min(numbers))
```
**Why use built-ins here (unlike For-Loop Problem 8):** You already practiced writing
the manual loop version — now that you understand the logic underneath, use the
built-in in real code. Knowing both is the point; manual loops teach the concept,
built-ins are what you'd actually ship.
</details>

---

### Problem 08: Sum and Average
**Question:** Given a list of numbers, calculate the sum and average.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)
```
**Why `len()` for the count:** The list itself already knows how many elements it
holds — never hardcode a count that the data structure can tell you directly, since
hardcoded counts break the moment the list changes size.
</details>

---

### Problem 09: Check Membership
**Question:** Given a list of names, check whether a specific name exists in it.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
names = ["Karthik", "Raj", "Priya", "Anu"]
search_name = input("Enter a name to search: ")
if search_name in names:
    print(search_name, "found in the list")
else:
    print(search_name, "not found")
```
**Why `in` beats a manual loop:** `in` internally does the searching for you — write
the manual for-loop version once to understand it (you sort of already did, in
For-Loop Problem 8's spirit), then use `in` afterward for real code.
</details>

---

### Problem 10: Count Occurrences
**Question:** Given a list with repeated numbers, count how many times a specific
number appears using `.count()`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = [1, 2, 2, 3, 2, 4, 2, 5]
target = 2
print(f"{target} appears", numbers.count(target), "times")
```
**When count() is the right tool:** Use `.count()` when you only need the frequency
of ONE value. If you needed frequencies of ALL values at once, a dictionary (next
topic) is the better tool — recognizing which tool fits which shape of problem is key.
</details>

---

### Problem 11: Merge Two Lists
**Question:** Merge two lists of numbers into one, using both `+` and `.extend()`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_with_plus = list1 + list2
print("Using +:", merged_with_plus)

list1.extend(list2)
print("Using extend():", list1)
```
**+ vs extend():** `+` creates a brand NEW list and leaves both originals unchanged;
`.extend()` modifies `list1` in place, adding list2's elements into it directly. Pick
`+` when you need to keep the originals intact.
</details>

---

### Problem 12: Remove Duplicates
**Question:** Given a list with duplicate numbers, produce a list with only unique values.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = [1, 2, 2, 3, 4, 4, 5, 1]
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)
```
**Why set() works but changes order:** A `set` can't contain duplicates by
definition, so converting to a set and back to a list strips them out automatically
— but sets don't preserve original order. If order matters, you'd loop and check
membership manually instead.
</details>

---

### Problem 13: List Comprehension — Squares
**Question:** Create a list of squares of numbers from 1 to 10 using a list comprehension.

**Think about it:**
- You already know how to do this with a for loop appending to an empty list — list
  comprehension is the same idea condensed into one line.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
squares = [x ** 2 for x in range(1, 11)]
print(squares)
```
**Why comprehension over a for-loop+append:**
```python
# The longer equivalent:
squares = []
for x in range(1, 11):
    squares.append(x ** 2)
```
Comprehensions are shorter and often faster, but only use them when the loop body is
a SINGLE simple expression — if the logic needs multiple steps or conditionals inside,
a regular loop is more readable.
</details>

---

### Problem 14: Second Largest Number
**Question:** Given a list of numbers, find the second largest value.

**Think about it:**
- Sorting the list first makes this trivial — think about which index holds it after sorting.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = [45, 12, 89, 3, 89, 27]
unique_sorted = sorted(set(numbers), reverse=True)
print("Second largest:", unique_sorted[1])
```
**Why `set()` before sorting:** If the largest value appears twice (like 89 here),
plain sorting would put the duplicate in the "second largest" spot — converting to a
set first removes duplicates so index `[1]` is a genuinely different value.
</details>

---

### Problem 15: Split into Even and Odd Lists
**Question:** Given a list of numbers, split them into two separate lists: evens and odds.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
numbers = [10, 15, 22, 33, 40, 51, 68]
evens = []
odds = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
print("Evens:", evens)
print("Odds:", odds)
```
**Why not one list with tags:** You could store `("even", 10)` tuples in one list,
but two clean, purpose-named lists are simpler to use afterward (no unpacking or
filtering needed) — prefer the data shape that matches how you'll actually use the result.
</details>
