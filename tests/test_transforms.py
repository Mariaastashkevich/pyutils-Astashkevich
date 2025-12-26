import pytest
import pathlib
import json
from pyutils.__init__ import get_column_stats, filter_rows, group_by


@pytest.fixture
def data():
    p = pathlib.Path("tests/sample.json")
    return json.loads(p.read_text(encoding="utf-8"))


@pytest.mark.parametrize(
    "key, expected",
    [
        ("age", {'min': 22, 'max': 30, 'mean': 27.833333333333332}),
        ("salary", {'min': 2800, 'max': 6000, 'mean': 4300.0})
    ]
)
def test_get_column_stats(data, key, expected):
    result = get_column_stats(data, key)
    assert result == expected


@pytest.mark.parametrize(
    "key, value, expected",
    [
        (
                "age",
                30,
                [
                    {'id': 2, 'name': 'Bob', 'age': 30, 'salary': 4200, 'department': 'HR'},
                    {'id': 4, 'name': 'Diana', 'age': 30, 'salary': 5000, 'department': 'Finance'},
                    {'id': 5, 'name': 'Masha', 'age': 30, 'salary': 6000, 'department': 'IT'},
                    {'id': 6, 'name': 'Nasty', 'age': 30, 'salary': 5000, 'department': 'IT'}]),
        (
                "salary",
                5000,
                [
                    {'id': 4, 'name': 'Diana', 'age': 30, 'salary': 5000, 'department': 'Finance'},
                    {'id': 6, 'name': 'Nasty', 'age': 30, 'salary': 5000, 'department': 'IT'}])
    ]
)
def test_filter_rows(data, key, value, expected):
    result = filter_rows(data, key, value)
    assert result == expected


@pytest.mark.parametrize(
    "key, expected",
    [
        (
                "department",
                {'IT':
                     [{'id': 1, 'name': 'Alice', 'age': 25, 'salary': 2800, 'department': 'IT'},
                      {'id': 3, 'name': 'Charlie', 'age': 22, 'salary': 2800, 'department': 'IT'},
                      {'id': 5, 'name': 'Masha', 'age': 30, 'salary': 6000, 'department': 'IT'},
                      {'id': 6, 'name': 'Nasty', 'age': 30, 'salary': 5000, 'department': 'IT'}],
                 'HR':
                     [{'id': 2, 'name': 'Bob', 'age': 30, 'salary': 4200, 'department': 'HR'}],
                 'Finance':
                     [{'id': 4, 'name': 'Diana', 'age': 30, 'salary': 5000, 'department': 'Finance'}]
                 }
        ),
        (
                "salary",
                {2800:
                     [{'id': 1, 'name': 'Alice', 'age': 25, 'salary': 2800, 'department': 'IT'},
                      {'id': 3, 'name': 'Charlie', 'age': 22, 'salary': 2800, 'department': 'IT'}],
                 4200:
                     [{'id': 2, 'name': 'Bob', 'age': 30, 'salary': 4200, 'department': 'HR'}],
                 5000:
                     [{'id': 4, 'name': 'Diana', 'age': 30, 'salary': 5000, 'department': 'Finance'},
                      {'id': 6, 'name': 'Nasty', 'age': 30, 'salary': 5000, 'department': 'IT'}],
                 6000:
                     [{'id': 5, 'name': 'Masha', 'age': 30, 'salary': 6000, 'department': 'IT'}]}

        )
    ]
)
def test_group_by(data, key, expected):
    result = group_by(data, key)
    assert result == expected
