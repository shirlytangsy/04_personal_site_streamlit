import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Marketing
    **The Chinese University of Hong Kong** | *August 2024 - July 2025*
    
    - GPA: 3.9/4.0
    - Major Track: "Big Data"
    - Relevant Coursework: Digital Marketing, Machine Learning, Customer Analytics, Social Media Analytics, Consumer Behaviors, Marketing Management, Big Data Strategies
    
    ### Bachelor of Arts in Business English
    **University of International Business and Economics** | *September 2020 - June 2024*
    
    - GPA: 3.68/4.0
    - Graduated with Honors
    - Relevant Coursework: Integrated Skills of Business English, Introduction to Intercultural Communication, English Grammar and Writing, Backgrounds to Western Culture, Business Research, Principles of Management, Principles of Microeconomics
    """)
    
    st.markdown("---")
    
    st.markdown("## Certifications")
    
    cert1, cert2, cert3 = st.columns(3)
    
    with cert1:
        st.markdown("""
        ### TEM-8 Certificate
        **The National Administry Committee on Teaching English Language to Majors in Higher Education under The Ministry of Education** | *March 2024*
        
        Demonstrated expertise in English.
        """)

    with cert2:
        st.markdown("""
        ### Volunteer Certificate
        **The Second United Nations Global Sustainable Transport Conference** | *October 2021*
        """)
    
    # If you have a third certificate, you can add it to cert3 like this:
    # with cert3:
    #     st.markdown("""
    #     ### [Your Third Certificate Title]
    #     **[Issuing Organization]** | *[Date]*
    #     
    #     [Optional short description]
    #     """)

    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### L'Oréal Brandstorm competition Hong Kong SAR
    - Collected second hand data and conducted first-hand interviews and surveys about men’s skincare journey.
    - Applied Issue Tree to identify one main problem.
    - Leveraged PowerPoint, 3D modeling and visualization to present the solution.
    
    ### Explore strategies towards high value customers on JD.com
    - Identified high value customers with RFM analysis. 
    - Used market basket analysis and data summary in R to learn demographic features and purchase behaviors of target customers.
    - Visualized data results in R and PowerPoint.
    """)
    
    st.markdown("---")