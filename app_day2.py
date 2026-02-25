import streamlit as st

st.title("Course Manager")
st.header("Course Management App")
st.subheader("Assignments Manager")

st.divider()

#load assignnments 
assignments=[ {"id": "HW1", 
     "title": "Introduction to Database", 
     "description": "basics of database design", 
     "points": 20, 
     "type": "homework"
     },
     {
         "id": "HW2", 
     "title": "Normalization", 
     "description": "writing SQL queries", 
     "points": 100, 
     "type": "homework"
     },
]

#Add New Assignment
st.markdown("# Add New Assignment")

#input


title = st.text_input("Title", placeholder="ex. Homework 1",
    help="This is the name of the assignment")  

description = st.text_area("Description", placeholder="ex. database design...",
                           help="Describe the assignment in detail")  
due_date = st.date_input("Due Date")
assignments_type = st.radio("Type", ["Homework", "Lab", "Other"])
assignments_type2 = st.selectbox("Type", ["Homework", "Lab", "Other"])
if assignments_type2 == "Other":
    assignments_type2 = st.text_input("Assignment Type")

lab = st.checkbox("Lab")

with st.expander("Advanced Options"):
    st.markdown("### Grading Options")
    st.markdown("#### Grading Scale")

btn_save = st.button("Save")
if btn_save:
    st.warning("working on it")