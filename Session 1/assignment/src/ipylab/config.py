from dataclasses import dataclass

@dataclass(frozen=True)
class LabConfig:
    """
    Lab Configuration.
    '''
    Attributes
    ----------
    sample_rate: int
      Sampling rate of the sensor
    duration_s: float
      Data Collection Period in Seconds
    noise_std: float
      Accepted Noice levels in the data
    median_window: int
      Median Window for the Lab
    chach_size: int
      Data Collection Chache

    Methods
    -------
    """  
    sample_rate: int = 1000
    duration_s: float = 2.0
    noise_std: float = 0.15
    median_window: int = 11
    cache_size: int = 256


