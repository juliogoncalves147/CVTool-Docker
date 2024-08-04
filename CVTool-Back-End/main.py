import json
from fastapi import FastAPI, File, HTTPException, Response, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from tempfile import NamedTemporaryFile
from src.controller import Controller

app = FastAPI()

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
    return {"Hello": "World"}

# Function to process a file and return the processed file path
def process_file(file_path: str) -> str:
    # Dummy file processing logic
    processed_file_path = file_path.replace(".tex", "_processed.tex")
    with open(file_path, 'r') as original, open(processed_file_path, 'w') as processed:
        for line in original:
            processed.write(line.upper())
    return processed_file_path

# Endpoint to upload a file and process it
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    global file_path_tmp
    
    # Create a NamedTemporaryFile within the 'tmp_files' directory
    with NamedTemporaryFile(dir='tmp_files', delete=False, suffix=".tex") as tmp:
        # Write the uploaded file content to the temporary file
        tmp.write(file.file.read())
        tmp_path = tmp.name
        print(f"Uploaded file path: {tmp_path}")
    
    # Get the original filename and create the target path
    original_filename = file.filename
    target_path = os.path.join('tmp_files', original_filename)
    
    # Move the temporary file to the target path with the original filename
    os.rename(tmp_path, target_path)
    print(f"File saved as: {target_path}")
    
    file_path_tmp = target_path
    print(f"File path tmp {file_path_tmp}")
    
    return {"original_filename": original_filename, "processed_file_path": file_path_tmp}


@app.get("/getfile/")
async def get_file(filename: str):
    print(f"Requested file name: {filename}")
    file_path = os.path.join(files_directory, filename)
    print(f"File path: {file_path}")
    try:
        return FileResponse(path=file_path, filename=filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found.")

@app.get("/downloadfile/")
async def download_file(filename: str):
    file_path = os.path.join(files_directory, filename)
    
    try:
        return FileResponse(path=file_path, filename=filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found.")
    
@app.post("/query/")
async def query(str_query: str = Form(...), filename: str = Form(...)):
    global controller
    file_path = os.path.join(files_directory, filename)
    print(f"Received query: {str_query}")
    print(f"File path tmp:" + str(file_path))
    try:
        controller.handle_query(file_path_tmp, str_query)
    except Exception:
        print("Error processing query")
        return {"status": "ERROR" ,"query": "Error processing your query. Validate your syntax!"}
    # Process the query
    return {"status": "OK", "query": str_query}


