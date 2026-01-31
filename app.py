# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Created on Sat Jan 31 13:13:14 2026
===================================

==============================
@author: tshephotrevormakgale
==============================
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

import streamlit as st
import pandas as pd
import numpy as np


# =========================================================================
#                                       RAGE
# =========================================================================

# Set page title
st.set_page_config(
    page_title= "Researcher Profile and STEM Data Explorer",
    page_icon= "🔬",
    layout= "wide"
)
# =========================================================================


# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["RESEARCH PROFILE","RESULTS","PUBLICATIONS","CONTACTS"],
)

# Dummy STEM data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# =========================================================================
#                                       FRONT: TITLE PAGE
# =========================================================================


# Sections based on menu selection
if menu == "RESEARCH PROFILE":
    st.title("RESEARCH PROFILE")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "(Mr) Tshepho Trevor Makgale"
    field = "Solar Material Science"
    institution = "University of Pretoria"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    st.markdown("**Department:** Physics")
    
    st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
)
    
# =========================================================================
#                                       PUBLICATIONS
# =========================================================================

elif menu == "PUBLICATIONS":
    st.title("PUBLICATIONS")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")


# =========================================================================
#                                       RESULTS
# =========================================================================
elif menu == "RESULTS":
    st.title("RESULTS")
    st.sidebar.header("RESULT Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose MATERIAL TYPE to explore", 
        ["Silver (Ag) Nanocomposites", "Gold (Au) Nanocomposites", "Blended Ag-Au Nanocomposites"]
    )

    if data_option == "Silver (Ag) Nanocomposites":
        st.write("### Silver (Ag) Nanocomposites")
        st.dataframe(physics_data)
        # Add widget to filter by Energy levels
        energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
        filtered_physics = physics_data[
            physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
        ]
        st.write(f"Filtered Results for Energy Range {energy_filter}:")
        st.dataframe(filtered_physics)

    elif data_option == "Gold (Au) Nanocomposites":
        st.write("### Gold (Au) Nanocomposites")
        st.dataframe(astronomy_data)
        # Add widget to filter by Brightness
        brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
        filtered_astronomy = astronomy_data[
            astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
        ]
        st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
        st.dataframe(filtered_astronomy)

    elif data_option == "Blended Ag-Au Nanocomposites":
        st.write("### Blended Ag-Au Nanocomposites")
        st.dataframe(weather_data)
        # Add widgets to filter by temperature and humidity
        temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
        humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
        filtered_weather = weather_data[
            weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
            weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
        ]
        st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
        st.dataframe(filtered_weather)
        
# =========================================================================
#                                       CONTACTS
# =========================================================================
       

elif menu == "CONSTACTS":
    # Add a contact section
    st.header("Contact Information")
    email = "u14007739@tuks.co.za"
    st.write(f"You can reach me at {email}.")
    st.markdown("**ORCID:** 0000-0002-4444-8881")
    
    # Footer
st.markdown("---")
footer_cols = st.columns(3)
with footer_cols[0]:
    st.markdown("**CSS-2026 Research Profile| Interactive Research Poster SAIP 2024**")
with footer_cols[1]:
    st.markdown("© 2026 Coding Summer School 2026")
with footer_cols[2]:
    st.markdown("Last updated: January 2026")
