import time, logging, functools
from typing import Callable, TypeVar, Any, ParamSpec, Optional

P = ParamSpec("P")
T = TypeVar("T")

def timed(threshold_ms: Optional[float] = None) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Decorator that logs runtime; if threshold_ms is set and runtime exceeds it,
    logs a WARNING, else INFO.
    """
    def decorate(fn: Callable[P, T]) -> Callable[P, T]:
        @functools.wraps(fn)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            start_time = time.perf_counter()
            result = fn(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed_time_sec = end_time - start_time
            elapsed_time_ms = elapsed_time_sec * 1000
            print(elapsed_time_ms)

            if threshold_ms is not None and elapsed_time_ms > threshold_ms:
                log_message = f"SLOW: {fn.__name__} took {elapsed_time_ms:.2f} ms"
                logging.getLogger(__name__).warning(log_message)
            else:
                log_message = f"{fn.__name__} took {elapsed_time_ms:.2f} ms"
                logging.getLogger(__name__).info(log_message)

            return result
        return wrapper
    return decorate
