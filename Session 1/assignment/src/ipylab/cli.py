# Optional CLI using typer
import typer, logging
from pathlib import Path
import numpy as np
from .context import timer
from .io import load_signal_csv, save_features_csv
from .features import feature_vector
from .vectorize import python_rms, numpy_rms
from .generators import chunks
import csv

app = typer.Typer(help="Intermediate Python Lab CLI")

@app.command()
def generate_data(out: Path = typer.Option(Path("data/signal.csv"), help="Output CSV path"), n: int = 4000, noise: float = 0.15):
    """
    Generate synthetic signal data (sine + square mixture) and save to CSV.
    """
    timeT = np.linspace(0, 100, n)
    sine_wave = np.sin(2*np.pi*timeT)
    square_wave = np.square(2*np.pi*timeT)
    signal = sine_wave + square_wave
    noise = np.random(0, noise, n)
    noicy_signal = noise+signal

    with open(out, "w") as datafile:
        writer = csv.writer(datafile)
        writer.writerows(noicy_signal)

@app.command()
def run_pipeline(inp: Path = Path("data/signal.csv"), out: Path = Path("data/features.csv"), chunk: int = 256):
    """
    Stream the input CSV in chunks, compute features per chunk, and save to CSV.
    """
    data = load_signal_csv(inp.absolute)
    pychunks = chunks(data, chunk)
    features = feature_vector(pychunks)

    save_features_csv(features, out)


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
    
