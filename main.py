from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import pickle
from preprocessing import proprocess_predict
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Google API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize FastAPI app
app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load models
try:
    with open("vectors.pkl", "rb") as file:
        vectors = pickle.load(file)  # Load fitted CountVectorizer

    with open("extra_tree.pkl", "rb") as file:
        model = pickle.load(file)  # Load trained model
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error loading models: {e}")

# Define function to generate content using Google Gemini


def generate_content(question):
    try:
        response = genai.GenerativeModel(
            "gemini-pro").generate_content(question)
        return response.text
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error generating content: {e}")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Initialize result as empty string
    return templates.TemplateResponse("index.html", {"request": request, "title": "Quora Duplication Question Finder", "result": ""})


@app.post("/", response_class=HTMLResponse)
async def predict_duplicate(request: Request, q1: str = Form(...), q2: str = Form(...)):
    try:
        processed_features = proprocess_predict(q1, q2)
        prediction = model.predict(processed_features)[0]

        if prediction:
            result = "Duplicate Question"
            response = generate_content(q1)
        else:
            result = "Not Duplicate Question"
            response = None

        return templates.TemplateResponse("index.html", {
            "request": request,
            "title": "Quora Duplication Question Finder",
            "result": result,
            "q1": q1,
            "q2": q2,
            "response": response
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error predicting: {e}")
