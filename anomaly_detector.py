
def classify_signal(features):
    """
    Rule-based classification of simulated acoustic signals.
    This is an experimental demonstration, not a landslide predictor.
    """

    rms = features["rms"]
    peak = features["peak_amplitude"]
    crest = features["crest_factor"]
    dominant_frequency = features["dominant_frequency"]

    score = 0
    reasons = []

    # Detect elevated background activity
    if rms > 0.38:
        score += 2
        reasons.append("Higher-than-baseline RMS amplitude")

    # Detect short, strong signal bursts
    if crest > 4.5:
        score += 2
        reasons.append("High crest factor")

    if peak > 1.5:
        score += 1
        reasons.append("High peak amplitude")

    # Classification
    if crest > 4.5 or (peak > 1.5 and rms < 0.38):
        label = "Transient Event"
    elif rms > 0.38:
        label = "Elevated Activity"
    else:
        label = "Baseline"

    if not reasons:
        reasons.append("No unusual signal characteristics detected")

    return {
        "classification": label,
        "anomaly_score": score,
        "reasons": reasons,
        "dominant_frequency": dominant_frequency
    }
