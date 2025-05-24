import streamlit as st
import plotly.express as px
from transform import merged_df 
def show():
    st.title("🏛 Government Support for Culture")

    st.subheader("Cultural Budget vs Tourism Footfall")

    fig = px.scatter(
        merged_df,
        x="ALLOCATION_IN_CR",
        y="TOTAL_VISITORS",
        size="TOTAL_VISITORS",
        color="INITIATIVE_TAKEN",
        hover_name="STATE",
        labels={"ALLOCATION_IN_CR": "Cultural Budget (Cr)", "TOTAL_VISITORS": "Visitors"},
        title="Does Higher Cultural Investment Correlate with More Tourists?"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Detailed View")
    st.dataframe(merged_df[["STATE", "TOTAL_VISITORS", "ALLOCATION_IN_CR", "INITIATIVE_TAKEN"]])
