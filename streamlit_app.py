import streamlit as st
import pandas as pd

st.title("🏔️ Colorado Springs Trip Poll: May 23-30")
st.subheader("Vote for your top 5 must-do activities!")

activities = [
    "Garden of the Gods", "Pikes Peak Summit", "Cheyenne Mountain Zoo", 
    "Territory Days (Street Fest)", "U.S. Olympic Museum", "Manitou Penny Arcade",
    "Royal Gorge Bridge", "Cave of the Winds", "Seven Falls", "Manitou Incline",
    "Old Colorado City", "Air Force Academy", "Glen Eyrie Castle", 
    "Red Rock Canyon", "Manitou Cliff Dwellings", "North Pole Amusement Park",
    "Paint Mines", "Royal Gorge Railroad", "Great Wolf Lodge", "MeadowGrass Music Fest"
]

# User selection
selections = st.multiselect("Select your favorites:", activities)

if st.button("Submit My Votes"):
    st.success(f"Awesome! You chose: {', '.join(selections)}")
    st.balloons()

# Simple scoreboard simulation
st.divider()
st.write("### Current Leaderboard (Mockup)")
st.bar_chart({"Votes": [10, 8, 7, 5, 4]}, x=None) 
