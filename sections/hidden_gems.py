import streamlit as st
import plotly.express as px
import pandas as pd
from transform import merged_df_2

def show():
    st.title("🌟 Hidden Cultural Gems Across India")

    st.markdown("""
        These are culturally rich states that may be underexplored in tourism. 
        Each row represents the most attended cultural event per state.
    """)

    st.dataframe(merged_df_2)

    st.subheader("🧭 Visitors vs Event Attendance")

    fig = px.scatter(
        merged_df_2,
        x="ATTENDANCE",
        y="TOTAL_VISITORS",
        size="TOTAL_VISITORS",
        color="SEASON",
        hover_name="STATE",
        text="EVENT_NAME",
        labels={"ATTENDANCE": "Event Attendance", "TOTAL_VISITORS": "Total Tourism Footfall"},
        title="Are We Visiting Our Most Culturally Vibrant States?"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🎨 Top Art Forms by State")
    st.table(merged_df_2[["STATE", "ART_FORM", "EVENT_NAME"]])
