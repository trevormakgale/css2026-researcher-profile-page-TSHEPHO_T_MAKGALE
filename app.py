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
#                                       PAGE
# =========================================================================

# Set page title
st.set_page_config(
    page_title= "Researcher Profile: Interactive Poster",
    page_icon= "🔬",
    layout= "wide"
)
# =========================================================================


# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["RESEARCH PROFILE", "INTRODUCTION and METHODS", "RESULTS", "PUBLICATIONS", "CONTACTS"],
)

# =========================================================================
#                                       FRONT: TITLE PAGE
# =========================================================================


# Sections based on menu selection
if menu == "RESEARCH PROFILE":
    st.title("RESEARCH PROFILE: INTERACTIVE POSTER")
    st.sidebar.header("Profile Options")

    # Collect basic information 
    name = "(Mr) Tshepho Trevor Makgale"
    field = "Solar Material Science"
    institution = " University of Pretoria, Private Bag X20, Hatfield 0028, South Africa"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    st.markdown("**Department:** Physics")
    
    st.image(
    "Solar-Materials.png",
    caption="Nature (Pixabay)")

    text = ''' I am a postgraduate researcher in the physical sciences with a strong focus on nanomaterials, photocatalysis, and solar energy conversion. 
    My current research explores carbon-based and plasmonic hybrid nanostructures for applications in photocatalytic hydrogen production, carbon dioxide 
    reduction, and solar steam generation. I am particularly interested in understanding and modelling the underlying mechanisms that govern charge transfer, 
    light–matter interactions, and reaction kinetics at the nanoscale.
    '''
    # Display basic profile information
    st.write(f"**Researcher Profile:** {text}")
    
# =========================================================================
#                                       INTRODUCTION and METHODS
# =========================================================================


# Sections based on menu selection
elif menu == "INTRODUCTION and METHODS":
    st.title("INTRODUCTION and METHODS")
    st.sidebar.header("Profile Options")

    # Research information
    text = '''Solar steam generation (SSG), which harnesses the abundant and clean energy of sunlight, has emerged as one of the most promising technologies in addressing global freshwater scarcity [1].
    One of the important applications of SSG is in water purification and desalination, which are processes critical to ensuring access to clean water. However, traditional SSG systems, which rely
    on sunlight to directly heat the entire bulk water, suffer from low solar energy conversion efficiency and result in insufficient bulk water temperatures [2, 3]. To overcome these limitations, re-
    searchers have explored a variety of solar absorbers including metallic nanomaterials [4], carbon-based materials [5], semiconductors, and polymers to develop more efficient, modern solar-
    driven evaporation systems. A particularly promising approach involves nanofluid-based SSG systems, where plasmonic noble metals like gold (Au) and silver (Ag) serve as direct-absorption
    solar energy collectors. In this study, Au and Ag nanostructures were coated with tin dioxide (SnO2), and their blended mixtures were assessed to develop enhanced photothermal materials for
    solar steam generation.'''

    # Display basic profile information
    st.write(f'''**Introduction:** 
                    {text}''')
    
    
    st.image(
    "Intro.png",
    caption="Nature (Pixabay)")
    
    st.markdown("**Methods:**")
    st.image(
    "Methods.png",
    caption="Nature (Pixabay)")
        
    
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
        st.markdown("**Transmission Electron Micrographs (TEM Images):**")
        st.image(
                "AgComposites.png",
                caption="Nature (Pixabay)")

        st.markdown("**Ultraviolet-Visible spectrographs (UV-VIS Images):**")
        st.image(
                "AgComposites_UV.png",
                caption="Nature (Pixabay)")
        
        

    elif data_option == "Gold (Au) Nanocomposites":
        st.write("### Gold (Au) Nanocomposites")
        st.markdown("**Transmission Electron Micrographs (TEM Images):**")
        st.image(
                "AuComposites.png",
                caption="Nature (Pixabay)")
        
        st.markdown("**Ultraviolet-Visible spectrographs (UV-VIS Images):**")
        st.image(
                "AuComposites_UV.png",
                caption="Nature (Pixabay)")
        

    elif data_option == "Blended Ag-Au Nanocomposites":
        st.write("### Blended Ag-Au Nanocomposites")
        st.markdown("**Transmission Electron Micrographs (TEM Images):**")
        st.image(
                "Ag-AuComposites.png",
                caption="Nature (Pixabay)")
        
        st.markdown("**Ultraviolet-Visible spectrographs (UV-VIS Images):**")
        st.image(
                "Ag-AuComposites_UV.png",
                caption="Nature (Pixabay)")
         
        
# =========================================================================
#                                       CONTACTS
# =========================================================================
       

elif menu == "CONTACTS":
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
