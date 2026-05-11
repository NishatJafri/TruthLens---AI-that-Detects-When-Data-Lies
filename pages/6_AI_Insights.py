import streamlit as st
import pandas as pd
from style import load_css

load_css()

st.title(" AI Insights Engine")

st.write("TruthLens automatically analyzes your dataset and generates intelligent insights.")

if "processed_data" not in st.session_state:
    st.warning("Run AI Analysis first")
    st.stop()

data = st.session_state["processed_data"]

st.subheader("Dataset Overview")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Rows", data.shape[0])
col2.metric("Columns", data.shape[1])
col3.metric("Missing Values", data.isnull().sum().sum())
col4.metric("Duplicates", data.duplicated().sum())

st.divider()

st.subheader("AI Generated Insights")

insights = []

missing_total = data.isnull().sum().sum()

if missing_total > 0:
    insights.append(f"The dataset contains {missing_total} missing values which may affect model accuracy.")

duplicates = data.duplicated().sum()

if duplicates > 0:
    insights.append(f"{duplicates} duplicate rows were detected in the dataset.")

if "anomaly" in data.columns:

    anomalies = (data["anomaly"] == -1).sum()

    anomaly_percent = (anomalies / len(data)) * 100

    insights.append(f"{anomalies} anomalies detected ({anomaly_percent:.2f}% of dataset).")

numeric_cols = data.select_dtypes(include="number").columns

if len(numeric_cols) > 0:

    high_variance = data[numeric_cols].var().sort_values(ascending=False)

    top_feature = high_variance.index[0]

    insights.append(f"Column '{top_feature}' shows the highest variance in the dataset.")

categorical_cols = data.select_dtypes(include="object").columns

if len(categorical_cols) > 0:

    col = categorical_cols[0]

    distribution = data[col].value_counts(normalize=True)

    if distribution.iloc[0] > 0.7:

        insights.append(f"Column '{col}' shows strong imbalance which may indicate bias.")

for insight in insights:

    st.info(insight)

st.divider()

st.subheader("AI Data Story")

story = f"""
The dataset contains **{data.shape[0]} records** and **{data.shape[1]} features**.

TruthLens analysis identified **{missing_total} missing values** and **{duplicates} duplicate rows**.

The anomaly detection engine flagged **{(data['anomaly'] == -1).sum()} suspicious records**.

Based on the analysis, the dataset reliability can be evaluated using the Truth Score generated in the AI Analysis page.
"""

st.write(story)

st.divider()

st.subheader("AI Recommendations")

recommendations = []

if missing_total > 0:
    recommendations.append("Consider handling missing values before training machine learning models.")

if duplicates > 0:
    recommendations.append("Duplicate rows should be removed to improve data quality.")

if "anomaly" in data.columns:

    anomalies = (data["anomaly"] == -1).sum()

    if anomalies > 0:
        recommendations.append("Investigate anomaly rows as they may indicate unusual behavior.")

for rec in recommendations:

    st.success(rec)

st.divider()

st.markdown("---")
st.caption("Designed & Developed by Aisha & Nishat")