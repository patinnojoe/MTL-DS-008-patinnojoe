import streamlit as st
from components.header import render_header
from components.footer import render_footer
from utils.data_loader import load_data



# create KPIs
df = load_data()

# Latest reporting period
latest = df.iloc[-1]

# First reporting period
earliest = df.iloc[0]

# Extract KPI values
current_backlog = latest["Total number of incomplete pathways"]

starting_backlog = earliest["Total number of incomplete pathways"]

backlog_change = current_backlog - starting_backlog

long_waits = latest["Total 52 plus weeks"]

performance_18_weeks = latest["% within 18 weeks"]

col1, col2, col3, col4 = st.columns(4)



#---------------

st.markdown(
    """
    <style>
        .stMainBlockContainer > div[data-testid="stVerticalBlock"] {
            min-height: calc(100vh - 4rem);
            display: flex;
            flex-direction: column;
        }

        .st-key-page_content {
            flex: 1;
        }
    </style>
    """,
    unsafe_allow_html=True
)



render_header("Project Overview")


with col1:
    st.metric(
        label="Current Backlog",
        value=f"{current_backlog:,.0f}",
        delta=f"{backlog_change:+,.0f} since {earliest['month_label']}",
        delta_color="inverse"
    )

with col2:
    st.metric(
        label="Backlog Change",
        value=f"{backlog_change:+,.0f}",
        help="Difference between the first and latest reporting periods."
    )

with col3:
    st.metric(
        label="Waiting 52+ Weeks",
        value=f"{long_waits:,.0f}"
    )

with col4:
    st.metric(
        label="Within 18 Weeks",
        value=f"{performance_18_weeks:.1f}%"
    )

  
st.write(" ")
st.write(" ")

st.markdown(
    """
    **Service:** Trauma and Orthopaedics (TOS)

    **Measure:** Incomplete Referral to Treatment (RTT) pathways

    This dashboard examines historical waiting-list trends and
    presents a six-month forecast to support service monitoring
    and capacity-planning discussions.
    """
)



st.caption(
    "Data period: January 2023 – July 2026 | "
    "Forecast horizon: August 2026 – January 2027"
)


render_footer()