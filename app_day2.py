import streamlit as st

st.title("Course Manager")
st.header("Course Management App")
st.subheader("Assignments Manager")

next_assignment_id_number = 3 

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

points = st.slider("Points", min_value=0, max_value=100, value=100, step=5)

#assignments_type2 = st.selectbox("Type", ["Homework", "Lab", "Other"])
#if assignments_type2 == "Other":
    #assignments_type2 = st.text_input("Assignment Type")

lab = st.checkbox("Lab")

with st.expander("Assignment Preview"):
    st.markdown("## Live Preview")
    st.markdown(f"Title: {title}")

btn_save = st.button("Save", width=True, disabled=False)

import time
import json
from pathlib import Path

json_path = Path("assignments.json")
if btn_save:
    with st.spinner("Saving assignment..."):
        time.sleep(5)  # Simulate a delay for saving
        if title == "":
            st.warning("Enter Assignment Title")
        else:
            #Add/Create new assignment
            new_assignment_id = "HW"+ str(next_assignment_id_number)
            next_assignment_id_number += 1

        assignments.append(
            {
                "id": new_assignment_id,
                "title": title,
                "description": description,
                "points": points,  # Default points
                "type": assignments_type
            }
        )

#Recording the data into an actual file
#if json_path.exists():
        with json_path.open("w", encoding="utf-8") as f:
            json.dump(assignments, f, indent=4)

        st.success("Assignment is recorded!")
        st.dataframe("Working on it")
