# Python Practice Questions

27 questions + 1 mini-project covering the Python fundamentals: basics, control
flow, data structures, functions, functional tools, OOP, and error handling.
Level 1 (Q1–Q18) follows the topics in order; Level 2 (Q19–Q27) mixes them.

**Rules:**

- Use **Python 3.9**, standard library only. No third-party packages.
- Write every answer as a small runnable script — `python3 my_answer.py` must work.
- For "predict the output" questions: **write your prediction down first**, then run
  the code and compare. The gap between prediction and reality is where the learning is.
- If your code crashes, read the full traceback bottom-up before asking anyone.

---

## Basics — Variables, Strings & Truthiness

**Q1. Predict the output**, then run it and check:

```python
a, b = 1, 2
a, b = b, a + b
print(a, b)

print(7 / 2, 7 // 2, 7 % 2)
```

What is the difference between `/` and `//`?

**Q2. String one-liners.** Solve each in a single line:

- Given `s = "  Naman.Jangid@Habilelabs.io  "`, produce `"habilelabs.io"`
  (strip, lowercase, split).
- Format `0.08765` as the string `"8.77%"` using an f-string format spec.
- Reverse the **word order** (not the characters) of `"train the freshers well"`.

**Q3. Truthiness.** Write a function `is_missing(value)` that returns `True` for
`None` and `""` but `False` for `0` and `False`.
Explain in a comment why `value or default` alone cannot do this.
Then rewrite `score >= 0 and score <= 100` as a single chained comparison.

---

## Control Flow

**Q4. Calculator without if/elif.** Rewrite this as a **dict of lambdas** lookup:

```python
if op == "add":   result = a + b
elif op == "sub": result = a - b
elif op == "mul": result = a * b
```

Handle an unknown `op` with a friendly message instead of a crash
(hint: `.get()`).

**Q5. Loop tools.** Two parts:

- Predict, then run:
  ```python
  for i in range(3):
      if i == 5:
          break
  else:
      print("no break happened")
  ```
  When does a loop's `else` run?
- Print each item of `["a", "b", "c"]` with a **1-based** index
  (output: `1. a`, `2. b`, `3. c`) using `enumerate()` — no manual counter.

---

## Data Structures — Lists, Dicts, Sets & Comprehensions

**Q6. The copy gotcha.** Predict, then run, then explain in one comment:

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

Show **two** different ways to make `b` an independent copy of `a`.

**Q7. Slicing skills.**

- Remove duplicates from `[3, 1, 3, 2, 1, 2]` **preserving first-seen order**
  (hint: `dict.fromkeys`). Why is `set()` alone the wrong answer here?
- Rotate `[1, 2, 3, 4, 5]` left by 2 using **only slicing** → `[3, 4, 5, 1, 2]`.

**Q8. Grouping and counting.** Given:

```python
people = [
    {"name": "Priya", "dept": "AI"},
    {"name": "Rahul", "dept": "Web"},
    {"name": "Aman",  "dept": "AI"},
]
```

- Group names by dept into `{"AI": ["Priya", "Aman"], "Web": ["Rahul"]}` using
  `collections.defaultdict`.
- Count the character frequencies of `"habilelabs"` with `collections.Counter`
  and print the 2 most common characters.

**Q9. Comprehensions and sets.**

- Given `requests = [("/home", 200, 0.02), ("/admin", 403, 0.01), ("/api", 200, 0.30)]`,
  build `{path: seconds}` **only** for requests with status 200–299, in one
  dict comprehension.
- Given two lists of emails with mixed upper/lower case, print the emails that
  appear in **both** lists, case-insensitively (use set intersection).

---

## Functions

**Q10. The mutable default bug.** Predict, then run:

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_item("a"))
print(add_item("b"))
```

Explain why the second call prints `['a', 'b']`, then fix it with the
`None`-default pattern.

**Q11. Keyword-only arguments.** Write
`format_currency(amount, *, symbol="₹", decimals=2)` that returns e.g. `₹1,500.00`.
Demonstrate that `format_currency(100, "$")` raises `TypeError`
(catch it and print the message) while `format_currency(100, symbol="$")` works.

**Q12. The late-binding trap.** Predict, then run:

```python
fns = [lambda: i for i in range(3)]
print([f() for f in fns])
```

Why is the result not `[0, 1, 2]`? Fix it so it is (hint: `lambda i=i: i`).

---

## Functional Tools — map, Iterators & Generators

**Q13. Laziness.** Predict, then run:

```python
m = map(str.upper, ["a", "b"])
print(list(m))
print(list(m))
```

Why is the second list empty? What kind of object is `m`?

**Q14. Generators.** Write a generator function `every_nth(iterable, n)` that
lazily yields every n-th item (index 0, n, 2n, …). Prove it is lazy: call it on
`range(10**12)` and print only the first 3 results without your machine hanging
(hint: `itertools.islice`).

---

## Object-Oriented Programming

**Q15. Make a class feel built-in.** Write a `Cart` class holding a list of
items with an `add(item)` method, then implement:

- `__len__` so `len(cart)` returns the item count,
- `__contains__` so `"apple" in cart` works.

**Q16. Frozen dataclass.** Make a frozen `@dataclass` `Money(amount, currency)`:

- `__add__` returns a new `Money` (raise `ValueError` if the currencies differ),
- `__str__` so `print(m)` shows `₹1,500.00`,
- show that assigning to a field of a frozen instance raises an error
  (catch it and print the exception type).

---

## Errors, Exceptions & Context Managers

**Q17. try / finally / return.** Predict the exact print order, then run:

```python
def f():
    try:
        return "returned"
    finally:
        print("finally")

print(f())
```

Then write a loop that asks for a number with `input()` until the user enters a
valid integer, using `try/except ValueError` — maximum 3 attempts, then give up
with a message.

**Q18. Context manager.** Using `contextlib.contextmanager`, write `timer()`
that prints how long the `with` block took:

```python
with timer():
    sum(range(10_000_000))
```

Make sure the time still prints **even if the block raises** — prove it by
running it once with a block that raises `ValueError`.

---

## Level 2 — Mixed Practice

**Q19. Input is always a string.** Write a script that asks the user for two
numbers with `input()` and prints their sum. It must print `15`, not `"105"`,
when the user enters `10` and `5`.

**Q20. FizzBuzz.** One loop from 1 to 30, no nested ifs: multiples of 3 print
`Fizz`, of 5 print `Buzz`, of both print `FizzBuzz`, everything else prints the
number. Think about the order of your conditions — why must the "both" check
come first?

**Q21. Tuples.** Write `min_max(nums)` that returns both the minimum and maximum
as a tuple, then unpack the result into two variables in one line. Then build a
dict `cache` keyed by `(user_id, endpoint)` tuples, and show that using a
**list** as a key raises an error (catch it and print the exception type).
Why do tuples work as dict keys but lists don't?

**Q22. Safe nested access.** Given `data = {"user": {"address": {"city": "Jaipur"}}}`,
read the city safely, and read the missing `data["user"]["phone"]["code"]`
**without crashing** — chained `.get()` calls with default values.

**Q23. Flexible signatures.** Write `describe(*args, **kwargs)` that prints how
many positional and how many keyword arguments it received. Call it three
different ways: only positional, only keyword, and a mix.

**Q24. Closures.** Write `once(fn)` that returns a wrapped function which calls
`fn` only the first time; every later call returns the first result without
calling `fn` again. No classes allowed — this is a closure exercise. Prove it
works with a counter.

**Q25. Advanced sorting.** Given:

```python
users = [
    {"name": "Zoya", "age": 25, "salary": 60},
    {"name": "Aman", "age": 30, "salary": 90},
    {"name": "Ravi", "age": 25, "salary": 75},
]
```

- Sort by **age descending, then name ascending**, with a single `key=` lambda
  returning a tuple.
- Find the 2 highest-paid users **without** sorting the whole list
  (hint: `heapq.nlargest`).

**Q26. The mutable class attribute bug.** Predict, then run:

```python
class Team:
    members = []
    def add(self, name):
        self.members.append(name)

a, b = Team(), Team()
a.add("Priya")
print(b.members)
```

Why does `b` see Priya? Fix the class so every `Team` gets its own list.

**Q27. Two error-handling styles.** `user = {"name": "Priya"}` may or may not
have an `"email"` key. Read it with a fallback in **two** styles:

- LBYL ("look before you leap") — check with `in` first,
- EAFP ("easier to ask forgiveness than permission") — `try/except KeyError`.

Which style is considered idiomatic Python, and when would you still prefer
the other?

---

## Mini-project — Log Analyzer (combines everything)

Put this list at the top of your script:

```python
LOGS = [
    "2026-09-09 10:01:22 INFO /home 200 0.031",
    "2026-09-09 10:01:25 ERROR /api/users 500 1.202",
    "2026-09-09 10:02:01 INFO /login 200 0.089",
    "2026-09-09 10:02:14 WARN /admin 403 0.011",
    "2026-09-09 10:02:20 ERROR /api/users 500 0.977",
    "2026-09-09 10:03:05 INFO /home 200 0.025",
    "bad line that should not crash the parser",
    "2026-09-09 10:03:40 INFO /api/orders 201 0.310",
]
```

Requirements:

1. Parse each line into a dict `{"time", "level", "path", "status", "seconds"}` —
   `status` as `int`, `seconds` as `float`. A malformed line must **not** crash
   the script: raise and catch a custom `ParseError`, and count the bad lines.
2. Print the number of requests per `level` (use `Counter`).
3. Print the average response time per `path`, sorted slowest first
   (use `defaultdict(list)`, a dict comprehension, and `sorted` with a `key=`).
4. Print the set of paths that ever returned a 5xx status.
5. Wrap the report in a `banner(title)` context manager that prints
   `=== title ===` before the block and `=== end ===` after it, even on error.
6. Guard everything with `if __name__ == "__main__":`.

A correct solution touches string parsing, unpacking, loops, dicts, sets,
comprehensions, functions, `Counter`/`defaultdict`, custom exceptions, and a
context manager — every concept from the sections above.

---

*Work in order — later questions assume the earlier ones. Discuss approaches with
each other, but type every solution yourself.*
