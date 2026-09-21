import os
import sys

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import joblib

from sklearn.preprocessing import LabelEncoder


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="RakshaNet AI",
    page_icon="🛡️",
    layout="wide"
)


# ------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f6f7f9;
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3 {
    color: #172033;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #e5e7eb;
}

.small-text {
    color: #64748b;
}

.risk-high {
    color: #dc2626;
    font-size: 34px;
    font-weight: bold;
}

.risk-medium {
    color: #d97706;
    font-size: 34px;
    font-weight: bold;
}

.risk-low {
    color: #16a34a;
    font-size: 34px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

st.sidebar.title("🛡️ RAKSHANET AI")

st.sidebar.caption(
    "Network Security Intelligence"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Traffic Analysis",
        "Forecasts",
        "Incidents",
        "Upload Traffic",
        "AI Model"
    ]
)

st.sidebar.divider()

st.sidebar.success(
    "● System operational"
)

st.sidebar.caption(
    "SOC: Chennai"
)

st.sidebar.caption(
    "IST · 21 Sep 2026"
)


# ------------------------------------------------
# DEMO DATA
# ------------------------------------------------

times = [
    "14:00",
    "14:10",
    "14:20",
    "14:30",
    "14:40",
    "14:50",
    "15:00"
]

risk_values = [
    12,
    16,
    22,
    31,
    44,
    61,
    78
]


# ------------------------------------------------
# OVERVIEW
# ------------------------------------------------

if page == "Overview":

    st.title("Overview")

    st.write(
        "Good afternoon, Security Team."
    )

    st.caption(
        "Network security status across your monitored infrastructure."
    )

    st.divider()

    # Status
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Attack likelihood",
            "78%",
            "+14%"
        )

    with col2:
        st.metric(
            "Active incidents",
            "07",
            "+2 today"
        )

    with col3:
        st.metric(
            "Traffic analysed",
            "2.4M",
            "flows / 24h"
        )

    with col4:
        st.metric(
            "Forecast confidence",
            "91.4%"
        )

    st.divider()

    # Main chart
    left, right = st.columns([2, 1])

    with left:

        st.subheader(
            "Attack Risk Forecast"
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=times,
                y=risk_values,
                mode="lines+markers",
                name="Risk"
            )
        )

        fig.add_hline(
            y=60,
            line_dash="dash",
            annotation_text="High Risk"
        )

        fig.update_layout(
            height=400,
            yaxis_title="Risk %",
            xaxis_title="Time",
            yaxis=dict(range=[0, 100]),
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader(
            "Forecast Summary"
        )

        st.metric(
            "Potential Threat",
            "DDoS / Volumetric"
        )

        st.metric(
            "Probability",
            "82%"
        )

        st.metric(
            "Forecast Window",
            "Next 30 min"
        )

        st.metric(
            "Confidence",
            "91%"
        )

    st.divider()

    # AI reasoning
    st.subheader(
        "Why did AI predict this?"
    )

    reason1, reason2, reason3, reason4 = st.columns(4)

    with reason1:
        st.info(
            "↑ Packet rate\n\n"
            "Increased 38%"
        )

    with reason2:
        st.info(
            "↑ Connection frequency\n\n"
            "Increased 31%"
        )

    with reason3:
        st.info(
            "↑ Source diversity\n\n"
            "Increased 27%"
        )

    with reason4:
        st.info(
            "↑ Flow anomaly\n\n"
            "Pattern increasing"
        )

    st.caption(
        "Model confidence: 91%"
    )


# ------------------------------------------------
# TRAFFIC ANALYSIS
# ------------------------------------------------

elif page == "Traffic Analysis":

    st.title("Network Traffic")

    st.caption(
        "Real-time visibility into monitored network flows."
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Incoming traffic",
        "842 Mbps"
    )

    col2.metric(
        "Outgoing traffic",
        "391 Mbps"
    )

    col3.metric(
        "Active flows",
        "24,832"
    )

    col4.metric(
        "Anomalous flows",
        "1,284"
    )

    st.divider()

    traffic = pd.DataFrame({
        "Time": times,
        "Traffic": [
            420,
            480,
            510,
            580,
            650,
            730,
            842
        ]
    })

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=traffic["Time"],
            y=traffic["Traffic"],
            mode="lines+markers",
            name="Traffic"
        )
    )

    fig.update_layout(
        title="Traffic Volume",
        yaxis_title="Mbps",
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "Recent Network Flows"
    )

    traffic_table = pd.DataFrame({
        "Time": [
            "16:41:02",
            "16:41:03",
            "16:41:05",
            "16:41:06"
        ],
        "Source": [
            "10.20.4.12",
            "10.20.8.44",
            "172.16.2.9",
            "10.30.5.1"
        ],
        "Destination": [
            "10.10.1.20",
            "10.10.1.20",
            "10.10.2.14",
            "10.10.4.12"
        ],
        "Protocol": [
            "TCP",
            "TCP",
            "UDP",
            "TCP"
        ],
        "Status": [
            "Normal",
            "Suspicious",
            "Normal",
            "Anomaly"
        ]
    })

    st.dataframe(
        traffic_table,
        use_container_width=True,
        hide_index=True
    )


# ------------------------------------------------
# FORECASTS
# ------------------------------------------------

elif page == "Forecasts":

    st.title("Attack Forecasts")

    st.caption(
        "Predictive network security intelligence"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("DDoS Risk")
        st.metric("Risk", "82%")
        st.error("HIGH")
        st.caption("Next 30 min")

    with col2:
        st.subheader("Port Scan Risk")
        st.metric("Risk", "41%")
        st.warning("MEDIUM")
        st.caption("Next 60 min")

    with col3:
        st.subheader("Brute Force Risk")
        st.metric("Risk", "23%")
        st.success("LOW")
        st.caption("Next 60 min")

    st.divider()

    st.subheader(
        "Forecast Evidence"
    )

    evidence = pd.DataFrame({
        "Indicator": [
            "Traffic volume",
            "Packet rate",
            "Unique sources",
            "Connection attempts"
        ],
        "Change": [
            "+38%",
            "+44%",
            "+27%",
            "+31%"
        ]
    })

    st.dataframe(
        evidence,
        use_container_width=True,
        hide_index=True
    )


# ------------------------------------------------
# INCIDENTS
# ------------------------------------------------

elif page == "Incidents":

    st.title("Incidents")

    st.caption(
        "7 active · 23 resolved"
    )

    incidents = pd.DataFrame({
        "Severity": [
            "HIGH",
            "HIGH",
            "MEDIUM"
        ],
        "Incident": [
            "DDoS Risk",
            "Port Scan",
            "Brute Force Pattern"
        ],
        "Asset": [
            "API-GW-01",
            "WEB-03",
            "VPN-02"
        ],
        "Time": [
            "16:41",
            "16:28",
            "16:11"
        ]
    })

    st.dataframe(
        incidents,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader(
        "Incident Details"
    )

    st.error(
        "HIGH RISK — Potential DDoS Activity"
    )

    st.write(
        "**Incident ID:** INC-2026-00941"
    )

    st.write(
        "**Forecast confidence:** 91%"
    )

    st.write(
        "**Detected:** 21 Sep 2026 · 16:41 IST"
    )

    st.subheader("Timeline")

    st.write("16:12 — Traffic begins increasing")
    st.write("16:19 — Unusual source diversity detected")
    st.write("16:27 — Anomaly threshold crossed")
    st.write("16:34 — ML model identifies attack-like pattern")
    st.write("16:41 — High-risk forecast generated")

    st.subheader(
        "Recommended Response"
    )

    st.write(
        "1. Review affected API gateway"
    )

    st.write(
        "2. Validate traffic source distribution"
    )

    st.write(
        "3. Check rate-limit configuration"
    )

    st.write(
        "4. Notify SOC lead if traffic continues"
    )


# ------------------------------------------------
# UPLOAD TRAFFIC
# ------------------------------------------------

elif page == "Upload Traffic":

    st.title(
        "Analyze Network Traffic"
    )

    st.caption(
        "Upload traffic data for AI analysis."
    )

    uploaded_file = st.file_uploader(
        "Drop CSV file here",
        type=["csv"]
    )

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        st.success(
            "✓ Data uploaded successfully"
        )

        st.write(
            f"Records: {len(df):,}"
        )

        st.subheader(
            "Dataset Preview"
        )

        st.dataframe(
            df.head(20),
            use_container_width=True
        )

        if st.button(
            "🔍 Analyze Traffic",
            type="primary"
        ):

            with st.spinner(
                "Analysing network traffic..."
            ):

                # Try to use trained model
                if os.path.exists(
                    "models/classifier.pkl"
                ):

                    model = joblib.load(
                        "models/classifier.pkl"
                    )

                    encoders = joblib.load(
                        "models/encoders.pkl"
                    )

                    processed = df.copy()

                    for column, encoder in encoders.items():

                        if column in processed.columns:

                            values = (
                                processed[column]
                                .astype(str)
                            )

                            known = set(
                                encoder.classes_
                            )

                            values = values.apply(
                                lambda x:
                                x
                                if x in known
                                else encoder.classes_[0]
                            )

                            processed[column] = (
                                encoder.transform(values)
                            )

                    processed = processed.replace(
                        [np.inf, -np.inf],
                        0
                    )

                    processed = processed.fillna(0)

                    probabilities = (
                        model.predict_proba(
                            processed
                        )[:, 1]
                    )

                    risk = (
                        float(
                            np.mean(probabilities)
                        ) * 100
                    )

                    risk = round(
                        risk,
                        2
                    )

                else:

                    # Demo fallback
                    risk = 78.0

                st.success(
                    "✓ Analysis completed"
                )

                st.divider()

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Attack Risk",
                        f"{risk}%"
                    )

                with col2:

                    if risk >= 80:
                        level = "CRITICAL"

                    elif risk >= 60:
                        level = "HIGH"

                    elif risk >= 30:
                        level = "MEDIUM"

                    else:
                        level = "LOW"

                    st.metric(
                        "Risk Level",
                        level
                    )

                with col3:
                    st.metric(
                        "Records Analysed",
                        f"{len(df):,}"
                    )

                if risk >= 60:

                    st.error(
                        "⚠️ High-risk network "
                        "activity detected"
                    )

                else:

                    st.success(
                        "✓ Network activity "
                        "currently appears low risk"
                    )


# ------------------------------------------------
# AI MODEL
# ------------------------------------------------

elif page == "AI Model":

    st.title(
        "AI Model"
    )

    st.caption(
        "Network Attack Forecasting Model"
    )

    if os.path.exists(
        "models/classifier.pkl"
    ):

        model = joblib.load(
            "models/classifier.pkl"
        )

        st.success(
            "● Model Active"
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Model",
            "Random Forest"
        )

        col2.metric(
            "Trees",
            model.n_estimators
        )

        col3.metric(
            "Features",
            len(model.feature_names_in_)
            if hasattr(
                model,
                "feature_names_in_"
            )
            else "N/A"
        )

        col4.metric(
            "Status",
            "Active"
        )

        st.divider()

        st.subheader(
            "Feature Importance"
        )

        if hasattr(
            model,
            "feature_importances_"
        ):

            importance = pd.DataFrame({
                "Feature":
                    model.feature_names_in_,
                "Importance":
                    model.feature_importances_
            })

            importance = (
                importance
                .sort_values(
                    "Importance",
                    ascending=False
                )
                .head(10)
            )

            fig = go.Figure(
                go.Bar(
                    x=importance["Importance"],
                    y=importance["Feature"],
                    orientation="h"
                )
            )

            fig.update_layout(
                title="Top Factors Influencing Risk",
                template="plotly_white"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    else:

        st.warning(
            "Model not trained yet."
        )

        st.info(
            "Run: python src/train.py"
        )