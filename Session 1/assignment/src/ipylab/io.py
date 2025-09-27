from pathlib import Path
import csv
import logging
from typing import Iterable, Sequence

def load_signal_csv(path: Path) -> list[float]:
    """
    Load a single-column CSV of floats into a list.
    TODO:
      - Validate that path exists and is a file; else raise FileNotFoundError
      - Read rows; parse as float; collect into list
      - Use try/except to catch ValueError and log it (then re-raise)
    """
    # TODO: implement
    return []

def save_features_csv(path: Path, rows: Iterable[Sequence[float]]) -> None:
    """
    Save a CSV with header: rms,zero_crossings,peak_to_peak,mad
    TODO:
      - Ensure parent dir exists (mkdir parents=True, exist_ok=True)
      - Write header and rows via csv.writer
    """
    # TODO: implement
    pass
