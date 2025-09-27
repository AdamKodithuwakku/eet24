# Optional CLI using typer
import typer, logging
from pathlib import Path
import numpy as np

from .io import load_signal_csv, save_features_csv
from .features import feature_vector

app = typer.Typer(help="Intermediate Python Lab CLI")

@app.command()
def generate_data(out: Path = typer.Option(Path("data/signal.csv"), help="Output CSV path"),
                  n: int = 4000,
                  noise: float = 0.15):
    """
    Generate synthetic signal data (sine + square mixture) and save to CSV.
    TODO:
      - Implement signal synthesis similar to dataset seeded in data/signal.csv
    """
    typer.echo("TODO: implement generate_data")

@app.command()
def run_pipeline(inp: Path = Path("data/signal.csv"),
                 out: Path = Path("data/features.csv"),
                 chunk: int = 256):
    """
    Stream the input CSV in chunks, compute features per chunk, and save to CSV.
    TODO:
      - Use load_signal_csv, slice into chunks, compute feature_vector on each chunk (np.array)
      - Save with save_features_csv
    """
    typer.echo("TODO: implement run_pipeline")

@app.command()
def profile():
    """
    Profile Python vs NumPy RMS on a large array and print timings.
    TODO:
      - Create 1e6 random floats (np.random.randn)
      - Time pure-python and numpy versions; print ms
    """
    typer.echo("TODO: implement profile")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app()
