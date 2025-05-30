# chains/coverletter_chain.py

from transformers import pipeline
from dotenv import load_dotenv
load_dotenv()

# Use a text-generation model from HuggingFace
cover_letter_generator = pipeline("text-generation", model="distilgpt2")

def generate_cover_letter(resume: str, job_description: str) -> str:
    prompt = (
        "Write a professional cover letter based on the following resume and job description.\n\n"
        f"Job Description:\n{job_description}\n\n"
        f"Resume:\n{resume}\n\n"
        "Cover Letter:"
    )
    output = cover_letter_generator(
        prompt,
        max_new_tokens=256,
        do_sample=True,
        top_k=50,
        truncation=True
    )[0]['generated_text']
    return output.split("Cover Letter:")[-1].strip()
