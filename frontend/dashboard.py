import streamlit as st
import requests

st.set_page_config(
    page_title="ReleasePilot AI",
    layout="wide"
)

st.title("🚀 ReleasePilot AI")

st.subheader("AI-Powered Release Governance Platform")

col1, col2 = st.columns(2)

with col1:
    open_critical = st.number_input(
        "Open Critical Defects",
        min_value=0,
        value=0
    )

    open_high = st.number_input(
        "Open High Defects",
        min_value=0,
        value=2
    )

with col2:
    test_pass_rate = st.number_input(
        "Test Pass Rate (%)",
        min_value=0,
        max_value=100,
        value=98
    )

    failed_tests = st.number_input(
        "Failed Tests",
        min_value=0,
        value=1
    )

if st.button("Analyze Release"):

    payload = {
        "open_critical": open_critical,
        "open_high": open_high,
        "test_pass_rate": test_pass_rate,
        "failed_tests": failed_tests
    }

    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        json=payload
    )

    data = response.json()

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Decision",
            data["release_decision"]["decision"]
        )

    with col2:
        st.metric(
            "Risk Score",
            data["risk_metrics"]["risk_score"]
        )

    with col3:
        st.metric(
            "Confidence",
            f'{data["risk_metrics"]["confidence"]}%'
        )

    st.divider()

    st.subheader("Executive Summary")

    st.write(
        data["executive_summary"]
    )

    st.divider()

    st.subheader("AI Release Assessment")

    st.write(
        data["ai_release_assessment"]
    )