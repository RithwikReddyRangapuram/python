# Python Practice Questions — Set 3

14 questions + 1 mini-project covering: **async Python (asyncio)** and the
**standard library** — collections, dates & times, regular expressions, and the
everyday modules (hashlib, uuid, random, logging).

**Rules (same as Sets 1 and 2):**

- Use **Python 3.9**, standard library only. No third-party packages.
- Every answer must be a **runnable script** — `python3 my_answer.py` must work.
- For "predict the output" questions: **write your prediction down first**, then
  run the code and compare.
- If your code crashes, read the full traceback bottom-up before asking anyone.

---

## Async Python (asyncio)

**Q1. Coroutines don't run by themselves.** Predict what this prints (and
what warning appears), then run it:

```python
import asyncio

async def greet():
    print("hello from the coroutine")

greet()                      # no await, no asyncio.run
print("end of script")
```

Then fix it so `hello from the coroutine` actually prints. What exactly does
calling an `async def` function return?

**Q2. Prove concurrency with a clock.** Write
`async def fetch(name, seconds)` that sleeps `seconds` (the async way!) and
returns `f"{name} done"`. Then time two versions with `time.perf_counter()`:

- `sequential()` — awaits `fetch("a", 1)` then `fetch("b", 1)` → ~2 s
- `concurrent()` — runs both with `asyncio.gather` → ~1 s

Print both measured times. Why is the second one twice as fast?

**Q3. When one task fails.** Make one of three gathered coroutines raise
`ValueError("boom")` while the other two succeed. Run the gather twice:

- default — what happens to the overall result? (catch and print it)
- with `return_exceptions=True` — print the results list; what type sits in
  the failed slot?

**Q4. Limit concurrency.** You have 6 jobs of 1 second each. Run them all with
`gather`, but use `asyncio.Semaphore(2)` so **at most 2 run at the same time**.
Measure the total time — explain why it lands near 3 seconds, not 1 and not 6.

---

## collections

**Q5. Counter.** Given a paragraph of text (pick any 4–5 sentences), print the
3 most common words — case-insensitive, ignoring punctuation
(hint: `str.lower`, `re.findall(r"[a-z]+", ...)` or `split` + `strip`).
Then show what `Counter` returns for a word that never appeared — why is that
nicer than a plain dict?

**Q6. deque.** Two small tasks:

- Build a "recently viewed" tracker with `deque(maxlen=3)`: push 6 page names
  through it and print it after each push — what happens to the oldest entry?
- In one comment line: why is `deque.popleft()` a better queue than
  `list.pop(0)`?

---

## Dates & Times

**Q7. The datetime round trip.** In one script:

- print the current time **UTC-aware** (not naive),
- print it as an ISO string,
- parse `"2026-09-14T10:30:00"` back into a `datetime`
  (hint: `fromisoformat`),
- print that parsed moment as `14 Sep 2026, 10:30 AM` using `strftime`.

**Q8. timedelta.** Two parts:

- Given a deadline of `2026-12-31`, print how many days are left from today —
  computed, not hard-coded.
- Print the date of **every Monday in the next 4 weeks**, starting from today
  (hint: `date.weekday()` — Monday is `0` — and a `timedelta` loop).

**Q9. Timezones.** Parse `"2026-07-30T14:45:30+00:00"` (a UTC moment) and
print the same moment in **Asia/Kolkata** time (hint: `zoneinfo.ZoneInfo`).
Print both, and the hour difference you observe. Why must you never do this
math by adding `timedelta(hours=5, minutes=30)` yourself?

---

## Regular Expressions

**Q10. Extract patterns.** From
`tweet = "Loving #python and #asyncio! Thanks @priya_dev and @aman for the tips #100DaysOfCode"`,
extract all hashtags into one list and all mentions into another, using
`re.findall`. (`['python', 'asyncio', '100DaysOfCode']` and
`['priya_dev', 'aman']`.)

**Q11. Validate and normalise.** Write `normalize_phone(raw)` that accepts
Indian numbers in messy forms — `"98765 43210"`, `"+91-9876543210"`,
`"09876543210"` — and returns the bare 10-digit string, or `None` if it isn't
a valid mobile number after cleaning. Use `re.sub` to strip separators and
`re.fullmatch` to validate. Why `fullmatch` and not `search` here?

**Q12. Replace with a function.** Convert `"user_first_name"` to
`"userFirstName"` using `re.sub` with a **lambda** as the replacement
(hint: the pattern is `_([a-z])`, and the lambda gets a match object).

---

## Standard Library Grab-bag

**Q13. Hashing, ids, reproducible randomness.** In one script:

- print the SHA-256 hex digest of the string `"habilelabs"`
  (mind the bytes/str difference — what happens without `.encode()`?),
- print a random UUID4,
- set `random.seed(42)` and print 3 dice rolls — run the script twice and
  confirm the rolls repeat. When is seeding useful, and when would it be a bug?

**Q14. logging over print.** Take this and rewrite it with the `logging`
module (`basicConfig` with a format that shows time + level + message):

```python
print("starting up")
print("connecting to db")
print("WARNING: retrying connection")
print("ERROR: could not connect")
```

Use the correct level for each line, set the level to `INFO`, and add one
`logging.debug(...)` line — why doesn't it appear, and what one-line change
makes it appear? Name two things logging gives you that `print` can't.

---

## Mini-project — Website Monitor (combines everything)

Simulate a monitoring tool that checks a list of sites **concurrently** and
prints a report. No real network calls — fake the latency with
`asyncio.sleep`.

```python
SITES = [
    "https://example.com",
    "https://api.example.com/health",
    "not a url",
    "https://shop.example.com",
    "ftp://old.example.com",       # wrong scheme — invalid
    "https://blog.example.com",
]
```

Requirements:

1. **Validate** each entry with a regex (`https://` + domain, use
   `re.fullmatch`). Log invalid ones with `logging.warning` and skip them.
2. `async def check_site(url)` — sleeps a random 0.1–1.0 s
   (`random.uniform`), then returns a dict:
   `{"url", "status", "seconds", "checked_at"}` where `status` is
   `random.choice([200, 200, 200, 500, 503])` and `checked_at` is a
   **UTC-aware ISO timestamp**.
3. Run all checks with `asyncio.gather` under an `asyncio.Semaphore(2)`
   (max 2 concurrent). Call `random.seed(1)` at the start so runs are
   reproducible.
4. Report, using the tools from this set:
   - each result via `logging.info` (url, status, seconds),
   - a `Counter` of statuses (how many 200 / 500 / 503),
   - the slowest site (`max` with a `key=`),
   - total wall-clock time vs the **sum** of individual times — print both
     and state in one sentence what that difference proves.
5. Guard with `if __name__ == "__main__":` and one `asyncio.run(main())`.

A correct solution touches coroutines, gather, Semaphore, regex validation,
timezone-aware datetimes, Counter, logging, and seeded randomness — everything
from this set.

---

*Discuss approaches with each other, but type every solution yourself.*
