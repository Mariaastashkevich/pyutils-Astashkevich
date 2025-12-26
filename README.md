# pyutils

A Python utility library for data transformation, file I/O operations, and performance monitoring. This package provides idiomatic Python functions with type hints, comprehensive error handling, logging, and caching capabilities.

## Features

- **Data Transformation Functions**: Filter, group, and analyze data from lists of dictionaries
- **File I/O Utilities**: Safe JSON file loading and saving with custom error handling
- **Performance Monitoring**: Execution time logging decorator
- **Caching**: LRU cache support for expensive computations
- **Type Safety**: Full type hints throughout the codebase
- **Structured Logging**: Comprehensive logging with timestamps and log levels
- **Error Handling**: Custom exceptions with helpful error messages

## Installation

This project requires Python 3.13 or higher.

### Using uv (Recommended)

```bash
uv sync
```

### Using pip

```bash
pip install -e .
```

## Project Structure

```
pyutils-Astashkevich/
├── pyutils/
│   ├── __init__.py          # Package exports
│   ├── transforms.py        # Data transformation functions
│   ├── io.py                # File I/O operations
│   ├── decorators.py        # Custom decorators
│   └── errors.py            # Custom exceptions
├── tests/
│   ├── __init__.py
│   ├── test_transforms.py   # Unit tests
│   └── sample.json          # Test data
├── main.py                  # Example usage
├── logging_config.py        # Logging configuration
├── pyproject.toml           # Project configuration
└── README.md
```

## Usage

### Basic Example

```python
import logging
from pyutils import filter_rows, group_by, get_column_stats, load_json, save_json
from logging_config import configure_logging
import pathlib

# Configure logging
configure_logging(level=logging.INFO)

# Load data from JSON file
data = load_json(pathlib.Path('tests/sample.json'))

# Filter records
filtered = filter_rows(data, key='salary', value=5000)

# Group records
grouped = group_by(data, key='department')

# Calculate statistics
stats = get_column_stats(data, key='age')
print(stats)  # {'min': 22, 'max': 30, 'mean': 27.833333333333332}

# Save data to file
save_json(data, pathlib.Path('output.json'))
```

## API Reference

### Data Transformation Functions

#### `filter_rows(data, key, value)`

Filters records from a list of dictionaries based on a key-value match.

**Parameters:**
- `data` (Iterable[Mapping[str, Any]])`: List of dictionaries to filter
- `key` (str)`: Key to filter by
- `value` (Any)`: Value to match

**Returns:**
- `list[Mapping[str, Any]]`: Filtered list of dictionaries

**Example:**
```python
data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
result = filter_rows(data, key='age', value=30)
# [{'name': 'Bob', 'age': 30}]
```

#### `group_by(data, key)`

Groups records by a specified key.

**Parameters:**
- `data` (Iterable[Mapping[str, Any]])`: List of dictionaries to group
- `key` (str)`: Key to group by

**Returns:**
- `dict[Any, list[Mapping[str, Any]]]`: Dictionary with grouped records

**Example:**
```python
data = [{'name': 'Alice', 'dept': 'IT'}, {'name': 'Bob', 'dept': 'HR'}]
result = group_by(data, key='dept')
# {'IT': [{'name': 'Alice', 'dept': 'IT'}], 'HR': [{'name': 'Bob', 'dept': 'HR'}]}
```

#### `get_column_stats(data, key)`

Calculates min, max, and mean for a numeric column.

**Parameters:**
- `data` (Iterable[Mapping[str, Any]])`: List of dictionaries
- `key` (str)`: Key of the numeric column

**Returns:**
- `dict[str, float]`: Dictionary with 'min', 'max', and 'mean' keys

**Raises:**
- `ValueError`: If no numeric values are found for the key

**Example:**
```python
data = [{'age': 25}, {'age': 30}, {'age': 22}]
result = get_column_stats(data, key='age')
# {'min': 22, 'max': 30, 'mean': 25.666666666666668}
```

#### `normalize(data)`

Normalizes numeric data by subtracting the mean from each value. Uses LRU cache for performance.

**Parameters:**
- `data` (tuple[Union[float, int], ...])`: Tuple of numeric values

**Returns:**
- `tuple[float, ...]`: Normalized tuple

**Example:**
```python
data = tuple([1, 2, 3, 4, 5])
result = normalize(data)
# (-2.0, -1.0, 0.0, 1.0, 2.0)
```

### File I/O Functions

#### `load_json(path)`

Safely loads a list of dictionaries from a JSON file.

**Parameters:**
- `path` (pathlib.Path)`: Path to the JSON file

**Returns:**
- `list[dict[str, Any]]`: Parsed JSON data

**Raises:**
- `JsonLoadError`: If the file cannot be loaded (file not found, permission denied, or invalid JSON)

**Example:**
```python
from pathlib import Path
data = load_json(Path('data.json'))
```

#### `save_json(data, path)`

Saves a list of dictionaries to a JSON file.

**Parameters:**
- `data` (Any)`: Data to save (typically list of dictionaries)
- `path` (pathlib.Path)`: Path where to save the file

**Example:**
```python
from pathlib import Path
save_json([{'name': 'Alice'}], Path('output.json'))
```

### Decorators

#### `@log_execution_time`

Decorator that logs the execution time of a function.

**Example:**
```python
from pyutils.decorators import log_execution_time

@log_execution_time
def my_function():
    # Function implementation
    pass
```

## Error Handling

The package includes custom exceptions for better error handling:

### `JsonLoadError`

Raised when a JSON file cannot be loaded. Provides specific error messages for:
- File not found
- Permission denied
- Invalid JSON format
- Other unexpected errors

**Example:**
```python
from pyutils.errors import JsonLoadError
from pyutils import load_json
from pathlib import Path

try:
    data = load_json(Path('nonexistent.json'))
except JsonLoadError as e:
    print(f"Error loading JSON: {e}")
```

## Testing

Run the test suite using pytest:

```bash
pytest
```

The test suite includes:
- Parametrized tests for `get_column_stats`
- Parametrized tests for `filter_rows`
- Parametrized tests for `group_by`

Test data is located in `tests/sample.json`.

## Type Checking and Linting

### Type Checking with mypy

Ensure the code passes mypy checks:

```bash
mypy pyutils/
```

### Running the Example

Execute the main example:

```bash
python main.py
```

## Logging

The package uses Python's standard `logging` module with structured logging. Configure logging using the `configure_logging` function:

```python
from logging_config import configure_logging
import logging

configure_logging(level=logging.INFO)
```

Log format includes:
- Timestamp with milliseconds
- Module name and line number
- Logger name
- Log level
- Message

## Performance Features

- **Execution Time Logging**: All transformation functions are decorated with `@log_execution_time` to monitor performance
- **LRU Caching**: The `normalize` function uses `@lru_cache` for efficient repeated computations

## Requirements

- Python >= 3.13
- pytest >= 9.0.2
- pytest-mock >= 3.15.1

## Development

### Setting Up Development Environment

1. Clone the repository
2. Install dependencies using `uv sync` or `pip install -e .`
3. Run tests: `pytest`
4. Type check: `mypy pyutils/`

### Code Style

- Type hints are used throughout the codebase
- List comprehensions are preferred where appropriate
- Error messages are descriptive and helpful
- Functions include docstrings

## License

This project is part of a practical task assignment.

## Author

Maryia Astashkevich
