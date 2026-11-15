import streamlit as st
from pathlib import Path

# Locate project assets
BASE_DIR = Path(__file__).resolve().parents[2]
LOGO_PATH = BASE_DIR / "assets" / "nhs-logo.webp"


def render_header(header_title):
    col_1, col_2 = st.columns([1, 5])
    
    # logo
    with col_1:
        st.image(str(LOGO_PATH), width=110, alt='NHS logo')
    
    # page title
    with col_2:
        st.header(header_title)
        st.markdown(
            """
            <h5 style="margin-top:-20px"> Lancashire Teaching Hospitals NHS Foundation Trust</h5>
            
            """,
            unsafe_allow_html=True
        )
    st.divider()