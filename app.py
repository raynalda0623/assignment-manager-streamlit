import streamlit as st
st.title("Course Manager")
st.write("Course Management Dashboard")
st.caption("MISY350")
st.divider()

assignments=[
    {"id": "HW1", 
     "title": "Introduction to Database", 
     "description": "basics of database design", 
     "points": 20, 
     "type": "homework"
     },
     {"id": "HW2", 
     "title": "Normalization", 
     "description": "writing SQL queries", 
     "points": 100, 
     "type": "homework"
     },
]

#3/ Step 3: Add New Assignment Section (Inputs & Layout)
st.subheader("Add New Assignment")
with st.container(border=True): #creates a container with a border around it
    col1,col2 = st.columns([2,1]) 

    with col1: #left side
        with st.container():
            st.markdown("### Assignment")
            title = st.text_input("Assignment title", placeholder="homework")
            description = st.text_input("Assignment Description", placeholder="description of the assignment")
            points = st.number_input("Points", min_value=0, step=1) #forces teh user to answer numbers
    #if I use col 2 instead of one, the input will be on the right side of the page, and if I use col 1, the input will be on the left side of the page.
    with col2: 
        st.markdown("**Time and Type**")
        due_date = st.date_input("Due Date")
        type= st.radio ("type",["Homework", "Lab"])


