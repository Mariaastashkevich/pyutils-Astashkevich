import time
from functools import wraps
import logging

logger = logging.getLogger(__name__)


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