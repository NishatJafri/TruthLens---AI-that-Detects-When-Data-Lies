import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* MAIN BACKGROUND */
    [data-testid="stAppViewContainer"]{
        background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
        color:white;
        font-family:'Segoe UI', sans-serif;
    }

    /* SIDEBAR */
    [data-testid="stSidebar"]{
        background:#111827;
        border-right:1px solid rgba(255,255,255,0.05);
    }

    [data-testid="stSidebar"] *{
        color:white;
    }

    /* PAGE SPACING */
    .block-container{
        padding-top:3rem;
    }

    [data-testid="stFileUploader"] button{
    background:linear-gradient(135deg,#00FFD1,#00b894);
    color:black !important;
    border-radius:10px;
    border:none;
    padding:6px 14px;
    font-weight:600;
    }

    /* METRIC TEXT FIX */
    [data-testid="stMetricLabel"]{
    color:#E5E7EB !important;
    }

    [data-testid="stMetricValue"]{
    color:#00FFD1 !important;
    font-weight:700;
    }   

    [data-testid="stFileUploader"]{
    color:white;
    }

    /* DOWNLOAD BUTTON */
    .stDownloadButton button{
    background:linear-gradient(135deg,#00FFD1,#00b894);
    color:black !important;
    font-weight:600;
    border-radius:10px;
    border:none;
    }    
    
    [data-testid="stAlert"]{
    color:white;
    }
                
    /* STREAMLIT BUTTON FIX */
    .stButton > button {
    background: linear-gradient(135deg,#00FFD1,#00b894);
    color: black !important;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: 600;
    }
    
    [data-testid="stHeader"]{
    display:none;
    }

    </style>
    """, unsafe_allow_html=True)