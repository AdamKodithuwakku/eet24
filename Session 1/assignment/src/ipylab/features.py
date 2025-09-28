import numpy as np
from typing import Sequence
from .vectorize import numpy_rms
from .generators import moving_median

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
    rms = numpy_rms(x)

    zero_crossings = len(np.where(np.diff(np.sign(x)) != 0)[0]) # count where sign is different

    peak_to_peak = np.max(x) - np.min(x)

    mean = np.mean(x)
    meanabsdiff = np.mean(np.abs(x - mean))


    return [rms, zero_crossings, peak_to_peak, meanabsdiff]
