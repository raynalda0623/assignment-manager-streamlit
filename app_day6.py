import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config(page_title="Course Manager", layout="centered")
st.title("Course Manager App")

# -----------------------
# FILE PATHS
# -----------------------
USERS_FILE = Path("users.json")
ASSIGNMENTS_FILE = Path("assignments.json")

# -----------------------
# INITIAL DATA FILES
# -----------------------
if not USERS_FILE.exists():
    default_users = [
        {
            "id": "1",
            "email": "admins@school.edu",
            "full_name": "System Admin",
            "password": "admin123",
            "role": "Admin",
            "registered_at": str(datetime.now())
        }
    ]
    with open(USERS_FILE, "w") as f:
        json.dump(default_users, f, indent=4)

if not ASSIGNMENTS_FILE.exists():
    with open(ASSIGNMENTS_FILE, "w") as f:
        json.dump([], f)

# -----------------------
# LOAD DATA
# -----------------------
def load_users():
    with open(USERS_FILE) as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def load_assignments():
    with open(ASSIGNMENTS_FILE) as f:
        return json.load(f)

def save_assignments(assignments):
    with open(ASSIGNMENTS_FILE, "w") as f:
        json.dump(assignments, f, indent=4)

# -----------------------
# SESSION STATE
# -----------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.user_email = None

users = load_users()
assignments = load_assignments()

# -----------------------
# LOGIN / REGISTER PAGE
# -----------------------
if not st.session_state.logged_in:

    st.subheader("Log In")

    with st.container(border=True):
        email_input = st.text_input("Email")
        password_input = st.text_input("Password", type="password")

        if st.button("Log In", use_container_width=True):

            with st.spinner("Logging in..."):
                time.sleep(1)

                for user in users:
                    if user["email"] == email_input and user["password"] == password_input:
                        st.session_state.logged_in = True
                        st.session_state.user_role = user["role"]
                        st.session_state.user_email = user["email"]
                        st.success("Login successful!")
                        st.rerun()

                st.error("Invalid email or password")

    # -----------------------
    # REGISTER
    # -----------------------
    st.subheader("New Instructor Account")

    with st.container(border=True):

        new_name = st.text_input("Full Name")
        new_email = st.text_input("Email Address")
        new_password = st.text_input("Password", type="password")

        if st.button("Create Account", use_container_width=True):

            if not new_email or not new_password or not new_name:
                st.error("All fields required")

            else:

                for user in users:
                    if user["email"] == new_email:
                        st.error("Email already registered")
                        st.stop()

                with st.spinner("Creating account..."):
                    time.sleep(1)

                    new_user = {
                        "id": str(uuid.uuid4()),
                        "email": new_email,
                        "full_name": new_name,
                        "password": new_password,
                        "role": "Instructor",
                        "registered_at": str(datetime.now())
                    }

                    users.append(new_user)
                    save_users(users)

                    st.success("Instructor account created!")

# -----------------------
# MAIN APP
# -----------------------
else:

    st.success(f"Logged in as {st.session_state.user_email} ({st.session_state.user_role})")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_role = None
        st.session_state.user_email = None
        st.rerun()

    st.divider()

    # -----------------------
    # CREATE ASSIGNMENT
    # -----------------------
    st.subheader("Create Assignment")

    title = st.text_input("Assignment Title")
    description = st.text_area("Description")
    due_date = st.date_input("Due Date")

    if st.button("Add Assignment"):

        if not title:
            st.error("Title required")

        else:

            new_assignment = {
                "id": str(uuid.uuid4()),
                "title": title,
                "description": description,
                "due_date": str(due_date),
                "created_by": st.session_state.user_email,
                "created_at": str(datetime.now())
            }

            assignments.append(new_assignment)
            save_assignments(assignments)

            st.success("Assignment created!")
            st.rerun()

    st.divider()