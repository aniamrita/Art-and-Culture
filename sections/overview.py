import streamlit as st

def show():
    st.title("🇮🇳 Cultural Tourism Insights – India")
    st.markdown("""
        **Welcome!** This app presents a data-driven journey through India's rich cultural and artistic landscape.
        
        ### 🎯 Project Goals
        - Showcase traditional art forms
        - Analyze cultural tourism trends
        - Visualize government support for culture
        - Promote responsible tourism to underexplored areas

        ### 📊 Data Sources
        - [data.gov.in](https://data.gov.in)
        - Snowflake-hosted tables from Ministries

        Navigate using the sidebar to explore the insights!
    """)
    st.image("https://en.wikipedia.org/wiki/Kathakali#/media/File:Kathakali_-Play_with_Kaurava.jpg", use_container_width=True)
