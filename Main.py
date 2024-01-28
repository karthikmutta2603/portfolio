import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")


with st.sidebar:
    selected = option_menu(
        menu_title="KARTHIK",
        options=["Home","Experience", "Education", "Skills", "Projects"],
        icons=["house", "clock history","book half", "tools", "clipboard"],
        menu_icon="none",
        default_index=0,
    )

if selected == "Home":
    st.title("MUTTA KARTHIK PATTABHI RAMA RAO")
    with st.container():
        matter, photo = st.columns(2)
        matter.write("<div style='font-size: 18px;'>Hi, I'm MUTTA KARTHIK PATTABHI RAMA RAO. I'm currently pursuing B.Tech 4th year in the department of Computer Science and Engineering at Sri Vasavi Engineering College, pedatadepalli affiliated to JNTUK</div>", unsafe_allow_html=True)
        matter.write("<div style='font-size: 18px;'>▶ In addition, I like to 🏓 play table tennis,🎮 play video games, 🎨 drawing,🎧 listening to music and... 🍽️ enjoy eating good food in my free time!</div>", unsafe_allow_html=True)
        
        photo.image("profile-pic.png")
elif selected == "Experience":
    st.header("Experience")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image("oasis.jpg")
        with text_column:
            st.subheader("Web Developer,Oasis Infobyte")
            st.write("**01-2023 to 02-2023**")
            st.markdown("""
             -  Developed landing page , portfolio , temprature converter by using 
            `HTML`,`CSS`,`JAVASCRIPT`.
            """)
    st.text("")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image("sync.jpg")
        with text_column:
            st.subheader("Web Developer,Sync Intern's")
            st.write("**01-2023 to 02-2023**")
            st.markdown("""
             -   Developed login authentication , quiz website by using 
            `HTML`,`CSS`,`JAVASCRIPT`.
            """)
elif selected == "Skills":
    st.header("Skills")
    
    with st.container():
        left,middle,right = st.columns(3)
        with left:
            with st.container():
                html = 90
                st.markdown("HTML")
                st.progress(html)
                st.write(html,"%")
                st.text("")
            with st.container():
                python = 70
                st.markdown("PYTHON")
                st.progress(python)
                st.write(python,"%")
                st.text("")
            with st.container():
                cp = 70
                st.markdown("C++")
                st.progress(cp)
                st.write(cp,"%")
                st.text("")
            with st.container():
                figma = 80
                st.markdown("FIGMA")
                st.progress(figma)
                st.write(figma,"%")
                st.text("")
        with middle:
            with st.container():
                css = 90
                st.markdown("CSS")
                st.progress(css)
                st.write(css,"%")
                st.text("")
            with st.container():
                sql = 80
                st.markdown("SQL")
                st.progress(sql)
                st.write(sql,"%")
                st.text("")
            with st.container():
                bs = 70
                st.markdown("BOOTSTRAP")
                st.progress(bs)
                st.write(bs,"%")
                st.text("")
        with right:
            with st.container():
                java = 80
                st.markdown("JAVA")
                st.progress(java)
                st.write(java,"%")
                st.text("")
            with st.container():
                js = 70
                st.markdown("JAVASCRPT")
                st.progress(js)
                st.write(js,"%")
                st.text("")
            with st.container():
                c = 70
                st.markdown("C")
                st.progress(c)
                st.write(c,"%")
                st.text("")


