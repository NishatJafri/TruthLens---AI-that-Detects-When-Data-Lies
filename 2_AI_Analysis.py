import streamlit as st
from src.preprocessing import clean_data
from src.anomaly_detection import detect_anomalies
from src.bias_detection import detect_bias
from src.truth_score import calculate_truth_score
from style import load_css

load_css()

st.title(" AI Analysis")

st.info("Pipeline: Cleaning → Anomaly Detection → Bias Detection → Truth Score")

if "dataset" not in st.session_state:
    st.warning("Upload dataset first")
    st.stop()

data = st.session_state["dataset"]

if st.button("Run AI Analysis"):

    with st.spinner("Running AI analysis..."):

        data = clean_data(data)

        data = detect_anomalies(data)

        bias_report = detect_bias(data)

        truth_score = calculate_truth_score(data)

        st.session_state["processed_data"] = data

    st.success("AI Analysis Completed")

    anomalies = (data["anomaly"] == -1).sum()

    anomaly_percent = (anomalies / len(data)) * 100

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Rows", len(data))
    col2.metric("Anomalies", anomalies)
    col3.metric("Anomaly %", f"{anomaly_percent:.2f}%")
    col4.metric("Truth Score", f"{truth_score}%")

    st.progress(truth_score/100)

    if truth_score > 80:
        st.success("Dataset reliability is high")

    elif truth_score > 60:
        st.warning("Dataset reliability is moderate")

    else:
        st.error("Dataset reliability is low")

    st.divider()

    st.subheader("Bias Report")

    st.json(bias_report)

    st.divider()

    st.subheader("Processed Dataset")

    st.dataframe(data.head(20), use_container_width=True)

    csv = data.to_csv(index=False)

    st.download_button(
        "Download Processed Dataset",
        csv,
        "processed_dataset.csv"
    )

st.markdown("---")
st.caption("Designed & Developed by Aisha & Nishat")
