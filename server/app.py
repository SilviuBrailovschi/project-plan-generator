from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import logging
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Log the value of HUGGINGFACE_TOKEN
token_value = os.getenv("READ_TOKEN")
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
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

# Initialize the text generation pipeline
tokenizer = None
model = None
pipe = None
try:
    logging.info("Initializing the text generation pipeline...")

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("togethercomputer/RedPajama-INCITE-Chat-3B-v1")
    model = AutoModelForCausalLM.from_pretrained("togethercomputer/RedPajama-INCITE-Chat-3B-v1")

    # Initialize the pipeline with the tokenizer and model
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    logging.info("Pipeline initialized successfully.")
except Exception as e:
    logging.error(f"Failed to initialize pipeline: {e}")
    raise

# Endpoint to check server status
@app.get("/")
async def read_root():
    return {"message": "Server is running"}

# Define the model generation endpoint
@app.post("/generate/")
async def generate_text(request: Request):
    if not pipe:
        logging.error("Pipeline is not initialized.")
        raise HTTPException(status_code=500, detail="Pipeline initialization failed.")

    data = await request.json()
    input_text = data.get("input_text")

    if not input_text:
        raise HTTPException(status_code=400, detail="Input text is required.")

    # Log the received input text
    logging.info(f"Received input text: {input_text}")
    prompt = f"""
            <human>: {input_text}
            """
    # Generate text using the pipeline
    try:
        # Tokenize input with truncation
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

        # Generate text
        outputs = model.generate(**inputs, max_length=50, do_sample=True, pad_token_id=tokenizer.eos_token_id)

        # Decode the generated tokens
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        logging.info(f"----------FULL RESPONSE----------: {generated_text}")
        # Extract text after <bot>:
        bot_response = generated_text.split("<bot>:")[1].strip() if "<bot>:" in generated_text else generated_text.strip()

        logging.info(f"----------MESSAGE----------: {bot_response}")
        return {"message": bot_response}
    except Exception as e:
        logging.error(f"Text generation failed: {e}")
        raise HTTPException(status_code=500, detail="Text generation failed")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)
