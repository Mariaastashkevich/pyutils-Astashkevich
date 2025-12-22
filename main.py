# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "frozendict>=2.4.7",
# ]
# ///
import logging
from pyUtils import *
from common import configure_logging

logger = logging.getLogger(__name__)

def main():
    configure_logging(level=logging.INFO)
    logger.warning('Starting main()')
    test_group_by = [
        {'name': 'Alice', 'city': 'Minsk'},
        {'name': 'Bob', 'city': 'Moskow'},
        {'name': 'Kate', 'city': 'Dubai'},
        {'name': 'Alex', 'city': 'Minsk'},
        {'name': 'Maria', 'city': 'Moskow'},
    ]
    test_column_stats = [
        {'name': 'Alice', 'age': 23},
        {'name': 'Bob', 'age': 24},
        {'name': 'Kate', 'age': 67},
        {'name': 'Alex', 'age': 43},
        {'name': 'Maria', 'age': 18},
    ]
    test_filter_rows = [
        {'name': 'Alice', 'age': 23},
        {'name': 'Bob', 'age': 24},
        {'name': 'Kate', 'age': 67},
        {'name': 'Alex', 'age': 23},
        {'name': 'Maria', 'age': 23},
    ]
    test_normalize = tuple([x for x in range(1, 1000)])
    normalize(test_normalize)

    print(group_by(test_group_by, key='city'))
    print(get_column_stats(test_column_stats, key='age'))
    print(filter_rows(test_filter_rows, key='age', value=23))

    logger.warning('Finishing main()')

if __name__ == "__main__":
    main()
