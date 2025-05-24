import streamlit as st
from sections import overview, tourism, govt_support, cultural_events, hidden_gems

# Page config
st.set_page_config(
    page_title="Indian Culture & Tourism",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio("Go to", [
    "Overview",
    "Tourism Trends",
    "Govt Contribution",
    "Cultural Events",
    "Hidden Cultural Gems"
])

# Route to sections
if menu == "Overview":
    overview.show()
elif menu == "Tourism Trends":
    tourism.show()
elif menu == "Govt Contribution":
    govt_support.show()
elif menu == "Cultural Events":
    cultural_events.show()
elif menu == "Hidden Cultural Gems":
    hidden_gems.show()