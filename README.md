# pyutils-Astashkevich
Create and organize a Python package pyutils/
Implement the following functions using idiomatic Python:

filter_rows(data, key, value) – filter records from list of dicts

group_by(data, key) – group records by key

get_column_stats(data, key) – calculate min, max, mean for numeric column
Include type hints, helpful error messages, and use comprehensions.

Add decorators for logging and caching

Create a @log_execution_time decorator to log how long each function takes

Use @lru_cache from functools on any pure function that can benefit from caching (e.g., expensive computation or simulated delay)

All logs should go through the standard logging module and be structured (e.g., include timestamps and levels)

Implement a minimal file I/O layer using pathlib

load_json(path) – safely load list-of-dicts from JSON file

save_json(data, path) – save results to file

Use match-case to handle different types of file read exceptions and raise custom errors

Add unit tests

Write at least 2 test functions using pytest for your core logic (e.g., get_column_stats, filter_rows)

Place them in tests/test_transforms.py

Add test data in tests/sample.json

Type-check and lint your code

Ensure the code passes mypy checks

Write a proper README.md

Once you complete your practical task and your dev branch is clean and ready:

Create a Pull Request from dev to main for review.