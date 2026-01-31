import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import io
import base64

# Page configuration
st.set_page_config(
    page_title="CSS2026 Research Profile",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2c3e50;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #3498db;
        border-bottom: 3px solid #3498db;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .paper-card {
        background: white;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #3498db;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🔬 CSS2026 Research Profile: Computational Social Science Researcher</h1>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=300", 
             caption="Research Profile", use_column_width=True)
    
    st.markdown("### Contact Information")
    st.markdown("**Institution:** University of Innovation")
    st.markdown("**Department:** Computational Social Science")
    st.markdown("**Email:** researcher@css2026.edu")
    st.markdown("**ORCID:** 0000-0000-0000-0000")
    
    st.markdown("---")
    
    st.markdown("### Research Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Citations", "1,234", "+12%")
    with col2:
        st.metric("h-index", "18", "+2")
    
    st.markdown("---")
    
    st.markdown("### Skills")
    skills = {
        "Python": 95,
        "R": 85,
        "Machine Learning": 90,
        "NLP": 80,
        "Network Analysis": 75,
        "Statistics": 95
    }
    
    for skill, level in skills.items():
        st.markdown(f"**{skill}**")
        st.progress(level/100)

# Main content in columns
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown('<h3 class="section-header">👤 About Me</h3>', unsafe_allow_html=True)
    st.markdown("""
    I'm a Computational Social Science researcher focused on:
    - Social network analysis
    - NLP for social media
    - Computational sociology
    - AI ethics and fairness
    
    My work bridges computer science and social sciences to understand human behavior through data.
    """)

with col2:
    st.markdown('<h3 class="section-header">📊 Current Research</h3>', unsafe_allow_html=True)
    
    # Research progress
    research_projects = pd.DataFrame({
        'Project': ['Social Media Analysis', 'Network Dynamics', 'AI Ethics', 'COVID-19 Impact'],
        'Progress': [85, 70, 60, 90],
        'Team Size': [5, 3, 4, 6]
    })
    
    fig = px.bar(research_projects, x='Project', y='Progress',
                 title='Research Project Progress',
                 color='Team Size',
                 color_continuous_scale='viridis')
    st.plotly_chart(fig, use_container_width=True)

with col3:
    st.markdown('<h3 class="section-header">🎓 Education</h3>', unsafe_allow_html=True)
    st.markdown("""
    - **PhD in Computational Social Science**  
      Stanford University (2020)
    
    - **MSc in Data Science**  
      MIT (2016)
    
    - **BSc in Sociology & Computer Science**  
      University of Chicago (2014)
    """)

# Publications section
st.markdown('<h3 class="section-header">📚 Recent Publications</h3>', unsafe_allow_html=True)

publications = [
    {
        "title": "Network Dynamics in Online Communities",
        "year": 2023,
        "journal": "Nature Communications",
        "citations": 142,
        "abstract": "Analyzing community formation and dissolution patterns in social networks."
    },
    {
        "title": "Bias Detection in Language Models",
        "year": 2023,
        "journal": "PNAS",
        "citations": 89,
        "abstract": "A novel method for detecting and mitigating biases in transformer models."
    },
    {
        "title": "COVID-19 Misinformation Spread",
        "year": 2022,
        "journal": "Science",
        "citations": 234,
        "abstract": "Network analysis of misinformation propagation during the pandemic."
    }
]

for pub in publications:
    with st.expander(f"{pub['title']} ({pub['year']}) - {pub['journal']} | Citations: {pub['citations']}"):
        st.markdown(f"**Abstract:** {pub['abstract']}")
        col1, col2 = st.columns(2)
        with col1:
            st.button("📄 PDF", key=f"pdf_{pub['title']}")
        with col2:
            st.button("🔗 DOI", key=f"doi_{pub['title']}")

# Research Data
st.markdown('<h3 class="section-header">📈 Research Data</h3>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Sample data visualization
    data = pd.DataFrame({
        'Year': list(range(2018, 2024)),
        'Publications': [3, 5, 8, 10, 12, 15],
        'Citations': [45, 120, 340, 560, 890, 1234]
    })
    
    fig = px.line(data, x='Year', y=['Publications', 'Citations'],
                  title='Research Output Over Time',
                  markers=True)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Collaboration network
    st.markdown("### Collaboration Network")
    st.graphviz_chart("""
        digraph {
            "You" -> "Columbia"
            "You" -> "MIT"
            "You" -> "Stanford"
            "You" -> "Oxford"
            "Columbia" -> "Harvard"
            "MIT" -> "Cambridge"
            "Stanford" -> "Berkeley"
            "Oxford" -> "Cambridge"
            node [shape=circle, style=filled, color=lightblue]
            "You" [color=orange]
        }
    """)

# Teaching section
st.markdown('<h3 class="section-header">👨‍🏫 Teaching & Mentoring</h3>', unsafe_allow_html=True)

teaching_cols = st.columns(3)

with teaching_cols[0]:
    st.markdown("### Courses Taught")
    st.markdown("""
    - CSS 101: Intro to Computational Social Science
    - CSS 301: Social Network Analysis
    - CSS 401: Advanced NLP for Social Data
    - CSS 501: Research Methods
    """)

with teaching_cols[1]:
    st.markdown("### Current PhD Students")
    students = pd.DataFrame({
        'Student': ['Alex Chen', 'Maria Garcia', 'David Kim'],
        'Year': [3, 2, 1],
        'Topic': ['AI Ethics', 'Network Theory', 'Social Media']
    })
    st.dataframe(students, use_container_width=True, hide_index=True)

with teaching_cols[2]:
    st.markdown("### Office Hours")
    st.markdown("""
    **Winter 2024:**
    - Monday: 2-4 PM
    - Wednesday: 10-12 PM
    
    **Location:**  
    CSS Building, Room 301
    
    **Book:** [Calendly Link](#)
    """)

# Footer
st.markdown("---")
footer_cols = st.columns(3)
with footer_cols[0]:
    st.markdown("**CSS2026 Research Profile**")
with footer_cols[1]:
    st.markdown("© 2024 Computational Social Science Lab")
with footer_cols[2]:
    st.markdown("Last updated: December 2024")

# Add download button for CV
st.sidebar.markdown("---")
st.sidebar.download_button(
    label="📥 Download CV",
    data="Sample CV content would go here",
    file_name="css2026_researcher_cv.pdf",
    mime="application/pdf"
)
