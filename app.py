
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from signal_engine import generate_signal, extract_features
from anomaly_detector import classify_signal


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Bhoo-Dhwani | Monitoring System",
    page_icon="⛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# CUSTOM DESIGN
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #0B1220;
    color: #E5EDF5;
}

[data-testid="stSidebar"] {
    background-color: #111C2D;
    border-right: 1px solid #26364B;
}

[data-testid="stSidebar"] * {
    color: #E5EDF5;
}

.main-title {
    font-size: 35px;
    font-weight: 800;
    color: #F0F7FF;
    letter-spacing: -1px;
    margin-bottom: 0;
}

.subtitle {
    color: #91A4B9;
    font-size: 14px;
    margin-top: 5px;
}

.section-title {
    font-size: 21px;
    font-weight: 700;
    color: #EAF3FC;
    margin-bottom: 15px;
}

.metric-card {
    background: linear-gradient(145deg, #17263A, #132033);
    border: 1px solid #293D54;
    border-radius: 13px;
    padding: 19px;
    min-height: 125px;
}

.metric-label {
    color: #9CB0C5;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.metric-value {
    color: #55D6BE;
    font-size: 25px;
    font-weight: 800;
    margin-top: 12px;
    overflow-wrap: anywhere;
}

.metric-description {
    color: #8296AC;
    font-size: 11px;
    margin-top: 5px;
}

.info-panel {
    background: #142337;
    border: 1px solid #2A4058;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 12px;
}

.info-heading {
    color: #55D6BE;
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 12px;
}

.info-text {
    color: #B8C9D9;
    font-size: 13px;
    line-height: 1.8;
}

.status-pill {
    display: inline-block;
    background: #173D38;
    color: #65E6C9;
    border: 1px solid #28685B;
    border-radius: 20px;
    padding: 5px 12px;
    font-size: 11px;
    font-weight: 700;
}

.header-line {
    border-bottom: 1px solid #293B50;
    margin: 18px 0 25px 0;
}

.footer {
    color: #71859B;
    font-size: 11px;
    text-align: center;
    padding: 20px 0;
}

div[data-testid="stMetric"] {
    background: #17263A;
    border: 1px solid #293D54;
    padding: 15px;
    border-radius: 12px;
}

div[data-testid="stMetricLabel"] {
    color: #9CB0C5;
}

div[data-testid="stMetricValue"] {
    color: #55D6BE;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
}

.stTabs [data-baseweb="tab"] {
    color: #A8BBD0;
}

.stTabs [aria-selected="true"] {
    color: #55D6BE !important;
}

.stDownloadButton button {
    background-color: #176B63;
    color: white;
    border: 1px solid #55D6BE;
    border-radius: 8px;
    font-weight: 700;
}

.stDownloadButton button:hover {
    background-color: #21877A;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("## ⛰️ BHOO-DHWANI")
    st.caption("SUBSURFACE ACOUSTIC MONITORING")

    st.divider()

    st.markdown("### ⚙️ Monitoring Controls")

    scenario = st.selectbox(
        "Signal Scenario",
        [
            "Baseline",
            "Elevated Activity",
            "Transient Event"
        ]
    )

    st.divider()

    st.markdown("### 📡 Signal Configuration")

    sample_rate = 5000
    duration = 2.0

    st.write("**Sampling frequency**")
    st.code("5000 Hz")

    st.write("**Signal duration**")
    st.code("2.0 seconds")

    st.write("**Total samples**")
    st.code(str(int(sample_rate * duration)))

    st.divider()

    st.markdown("### 🖥️ System Information")

    st.markdown(
        '<span class="status-pill">● SIMULATION ACTIVE</span>',
        unsafe_allow_html=True
    )

    st.caption("Software prototype v2.0")
    st.caption("SCERT Uttarakhand Hackathon 3.0")


# ==========================================
# GENERATE AND ANALYSE SIGNAL
# ==========================================

time, signal = generate_signal(
    sample_rate=sample_rate,
    duration=duration,
    scenario=scenario
)

features = extract_features(signal, sample_rate)

result = classify_signal(features)


# ==========================================
# HEADER
# ==========================================

header_col1, header_col2 = st.columns([4, 1])

with header_col1:

    st.markdown(
        '<div class="main-title">⛰️ Bhoo-Dhwani</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Experimental Subsurface Acoustic Monitoring System'
        '</div>',
        unsafe_allow_html=True
    )

with header_col2:

    st.markdown(
        '<div style="text-align:right; padding-top:12px;">'
        '<span class="status-pill">DEMO MODE</span>'
        '</div>',
        unsafe_allow_html=True
    )

st.markdown('<div class="header-line"></div>', unsafe_allow_html=True)


# ==========================================
# DEMONSTRATION NOTICE
# ==========================================

st.warning(
    "DEMONSTRATION ENVIRONMENT — This prototype uses "
    "synthetic signals. It is not connected to real geological "
    "sensors and does not predict landslides."
)


# ==========================================
# MONITORING OVERVIEW
# ==========================================

st.markdown(
    '<div class="section-title">Monitoring Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Signal Classification</div>
            <div class="metric-value">{result["classification"]}</div>
            <div class="metric-description">Current simulation scenario</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Anomaly Score</div>
            <div class="metric-value">{result["anomaly_score"]}</div>
            <div class="metric-description">Experimental rule-based score</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">RMS Amplitude</div>
            <div class="metric-value">{features["rms"]:.4f}</div>
            <div class="metric-description">Signal amplitude measurement</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


# ==========================================
# NAVIGATION TABS
# ==========================================

overview_tab, analysis_tab, export_tab = st.tabs(
    [
        "📊 Monitoring Overview",
        "🔬 Signal Analysis",
        "📁 Data & Methodology"
    ]
)


# ==========================================
# OVERVIEW TAB
# ==========================================

with overview_tab:

    st.markdown(
        '<div class="section-title">Acoustic Signal Visualization</div>',
        unsafe_allow_html=True
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=time,
            y=signal,
            mode="lines",
            name="Synthetic Signal",
            line=dict(
                color="#55D6BE",
                width=1.2
            ),
            hovertemplate=(
                "Time: %{x:.5f} s<br>"
                "Amplitude: %{y:.5f}"
                "<extra></extra>"
            )
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=430,
        paper_bgcolor="#142337",
        plot_bgcolor="#142337",
        font=dict(
            color="#C7D6E5",
            family="Inter"
        ),
        margin=dict(l=25, r=25, t=30, b=25),
        xaxis=dict(
            title="Time (seconds)",
            gridcolor="#293D54",
            zerolinecolor="#40546B"
        ),
        yaxis=dict(
            title="Amplitude (arbitrary units)",
            gridcolor="#293D54",
            zerolinecolor="#40546B"
        ),
        hovermode="x unified",
        legend=dict(
            orientation="h",
            y=1.12
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption(
        f"Scenario: {scenario} | "
        f"Sampling frequency: {sample_rate} Hz | "
        f"Duration: {duration} seconds"
    )

    st.write("")

    

    

    left, right = st.columns(2)

    with left:
        scenario_descriptions = {
            "Baseline": "Reference synthetic waveform",
            "Elevated Activity": "Increased synthetic signal activity",
            "Transient Event": "Short-duration synthetic signal event"
        }

        st.markdown(
            '<div class="info-panel">'
            '<div class="info-heading">📡 Signal Information</div>'
            '<div class="info-text">'
            f'Scenario: {scenario}<br>'
            f'Profile: {scenario_descriptions[scenario]}<br>'
            f'Total samples: {len(signal)}<br>'
            f'Sampling frequency: {sample_rate} Hz<br>'
            f'Dominant frequency: '
            f'{features["dominant_frequency"]:.2f} Hz'
            '</div></div>',
            unsafe_allow_html=True
        )

    with right:
        st.markdown(
            '<div class="info-panel">'
            '<div class="info-heading">🧠 Classification Result</div>'
            '<div class="info-text">'
            f'Current classification: {result["classification"]}<br>'
            f'Anomaly score: {result["anomaly_score"]}<br>'
            f'Analysis scenario: {scenario}'
            '</div></div>',
            unsafe_allow_html=True
        )



# ==========================================
# SIGNAL ANALYSIS TAB
# ==========================================

with analysis_tab:

    st.markdown(
        '<div class="section-title">Extracted Signal Features</div>',
        unsafe_allow_html=True
    )

    feature_columns = st.columns(2)

    for index, (name, value) in enumerate(features.items()):

        with feature_columns[index % 2]:

            st.metric(
                label=name.replace("_", " ").title(),
                value=f"{value:.4f}"
            )

    st.divider()

    st.markdown(
        '<div class="section-title">Anomaly Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="info-panel">
            <div class="info-heading">Classification: {result["classification"]}</div>
            <div class="info-text">
                The experimental analysis identified the following observations.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    for reason in result["reasons"]:

        st.markdown(f"- {reason}")

    st.info(
        "The anomaly score is a rule-based experimental score. "
        "It is not a probability, geological stress measurement "
        "or landslide risk estimate."
    )


# ==========================================
# DATA AND METHODOLOGY TAB
# ==========================================

with export_tab:

    st.markdown(
        '<div class="section-title">Data Export</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Export the generated synthetic acoustic waveform "
        "for further analysis."
    )

    csv_data = pd.DataFrame({
        "time_seconds": time,
        "amplitude": signal
    })

    csv_bytes = csv_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Signal Data (CSV)",
        data=csv_bytes,
        file_name="bhoo_dhwani_synthetic_signal.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.caption(
        "The exported data represents a synthetic simulation, "
        "not a real sensor recording."
    )

    st.divider()

    st.markdown(
        '<div class="section-title">System Methodology</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-panel">
        <div class="info-heading">01 — Signal Generation</div>
        <div class="info-text">
            Synthetic acoustic waveforms are generated using
            predefined simulation scenarios.
        </div>
    </div>

    <div class="info-panel">
        <div class="info-heading">02 — Feature Extraction</div>
        <div class="info-text">cd ~/Bhoo-Dhwani
source .venv/bin/activate
streamlit run app.pycd ~/Bhoo-Dhwani
source .venv/bin/activate
streamlit run app.pycd ~/Bhoo-Dhwanicd ~/Bhoo-Dhwanicd ~/Bhoo-Dh
streamlit run app.pycd ~/Bhoo-Dhwani
source .venv/bin/activate
streamlit run app.pycd ~/Bhoo-Dhwanicd ~/Bhoo-Dhwanicd ~/Bhoo-Dh
streamlit run app.pycd ~/Bhoo-Dhwani
source .venv/bin/activate
streamlit run app.pycd ~/Bhoo-Dhwanicd ~/Bhoo-Dhwanicd ~/Bhoo-Dhwani
source .venv/bin/activate
streamlit run app.py
source .venv/bin/activate
streamlit run app.py
source .venv/bin/activate
streamlit run app.py
            Signal characteristics such as RMS amplitude,
            peak amplitude, standard deviation and dominant
            frequency are extracted.
        </div>
    </div>

    <div class="info-panel">
        <div class="info-heading">03 — Anomaly Classification</div>
        <div class="info-text">
            An experimental rule-based detector evaluates
            extracted features and assigns a classification.
        </div>
    </div>

    <div class="info-panel">
        <div class="info-heading">04 — Visualization</div>
        <div class="info-text">
            Results are presented through interactive plots,
            feature measurements and downloadable datasets.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### ⚠️ Current Limitations")

    st.write(
        "- No real geological sensors are connected."
    )
    st.write(
        "- All current signals are synthetically generated."
    )
    st.write(
        "- The anomaly detector uses experimental rules."
    )
    st.write(
        "- Real-world validation and expert assessment "
        "are future development requirements."
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown(
    """
    <div class="footer">
        BHOO-DHWANI · EXPERIMENTAL SOFTWARE PROTOTYPE<br>
        SCERT UTTARAKHAND HACKATHON 3.0<br>
        Synthetic demonstration data · Not for operational
        geological or landslide-risk decisions
    </div>
    """,
    unsafe_allow_html=True
)
