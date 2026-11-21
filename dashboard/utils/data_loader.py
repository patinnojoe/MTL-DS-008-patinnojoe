from pathlib import Path
import pandas as pd
import streamlit as st

# Locate project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Locate dataset
DATA_PATH = BASE_DIR / "data" / "analytical" / "combined.csv"
ANALYTICAL_PATH = BASE_DIR / "data" / "analytical" / "forecast.csv"
EVALAUTION_WINDOW_PATH = BASE_DIR / "data" / "analytical" / "cv_window_evaluation.csv"
EVALAUTION_PATH = BASE_DIR / "data" / "analytical" / "evaluation.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=['period'])
    df = df.sort_values('period').reset_index(drop=True)
    return df

@st.cache_data
def load_forecast():
    df = pd.read_csv(ANALYTICAL_PATH, parse_dates=['ds'])
    df = df.sort_values('ds').reset_index(drop=True)
    return df

@st.cache_data
def load_evaluation():
     df = pd.read_csv(EVALAUTION_PATH)
     return df
 
@st.cache_data
def load_evaluation_window():
     df = pd.read_csv(EVALAUTION_WINDOW_PATH)
     return df