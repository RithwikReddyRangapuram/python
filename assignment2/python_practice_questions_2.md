# Python Practice Questions — Set 2

14 questions + 1 mini-project covering today's topics: **working with JSON,
files & paths, modules & imports, and type hints.**

**Rules (same as Set 1):**

- Use **Python 3.9**, standard library only. No third-party packages.
- Every answer must be a **runnable script** — `python3 my_answer.py` must work.
- For "predict the output" questions: **write your prediction down first**, then
  run the code and compare.
- Type hints on 3.9: use `Optional[str]` / `Union[int, str]` — the `str | None`
  syntax needs Python 3.10+.
- If your code crashes, read the full traceback bottom-up before asking anyone.

---

## Working with JSON

**Q1. The four functions.** In one comment line each, state the difference
between `json.dumps`, `json.loads`, `json.dump`, `json.load`.
Then predict what happens for each of these — and run them:

```python
import json
print(json.loads(json.dumps((1, 2, 3))))    # what comes back — tuple or list?
print(json.dumps({1: "a"}))                 # what happens to the int key?
print(json.dumps({(1, 2): "b"}))            # and to a tuple key?
```

**Q2. Pretty printing.** Given:

```python
order = {"customer": "Priya", "total": 1499.5, "currency": "₹",
         "items": [{"sku": "A1", "qty": 2}, {"sku": "B7", "qty": 1}]}
```

print it as JSON that is (a) indented by 2 spaces, (b) has sorted keys, and
(c) shows the `₹` symbol as-is instead of a `₹` escape.

**Q3. Teaching dumps new types.** `json.dumps` refuses `datetime` and `set`
values. Build a payload containing both, show the `TypeError` (catch and print
it), then write a `json_default(obj)` function and pass it via
`json.dumps(payload, default=...)` so the datetime becomes an ISO string and
the set becomes a sorted list. Any other unknown type must still raise
`TypeError`.

**Q4. Dataclass round-trip.** Define `@dataclass User(name: str, age: int)`.
Serialize an instance to a JSON string (hint: `dataclasses.asdict`), then
deserialize that string back into a real `User` object (hint: `**`), and prove
the round-trip worked with `==`.

---

## Files & Paths

**Q5. Path anatomy.** Using `pathlib.Path`, build the path
`reports/2026/sales.json` (with `/`, not string concatenation) and print its
`name`, `stem`, `suffix`, and `parent`. Then explain in one comment why a
script should resolve data files with `Path(__file__).resolve().parent`
instead of a plain relative path like `Path("data.json")`.

**Q6. Write, append, read.** In a `data/` folder **created by your script**
(`mkdir` with the right flags so re-running never crashes):

- write `"line 1\n"` to `notes.txt`,
- append `"line 2\n"` to it (mind the mode — what would `"w"` have done?),
- read the file back and print it with line numbers.

Every open/read/write must pass `encoding="utf-8"`.

**Q7. Robust JSON store.** Write two functions:

- `load_json(path)` — returns the parsed data; returns `{}` if the file
  doesn't exist; raises a clear `ValueError` (chained with `from`) if the file
  exists but contains invalid JSON.
- `save_json(path, data)` — **atomic** write: dump to a temporary file next to
  the target first, then `replace()` it over the real one, so a crash mid-write
  can never leave a half-written file.

Demonstrate all three cases: missing file, corrupt file (write `"{oops"` into
one), and a successful round-trip.

**Q8. Directory walk.** Print every `.py` file under a folder tree
(recursively, hint: `rglob`), each with its size in bytes, then print the
total count and total size. Run it on the `_python` folder.

---

## Modules & Imports

**Q9. Modules run once.** Create `config.py` containing a top-level
`print("loading config")` and `settings = {"debug": True}`. In `main.py`,
import it **twice** (two import statements) and predict how many times the
message prints. Then mutate `config.settings["debug"] = False` in `main.py`
and explain in a comment why every other module that imports `config` would
see the change.

**Q10. The shadowing trap.** In a fresh folder, create a file named
`random.py` containing `print("I am the fake random")`, and next to it
`main.py` with:

```python
import random
print(random.randint(1, 6))
```

Run `main.py`, read the error carefully, and explain in comments: **why** did
Python load your file instead of the standard library's (in what order does
Python search for modules?), and what is the rule that prevents this bug?
Then fix it by renaming and show it working.

**Q11. Build a package.** Create this structure and make it work:

```
myutils/
    __init__.py      # re-export slugify so `from myutils import slugify` works
    text.py          # slugify("Hello World!") -> "hello-world"
main.py              # imports from myutils and prints slugify("Python Is Fun")
```

`text.py` must also have an `if __name__ == "__main__":` block with a quick
self-test, and you must show both ways of running it:
`python3 main.py` and `python3 -m myutils.text`.

---

## Type Hints

**Q12. Annotate it.** Add full type hints (3.9 syntax) to these functions —
then add one comment answering: does Python itself stop you from calling
`total(["a", "b"])`? Why or why not?

```python
def total(prices, tax=0.18):          # takes a list of floats, returns a float
    return sum(prices) * (1 + tax)

def find_user(users, name):           # list of dicts (str -> str); returns a
    for u in users:                   # matching dict OR None
        if u["name"] == name:
            return u
    return None
```

**Q13. TypedDict.** Define a `TypedDict` called `Contact` with fields
`name: str`, `phone: str`, `email: Optional[str]`. Write
`summarize(contacts: list[Contact]) -> dict[str, int]` that returns
`{"total": ..., "with_email": ...}`. Create three contacts (one without an
email) and print the summary.

**Q14. Narrowing.** Write `describe(x: Union[int, str]) -> str` that returns
`"number: <x+1>"` for ints and the uppercased string for strs, using an
`isinstance` check. Then (if you can) `pip install mypy` and run
`mypy your_file.py` — first with correct calls, then add
`describe([1, 2])` and see what mypy says **without running the code**.

---

## Mini-project — Contacts Book (combines everything)

Build a small contacts manager backed by a JSON file, structured as a package:

```
contacts_app/
    __init__.py          # re-export the public functions
    storage.py           # all file/JSON handling lives here
main.py                  # the demo script
```

Requirements:

1. **`storage.py`** — a `Contact` TypedDict (`name: str`, `phone: str`,
   `email: Optional[str]`), and fully type-hinted functions:
   - `load_contacts(path: Path) -> list[Contact]` — missing file → `[]`;
     corrupt JSON → a clear `ValueError` chained with `from`.
   - `save_contacts(path: Path, contacts: list[Contact]) -> None` — atomic
     write (temp file + `replace`), `indent=2`, `ensure_ascii=False`.
   - `add_contact(contacts, contact)` — reject a duplicate phone number by
     raising a custom `DuplicateContactError`.
   - `find_contact(contacts, name) -> Optional[Contact]`.
2. **`main.py`** — resolves `contacts.json` **relative to `__file__`**, then:
   adds 3 contacts, tries to add a duplicate (catch and report the error),
   searches for one that exists and one that doesn't, saves, and prints the
   file's size in bytes afterwards. Guard it all with
   `if __name__ == "__main__":`.
3. Running `python3 main.py` **twice in a row** must work — the second run
   loads the existing file first and must not crash on the duplicates it now
   finds (handle it, don't avoid it).

A correct solution touches JSON (de)serialization, `pathlib`, atomic writes,
error handling with custom exceptions, a real package with `__init__.py`
re-exports, and type hints throughout — everything from today.

---

*Discuss approaches with each other, but type every solution yourself.*
