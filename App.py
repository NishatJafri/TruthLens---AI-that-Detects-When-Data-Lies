import streamlit as st
from style import load_css

load_css()

# PAGE CONFIG
st.set_page_config(
    page_title="TruthLens",
    page_icon="https://cdn-icons-png.flaticon.com/512/622/622669.png",
    layout="wide",
)

# CUSTOM CSS (UI DESIGN)
# CUSTOM CSS (ADVANCED UI DESIGN)
st.markdown("""
<style>

/* ---------- MAIN BACKGROUND ---------- */
[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
font-family: 'Segoe UI', sans-serif;
}

/* ---------- SIDEBAR ---------- */
[data-testid="stSidebar"]{
background: #111827;
border-right:1px solid rgba(255,255,255,0.05);
}

[data-testid="stSidebar"] *{
color:white;
}

/* ---------- SCROLLBAR ---------- */
::-webkit-scrollbar{
width:8px;
}

::-webkit-scrollbar-track{
background:#0f2027;
}

::-webkit-scrollbar-thumb{
background:#00FFD1;
border-radius:10px;
}

/* ---------- FORCE STREAMLIT METRIC COLORS ---------- */
:root{
--text-color:#ffffff;
--secondary-text-color:#ffffff;
}

/* ---------- METRIC CARDS ---------- */
.metric-box{
background:rgba(30,41,59,0.85);
padding:25px;
border-radius:20px;
text-align:center;
box-shadow:0px 8px 25px rgba(0,0,0,0.45);
transition:all 0.35s ease;
backdrop-filter:blur(8px);
border:1px solid rgba(255,255,255,0.05);
height:140px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
cursor:pointer;
}

.metric-box:hover{
transform:translateY(-10px) scale(1.03);
box-shadow:0px 18px 45px rgba(0,255,209,0.45);
border:1px solid #00FFD1;
}

.metric-box span{
color:#e5e7eb;
font-size:15px;
font-weight:600;
display:block;
margin-bottom:8px;
letter-spacing:0.5px;
white-space:nowrap; 
}

.metric-box h2{
color:#00FFD1;
font-size:30px;
font-weight:700;
}

/* ---------- HEADINGS ---------- */
h1{
font-size:60px;
color:#00FFD1;
text-align:center;
font-weight:700;
}

h2{
color:#00FFD1;
font-weight:600;
}

h3{
color:#ffffff;
}

/* ---------- FEATURE CARDS ---------- */
.feature-card{
background:rgba(31,41,55,0.9);
padding:22px;
border-radius:18px;
text-align:center;
margin:10px;
box-shadow:0px 8px 25px rgba(0,0,0,0.4);
transition:all 0.35s ease;
border:1px solid rgba(255,255,255,0.05);
}

.feature-card:hover{
transform:translateY(-6px);
box-shadow:0px 12px 35px rgba(0,255,209,0.25);
}

.feature-card h3{
color:#00FFD1;
font-weight:600;
}

/* ---------- BUTTON STYLE ---------- */
.stButton>button{
background:linear-gradient(135deg,#00FFD1,#00b894);
color:black;
border:none;
border-radius:10px;
padding:10px 20px;
font-weight:600;
transition:all 0.3s ease;
}

.stButton>button:hover{
transform:scale(1.05);
box-shadow:0px 5px 20px rgba(0,255,209,0.4);
}

/* ---------- INPUT BOXES ---------- */
.stTextInput>div>div>input{
background:#1f2937;
color:white;
border-radius:10px;
border:1px solid rgba(255,255,255,0.1);
}

/* ---------- DATAFRAME STYLE ---------- */
[data-testid="stDataFrame"]{
border-radius:12px;
overflow:hidden;
}

/* ---------- FOOTER ---------- */
.creator{
text-align:center;
font-size:20px;
color:#FFD700;
margin-top:40px;
font-weight:600;
letter-spacing:0.5px;
}

/* ---------- PAGE SPACING ---------- */
.block-container{
padding-top:2rem;
}

/* ---------- DIVIDER ---------- */
hr{
border:0;
height:1px;
background:linear-gradient(to right,transparent,#00FFD1,transparent);
}

</style>
""", unsafe_allow_html=True)



st.sidebar.info("Upload dataset → Run AI analysis → Explore insights")

# HERO TITLE
st.title("TruthLens AI Platform")

st.markdown("""
###  AI That Detects When Data Lies

TruthLens is an **AI-powered data reliability analysis platform**  
designed to detect hidden issues in datasets before they impact machine learning models.
""")

st.divider()

# METRICS DASHBOARD
st.subheader(" Platform Capabilities")

col1, col2, col3, col4 = st.columns(4)

col1.markdown("""
<div class="metric-box">
<span>Anomaly Detection</span>
<h2>AI Powered</h2>
</div>
""", unsafe_allow_html=True)

col2.markdown("""
<div class="metric-box">
<span>Bias Detection</span>
<h2>Automated</h2>
</div>
""", unsafe_allow_html=True)

col3.markdown("""
<div class="metric-box">
<span>Data Quality Analysis</span>
<h2>Advanced</h2>
</div>
""", unsafe_allow_html=True)

col4.markdown("""
<div class="metric-box">
<span>Truth Score Engine</span>
<h2>Real-Time</h2>
</div>
""", unsafe_allow_html=True)

st.divider()

# HOW IT WORKS
st.subheader(" How TruthLens Works")

c1,c2,c3,c4,c5 = st.columns(5)

c1.markdown(" **Upload Dataset**")
c2.markdown(" **Data Cleaning**")
c3.markdown(" **Anomaly Detection**")
c4.markdown(" **Bias Analysis**")
c5.markdown(" **Visual Insights**")

st.divider()

# FEATURE CARDS
st.subheader(" Key Features")

f1,f2,f3 = st.columns(3)

with f1:
    st.markdown("""
<div class="feature-card">

###  Data Quality Dashboard

Automatically analyzes missing values, duplicates, and dataset structure.

</div>
""", unsafe_allow_html=True)

with f2:
    st.markdown("""
<div class="feature-card">

###  AI Anomaly Detection

Isolation Forest algorithm identifies suspicious patterns and outliers.

</div>
""", unsafe_allow_html=True)

with f3:
    st.markdown("""
<div class="feature-card">

###  Bias Detection

Detect imbalance in categorical data to prevent biased AI models.

</div>
""", unsafe_allow_html=True)

f4,f5,f6 = st.columns(3)

with f4:
    st.markdown("""
<div class="feature-card">

###  Truth Reliability Score

Evaluate dataset reliability using anomaly-based scoring.

</div>
""", unsafe_allow_html=True)

with f5:
    st.markdown("""
<div class="feature-card">

###  Interactive Visualization

Generate scatter plots, heatmaps, histograms, and boxplots.

</div>
""", unsafe_allow_html=True)

with f6:
    st.markdown("""
<div class="feature-card">

###  AI Insight Engine

Automatically generates intelligent insights and data stories.

</div>
""", unsafe_allow_html=True)

st.divider()

# AI CAPABILITIES
st.subheader(" AI Capabilities")

ai1,ai2,ai3 = st.columns(3)

ai1.success("Automated anomaly detection using Isolation Forest")
ai2.success("Explainable AI insights for anomaly reasoning")
ai3.success("AI-generated dataset recommendations")

st.divider()

# PLATFORM DESCRIPTION
colA,colB = st.columns([1,2])

with colA:
    st.markdown("""
        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71"
        style="
        width:100%;
        height:320px;
        object-fit:contain;
        border-radius:18px;
        ">
        """, unsafe_allow_html=True)

with colB:

    st.markdown("""
###  What TruthLens Detects

TruthLens scans datasets to identify critical data problems.

✔ Missing values  
✔ Duplicate records  
✔ Statistical anomalies  
✔ Bias in categorical attributes  
✔ Suspicious patterns  

The system then calculates a **Truth Score** indicating overall dataset reliability.
""")

st.divider()

# TECHNOLOGY STACK
st.subheader(" Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.markdown("""
<div class="metric-box">
<span>Python</span>
<h2>Core Engine</h2>
</div>
""", unsafe_allow_html=True)

tech2.markdown("""
<div class="metric-box">
<span>Streamlit</span>
<h2>Frontend UI</h2>
</div>
""", unsafe_allow_html=True)

tech3.markdown("""
<div class="metric-box">
<span>Scikit-Learn</span>
<h2>AI Models</h2>
</div>
""", unsafe_allow_html=True)

tech4.markdown("""
<div class="metric-box">
<span>Pandas</span>
<h2>Data Processing</h2>
</div>
""", unsafe_allow_html=True)

st.divider()

# WORKFLOW DIAGRAM
st.subheader(" System Workflow")

st.markdown("""
Upload Dataset  
⬇  
Data Cleaning  
⬇  
AI Analysis (Anomaly + Bias Detection)  
⬇  
Truth Score Evaluation  
⬇  
Interactive Visualization  
⬇  
AI Insights & Recommendations
""")

st.divider()

# FUTURE SCOPE
st.subheader(" Future Enhancements")

future1,future2,future3 = st.columns(3)

future1.info("Real-time streaming dataset analysis")
future2.info("Cloud deployment with automated monitoring")
future3.info("Integration with machine learning pipelines")

st.divider()

# FOOTER
st.markdown("""
<div class="creator">
Designed & Developed by <b>Aisha</b> & <b>Nishat</b>
</div>
""", unsafe_allow_html=True)