# chains/resume_chain.py
from dotenv import load_dotenv
load_dotenv()
from transformers import pipeline

# Load a text-generation model from HuggingFace (lightweight and fast)
resume_generator = pipeline("text-generation", model="distilgpt2")

def improve_resume(resume: str, job_description: str) -> str:
    prompt = (
        "Improve the following resume to better match the given job description.\n\n"
        f"Job Description:\n{job_description}\n\n"
        f"Original Resume:\n{resume}\n\n"
        "Improved Resume:"
    )
    output = resume_generator(prompt, max_length=512, do_sample=True, top_k=50)[0]['generated_text']
    return output.split("Improved Resume:")[-1].strip()
