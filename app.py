from fastapi import FastAPI
from pydantic import BaseModel
from chains.resume_chain import improve_resume
from chains.coverletter_chain import generate_cover_letter

from chains.interview_chain import interview_response

app = FastAPI()


# Request Schemas
class ResumeRequest(BaseModel):
    resume: str
    job_description: str

class InterviewRequest(BaseModel):
    message: str


# Resume Improvement Endpoint
@app.post("/resume")
def rewrite_resume(req: ResumeRequest):
    improved_text = improve_resume(req.resume, req.job_description)
    return {"improved_resume": improved_text}


# Cover Letter Generation Endpoint
@app.post("/coverletter")
def generate_cover_letter_route(req: ResumeRequest):
    return {
        "cover_letter": generate_cover_letter(
            resume=req.resume,
            job_description=req.job_description
        )
    }

# Mock Interview Chat Endpoint
@app.post("/interview")
def mock_interview(req: InterviewRequest):
    reply = interview_response(req.message)
    return {"reply": reply}
