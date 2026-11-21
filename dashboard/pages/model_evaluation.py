import streamlit as st
import pandas as pd
from components.header import render_header
from components.footer import render_footer
from utils.data_loader import load_evaluation
from utils.data_loader import load_evaluation_window
import altair as alt

# load evaluation data
df = load_evaluation()
evaluation_window = load_evaluation_window()

# model metrics
naive_results = df.loc[
    df["model"] == "Naive"
].iloc[0]

holdout_mae = naive_results["holdout_mae"]
cv_mae = naive_results["cv_mae"]

# model evaluation chart
chart_data = df.melt(
    id_vars="model",
    value_vars=["holdout_mae", "cv_mae"],
    var_name="Evaluation",
    value_name="MAE"
)

# model window evaluation
cv_chart_data = evaluation_window[
    ["cutoff", "Naive", "SARIMA"]
].melt(
    id_vars="cutoff",
    value_vars=["Naive", "SARIMA"],
    var_name="Model",
    value_name="MAE"
)

#---------------
st.markdown(
    """
    <style>
        .stMainBlockContainer {
            min-height: 100vh;
        }

        html, body {
            overflow-y: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# header
render_header("Model Evaluation")

# note
st.markdown(
    """
    This page evaluates seven forecasting models using
    **Mean Absolute Error (MAE)**.

    Models were assessed using a seven-month holdout period
    (January–July 2026) and three rolling-origin
    cross-validation windows.

    **Lower MAE indicates better forecasting accuracy.**
    """
)

# metrics
col_1, col_2, col_3 = st.columns(3)

with col_1:
    st.metric(label="Model Name", value='Naive')
with col_2:
    st.metric(label='Hold out MAE', value=f"{holdout_mae:,.2f}")
with col_3:
    st.metric(label="Cross Validation MAE", value=f"{cv_mae:,.2f}")
    
    


st.subheader("Forecasting Model Performance")

model_chart = (
    alt.Chart(chart_data)
    .mark_bar()
    .encode(
        x=alt.X(
            "model:N",
            title="Forecasting Model",
            sort=None,
            axis=alt.Axis(labelAngle=-35)
        ),
        xOffset=alt.XOffset("Evaluation:N"),
        y=alt.Y(
            "MAE:Q",
            title="Mean Absolute Error (Pathways)"
        ),
        color=alt.Color(
            "Evaluation:N",
            title="Evaluation Method",
            scale=alt.Scale(
                domain=["holdout_mae", "cv_mae"],
                range=["#0072B2", "#E69F00"]
            )
        ),
        tooltip=[
            alt.Tooltip("model:N", title="Model"),
            alt.Tooltip("Evaluation:N", title="Evaluation"),
            alt.Tooltip("MAE:Q", title="MAE", format=".2f")
        ]
    )
    .properties(height=400)
)

st.altair_chart(
    model_chart,
    use_container_width=True
)
st.caption(
    "Lower MAE indicates better forecasting accuracy. "
    "Naive and ARIMA achieved the lowest holdout MAE (105.71), "
    "while SARIMA achieved the lowest average cross-validation MAE (150.11)."
)





st.subheader("Cross-Validation Performance by Window")

cv_chart = (
    alt.Chart(cv_chart_data)
    .mark_bar()
    .encode(
        x=alt.X(
            "yearmonth(cutoff):O",
            title="Forecast Origin",
            axis=alt.Axis(format="%b %Y")
        ),
        xOffset=alt.XOffset("Model:N"),
        y=alt.Y(
            "MAE:Q",
            title="Mean Absolute Error (Pathways)"
        ),
        color=alt.Color(
            "Model:N",
            title="Forecasting Model"
        ),
        tooltip=[
            alt.Tooltip(
                "cutoff:T",
                title="Forecast Origin",
                format="%b %Y"
            ),
            alt.Tooltip("Model:N"),
            alt.Tooltip("MAE:Q", format=".2f")
        ]
    )
    .properties(height=350)
)

st.altair_chart(cv_chart, use_container_width=True)
st.markdown(
    """
    **Cross-Validation Findings**

    - **March 2024:** Naive and SARIMA achieved identical MAE
      scores of approximately 153.86 pathways.
    - **October 2024:** Naive outperformed SARIMA, recording
      an MAE of 109.14 compared with 187.46.
    - **May 2025:** SARIMA substantially outperformed Naive,
      recording an MAE of 109.00 compared with 354.14.

    SARIMA achieved the lowest average cross-validation MAE,
    but its advantage was concentrated in the third evaluation
    window. Neither model consistently outperformed the other
    across all three windows.
    """
)

st.subheader("Model Selection and Limitations")

st.markdown(
    """
    **Selected Model: Naive**

    The Naive model was selected for the final six-month forecast
    because it achieved the joint-lowest holdout MAE (105.71)
    and provides a simple, interpretable forecasting baseline.

    Although SARIMA performed better on average during
    cross-validation, its performance varied across evaluation
    windows.

    **Limitations**

    - The dataset contains only 43 monthly observations,
      limiting the assessment of long-term seasonal patterns.
    - The Naive model assumes the most recent observed backlog
      remains the point forecast for subsequent months.
    - Forecasts are estimates, not guaranteed future outcomes.
    """
)



# footer
render_footer()