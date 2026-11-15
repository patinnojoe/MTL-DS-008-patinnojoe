from pathlib import Path
import pandas as pd
import streamlit as st

# Locate project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Locate dataset
DATA_PATH = BASE_DIR / "data" / "analytical" / "combined.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=['period'])
    df = df.sort_values('period').reset_index(drop=True)
    return df