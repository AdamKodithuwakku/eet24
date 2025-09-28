from typing import Sequence
import numpy as np
import math

def python_rms(seq: Sequence[float]) -> float:
    """
    Pure-Python RMS implementation.
    """
    sqsum = 0.0
    for item in seq:
        sqsum += item * item


    return math.sqrt(sqsum/len(seq))

def numpy_rms(arr: np.ndarray) -> float:
    """
    NumPy-vectorized RMS implementation.
    """
    return np.sqrt(np.mean(np.square(arr)))
