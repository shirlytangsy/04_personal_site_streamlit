import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Shirly Tang </h4>
        <p>Recent Master's Graduate in Marketing<br>
        The Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:t1776130246@gmail.com">t1776130246@gmail.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a recent Master's graduate in Marketing from the The Chinese Univerity of Hong Kong, eager to apply my knowledge and skills in a professional setting. During my academic journey and past working experience, I developed a strong foundation in Big Data marketing and brand management.

        As part of my Master's program, I completed several projects that involved working with real-world business cases and applying various marketing theories and data analysis techniques. These projects allowed me to gain hands-on experience in digital marketing, customer analytics, social media analytics, and marketing research.

        I am passionate about leveraging data to find out consumer insights and make smart decisions. As an ENFJ, I am reliable, responsible, outgoing and confident. In work, I am a quick learner, a collaborative team player, and possess strong problem-solving skills. I am excited to contribute my skills and grow as a professional marketer in a dynamic and challenging environment.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Video Editing: Pr, JianYing
        - Graphic Design: Canava, Photoshop
        - Data Analysis: Vlookup, PivotTable, PivotChart, Conditional Formatting in Excel
        - Data Visualization: Tableau, Power BI
        - Language: Proficiency in Mandarin, English, Cantonese.
        - Communication: Presentation Skills, Copywriting
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 