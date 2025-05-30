import streamlit as st
import json

st.title("📊 AutoAgentX Dashboard")

with open("./data/applications_log.json") as f:
    log = json.load(f)

st.write("### Application History")
for entry in log:
    st.write(f"**Job:** {entry['job_title']} | **Status:** {entry['status']}")
