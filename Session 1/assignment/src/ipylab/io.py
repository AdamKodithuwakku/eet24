from pathlib import Path
import pandas as pd
import csv
import os
import logging
from typing import Iterable, Sequence

def load_signal_csv(path: Path) -> list[float]:
    """
    Load a single-column CSV of floats into a list.
    """
    
    if not path.exists():
        raise FileNotFoundError("Could not find file specified")
    
    try:
        data = pd.read_csv(path, header=None, dtype={0: float})
    except:
        raise ValueError(f"INVALID inputs in {path}.")
    return data

def save_features_csv(path: Path, rows: Iterable[Sequence[float]]) -> None:
    """
    Save a CSV with header: rms,zero_crossings,peak_to_peak,mad
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', newline='') as datafile:
        writer = csv.writer()
        writer.writerow(["RMS", "0 Crossings", "Peak to Peak", "Mean Abs Diff"])
        writer.writerows(rows)

