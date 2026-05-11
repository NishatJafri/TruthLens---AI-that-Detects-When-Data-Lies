import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from style import load_css

load_css()

st.title(" Visualization Dashboard")

if "processed_data" not in st.session_state:
    st.warning("Run AI Analysis first")
    st.stop()

data = st.session_state["processed_data"]

numeric_cols = data.select_dtypes(include=["int64","float64"]).columns

st.subheader("Scatter Plot")

if len(numeric_cols) >= 2:

    col1,col2 = st.columns(2)

    x_axis = col1.selectbox("X Axis", numeric_cols)
    y_axis = col2.selectbox("Y Axis", numeric_cols)

    fig, ax = plt.subplots()

    if "anomaly" in data.columns:

        sns.scatterplot(
            data=data,
            x=x_axis,
            y=y_axis,
            hue="anomaly",
            palette={1:"blue",-1:"red"},
            ax=ax
        )

    else:

        sns.scatterplot(
            data=data,
            x=x_axis,
            y=y_axis,
            ax=ax
        )

    st.pyplot(fig)

st.divider()

st.subheader("Histogram")

column = st.selectbox("Select Column", numeric_cols)

fig, ax = plt.subplots()

sns.histplot(data[column], kde=True, ax=ax)

st.pyplot(fig)

st.divider()

st.subheader("Box Plot")

fig, ax = plt.subplots()

sns.boxplot(x=data[column], ax=ax)

st.pyplot(fig)

st.divider()

st.subheader("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(8,6))

sns.heatmap(
    data[numeric_cols].corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)

st.markdown("---")
st.caption("Designed & Developed by Aisha & Nishat")