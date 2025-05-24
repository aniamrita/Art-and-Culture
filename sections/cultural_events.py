import streamlit as st
import plotly.express as px
from transform import cult_event_df

def show():
    st.title("🎭 Cultural Events & Seasonality")

    st.subheader("Event Distribution by Season")
    season_counts = cult_event_df["SEASON"].value_counts().reset_index()
    season_counts.columns = ["Season", "Event Count"]
    fig = px.pie(season_counts, names="Season", values="Event Count", title="Event Seasonality")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Events by State")
    selected_state = st.selectbox("Select State", sorted(cult_event_df["STATE"].dropna().unique()))
    st.dataframe(
        cult_event_df[cult_event_df["STATE"] == selected_state][["EVENT_NAME", "ART_FORM", "SEASON", "DATE", "ATTENDANCE"]]
    )
