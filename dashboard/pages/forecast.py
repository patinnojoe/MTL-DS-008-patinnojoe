import streamlit as st

from components.header import render_header
from components.footer import render_footer
from utils.data_loader import load_data, load_forecast
import pandas as pd
import altair as alt


# Load historical data
df = load_data()
forecast_df = load_forecast()

# latest data
last_observed_month = df.iloc[-1]['period'].strftime("%B %Y")
last_observed_backlog = df.iloc[-1]['Total number of incomplete pathways']



# Prepare historical observations
historical = df[
    ["period", "Total number of incomplete pathways"]
].rename(
    columns={
        "period": "Date",
        "Total number of incomplete pathways": "Actual"
    }
)

# Prepare forecast observations
predictions = forecast_df[
    ["ds", "Naive"]
].rename(
    columns={
        "ds": "Date",
        "Naive": "Forecast"
    }
)


chart_data = pd.concat(
    [historical, predictions],
    ignore_index=True
).sort_values("Date")



# add uncertain values
forecast_chart = forecast_df.rename(
    columns={
        "ds": "Date",
        "Naive": "Forecast",
        "Naive-lo-80": "Lower 80",
        "Naive-hi-80": "Upper 80",
        "Naive-lo-95": "Lower 95",
        "Naive-hi-95": "Upper 95"
    }
)
# make dates consistent
historical["Date"] = pd.to_datetime(historical["Date"])
forecast_chart["Date"] = pd.to_datetime(forecast_chart["Date"])

# metrics
final_forecast = forecast_chart.iloc[-1]

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


# Page header
render_header("Waiting List Forecast")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Forecast Backlog",
        value=f"{final_forecast['Forecast']:,.0f}",
        delta=f"{final_forecast['Date'].strftime("%B %Y")}",
         delta_color="off"
    )
with col2:
    st.metric(
            label="80% Prediction Interval",
            value=f"{final_forecast['Lower 80']:,.0f} - {final_forecast['Upper 80']:,.0f}",
            delta=f"{final_forecast['Date'].strftime("%B %Y")}",
            delta_color="off"
        )
with col3:
    st.metric(
            label="95% Prediction Interval",
            value=f"{final_forecast['Lower 95']:,.0f} - {final_forecast['Upper 95']:,.0f}",
            delta=f"{final_forecast['Date'].strftime("%B %Y")}",
             delta_color="off"
        )


st.markdown(
    """
    This page presents a six-month forecast of incomplete
    Referral to Treatment (RTT) pathways in Trauma and
    Orthopaedics at Lancashire Teaching Hospitals NHS
    Foundation Trust.

    The forecast uses historical data from January 2023
    to July 2026.
    """
)

# Shared chart axes
x_axis = alt.X(
    "Date:T",
    title="Reporting Month",
    axis=alt.Axis(format="%b %Y")
)

y_axis = alt.Y(
    "Actual:Q",
    title="Incomplete RTT Pathways",
    scale=alt.Scale(zero=False)
)

# 80% prediction interval
band_80 = alt.Chart(forecast_chart).mark_area(
    color="steelblue",
    opacity=0.50
).encode(
    x=x_axis,
    y=alt.Y("Lower 80:Q", title="Incomplete RTT Pathways"),
    y2="Upper 80:Q",
    tooltip=[
        alt.Tooltip("Date:T", title="Month", format="%b %Y"),
        alt.Tooltip("Forecast:Q", title="Point Forecast", format=",.0f"),
        alt.Tooltip("Lower 80:Q", title="80% Lower Bound", format=",.0f"),
        alt.Tooltip("Upper 80:Q", title="80% Upper Bound", format=",.0f")
    ]
)

# 95% prediction interval
band_95 = alt.Chart(forecast_chart).mark_area(
    color="steelblue",
    opacity=0.15
).encode(
    x=x_axis,
    y=alt.Y("Lower 95:Q", title="Incomplete RTT Pathways"),
    y2="Upper 95:Q",
    tooltip=[
        alt.Tooltip("Date:T", title="Month", format="%b %Y"),
        alt.Tooltip("Forecast:Q", title="Point Forecast", format=",.0f"),
        alt.Tooltip("Lower 95:Q", title="95% Lower Bound", format=",.0f"),
        alt.Tooltip("Upper 95:Q", title="95% Upper Bound", format=",.0f")
    ]
)

# Historical line
historical_line = alt.Chart(historical).mark_line(
    color="#222222",
    strokeWidth=2.5,
    point=True
).encode(
    x=x_axis,
    y=y_axis,
    tooltip=[
        alt.Tooltip("Date:T", title="Month", format="%b %Y"),
        alt.Tooltip("Actual:Q", title="Actual Backlog", format=",")
    ]
)

# Forecast line
forecast_line = alt.Chart(forecast_chart).mark_line(
    color="#E67E22",
    strokeWidth=3,
    strokeDash=[6, 4],
    point=True
).encode(
    x=x_axis,
    y=alt.Y("Forecast:Q", title="Incomplete RTT Pathways"),
    tooltip=[
        alt.Tooltip("Date:T", title="Month", format="%b %Y"),
        alt.Tooltip("Forecast:Q", title="Forecast Backlog", format=",")
    ]
)

# Combined chart
combined_chart = alt.layer(
    band_95,
    band_80,
    historical_line,
    forecast_line
).resolve_scale(
    x="shared",
    y="shared"
).properties(
    height=450
)

st.subheader("Historical Backlog and Six-Month Forecast")

st.caption(
    "Black: historical backlog | Orange dashed: Naive forecast | "
    "Dark blue: 80% prediction interval | Light blue: 95% prediction interval"
)

st.altair_chart(
    combined_chart,
    use_container_width=True
)

# forecast table
st.subheader('Six-Month Forecast, August 2026 - January 2027')
st.dataframe(forecast_df)

# forecast interpretation
st.subheader("Forecast Interpretation")
st.markdown(
    """
    #### Projected Waiting-List Backlog

    The Naive forecasting model projects **4,771 incomplete RTT pathways per month**
    from August 2026 to January 2027, based on the last observed backlog in July 2026.

    The constant forecast reflects the model's use of the most recent observation
    as the prediction for subsequent months. However, this does not imply that
    actual waiting-list levels will remain unchanged.

    #### Forecast Uncertainty

    Although the point forecast remains constant at **4,771 pathways**, actual
    future backlog levels may differ from this estimate. To quantify this
    uncertainty, the model produces **80% and 95% prediction intervals**.

    These intervals provide ranges intended to contain future observations at
    their respective coverage levels, assuming the model's uncertainty estimates
    are appropriately calibrated.

    Prediction intervals widen as the forecast horizon increases, reflecting
    greater uncertainty about backlog levels further into the future.

    **For example, the 95% prediction intervals are:**

    - **August 2026:** 4,499–5,043 incomplete pathways.
    - **January 2027:** 4,105–5,437 incomplete pathways.

    The widening range indicates that the model is less certain about the
    backlog six months ahead than one month ahead.
    """
)



render_footer()