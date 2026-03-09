import streamlit as st
import json
from pathlib import Path
import datetime as dt
import uuid as uuid_lib
import time as time

st.set_page_config(page_title="Course Manager", 
    page_icon="", 
    layout="wide", 
    initial_sidebar_state="collapsed")

users = [
    {
        "id": "1",
        "email": "admins@school.edu",
        "full_name": "System Admin",
        "password": "123ssag@3AE",
        "role": "Admin",
        "registered_at": "..."
    }
]


json_path = Path("users.json")

if json_path.exists():
    with json_path.open("r", encoding="utf-8") as f:
        users = json.load(f)

tab1, tab2, tab3= st.tabs(["Log In", "Register"])

with tab1:
    with st.container(bordered=True):
        st.markdown("# Log In")
        user_name = st.text_input("Email")
        password = st.text_input("Password", type="password")
    
    if st.button("Login",type="primary", key="login_button",use_container_width=True):
        with st.spinner("Checking the login..."):
            time.sleep(5)

with tab2:
    with st.container(bordered=True):
        st.markdown("# Register")
        name = st.text_input("Full Name")
        email = st.text_input("Email", key-"email_in")
        password = st.text_input("Password", type="password")
    
    if st.button("Login",type="primary", key="login_button",use_container_width=True):
        with st.spinner("Checking the login..."):
            time.sleep(5)


    st.dataframe(users)
    with tab1:
        st.info("Use the following credentials to log in as admin: \n\nEmail: admins@school.edu\nPassword: 123ssag@3AE")
    st.dataframe()

with tab2:
    st.markdown()

    with json_path.open("w", encoding="utf-8") as f: 
        json.dump(users, f, indent=4)