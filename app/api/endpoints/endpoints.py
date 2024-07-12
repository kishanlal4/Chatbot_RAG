#For setting all endpoints or router
from fastapi import FastAPI, File, UploadFile, Request, APIRouter
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.services.chat import main_ask
from app.core.config import openai_key
import os


router = APIRouter()

UPLOAD_FOLDER = "uploaded_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_location = os.path.join(UPLOAD_FOLDER, "sample.pdf")
        with open(file_location, "wb") as f:
            f.write(await file.read())
        return JSONResponse(status_code=200, content={"message": "File uploaded successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message")
    openai_api_key = openai_key

    # print(os.getcwd())
    # print(os.listdir('uploaded_files'))
    pdf_path = r"uploaded_files/sample.pdf"
    message1 = main_ask(message, pdf_path, openai_api_key)
    response_message = f"{message1}"
    return JSONResponse(status_code=200, content={"response": response_message})
