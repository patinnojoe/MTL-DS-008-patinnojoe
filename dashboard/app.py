import streamlit as st
from pathlib import Path
from components.navigation import render_navigation

# Resolve the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Locate the NHS logo
logo_path = BASE_DIR / "assets" / "nhs-logo.webp"




st.set_page_config(
    page_title="Lancashire NHS RTT Waiting List Dashboard",
    layout="wide",
    page_icon=str(logo_path),
)


# Initialise navigation
pages = render_navigation()

# Display selected page
pages.run()

import pandas as pd

df = pd.read_csv("data/analytical/combined.csv")

print(df.head())
print(df.columns.tolist())
print(df.dtypes)
print(df.shape)