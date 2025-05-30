# chains/interview_chain.py

from transformers import pipeline
from dotenv import load_dotenv
load_dotenv()

# Load a conversational model
interview_bot = pipeline("text-generation", model="distilgpt2")

def interview_response(message: str) -> str:
    prompt = (
        "You are an AI interview coach. Respond to the following message as if conducting a mock interview.\n\n"
        f"Candidate: {message}\n\n"
        "AI:"
    )
    output = interview_bot(prompt, max_length=150, do_sample=True, top_k=50)[0]['generated_text']
    return output.split("AI:")[-1].strip()
