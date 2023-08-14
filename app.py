from PIL import Image
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My profile", page_icon=":tada:",layout="wide")

with open("design.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>",unsafe_allow_html=True)

colright,colleft=st.columns(2)
with colright:
    st.write("<h1 style='text-align:center;'>HI,WELCOME !</h1", unsafe_allow_html=True)

with colleft:
    url = requests.get("https://lottie.host/b902eff0-cf19-4c18-8977-ce827c6d9d2f/A62X53HnnL.json")

    urljson = dict()

    if url.status_code == 200:
        urljson = url.json()
    else:
        print("Error in the URL")

    st_lottie(urljson, height=125, width=150)


with st.sidebar:
        st.write("This code will be printed to the sidebar.")


tab1,tab2=st.tabs(["HOME", "MORE"])


with tab1:
    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
        st.markdown("<h3 style='text-align:center;'>ABOUT ME</h3", unsafe_allow_html=True)
        with st.container():
            st.write(" I am Vaishnavi Gambheera Rao, a 2nd year student in \'National Institute of Technology Warangal\' "
                 "pursing Electrical and Electronics Engineering course.")  
            url = requests.get("https://lottie.host/cdce4c89-63be-400c-a60b-d014e95a9a3b/UGSYrZmJfB.json")

            url_json = dict()

            if url.status_code == 200:
                url_json = url.json()
            else:
                print("Error in the URL")

            st_lottie(url_json, height=200, width=200)

    with col2:
        st.markdown("<h3 style='text-align:center;'>SKILLS</h3", unsafe_allow_html=True)
        with st.expander("PYTHON"):
            st.write("abc")
        with st.expander("DBMS"):
            st.write("xyz")
        with st.expander("C++"):
            st.write("xyz")
        with st.expander("HTML/CSS"):
            st.write("xyz") 
    

    with col3:
        st.markdown("<h3 style='text-align:center;'>INTERESTS</h3", unsafe_allow_html=True)
        with st.container():
            st.write("abc")

    with col4:
        st.markdown("<h3 style='text-align:center;'>CONTACT</h3", unsafe_allow_html=True)
        with st.container():
            st.write("Email id:   vaishnavigambhir15@gmail.com")
            st.write("Phone no:   +91 9121439101")

    with col5:
        url = requests.get("https://lottie.host/b70e421b-15b8-4b94-9f62-39e7d6a358ba/tvUZ1WYKlq.json")
        url_json = dict()
        if url.status_code == 200:

            url_json = url.json()
        else:
            print("error")
        st_lottie(url_json, width=50, height=50)
        url = requests.get("https://lottie.host/f7c2d6f1-20c8-4b89-9711-a0fe05bf0945/5sHaSVpXxl.json")
        url_json = dict()
        if url.status_code == 200:
            url_json = url.json()
        else:
            print("error")
        st_lottie(url_json, width=50, height=50)  

with tab2:
    with st.form(key="form1",clear_on_submit=True):
        name=st.text_input("Enter your name")
        email=st.text_input("Enter your email")
        comment=st.text_input("Comment")
        submit_button = st.form_submit_button(label='submit')    


    






