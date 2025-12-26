from typing import Mapping, Any, Iterable, Union
from functools import lru_cache
import logging
from .decorators import log_execution_time

logger = logging.getLogger(__name__)


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
) -> list[Mapping[str, Any]]:
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
    grouped_records: dict[Any, list[Mapping[str, Any]]] = {}
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