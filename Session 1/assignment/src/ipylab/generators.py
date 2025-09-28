from collections import deque
from statistics import median
from typing import Iterable, Iterator, TypeVar, Deque, Optional

T = TypeVar("T", int, float)

def chunks(iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    """
    Yield lists of length `size` from `iterable`.
    """
    chunk = []

    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    
    #Last chunk may be shorter.
    if chunk:
        yield chunk
        


def moving_average(window: int):
    """
    Stateful GENERATOR that yields the moving average each time a new value is sent.
    """
    history = deque(maxlen=window)
    total = float(0)
    count = float(0)

    while True: # This is never getting stuck on this; because we are yeilding every time the fucn is called
        value = yield total / count if count > 0 else 0.0

        if value is None: continue # without this gives an error ???

        if(len(history) >= window):
            history.popleft()

        history.append(window)
        total += value
        count = len(history)


def moving_median(window: int):
    """
    Stateful GENERATOR that yields the moving median each time a new value is sent.
    """
    history = Deque(maxlen=window)

    while True:       
        value = yield median(sorted(history)) if history else 0.0
        if value is None: 
            continue 

        if(len(history) >= window):
            history.popleft()
        history.append(value)
