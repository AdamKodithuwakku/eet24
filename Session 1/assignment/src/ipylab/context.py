from contextlib import contextmanager
import time
import logging
from typing import Iterator

@contextmanager
def timer(label: str) -> Iterator[None]:
    """
    Context manager that logs how long the block took (in ms).
    
    Args:
      label (str): Timer Message
    Returns:
      Iterator
    """
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        logging.getLogger(__name__).info(f"{label} {(end-start)*1000} ms")

@contextmanager
def suppress_and_log(*exc_types: type[BaseException]) -> Iterator[None]:
    """
    Context manager that suppresses given exception types and logs the exception.
    
    Args:
      exc_types: type[BaseException]
    
    Returns:
      Iterator
    """
    try:
        yield
    except exc_types as e:
        logging.getLogger(__name__).exception(str(e))
    finally:
        pass
