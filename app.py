import streamlit as st
import requests
import pandas as pd

st.title("🌌 Current Space Station Tracker")
st.markdown("""
This app shows:
- The total number of people currently in space
- The names of astronauts currently in orbit
- The **real-time location of the International Space Station (ISS)** visualized on a map
""")

# 1. Fetch data about astronauts in space
astro_url = "http://api.open-notify.org/astros.json"
astro_response = requests.get(astro_url)

if astro_response.status_code == 200:
    astro_data = astro_response.json()
    num_people = astro_data.get('number', 0)
    people = astro_data.get('people', [])
    
    st.subheader(f"👨‍🚀 Total number of people in space: {num_people}")
    st.markdown("### Names of astronauts currently in space:")
    for person in people:
        st.write(f"- {person['name']} ({person['craft']})")
else:
    st.error("Failed to load astronauts data.")

# 2. Fetch ISS current location
iss_url = "http://api.open-notify.org/iss-now.json"
iss_response = requests.get(iss_url)

if iss_response.status_code == 200:
    iss_data = iss_response.json()
    position = iss_data.get('iss_position', {})
    latitude = float(position.get('latitude', 0))
    longitude = float(position.get('longitude', 0))
    
    st.subheader("🛰️ Current location of the ISS")
    st.markdown(f"The International Space Station is currently at:")
    st.markdown(f"- Latitude: {latitude:.4f}")
    st.markdown(f"- Longitude: {longitude:.4f}")
    
    # 3. Show ISS location on a map
    df_location = pd.DataFrame({
        'lat': [latitude],
        'lon': [longitude]
    })
    
    st.map(df_location)
    
    st.markdown("The map above shows the real-time position of the ISS on Earth.")
else:
    st.error("Failed to load ISS location data.")
