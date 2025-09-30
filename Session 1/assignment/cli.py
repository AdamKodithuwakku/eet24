# Optional CLI using typer
import typer, logging
from pathlib import Path
import numpy as np
import csv
import itertools
import operator
import functools
import time 

from dataclasses import dataclass

from src.ipylab.context import timer
from src.ipylab.io import load_signal_csv, save_features_csv
from src.ipylab.features import feature_vector
from src.ipylab.vectorize import python_rms, numpy_rms
from src.ipylab.generators import chunks
from src.ipylab.config import LabConfig
from src.ipylab.decorators import timed

app = typer.Typer(help="Intermediate Python Lab CLI")

@dataclass(slots=True)
class SlotedDataClass:
    x: int
    y: int

@dataclass
class RegularDataClass:
    x: int
    y: int

@app.command()
def rolling_sum(inp: Path = typer.Option(Path("data/signal.csv"), help="Input Singal Data"), out: Path = typer.Option(Path("data/rolling.csv"), help="Output CSV path")):
    """
    Create the Rolling sum for the given input fiel
    """
    data = load_signal_csv(inp)
    rolling_sum = np.array(itertools.accumulate(data)).reshape([-1, 1])
    
    with open(out, "w", newline="") as datafile:
        csvwrite = csv.writer(datafile)
        csvwrite.writerow("Rolling Sum")
        csvwrite.writerows(rolling_sum)

@app.command()
def rolling_mul(inp: Path = typer.Option(Path("data/signal.csv"), help="Input Singal Data"), out: Path = typer.Option(Path("data/rollingmul.csv"), help="Output CSV path")):
    """
    Calculate the Rolling Multiplication for the given input file
    """
    data = load_signal_csv(inp)
    rolling_mul = np.array(itertools.accumulate(data)).reshape([-1, 1])
    
    with open(out, "w", newline="") as datafile:
        csvwrite = csv.writer(datafile)
        csvwrite.writerow("Rolling mul")
        csvwrite.writerows(rolling_mul)

@app.command()
def pairwise(inp: Path = typer.Option(Path("data/signal.csv"), help="Input Singal Data"), out: Path = typer.Option(Path("data/pairwise.csv"), help="Output CSV path")):
    """
    Calculate the Pair wise for the given input file
    """
    data = load_signal_csv(inp)
    pairwise_diff = np.array([b-a for a, b in itertools.pairwise(data)]).reshape([-1,1])
    
    with open(out, "w", newline="") as datafile:
        csvwrite = csv.writer(datafile)
        csvwrite.writerow("Pairwise Difference")
        csvwrite.writerows(pairwise_diff)

@app.command()
def tricommand(inp: Path = typer.Option(Path("data/signal.csv"), help="Input Singal Data"), out: Path = typer.Option(Path("data/tri.csv"), help="Output CSV path")):
    """
    Create the Rolling sum for the given input fiel
    """
    data = load_signal_csv(inp)
    
    rollingsum = list(itertools.accumulate(data))
    rollingmul = list(itertools.accumulate(data, operator.mul))
    
    pairwisediff = [data[0]]+[b-a for a, b in itertools.pairwise(data)]
    
    tridata = np.array([rollingsum, rollingmul, pairwisediff])
    
    with open(out, "w", newline="") as datafile:
        csvwrite = csv.writer(datafile)
        csvwrite.writerow(["Rolling Sum", "Rolling multiplication","Pairwise Difference"])
        csvwrite.writerows(tridata.T)
    



@app.command() ##### This decorator needs to be on top; others
@timed(threshold_ms=1)
@functools.lru_cache(maxsize=None) 
def sleepy(n: int = 5):
    """
        Expensive Function with Chaching.
    """
    time.sleep(1)
    return n*2

@app.command()
def sleepytwo(n: int = 5):
    sleepy(n) 
    sleepy(n) # second files is calcualted from cache





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
    logging.basicConfig(filename='my_app.log', level=logging.INFO)
    app()
    
