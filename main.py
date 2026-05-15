from fastapi import FastAPI, UploadFile, File
import pdfplumber

app = FastAPI()

@app.get("/")
def health_check():
    return {"Status" : "Healthy"}

@app.post("/upload/")
async def upload_file(file: UploadFile):
    
    if file.content_type != "application/pdf":
        return {"error" : "invalid file type"}
    
    with pdfplumber.open(file.file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    
    return {"#content" : text}
