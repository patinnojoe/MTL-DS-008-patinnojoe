
import streamlit as st
import pandas as pd
from components.header import render_header
from components.footer import render_footer
from utils.data_loader import load_data


# Load data
df = load_data()


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



# --------------------------------
# Waiting-time categories
# --------------------------------

short_wait_columns = [
    f">{i}-{i+1}" for i in range(0, 12)
]

standard_wait_columns = [
    f">{i}-{i+1}" for i in range(12, 18)
]

long_wait_columns = [
    f">{i}-{i+1}" for i in range(18, 104)
] + ["104 plus"]

df["Short Waits"] = df[short_wait_columns].sum(axis=1)
df["Standard Waits"] = df[standard_wait_columns].sum(axis=1)
df["Long Waits"] = df[long_wait_columns].sum(axis=1)


# --------------------------------
# Waiting-time profile data
# --------------------------------

waiting_time_profile = df[
    ["period", "Short Waits", "Standard Waits", "Long Waits"]
]


# Annual waiting-time profile
annual_waiting_profile = (
    df.groupby("year")[
        ["Short Waits", "Standard Waits", "Long Waits"]
    ].sum()
)

annual_waiting_profile["Total"] = (
    annual_waiting_profile[
        ["Short Waits", "Standard Waits", "Long Waits"]
    ].sum(axis=1)
)

annual_waiting_percent = (
    annual_waiting_profile[
        ["Short Waits", "Standard Waits", "Long Waits"]
    ]
    .div(annual_waiting_profile["Total"], axis=0)
    .mul(100)
    .reset_index()
)


# --------------------------------
# KPI calculations
# --------------------------------

# 1. Average monthly median waiting time
average_median_wait = df[
    "Average (median) waiting time (in weeks)"
].mean()


# 2. Percentage of recorded pathways within 18 weeks
within_18_percentage = (
    df["Total within 18 weeks"].sum()
    / df["Total number of incomplete pathways"].sum()
) * 100


# 3. Percentage of recorded pathways waiting 52+ weeks
waiting_52_percentage = (
    df["Total 52 plus weeks"].sum()
    / df["Total number of incomplete pathways"].sum()
) * 100


# 4. Largest waiting-time group in 2026
df_2026 = df[df["year"] == 2026]

average_2026_categories = df_2026[
    ["Short Waits", "Standard Waits", "Long Waits"]
].mean()

largest_2026_category = average_2026_categories.idxmax()
largest_2026_count = average_2026_categories.max()

# 5. average waiting time within 18 weeks
waiting_time_percentiles = df[
    [
        "period",
        "Average (median) waiting time (in weeks)",
        "92nd percentile waiting time (in weeks)"
    ]
]


# 

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

render_header("Waiting Time Profile")


# --------------------------------
# KPIs
# --------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Average Monthly Median Wait",
        value=f"{average_median_wait:.1f} weeks"
    )

with col2:
    st.metric(
        label="Within 18 Weeks",
        value=f"{within_18_percentage:.1f}%",
        help=(
            "Percentage of recorded incomplete pathway-month "
            "observations within 18 weeks across January 2023 "
            "to July 2026. Calculated using summed monthly counts."
        )
    )

with col3:
    st.metric(
        label="Waiting 52+ Weeks",
        value=f"{waiting_52_percentage:.1f}%",
         help=(
            "Percentage of recorded incomplete pathway-month "
            "observations waiting at least 52 weeks across "
            "January 2023 to July 2026. Calculated using "
            "summed monthly counts."
        )
    )

with col4:
    st.metric(
        label=f"Largest Waiting Group (2026)",
        value=largest_2026_category,
        delta=f"{largest_2026_count:,.0f} average pathways/month",
        delta_color="off"
    )


# --------------------------------
# Waiting-time statistics
# --------------------------------

st.subheader("Waiting-Time Statistics")

st.line_chart(
    data=waiting_time_profile,
    x="period",
    y=["Short Waits", "Standard Waits", "Long Waits"],
    x_label="Reporting Month",
    y_label="Incomplete Pathways"
)


# --------------------------------
# Annual waiting-time composition
# --------------------------------

st.subheader("Annual Waiting-Time Distribution")
st.caption("2026 figures cover January–July only.")

st.bar_chart(
    data=annual_waiting_percent,
    x="year",
    y=["Short Waits", "Standard Waits", "Long Waits"],
    stack=True,
    x_label="Year",
    y_label="Percentage of Incomplete Pathways"
)




# ---------------
# waiting time median and 92nd percentile
# ---------------
st.subheader("Median and 92nd Percentile Waiting Time")
st.line_chart(
    data=waiting_time_percentiles, 
    x="period",
    y=[
        "Average (median) waiting time (in weeks)",
        "92nd percentile waiting time (in weeks)"
    ],
    x_label="Reporting Month",
    y_label="Waiting Time (Weeks)"
)

render_footer()
