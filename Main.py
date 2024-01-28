import streamlit as st
from streamlit_option_menu import option_menu
import base64
st.set_page_config(layout="wide")

def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="KARTHIK",
        options=["Home","Experience", "Education", "Skills", "Resume","Contact"],
        icons=["house", "clock history","book half", "tools", "paperclip","envelope"],
        menu_icon="none",
        default_index=0,
    )

if selected == "Home":
    st.markdown("<div style='text-align:center;margin-top:20px'><h1>ABOUT ME</h1></div>",unsafe_allow_html=True)
    with st.container():
        matter, photo = st.columns(2)
        with matter:
            st.markdown("<div style='text-align:center;margin-top:80px'></div>",unsafe_allow_html=True)
            st.write("<div style='font-size: 18px;'>Hi, I'm MUTTA KARTHIK PATTABHI RAMA RAO. I'm currently pursuing B.Tech 4th year in the department of Computer Science and Engineering at Sri Vasavi Engineering College, pedatadepalli affiliated to JNTUK</div>", unsafe_allow_html=True)
            st.text("")
            st.write("<div style='font-size: 18px;'>▶ In addition I like to play table tennis 🏓 ,  play video games 🎮 ,  drawing 🎨 , listening to music 🎧 and...  enjoy eating good food 🍽️ in my free time!</div>", unsafe_allow_html=True)
            st.text("")
            st.markdown("<div><h4>Social Media</h4></div>",unsafe_allow_html=True)
            st.markdown("""
                -  [linkedIN](https://www.linkedin.com/in/karthik-mutta-830413253/)
                -  [Github](https://www.linkedin.com/in/karthik-mutta-830413253/)
                -  [Instagram](https://www.linkedin.com/in/karthik-mutta-830413253/)
                """)
            st.markdown("<div><h4>Resume</h4></div>",unsafe_allow_html=True)
           
        photo.image("profile-pic.png")
elif selected == "Experience":
    st.markdown("<div style='text-align:center;margin-top:10px'><h1>EXPERIENCE</h1></div>",unsafe_allow_html=True)
    left,right = st.columns(2)
    with left:
        st.markdown("<div style='text-align:center;margin-top:50px'></div>",unsafe_allow_html=True)
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image("oasis.jpg")
        with text_column:
            st.subheader("Web Developer , Oasis Infobyte")
            st.write("**01-2023 to 02-2023**")
            st.markdown("""
             -  Developed landing page , portfolio , temprature converter by using 
            `HTML`,`CSS`,`JAVASCRIPT`.
            """)
    with right:
        st.markdown("<div style='text-align:center;margin-top:50px'></div>",unsafe_allow_html=True)
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image("sync.jpg")
        with text_column:
            st.subheader("Web Developer , Sync Intern's")
            st.write("**01-2023 to 02-2023**")
            st.markdown("""
             -   Developed login authentication , quiz website by using 
            `HTML`,`CSS`,`JAVASCRIPT`.
            """)

elif selected == "Skills":
    st.markdown("<div style='text-align:center;margin-top:10px'><h1>SKILLS</h1></div>",unsafe_allow_html=True)
    
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
elif selected == "Contact":
    st.markdown("<div style='text-align:center;margin-top:10px'><h1>FEEDBACK FORM</h1></div>",unsafe_allow_html=True)
    with st.form("Form1"):
        col1,col2 = st.columns(2)
        firstname = col1.text_input("First Name :")
        lastname = col2.text_input("Last Name :")
        email = st.text_input("Email :")
        mobile = st.text_input("Mobile Number")
        textarea = st.text_area("Feedback")
        state = st.form_submit_button("Submit",type="primary")

    st.markdown("<div style='text-align:center;margin-top:10px'><h4>MAIL-ID : </h4><h6>karthikmutta26@gmail.com</h6></div>",unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;margin-top:10px'><h4>MOBILE MUMBER : </h4><h6>+91 7981613722</h6></div>",unsafe_allow_html=True)
    if state:
        if firstname == "" or lastname == "" or email == "" or mobile == "" or textarea == "":
            st.warning("please enter all the fields")
        else:
            st.success("Submited Successfully")
elif selected == "Education":
    st.markdown("<div style='text-align:center;margin-top:10px'><h1>EDUCATION</h1></div>",unsafe_allow_html=True)
    
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("school1.jpg", use_column_width=True)
            st.markdown("<div align='center'><b>Vasavi Ideal Public School</b> <br> <b>High School</b> <br> <b>Percentage - 77.2%</b> </div>", unsafe_allow_html=True)
            st.text("")

        with col2:
            st.image("inter.jpg", use_column_width=True)
            st.markdown("<div align='center'><b>Tirumala Junior College</b> <br> <b>Intermediate</b> <br> <b>Percentage - 93.7%</b> </div>", unsafe_allow_html=True)
            st.text("")

        with col3:
            st.image("college.jpg", use_column_width=True)
            st.markdown("<div align='center'><b>Sri Vasavi Engineering College</b>  <br> <b> Bachelor of Technology</b> <br> <b>Computer Science and Engineering</b> <br> <b>Percentage - 79.34%</b></div>", unsafe_allow_html=True)
            st.text("")
elif selected == "Resume":   
    resume_url = "https://drive.google.com/file/d/1jDk641XVjRTc5wtMz7C7wCg75nVJKJNQ/view?usp=drive_link"
    st.markdown("<div style='text-align:center;margin-top:10px'><h1>RESUME</h1></div>",unsafe_allow_html=True)
    
    show_pdf("MUTTA-KARTHIK-PATTABHI-RAMA-RAO-RESUME.pdf")
    with open("MUTTA-KARTHIK-PATTABHI-RAMA-RAO-RESUME.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="MUTTA-KARTHIK-PATTABHI-RAMA-RAO-RESUME.pdf",
            mime="application/pdf",type="primary"
        )
