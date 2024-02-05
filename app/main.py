from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.data import read_countries
from app.openai_interface import query_open_ai

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/views")


@app.get("/", response_class=HTMLResponse)
async def display_webpage(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"countries": read_countries()}
    )


@app.get("/test")
async def test_open_ai(request: Request):
    return await query_open_ai()
