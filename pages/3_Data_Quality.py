import streamlit as st
import pandas as pd
from style import load_css

load_css()

st.title(" Data Quality Dashboard")

if "dataset" not in st.session_state:
    st.warning("Upload dataset first")
    st.stop()

data = st.session_state["dataset"]

st.subheader("Dataset Summary")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Rows", data.shape[0])
col2.metric("Columns", data.shape[1])
col3.metric("Missing Values", data.isnull().sum().sum())
col4.metric("Duplicates", data.duplicated().sum())

st.divider()

st.subheader("Missing Values Analysis")

missing = data.isnull().sum()

missing_percent = (missing / len(data)) * 100

missing_df = pd.DataFrame({
    "Column": data.columns,
    "Missing Count": missing.values,
    "Missing %": missing_percent.values
})

st.dataframe(missing_df)

st.bar_chart(missing)

problem_cols = missing_percent[missing_percent > 20]

if len(problem_cols) > 0:

    st.warning("Columns with high missing data")

st.divider()

st.subheader("Statistical Summary")

st.dataframe(data.describe(), use_container_width=True)

st.markdown("---")
st.caption("Designed & Developed by Aisha & Nishat")