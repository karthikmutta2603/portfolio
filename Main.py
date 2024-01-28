import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

custom_css = """
<style>
body {
    background-image: url('bg.png'); /* Replace 'background.jpg' with your image file */
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    margin: 0;
}
</style>
"""

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
        matter.markdown("""
             -  linkedIN
            """)
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


