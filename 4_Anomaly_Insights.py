import streamlit as st
from src.explanation_engine import explain_anomalies
from style import load_css

load_css()

st.title(" Anomaly Insights")

if "processed_data" not in st.session_state:
    st.warning("Run AI Analysis first")
    st.stop()

data = st.session_state["processed_data"]

anomalies = data[data["anomaly"] == -1]

st.subheader("Anomaly Summary")

col1,col2 = st.columns(2)

col1.metric("Total Rows", len(data))
col2.metric("Anomalies Detected", len(anomalies))

st.divider()

st.subheader("Detected Anomalies")

rows = st.slider("Rows to display",5,100,20)

st.dataframe(anomalies.head(rows), use_container_width=True)

st.divider()

st.subheader("AI Explanations")

explanations = explain_anomalies(data)

for e in explanations:

    st.info(f"Row {e['row']} → {e['reason']}")

st.divider()

csv = anomalies.to_csv(index=False)

st.download_button(
    "Download Anomaly Data",
    csv,
    "anomalies.csv"
)

st.markdown("---")
st.caption("Designed & Developed by Aisha & Nishat")
