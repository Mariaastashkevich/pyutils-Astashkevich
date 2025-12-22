from typing import Mapping, Any, Iterable, Union
import time
from functools import wraps, lru_cache
from frozendict import frozendict
import logging
import pathlib


logger = logging.getLogger(__name__)
# def freezeargs(func):
#     """Convert a mutable dictionary into immutable.
#         Useful to be compatible with lru_cache
#         """
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         arg_iterable = [arg for arg in args if isinstance(arg, Iterable)][0]
#         not_iterable_args = (arg for arg in args if not isinstance(arg, Iterable))
#         freeze_arg = tuple([frozendict(row) for row in arg_iterable])
#
#         args = freeze_arg + tuple(not_iterable_args)
#         kwargs = {k: frozendict(v) if isinstance(v, dict) else v for k, v in kwargs.items()}
#         result = func(*args, **kwargs)
#         return result
#     return wrapper


def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            duration = time.perf_counter() - start_time
            logger.info(
                "Function %s took %.6f seconds to execute",
                func.__name__,
                duration,
            )
    return wrapper

@log_execution_time
def get_column_stats(
        data: Iterable[Mapping[str, Any]],
        key: str
) -> dict[str, float]:
    """ Calculates min, max, mean for numeric column """
    logger.info(
        "Calculating statistics for key: %s ...",
        key
    )
    values = [row[key] for row in data if isinstance(row.get(key), (float, int))]
    if not values:
        raise ValueError(f'No numeric values for {key}')
    stats_dict = {
        'min': min(values),
        'max': max(values),
        'mean': sum(values) / len(values),
    }
    logger.debug(
        "Statistics for key %s were successfully calculated, stats: %s",
        key,
        stats_dict
    )
    return stats_dict


@log_execution_time
def filter_rows(
        data: Iterable[Mapping[str, Any]],
        key: str,
        value: Any
) -> list[Mapping]:
    """ Filters records from list of dicts """
    logger.info(
        "Filtering records for key %s over value: %s ...",
        key,
        value
    )
    filtered_records = [item for item in data if item.get(key) == value]
    logger.debug(
        "Filtered %d records successfully for key %s = %r !",
        len(filtered_records),
        key,
        value
    )
    return filtered_records


@log_execution_time
def group_by(
        data: Iterable[Mapping[str, Any]],
        key: str
) -> dict[Any, list[Mapping[str, Any]]]:
    """ Groups records by key """
    logger.info(
        "Grouping records for key %s ...",
        key
    )
    grouped_records = {}
    for item in data:
        item_key = item.get(key)
        if item_key not in grouped_records:
            grouped_records[item_key] = []
        grouped_records[item_key].append(item)
    logger.debug(
        "Records for key %s were successfully grouped!",
        key
    )
    return grouped_records


@lru_cache(maxsize=None)
@log_execution_time
def normalize(
        data: tuple[Union[float, int], ...],
) -> tuple[float, ...]:
    """ Normalizes numeric records """
    mean = sum(data) / len(data)
    logger.info(
        "Normalizing numeric records with mean %s ...",
        mean
    )
    normalized_data = tuple(x - mean for x in data)
    logger.debug(
        "Numeric records were successfully normalized!",
    )
    return normalized_data


def load_json(path):
    """ Safely loads list-of-dicts from JSON file """
    p = pathlib.Path(path)


def save_json(data, path):
    """ Saves list-of-dicts to JSON file """







