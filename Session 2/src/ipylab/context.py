from contextlib import contextmanager
import time
import logging
from typing import Iterator

@contextmanager
def timer(label: str) -> Iterator[None]:
    """
    Context manager that logs how long the block took (in ms).
    TODO:
      - Record start time
      - Yield control
      - On exit, compute elapsed ms and log with INFO level using logging.info
    """
    # TODO: implement
    yield

@contextmanager
def suppress_and_log(*exc_types: type[BaseException]) -> Iterator[None]:
    """
    Context manager that suppresses given exception types and logs the exception.
    Example:
        with suppress_and_log(ValueError):
            int("not int")  # won't crash; logs the error
    TODO:
      - Wrap the body in try/except for the given exc_types
      - On exception, log with logging.exception and do NOT re-raise
    """
    # TODO: implement
    yield
