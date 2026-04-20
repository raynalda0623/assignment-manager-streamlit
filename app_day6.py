import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config(page_title="Course Manager", layout="centered")
st.title("Course Manager App")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "user" not in st.session_state:
    st.session_state["user"] = None

if "role" not in st.session_state:
    st.session_state["role"] = None

if "page" not in st.session_state:
    st.session_state["page"] = "login"


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
    with open(json_path, "r") as f:
        users = json.load(f)

if st.session_state["role"] == "Admin":
    st.markdown("This is the Admin UI- Dashboard.")


st.subheader("Log In")
with st.container(border=True):
    email_input = st.text_input("Email", key="login_email")
    password_input = st.text_input("Password", type="password", key="login_password")
    
    if st.button("Log In", type="primary", use_container_width=True):
        with st.spinner("Logging in..."):
            time.sleep(2) # Fake backend delay
            

# --- REGISTRATION ---
st.subheader("New Instructor Account")
with st.container(border=True):
    new_email = st.text_input("Email Address", key="reg_email")
    new_password = st.text_input("Password", type="password", key="reg_password")
    
    if st.button("Create Account", type="secondary", use_container_width=True):
        with st.spinner("Creating account..."):
            time.sleep(2) # Fake backend delay
            # ... (Assume validation logic here) ...
            users.append({
                "id": str(uuid.uuid4()),
                "email": new_email,
                "password": new_password,
                "role": "Instructor"
            })
            #with open(json_file, "w") as f:
               # json.dump(users, f, indent=4)
            st.success("Account created!")
            st.rerun()


            with st.sidebar:
                st.markdown("Course Manager Sidebar")
                st.dataframe(users)