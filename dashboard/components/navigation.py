
import streamlit as st


def render_navigation():

    pages = [
        st.Page(
            "pages/overview.py",
            title="Overview",
            icon=":material/dashboard:",
            default=True
        ),

        st.Page(
            "pages/waiting_list_trends.py",
            title="Waiting List Trends",
            icon=":material/trending_up:"
        ),

        st.Page(
            "pages/waiting_time_profile.py",
            title="Waiting-Time Profile",
            icon=":material/schedule:"
        ),

        st.Page(
            "pages/forecast.py",
            title="Forecast",
            icon=":material/monitoring:"
        ),

        st.Page(
            "pages/model_evaluation.py",
            title="Model Evaluation",
            icon=":material/analytics:"
        )
    ]

    return st.navigation(
        pages,
        position="sidebar"
    )
