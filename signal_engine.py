
import numpy as np
from scipy.signal import periodogram

SCENARIOS = [
    "Baseline",
    "Elevated Activity",
    "Transient Event"
]


def generate_signal(sample_rate=5000, duration=2.0,
                    scenario="Baseline", seed=42):

    if scenario not in SCENARIOS:
        raise ValueError(f"Unknown scenario: {scenario}")

    if sample_rate <= 0 or duration <= 0:
        raise ValueError("Sample rate and duration must be positive.")

    rng = np.random.default_rng(seed)

    samples = int(sample_rate * duration)
    time = np.arange(samples) / sample_rate

    # Background signal
    signal = (
        0.4 * np.sin(2 * np.pi * 120 * time)
        + 0.2 * np.sin(2 * np.pi * 350 * time)
    )

    # Add background noise
    signal += rng.normal(0, 0.08, samples)

    if scenario == "Elevated Activity":
        signal += rng.normal(0, 0.20, samples)
        signal += 0.25 * np.sin(2 * np.pi * 650 * time)

    elif scenario == "Transient Event":
        start = int(0.8 * sample_rate)
        end = min(start + int(0.25 * sample_rate), samples)

        burst_time = time[start:end] - time[start]

        burst = (
            1.5
            * np.sin(2 * np.pi * 900 * burst_time)
            * np.exp(-20 * burst_time)
        )

        signal[start:end] += burst

    return time, signal


def extract_features(signal, sample_rate):

    signal = np.asarray(signal)

    if signal.ndim != 1 or len(signal) < 2:
        raise ValueError("Signal must be a 1D array with at least 2 samples.")

    if sample_rate <= 0:
        raise ValueError("Sample rate must be positive.")

    peak = float(np.max(np.abs(signal)))
    rms = float(np.sqrt(np.mean(signal ** 2)))

    frequencies, power = periodogram(signal, sample_rate)
    dominant_frequency = float(frequencies[np.argmax(power)])

    zero_crossings = np.where(np.diff(np.signbit(signal)))[0]
    zero_crossing_rate = len(zero_crossings) / len(signal)

    return {
        "peak_amplitude": peak,
        "rms": rms,
        "mean": float(np.mean(signal)),
        "standard_deviation": float(np.std(signal)),
        "crest_factor": float(peak / rms) if rms > 0 else 0.0,
        "zero_crossing_rate": float(zero_crossing_rate),
        "dominant_frequency": dominant_frequency
    }
