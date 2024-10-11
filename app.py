from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pwd_random_generator import create_random_pwd
from salvar_senha import salvar_senha


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/generate")
async def generate_password(
    length: int = Form(...),
    use_lowercase: bool = Form(True),
    use_uppercase: bool = Form(True),
    use_punctuation: bool = Form(True),
    use_digits: bool = Form(True)
):
    password = create_random_pwd(length, use_lowercase, use_uppercase, use_punctuation, use_digits)
    salvar_senha(password)
    return {"senha gerada": password}