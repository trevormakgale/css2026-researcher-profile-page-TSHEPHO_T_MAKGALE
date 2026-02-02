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
    ["RESEARCH PROFILE", "INTRODUCTION and METHODS", "RESULTS and DISCUSSION", "PUBLICATIONS", "CONTACTS"],
)
Ag_text = '''
Figure 1. UV-Vis absorption spectra of CTAB-stabilized (Ag-NRs) and SnO₂-stabilized (Ag-NRs@SnO₂) silver nanorods. Uncoated Ag-NRs exhibit transverse SPR peaks at 412 nm, 411 nm, and 410 nm, with corresponding longitudinal SPR peaks at 548 nm, 549 nm, and 710 nm for samples A, B, and C 
(aspect ratios: 2.4, 2.8, and 3.3). Coated Ag-NRs@SnO₂ show red-shifted transverse SPR peaks at 452 nm, 453 nm, and 448 nm, with longitudinal SPR peaks at 605 nm, 655 nm, and 715 nm. Heat capacities of SnO₂-stabilized Ag-NRs-water mixtures (25% by volume) were measured at 8797.65, 8134.74, and 8454.38 J/°
C·Kg, surpassing those of CTAB-stabilized counterparts, which recorded 8045.44, 8004.88, and 7651.65 J/°C·Kg.
'''
Au_text = '''
Figure 2. UV-Vis absorption spectra and thermal capacity measurements of CTAB-stabilized (Au-NRs) and SnO₂-stabilized (Au-NRs@SnO₂) gold nanorods. Uncoated Au-NRs exhibit transverse SPR peaks at 585 nm, 575 nm, and 574 nm, with longitudinal SPR
peaks at 851 nm (sample A), 810 nm and 860 nm (sample B), and 760 nm, 825 nm, and 865 nm (sample C), corresponding to aspect ratios of 2.2, 2.4, and 2.6. Coated Au-NRs@SnO₂ show blue-shifted transverse SPR peaks at 565 nm, 570 nm, and 549 nm due 
to size reduction from the SnO₂ coating, with longitudinal SPR peaks at 680, 750, 820, 870, and 920 nm (sample A), 680, 755, 800, and 900 nm (sample B), and 790, 849, and 925 nm (sample C). 
Heat capacities of SnO₂-stabilized Au-NRs-water mixtures were measured at 7850.58, 8324.08, and 7918.39 J/°C·Kg, surpassing those of CTAB-stabilized counterparts at 7807.70, 8003.29, and 7773.63 J/°C·Kg.
'''

Ag_Ag_text = '''
Figure 3. UV-Vis spectra of uncoated and SnO₂-coated materials. The uncoated materials exhibit distinct SPR peaks at 410 nm and 560 nm, highlighting their plasmonic properties, while the SnO₂-coated materials show a broader absorption profile (350–850 nm). 
The figure also presents the thermal properties of SnO₂-coated and uncoated Ag-Au-NRs-water mixtures, with heat capacities of 7734.12 and 7709.25 J/°C·Kg, respectively. Additionally, Under 1.3511 Suns, solar steam generation efficiencies were found to be 10.87, 10.71, 
and 10.32 for SnO₂-coated materials, uncoated materials, and pure water, respectively.
'''

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
elif menu == "RESULTS and DISCUSSION":
    st.title("RESULTS and DISCUSSION")
    st.sidebar.header("RESULT Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose MATERIAL TYPE to explore", 
        ["Silver (Ag) Nanocomposites", "Gold (Au) Nanocomposites", "Blended Ag-Au Nanocomposites", "CONCLUSION"]
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
        
        st.write(f'''**Discussion:** 
                    {Ag_text}''')
        

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
        
        st.write(f'''**Discussion:** 
                    {Au_text}''')
        

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
        
        st.write(f'''**Discussion:** 
                    {Ag_Ag_text}''')
        
    elif data_option == "CONCLUSION":
        st.write("### CONCLUSION")
         
        st.write('''This study demonstrated that encapsulating silver and gold nanorods with tin dioxide (SnO₂) significantly enhanced their optical and thermal properties, making them highly effective for solar steam generay blending Au@SnO₂ and Ag@SnO₂ nanocomposites, we further improved spectral coverage, thereby maximisbroadens their light absorption range, overcoming the narrow-band limitations of individual metal nanorods. 
         Additionally, blending Au@SnO₂ and Ag@SnO₂ nanocomposites, we were able to further improve spectral coverage, maximizing solar energy capture.
         ''') 
         
        st.write('''The SnO₂-coated nanorods exhibited higher heat capacities than their CTAB-stabilized counterparts and pure water, improving thermal energy retention and conversion. Under 1.35 Suns, solar steam generation efficiencies reached 
         10.87% for SnO₂-coated materials, surpassing the 10.71% and 10.32% efficiencies of uncoated materials and pure water, respectively, within just 30 minutes of solar exposure. These findings highlight the potential of SnO₂ 
         encapsulation and strategic nanocomposite blending as a promising pathway to advancing solar-driven water purification and energy applications.
         ''')
        st.markdown("**References:**")
        st.image("references.png")
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
    st.image("footer.png")
with footer_cols[1]:
    st.markdown("© 2026 Coding Summer School 2026")
with footer_cols[2]:
    st.markdown("Last updated: January 2026")
