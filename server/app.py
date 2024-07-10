from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Log the value of HUGGINGFACE_TOKEN
token_value = os.getenv("READ_TOKEN")
if not token_value:
    logging.error("READ_TOKEN is not set in the environment.")
else:
    logging.info(f"READ_TOKEN value: {token_value}")

# Configure CORS
origins = [
    "http://localhost:3000",  # React frontend
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint to check server status
@app.get("/")
async def read_root():
    return {"message": "Server is running"}

# Define a placeholder endpoint for the future model API
@app.post("/generate/")
async def generate_text(request: Request):
    data = await request.json()
    input_text = data.get("input_text")

    if not input_text:
        raise HTTPException(status_code=400, detail="Input text is required.")

    # Log the received input text
    logging.info(f"Received input text: {input_text}")

    # Respond with a confirmation message
    return {"message": "Your submission was registered."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
