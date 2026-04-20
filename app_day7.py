import streamlit as st
import time
import json
from pathlib import Path
import uuid

st.set_page_config(
    page_title="Course Management",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Course Management App")
st.divider()
```

### 0.2 Loading the Data
Next, we define our default assignment data and try to load any existing saved data from a JSON file.

```python
# Placeholder Default Data
assignments = [
    {
        "id": "HW1",
        "title": "Intro to Database",
        "description": "basics of database design",
        "points": 100,
        "type": "homework"
    },
    {
        "id": "HW2",
        "title": "Normalization",
        "description": "normalizing",
        "points": 100,
        "type": "homework"
    }
]

json_path = Path("assignments.json")

# Load the data from a json file if it exists
if json_path.exists():
    with open(json_path, "r", encoding="utf-8") as f:
        assignments = json.load(f)


if "page" not in st.session_state:
    st.session_state["page"] = "Assignments Dashboard"

if "draft" not in st.session_state:
    st.session_state["draft"] = {}


pass

elif
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("## Add New Assignment")
    with col2:
        if st.button("Back", key="back_btn", use_container_width=False):
            st.session_state["page"] = "Assignments Dashboard" 
            st.rerun()

elif st.session_state["page"]=="Edit Assignment":
    pass