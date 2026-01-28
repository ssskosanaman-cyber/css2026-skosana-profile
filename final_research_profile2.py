# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 17:55:29 2026

@author: Sibusiso Steven Skosana
"""

import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="SS Skosana - Research Profile",
    page_icon="🔬",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        padding: 1rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #3B82F6;
        border-bottom: 2px solid #3B82F6;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .project-card {
        background-color: #F8FAFC;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #F0F8FF;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #B0E0E6;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_1280.png", width=200)

with col2:
    st.markdown('<h1 class="main-header">Sibusiso Steven Skosana</h1>', unsafe_allow_html=True)
    st.write("**📧 Email:** ssskosana.man@gmail.com")
    st.write("**📞 Phone:** 076 407 3162")
    st.write("**🏛️ Institution:** Sefako Makgatho Health Sciences University")
    st.write("**🔬 Department:** Medical Physics")
    st.write("**📚 Program:** Masters in Medical Physics (Student No: 201106614)")
    st.write("**📍 Address:** Stand no: 823 Sun city B, Thembisa, Kwamhlanga, Bronkhorstspruit 1022")
    
    # Supervisors
    st.markdown("**👨‍🏫 Supervisor:** Dr S Ngcezu")
    st.markdown("**👨‍🏫 Co-Supervisor:** Mr Mandiwana")

# Tabs for different sections
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🎯 Research Project", "📊 Methodology", "🎓 Education", "💼 Experience", "🛠️ Skills", "📞 Contact"])

with tab1:
    st.markdown('<h2 class="section-header">Research Project</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <h3>EVALUATING THE PROGNOSTIC VALUE OF MULTIMODAL TUMOUR SEGMENTATION IN PET/CT RADIOMICS COMPARED TO CT-ONLY RADIOMICS</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Research Aim
    st.markdown("### 🎯 Research Aim")
    st.markdown("""
    The aim of this study is to develop a robust PET/CT-enhanced tumour segmentation pipeline and evaluate how the inclusion of PET information influences the reproducibility of radiomic features specifically IBSI-compliant features compared with CT-only segmentation.
    """)
    
    # Objectives
    st.markdown("### 📋 Objectives")
    objectives = [
        "To implement a robust segmentation workflow on CT images of NSCLC tumours using model-assisted or semi-automated tools.",
        "To incorporate PET metabolic information to refine CT-derived masks using a progressive segmentation strategy.",
        "To compare CT-only and PET-enhanced segmentation masks in terms of derived radiomic features.",
        "To assess differences in prognostic model performance between CT-only and PET-enhanced feature sets."
    ]
    for obj in objectives:
        st.markdown(f"- {obj}")
    
    # Research Questions
    st.markdown("### ❓ Research Questions")
    questions = [
        "Does multimodal tumour segmentation using PET/CT improve the reproducibility and robustness of radiomic features compared to CT-only segmentation across different tumor types?",
        "How do radiomic features extracted from PET/CT segmentation differ in consistency and prognostic relevance compared to those extracted from CT-only segmentation?"
    ]
    for q in questions:
        st.markdown(f"- {q}")
    
    # Study Design
    st.markdown("### 🧪 Study Design")
    st.markdown("""
    - **Type:** Quantitative, retrospective imaging and data analysis study
    - **Data Source:** Publicly available PET/CT datasets from The Cancer Imaging Archive (TCIA)
    - **Sample Size:** 50–100 NSCLC patients
    - **Focus:** Comparison of multimodal segmentation techniques vs CT-only segmentation
    """)

with tab2:
    st.markdown('<h2 class="section-header">Methodology Overview</h2>', unsafe_allow_html=True)
    
    methodology_steps = [
        ("Data Processing", "Co-registration and resampling of PET/CT scans, intensity normalization"),
        ("CT-Based Segmentation", "Initial segmentation using thresholding, region-growing, or nnU-Net"),
        ("PET-Enhanced Segmentation", "Refine CT masks using PET metabolic information (40% SUVmax threshold)"),
        ("Radiomic Feature Extraction", "Using PyRadiomics for shape, intensity, and texture features"),
        ("Feature Analysis", "ICC and CV calculations for reproducibility assessment"),
        ("Prognostic Analysis", "Cox models and Kaplan-Meier curves for clinical outcomes")
    ]
    
    for step, description in methodology_steps:
        with st.expander(f"🔬 {step}"):
            st.write(description)
    
    # Tools and Software
    st.markdown("### 🛠️ Tools and Software")
    tools = [
        ("3D Slicer", "Tumor segmentation and visualization"),
        ("PyRadiomics", "Standardized feature extraction"),
        ("Python Libraries", "SimpleITK, NumPy, MONAI, PyTorch for processing"),
        ("Statistical Tools", "Python (scipy, statsmodels) or R for analysis")
    ]
    
    for tool, purpose in tools:
        st.markdown(f"- **{tool}:** {purpose}")

with tab3:
    st.markdown('<h2 class="section-header">Education Background</h2>', unsafe_allow_html=True)
    
    education = [
        {
            "degree": "Bachelor of Science Honours in Medical Physics",
            "institution": "Sefako Makgatho Health Science University",
            "year": "2024"
        },
        {
            "degree": "Bachelor of Science in Physics",
            "institution": "Sefako Makgatho Health Science University",
            "year": "2023"
        },
        {
            "degree": "Matric",
            "institution": "LD Moetanalo Secondary School",
            "year": "2010",
            "grade": "12"
        }
    ]
    
    for edu in education:
        with st.container():
            st.markdown(f"""
            <div style='padding: 1rem; margin-bottom: 1rem; border-left: 4px solid #3B82F6;'>
                <h4>🎓 {edu['degree']}</h4>
                <p><strong>Institution:</strong> {edu['institution']}</p>
                <p><strong>Year:</strong> {edu['year']}</p>
                {f"<p><strong>Grade:</strong> {edu['grade']}</p>" if 'grade' in edu else ""}
            </div>
            """, unsafe_allow_html=True)
    
    # Current Academic Role
    st.markdown("### 👨‍🏫 Current Academic Role")
    st.markdown("""
    **Tutor | Sefako Makgatho Health Science University (2024)**
    - Assist students with academics
    - Lecture and demonstrate practical experiments
    - Assess practical reports, tutorials and assignments
    - Organize attendance schedules
    """)

with tab4:
    st.markdown('<h2 class="section-header">Work Experience</h2>', unsafe_allow_html=True)
    
    experiences = [
        {
            "position": "Tutor",
            "company": "Sefako Makgatho Health Science University",
            "period": "Jan 2024 - Dec 2024",
            "responsibilities": [
                "Assist students with academics",
                "Lecturing and demonstrate practical experiments",
                "Assess practical reports, tutorials and assignments",
                "Organize attendance schedules"
            ]
        },
        {
            "position": "Waiter",
            "company": "Spur Steak Ranches - Smokey Rich",
            "period": "2017 - 2019",
            "responsibilities": [
                "Provide customer satisfaction through service delivery",
                "Assist customers navigate the restaurant"
            ]
        },
        {
            "position": "Scanning Clerk",
            "company": "Shoprite",
            "period": "2015 - 2017",
            "responsibilities": [
                "Organize paper filing",
                "Monitor and update outdated price tags on shelves",
                "Interact with customers to provide better shopping experience"
            ]
        }
    ]
    
    for exp in experiences:
        with st.container():
            st.markdown(f"### 💼 {exp['position']}")
            st.markdown(f"**{exp['company']}** | *{exp['period']}*")
            for resp in exp['responsibilities']:
                st.markdown(f"- {resp}")
            st.divider()

with tab5:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🧠 Technical Skills")
        tech_skills = [
            "Medical Image Processing",
            "PET/CT Imaging Analysis",
            "Radiomics Feature Extraction",
            "Python Programming",
            "Statistical Analysis",
            "3D Slicer Software",
            "PyRadiomics Library"
        ]
        for skill in tech_skills:
            st.markdown(f"✅ {skill}")
        
        st.markdown("### 🔬 Research Skills")
        research_skills = [
            "Research Methodology",
            "Data Collection & Analysis",
            "Academic Writing",
            "Literature Review",
            "Experimental Design",
            "Statistical Modeling"
        ]
        for skill in research_skills:
            st.markdown(f"📚 {skill}")
    
    with col2:
        st.markdown("### 🤝 Professional Skills")
        prof_skills = [
            "Problem Solving",
            "Decision Making",
            "Team Building",
            "Organization",
            "Teaching/Tutoring",
            "Customer Service"
        ]
        for skill in prof_skills:
            st.markdown(f"🌟 {skill}")
        
        st.markdown("### 📊 Software Proficiency")
        software = [
            "3D Slicer",
            "Python (NumPy, SciPy, PyRadiomics)",
            "Statistical Software (R/Python)",
            "Microsoft Office",
            "Research Documentation Tools"
        ]
        for soft in software:
            st.markdown(f"🖥️ {soft}")

with tab6:
    st.markdown('<h2 class="section-header">Contact Information</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📱 Personal Contact")
        st.markdown("**Phone:** 076 407 3162")
        st.markdown("**Email:** ssskosana.man@gmail.com")
        st.markdown("**Address:** Stand no: 823 Sun city B, Thembisa, Kwamhlanga, Bronkhorstspruit 1022")
        
        st.markdown("### 🏛️ Academic Information")
        st.markdown("**Student Number:** 201106614")
        st.markdown("**University:** Sefako Makgatho Health Sciences University")
        st.markdown("**Department:** Medical Physics")
    
    with col2:
        st.markdown("### 👥 References")
        references = [
            ("Mabidi Precious", "Sefako Makgatho Health Science University Lecturer", "precious.mabidi@smu.ac.za", "065 740 5277"),
            ("Skosana Gabisile", "Shoprite Admin Manager", "", "013 698 3640"),
            ("Mr. Mabhengu Thulani", "Sefako Makgatho Health Science University Supervisor", "Thulani.mabhengi@up.ac.za", "012 354 1228"),
            ("Mr. V Tholo", "LD Moetanalo Secondary School Principal", "", "013 546 3780")
        ]
        
        for ref in references:
            with st.expander(f"{ref[0]} - {ref[1]}"):
                st.write(f"**Email:** {ref[2] if ref[2] else 'Not provided'}")
                st.write(f"**Phone:** {ref[3]}")
    
    # Contact Form
    st.markdown("### 📧 Send Message")
    contact_form = """
    <form action="https://formsubmit.co/ssskosana.man@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required style="width:100%; padding:8px; margin-bottom:10px;">
        <input type="email" name="email" placeholder="Your Email" required style="width:100%; padding:8px; margin-bottom:10px;">
        <textarea name="message" placeholder="Your Message" required style="width:100%; padding:8px; margin-bottom:10px; height:100px;"></textarea>
        <button type="submit" style="background-color:#3B82F6; color:white; padding:10px 20px; border:none; border-radius:5px;">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

# Project Timeline
st.markdown('<h2 class="section-header">📅 Project Timeline</h2>', unsafe_allow_html=True)

# Create a simplified timeline
timeline_data = {
    "Jun-Jul 2025": "SREC Submission",
    "jan-feb 2026": "SMUREC Submission",
    "march-april 2026": "Permission Gauteng Provincial Health",
    "Jul-Aug 2026": "Report Writing (Chapters 1-2)",
    "Sep-Oct 2026": "Report Writing (Chapter 3)",
    "Nov-Dec 2026": "Data Collection & Analysis",
    "Dec 2027-Jan 2026": "Report Writing (Chapters 4-5)",
    "Jan-Feb 2027": "Manuscript Writing"
}

for period, activity in timeline_data.items():
    st.markdown(f"**{period}:** {activity}")

# Footer
st.divider()
st.markdown(f"""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>© {datetime.now().year} Sibusiso Steven Skosana | Medical Physics Research Profile</p>
    <p>Last Updated: {datetime.now().strftime("%B %d, %Y")} | Built with Streamlit</p>
    <p>Master's Research: "Evaluating the Prognostic Value of Multimodal Tumour Segmentation in PET/CT Radiomics"</p>
</div>
""", unsafe_allow_html=True)