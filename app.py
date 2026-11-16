
import streamlit as st
import plotly.graph_objects as go
import numpy as np

from signal_engine import generate_signal, extract_features
from anomaly_detector import classify_signal

# Page configuration
st.set_page_config(
    page_title="Bhoo-Dhwani | Acoustic Monitoring",
    page_icon="⛰️",
    layout="wide"
)

# Header
st.title("⛰️ Bhoo-Dhwani")
st.subheader("Experimental Subsurface Acoustic Monitoring System")

st.info(
    "DEMONSTRATION MODE: This dashboard uses synthetic signals. "
    "It is not connected to real geological sensors and does not "
    "predict landslides."
)

# Sidebar
st.sidebar.title("Monitoring Controls")

scenario = st.sidebar.selectbox(
    "Select Signal Scenario",
    ["Baseline", "Elevated Activity", "Transient Event"]
)

sample_rate = 5000
duration = 2.0

st.sidebar.write("Sample Rate: 5000 Hz")
st.sidebar.write("Duration: 2 seconds")

# Generate signal
time, signal = generate_signal(
    sample_rate=sample_rate,
    duration=duration,
    scenario=scenario
)

# Extract features and classify
features = extract_features(signal, sample_rate)
result = classify_signal(features)

# Status
st.subheader("Monitoring Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Signal Classification", result["classification"])

with col2:
    st.metric("Anomaly Score", result["anomaly_score"])

with col3:
    st.metric("RMS Amplitude", f"{features['rms']:.4f}")

# Signal chart
st.subheader("Acoustic Signal Visualization")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=time,
        y=signal,
        mode="lines",
        name="Synthetic Signal",
        line=dict(width=1)
    )
)

fig.update_layout(
    xaxis_title="Time (seconds)",
    yaxis_title="Amplitude (arbitrary units)",
    template="plotly_white",
    height=400
)

st.plotly_chart(fig, use_container_width=True)

# Feature analysis
st.subheader("Signal Analysis")

col1, col2 = st.columns(2)

with col1:
    st.write("**Extracted Signal Features**")

    for name, value in features.items():
        st.write(f"**{name.replace('_', ' ').title()}:** {value:.4f}")

with col2:
    st.write("**Anomaly Analysis**")

    for reason in result["reasons"]:
        st.write(f"• {reason}")

    st.write(
        f"**Classification:** {result['classification']}"
    )

    st.caption(
        "The anomaly score is an experimental rule-based score, "
        "not a probability or landslide risk estimate."
    )

# Download generated data
st.subheader("Export Data")

csv_data = "time,amplitude\n" + "\n".join(
    f"{t},{s}" for t, s in zip(time, signal)
)

st.download_button(
    label="Download Signal Data (CSV)",
    data=csv_data,
    file_name="bhoo_dhwani_synthetic_signal.csv",
    mime="text/csv"
)

# Footer
st.divider()

st.caption(
    "Bhoo-Dhwani | SCERT Uttarakhand Hackathon 3.0 | "
    "Experimental Software Prototype"
)
