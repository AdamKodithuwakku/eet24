import numpy as np
from typing import Sequence

def feature_vector(x: np.ndarray) -> list[float]:
    """
    Compute basic features for 1D signal x:
      - RMS
      - zero-crossings (count)
      - peak-to-peak (max - min)
      - mean absolute diff (MAD)
    Use NumPy vectorized ops only.
    Return as [rms, zc, p2p, mad].
    TODO: implement.
    """
    # TODO: implement
    return [0.0, 0.0, 0.0, 0.0]
