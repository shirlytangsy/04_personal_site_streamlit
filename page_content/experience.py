import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Account Executive Intern
    **Leo Burnett, Publicis Groupe** | *March 2024 - June 2024*
    
    - Prepared Olympic marketing campaigns for Paris 2024: designed brand interactive videos on social media, proposed co-branding marketing of AMX and local brands in Paris.
    - Conducted market research: wrote reports regarding competitors and industry news, including new products, recent marketing campaigns, and relevant policies, and sought potential opportunities.
    - Proposed new product concepts: added new flavors to the product line with strong selling points.
    - Assisted day-to-day communication with clients: acting as an intermediary, facilitating communication about ad requirements between clients and designers.
    """)
    
    st.markdown("""
    ### Public Relation Intern
    **Ruder Finn** | *Febrary 2023 - August 2023*
    
    - Seeding: independently contacted and reached seeding cooperation with 20 KOLs on social media; managed post-production of influencer-generated content, including graphic editing.
    - Created content: conducted over 50 Tissot brand copywriting and on Weibo and WeChat platforms; participated in drafting and translating 20 brand and product press releases.
    - Maintained media relations: built and regularly updated media contact list, conducted proactive outreach to understand journalists' needs, and pitched relevant stories to secure coverage.
    - Supported offline events: involved in rundown planning and event promotion of “Tissot x NBA” watch exhibition, Tissot x Hainan Consumer Fair, Asian Games, etc.
    """)
    
    st.markdown("""
    ### Brand Promotion Intern
    **Everbright Senior Healthcare** | *July 2022 - October 2022*
    
    - Designed 20 brand posters with Canava.
    - Wrote 14 brand stories on owned social media.
    - Edited a five-minute video about brand promotion.
    """)
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL, JavaScript
        - **Video Editing:** Pr, JianYing
        - **Graphic Design:** Canava, Photoshop
        - **Data Analysis:** Vlookup, PivotTable, PivotChart, Conditional Formatting in Excel
                """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Language:** Proficiency in Mandarin, English, Cantonese.
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 