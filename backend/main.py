from fastapi import FastAPI, UploadFile, File
from resume_parser import extract_text_from_pdf

app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI Resume Matcher Backend Running"}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file)
    return {
        "message": "Resume uploaded successfully",
        "resume_text": text[:1000]  # first 1000 chars only
    }
