import streamlit as st
import requests

st.set_page_config(page_title="AutoGenXT - Resume Assistant")

st.title("📝 AutoGenXT - Resume & Interview Assistant")

option = st.selectbox(
    "Choose a service",
    ("Improve Resume", "Generate Cover Letter", "Mock Interview")
)

if option in ["Improve Resume", "Generate Cover Letter"]:
    resume_text = st.text_area("Paste your resume text here:")
    jd_text = st.text_area("Paste the job description here:")

    if st.button("Submit"):
        if not resume_text or not jd_text:
            st.warning("Please provide both resume and job description.")
        else:
            endpoint = "/resume" if option == "Improve Resume" else "/coverletter"
            response = requests.post(
                f"http://127.0.0.1:8000{endpoint}",
                json={"resume": resume_text, "job_description": jd_text}
            )
            if response.status_code == 200:
                result = response.json()
                key = "improved_resume" if option == "Improve Resume" else "cover_letter"
                st.subheader("Generated Output:")
                st.write(result[key])
            else:
                st.error("❌ Error occurred while processing your request.")

elif option == "Mock Interview":
    message = st.text_input("Ask an interview question:")

    if st.button("Ask"):
        if not message:
            st.warning("Please enter a message.")
        else:
            response = requests.post(
                "http://127.0.0.1:8000/interview",
                json={"message": message}
            )
            if response.status_code == 200:
                st.subheader("Interview Bot:")
                st.write(response.json()["reply"])
            else:
                st.error("❌ Error occurred during interview chat.")
