# Optional CLI using typer
import typer, logging
from pathlib import Path
import numpy as np
import csv

from src.ipylab.context import timer
from src.ipylab.io import load_signal_csv, save_features_csv
from src.ipylab.features import feature_vector
from src.ipylab.vectorize import python_rms, numpy_rms
from src.ipylab.generators import chunks
from src.ipylab.config import LabConfig

app = typer.Typer(help="Intermediate Python Lab CLI")

@app.command()
def generate_data(out: Path = typer.Option(Path("data/signal.csv"), help="Output CSV path"), n: int = 4000, noise: float = 0.15):
    """
    Generate synthetic signal data (sine + square mixture) and save to CSV.
    """

    labdata = LabConfig()

    time_elapsed = np.linspace(0, labdata.duration_s, n)
    
    sine_wave = np.sin(time_elapsed)
    square_wave = np.square(time_elapsed)

    pure_signal = sine_wave + square_wave
    noise_variation = np.random.normal(noise, labdata.noise_std, [n])
    noicy_signal = noise_variation + pure_signal

    noicy_signal = noicy_signal.reshape(-1, 1)

    with open(out, "w", newline="") as datafile:
        writer = csv.writer(datafile)
        writer.writerow(["Signal"])
        writer.writerows(noicy_signal)


@app.command()
def run_pipeline(inp: Path = Path("data/signal.csv"), out: Path = Path("data/features.csv"), chunk: int = 256):
    """
    Stream the input CSV in chunks, compute features per chunk, and save to CSV.
    """
    data = load_signal_csv(inp)
    pychunks = chunks(data, chunk)
    
    features = []
    for chunk in pychunks:
        feature = feature_vector(np.array(chunk))
        features.append(feature)

    save_features_csv(out, features)


@app.command()
def profile():
    """
    Profile Python vs NumPy RMS on a large array and print timings.
    """
    data = np.random.randn(10**6)
    with timer("Pure Python RMS"):
        python_rms(data)
    
    with timer("Numpy RMS"):
        numpy_rms(np.array(data))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app()
    
