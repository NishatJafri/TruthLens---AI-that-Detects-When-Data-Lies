import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from style import load_css

load_css()

st.title(" Dataset Explorer")

st.write("Upload a dataset to begin analysis with TruthLens AI")

uploaded_file = st.file_uploader("Upload CSV Dataset", type=["csv"])

if uploaded_file:

    data = pd.read_csv(uploaded_file)

    st.session_state["dataset"] = data

    st.success("Dataset uploaded successfully")

    st.subheader("Dataset Overview")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Rows", data.shape[0])
    col2.metric("Columns", data.shape[1])
    col3.metric("Missing Values", data.isnull().sum().sum())
    col4.metric("Duplicates", data.duplicated().sum())

    st.divider()

    st.subheader("Dataset Preview")

    rows = st.slider("Rows to display",5,100,10)

    st.dataframe(data.head(rows), use_container_width=True)

    st.divider()

    st.subheader("Column Inspector")

    column = st.selectbox("Select column", data.columns)

    st.write("Unique values:", data[column].nunique())
    st.write("Missing values:", data[column].isnull().sum())

    st.divider()

    st.subheader("Column Data Types")

    dtype_df = pd.DataFrame({
        "Column": data.columns,
        "Type": data.dtypes
    })

    st.dataframe(dtype_df, use_container_width=True)

    st.divider()

    numeric_cols = data.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:

        st.subheader("Distribution Preview")
        plt.style.use("dark_background")
        fig, ax = plt.subplots()

        sns.histplot(data[numeric_cols[0]], kde=True, ax=ax)
        st.pyplot(fig)

    st.divider()

    csv = data.to_csv(index=False)

    st.download_button(
        "Download Dataset",
        csv,
        "dataset.csv"
    )

else:

    st.info("Upload dataset to start.")

st.markdown("---")
st.caption("Designed & Developed by Aisha & Nishat")