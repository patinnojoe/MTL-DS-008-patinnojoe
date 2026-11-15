
import streamlit as st


def render_footer():

    st.divider()

    st.markdown(
        """
        <div style="
            display: flex;
            justify-content: center;
            align-items: end;
            gap: 12px;
            padding: 12px 0;
            font-size: 14px;
            margin-top: 20px;"
            >
            <span>Created by Innocent Josiah Patrick</span>
            <span>|</span>
            <a href="https://www.linkedin.com/in/innocentjosiah57/" target="_blank">
                LinkedIn
            </a>
            <span>|</span>
            <a href="https://x.com/patinnojoe" target="_blank">
                X
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
