import time, logging, functools
from typing import Callable, TypeVar, Any, ParamSpec, Optional

P = ParamSpec("P")
T = TypeVar("T")

def timed(threshold_ms: Optional[float] = None) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Decorator that logs runtime; if threshold_ms is set and runtime exceeds it,
    logs a WARNING, else INFO.
    TODO:
      - Use functools.wraps
      - Measure with time.perf_counter
      - Log "SLOW: {fn.__name__} took {ms:.2f} ms" when exceeding threshold
    """
    def decorate(fn: Callable[P, T]) -> Callable[P, T]:
        # TODO: implement
        return fn  # placeholder
    return decorate
