from fastapi import FastAPI, File, HTTPException, Header, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from src.controller import Controller

import os
import aiofiles

app = FastAPI()

BASE_DIR = 'tmp_files'

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust according to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

file_path_tmp = ""
files_directory = 'tmp_files' 

controller = Controller()

@app.get("/")
async def read_root():
    return {"Hello": "World2"}

# Function to process a file and return the processed file path
def process_file(file_path: str) -> str:
    # Dummy file processing logic
    processed_file_path = file_path.replace(".tex", "_processed.tex")
    with open(file_path, 'r') as original, open(processed_file_path, 'w') as processed:
        for line in original:
            processed.write(line.upper())
    return processed_file_path

def get_user_directory(session_id: str) -> str:
    return os.path.join(BASE_DIR, session_id)

# Endpoint to upload a file and process it
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...), session_id: str = Header(None)):
    if not session_id:
        raise HTTPException(status_code=400, detail="Session-Id header missing")

    user_dir = get_user_directory(session_id)
    os.makedirs(user_dir, exist_ok=True)

    file_path = os.path.join(user_dir, file.filename)
    async with aiofiles.open(file_path, "wb") as buffer:
        content = await file.read()
        await buffer.write(content)
    
    return {"original_filename": file.filename, "processed_file_path": file_path, "session_id": session_id}


@app.get("/getfile/")
async def get_file(filename: str, session_id: str = Header(None)):
    if not session_id:
        raise HTTPException(status_code=400, detail="Session-Id header missing")
    
    user_dir = get_user_directory(session_id)
    file_path = os.path.join(user_dir, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(path=file_path, filename=filename)

@app.get("/downloadfile/")
async def download_file(filename: str, session_id: str = Header(None)):
    if not session_id:
        raise HTTPException(status_code=400, detail="Session-Id header missing")
    
    user_dir = get_user_directory(session_id)
    file_path = os.path.join(user_dir, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(path=file_path, filename=filename)
    
@app.post("/query/")
async def query(str_query: str = Form(...), filename: str = Form(...), session_id: str = Header(None)):
    if not session_id:
        raise HTTPException(status_code=400, detail="Session-Id header missing")
    
    user_dir = get_user_directory(session_id)
    file_path = os.path.join(user_dir, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        controller.handle_query(file_path, str_query)
    except Exception as e:
        print(f"Error processing query: {e}")
        return {"status": "ERROR", "query": f"Error processing your query. Validate your syntax!     QUERY - {str_query}"}
    
    # Process the query
    return {"status": "OK", "query": str_query}


