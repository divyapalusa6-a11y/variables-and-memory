---
name: variable-memory-debugging
description: Fix incomplete beginner Python exercises about variable assignment, list references, mutation, and string behavior in the Variables and Memory activity; reproduce the issue, restore the intended demonstration logic, and validate with both runtime output and automated tests.
---

# Variables and Memory debugging workflow

Use this skill when a student is working on the Python exercises in this activity and the code is incomplete, misleading, or not behaving like the lesson intends.

## Goal

Resolve the root cause in the challenge file while preserving the learning objective: demonstrate how Python variables, lists, and references behave.

## Typical problem pattern

The challenge file often contains placeholder comments like "# 1", "# 2", or incomplete function bodies instead of actual demonstration code. This is usually not a Python syntax issue; it is a missing or unfinished demonstration of the lesson concept. The task is to restore the logic that teaches value copying, shared references, and mutation, not just to make the file run.

The agent should also watch for the fact that the project has a main entry point in `main.py`, but the individual challenge script may be incomplete even when the project entry point appears to run without crashing.

## Required workflow

### 1. Reproduce the behavior first

Run the module as the student would:

```bash
cd /Users/newstudent/ada/Developer/activities/variables-and-memory
python main.py
```

If the issue is isolated to one challenge file, also run it directly:

```bash
python challenges/reference_challenges.py
```

This reveals whether the bug is a runtime error, a missing demonstration, or both.

### 2. Inspect the evidence in the target file

Read the challenge file and identify:

- missing assignments or print statements
- placeholder comments that indicate unfinished work
- mutation patterns that should be demonstrated
- accidental variable rebinding versus shared reference behavior

For this activity, the key concepts are:

- value assignment: `x = y` copies the value
- aliasing: `b = a` means both names refer to the same list object
- mutation: `list.append(...)` changes the original list
- reassignment: `word = word + "s"` creates a new string value rather than mutating the old one

### 3. Fix the root cause, not just the symptom

Do not add random prints without preserving the lesson. Instead, repair the functions so they demonstrate the expected behavior clearly.

Examples of correct fixes:

- keep a value-copy example: `papaya = apples` then reassign `apples`
- keep a shared-list example: `b = a` then mutate `b`
- keep a helper mutation example: pass a list to a function and call `.append()`
- add explicit output showing before/after values

Use the smallest possible edit. The point is to teach the concept, not to create a large rewrite.

### 4. Add verification tests if the file is meant to be exercised programmatically

Create a test file such as `test_reference_challenges.py` that validates the intended behavior.

Good tests for this activity include:

- value reassignment does not change the copied variable
- list mutation affects shared references
- empty list mutation works
- string reassignment creates a new value instead of mutating the original
- aliasing: two names referencing the same list should reflect the same mutation

The agent should not assume pytest is installed globally. In this project, it may need to be created in a local virtual environment before running checks:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install pytest
```

Use `pytest` when available and also confirm the stdlib test runner works:

```bash
source venv/bin/activate
pytest -q
python -m unittest -q
```

### 5. Validate before completion

Always run the relevant command after the fix:

```bash
source venv/bin/activate
python challenges/reference_challenges.py
pytest -q
python -m unittest -q
```

The agent should only report success if the outputs confirm the code runs and the tests pass.

## Example completion criteria

A completed task should satisfy all of the following:

- the challenge functions run without crashing
- the printed output clearly demonstrates variable behavior
- the lesson concepts are visible in the actual execution
- tests exercise the expected cases
- all checks pass in the active environment

## Typical lesson-specific expectations

For this repo, the final examples should cover at least these ideas:

1. value-copy behavior in a simple integer example
2. list reference-sharing behavior
3. mutation through a helper function
4. empty list mutation
5. string immutability via reassignment
6. aliasing with multiple variable names sharing the same list

## Gotchas

These are the specific pitfalls that showed up while completing this task:

- The file may look "fine" at a glance because it has valid Python syntax, even though it is missing the educational demonstration logic.
- `main.py` may run without crashing while the challenge file still does not teach the intended concept.
- A list can be mutated through a helper function even when the variable names inside the helper differ from the original call site.
- Reassigning a variable is not the same as mutating a list; `oranges = oranges + 10` does not change the earlier list contents.
- Strings are immutable: `word = word + "s"` creates a new string value rather than modifying the original string in place.
- `pytest` may not be installed in the active environment. The agent should create or activate a local venv before installing and running it.
- Running only `main.py` is not enough validation; the challenge-specific script and tests should also be exercised directly.

## Final response pattern

When finished, report:

- what was broken
- what root cause was found
- what changed
- how it was verified
- the exact commands and evidence from the run
- any gotchas that would trip up a future agent

Example summary:

- The script was incomplete and had missing demonstration code; the real issue was missing educational logic, not a runtime crash.
- I restored the intended value/reference examples and included aliasing, empty-list, and string edge cases.
- Verified with `python challenges/reference_challenges.py`, `pytest -q`, and `python -m unittest -q`.
- Result: all checks passed.
- Gotcha: `pytest` was not installed globally, so the project needed a local venv first.
