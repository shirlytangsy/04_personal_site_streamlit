import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "Shirly Tang.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Shirly_Tang_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Shirly Tang")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** t1776130246@gmail.com
    - **Phone:** (852) 9025-4929
    - **LinkedIn:** [linkedin.com/in/ShirlyTang](www.linkedin.com/in/shirly-tang-067302341)
    - **Address:**  12 Chak Cheung St., Ma Liu Shui, HKSAR
    """)

    st.header("Professional Summary")
    st.markdown("""
    A passionate marketer with strong experience and konwledge equipment in marketing management. Proven ability to lead teams, manage projects, and improve brand performance. Seeking a challenging role to utilize my technical expertise and problem-solving skills.
    """)

    st.header("Work Experience")
    st.markdown("""
    **Account Executive Intern, Leo Burnett, Publicis Groupe.**
    - *March 2024 – June 2024*
    - Prepared Olympic marketing campaigns for Paris 2024: designed brand interactive videos on social media, proposed co-branding marketing of AMX and local brands in Paris.
    - Conducted market research: wrote reports regarding competitors and industry news, including new products, recent marketing campaigns, and relevant policies, and sought potential opportunities.
    - Proposed new product concepts: added new flavors to the product line with strong selling points.
    - Assisted day-to-day communication with clients: acting as an intermediary, facilitating communication about ad requirements between clients and designers.

    **Public Relation Intern, Ruder Finn**
    - *Febrary 2023 – August 2023*
    - Seeding: independently contacted and reached seeding cooperation with 20 KOLs on social media; managed post-production of influencer-generated content, including graphic editing.
    - Created content: conducted over 50 Tissot brand copywriting and on Weibo and WeChat platforms; participated in drafting and translating 20 brand and product press releases.
    - Maintained media relations: built and regularly updated media contact list, conducted proactive outreach to understand journalists' needs, and pitched relevant stories to secure coverage.
    - Supported offline events: involved in rundown planning and event promotion of “Tissot x NBA” watch exhibition, Tissot x Hainan Consumer Fair, Asian Games, etc.
    """)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**
    - The Chinese University of Hong Kong
    - *Graduated: July 2025*
    - GPA: 3.9/4.0

    **Bachelor of Arts in Business English**
    - University of International Business and Economics
    - *Graduated: June 2024*
    - GPA: 3.68/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, R, SQL, JavaScript
    - **Video Editing:** Pr, JianYing
    - **Graphic Design:** Canava, Photoshop
    - **Data Analysis:** Vlookup, PivotTable, PivotChart, Conditional Formatting in Excel
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)

    st.header("Certifications")
    st.markdown("""
     TEM-8 Certificate
    **The National Administry Committee on Teaching English Language to Majors in Higher Education under The Ministry of Education** | *March 2024*
    """)
    st.markdown("""
     Volunteer Certificate
    **The Second United Nations Global Sustainable Transport Conference** | *October 2021*
    """)
   
    st.header("Projects")
    st.markdown("""
    ### L'Oréal Brandstorm competition Hong Kong SAR
    - Collected second hand data and conducted first-hand interviews and surveys about men’s skincare journey
    - Applied Issue Tree to identify one main problem.
    - Leveraged PowerPoint, 3D modeling and visualization to present the solution.
    """)

    st.header("Languages")
    st.markdown("""
    - **Mandarin:** Native
    - **English:** Proficiency
    - **Cantonese:** Proficiency
    """)

    st.header("Interests")
    st.markdown("""
    - Stock market
    - Drama and talk show
    - Hiking and outdoor activities
    """)

    st.markdown("---") 