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
        # 3-column layout for highlights
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("States Covered", "30+")

    with col2:
        st.metric("Tourism Records", "18,000,000+")

    with col3:
        st.metric("Cultural Events", "500+")

    st.markdown("""
        ---
        ### 🔍 Navigate Through the App

        Use the sidebar to explore:
        - **Tourism Trends** → Compare visitor footfall across years and regions
        - **Government Support** → See where cultural funding is flowing
        - **Cultural Events** → Discover seasonal festivals and traditional performances
        - **Hidden Gems** → Spot the culturally rich yet overlooked states
    """)
