import streamlit as st
import plotly.express as px
from read_snowflake_tables import read_table

def show():
    st.title("🚶 Tourism Trends by State")

    df = read_table("STATE_WISE_TOURISM")
    df["TOTAL_VISITORS"] = df[["DTVS_2019", "DTVS_2020", "DTVS_2021", "FTVS_2019", "FTVS_2020", "FTVS_2021"]].fillna(0).sum(axis=1)
    df["STATE_UT"] = df["STATE_UT"].str.title()
    st.subheader("Top 10 States by Tourist Footfall (2019–2021)")
    df = df[df["STATE_UT"].str.lower() != "total"]
    top_states = df.sort_values("TOTAL_VISITORS", ascending=False).head(10)
    fig = px.bar(top_states, x="STATE_UT", y="TOTAL_VISITORS", color="STATE_UT", title="Most Visited States")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("All States – Visitors Table")
    st.dataframe(df[["STATE_UT", "TOTAL_VISITORS"]].sort_values("TOTAL_VISITORS", ascending=False))
