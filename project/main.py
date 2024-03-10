from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
feedbacks = []

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about_page():
    with open("templates/about.html", "r") as f:
        about_content = f.read()
    return HTMLResponse(content=about_content)

@app.get("/contact", response_class=HTMLResponse)
async def contact_page():
    with open("templates/contact.html", "r") as f:
        contact_content = f.read()
    return HTMLResponse(content=contact_content)

async def call_openai_api(problem_description: str):
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=problem_description,
        max_tokens=100,
        temperature=0.7,
        stop=["\\n"],
    )
    return response.choices[0].text.strip()

@app.post("/generate", response_class=HTMLResponse)
async def generate_code(request: Request, problem_description: str = Form(...)):
    generated_code = await call_openai_api(problem_description)
    return templates.TemplateResponse("index.html", {"request": request, "response": generated_code, "problem_description": problem_description})

@app.post("/feedback", response_class=HTMLResponse)
async def submit_feedback(request: Request, problem_description: str = Form(...), response: str = Form(...), feedback: str = Form(...)):
    feedbacks.append(feedback)
    print("Feedback received:", feedback)
    updated_prompt = f"I asked: {problem_description}\n. You generated: {response}\n. Consider this: {feedback}"
    updated_response = await call_openai_api(updated_prompt)
    return templates.TemplateResponse("index.html", {"request": request, "response": updated_response, "problem_description": problem_description, "feedback": feedback})
