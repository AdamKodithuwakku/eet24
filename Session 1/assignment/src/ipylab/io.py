from pathlib import Path
import csv
import logging
from typing import Iterable, Sequence

def load_signal_csv(path: Path) -> list[float]:
    """
    Load a single-column CSV of floats into a list.
    """
    
    if not path.is_file():
        raise FileNotFoundError("Could not find file specified")
    
    
    try:
        data = []
        with open(path, "r", newline="") as datafile:
            csvfile = csv.reader(datafile)
            header = next(csvfile)

            if header[0].isdigit():
                data.append(float(header[0]))

            for df in csvfile:
                data.append(float(df[0]))

    except:
        raise ValueError(f"INVALID inputs in {path}.")
    
    else:
        return data

def save_features_csv(path: Path, rows: Iterable[Sequence[float]]) -> None:
    """
    Save a CSV with header: rms,zero_crossings,peak_to_peak,mad
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', newline='') as datafile:
        writer = csv.writer(datafile)
        writer.writerow(["RMS", "0 Crossings", "Peak to Peak", "Mean Abs Diff"])
        writer.writerows(rows)

