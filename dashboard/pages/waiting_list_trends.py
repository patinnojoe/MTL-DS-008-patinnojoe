import streamlit as st
from components.header import render_header
from components.footer import render_footer
from utils.data_loader import load_data
import pandas as pd



#---------------
# load data
df = load_data()
# monthly change
df['monthly_change'] = df['Total number of incomplete pathways'].diff()

# largest monthly change
largest_monthly_changes = (
    df.nlargest(5, "monthly_change")
    [["month_label", "monthly_change"]]
    .reset_index(drop=True)
)
# summary statistics
backlog_column = "Total number of incomplete pathways"

starting_backlog = df.iloc[0][backlog_column]
latest_backlog = df.iloc[-1][backlog_column]

net_change = latest_backlog - starting_backlog

percentage_change = (net_change / starting_backlog) * 100

largest_increase = df.loc[df["monthly_change"].idxmax()]

# average RTT by year
average_incomplete_RTT_by_year = (
    df.groupby("year")["Total number of incomplete pathways"]
    .mean()
    .reset_index()
    .rename(columns={
        "year": "Year",
        "Total number of incomplete pathways": "Average Incomplete Pathways"
    })
)





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



render_header("Waiting List Trends")

# backlog change overtime
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Net Backlog Change",
        value=f"{net_change:+,.0f}",
        delta="Since January 2023",
        delta_color="inverse"
    )

with col2:
    st.metric(
        label="Overall Backlog Growth",
        value=f"{percentage_change:+.1f}%",
        delta="Since January 2023",
        delta_color="inverse"
    )

with col3:
    st.metric(
        label="Largest Monthly Increase",
        value=f"{largest_increase['monthly_change']:+,.0f}",
        delta=largest_increase["month_label"],
        delta_color="inverse"
    )
    
st.write(" ")
st.write(" ")

# plot RTT overtime
st.subheader("Incomplete RTT Pathways Over Time")
st.line_chart(
    data=df,
    x="period",
    y="Total number of incomplete pathways",
    x_label="Reporting Month",
    y_label="Incomplete Pathways"
)

st.write(" ")
st.write(" ")

# plot RTT change month by month
st.subheader("Month by Month Change in Incomplete Pathways")
st.bar_chart(
    data=df,
    x="period",
    y="monthly_change",
    x_label="Reporting Month",
    y_label="Incomplete Pathways Monthly Change"
    
)

st.write(" ")
st.write(" ")



# plot year on year average for Incomplete RTT
st.subheader("Yearly Average of Incomplete pathways")
st.caption("2026 figures cover January–July only.")
st.bar_chart(y='Average Incomplete Pathways', x='Year', data=average_incomplete_RTT_by_year)





render_footer()


