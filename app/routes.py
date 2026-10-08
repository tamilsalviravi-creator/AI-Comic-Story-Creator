import os
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from app.gemini_flash import generate_outline
from app.gemini_pro import generate_story
from app.image_generator import generate_image
from app.layout_builder import build_comic_layout
from app.exporters import save_pdf

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Updated Jinja2 syntax for newer FastAPI versions
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )

@router.post("/generate", response_class=HTMLResponse)
async def create_comic(request: Request, user_prompt: str = Form(...)):
    # 1. Generate 4 panel outline using Flash
    outline = generate_outline(user_prompt)

    # 2. Generate overall story using Pro
    story = generate_story(outline)

    # 3. Generate panel images
    images = []
    for panel in outline:
        prompt = panel.get("description", "Comic panel scene")
        img_url = generate_image(prompt)
        images.append(img_url)

    # 4. Build complete layout dictionary
    comic_data = build_comic_layout(images, story, outline)

    # 5. Export PDF placeholder
    pdf_url = save_pdf(comic_data)

    return templates.TemplateResponse(
        request=request, 
        name="comic_preview.html", 
        context={
            "comic": comic_data, 
            "pdf_url": pdf_url, 
            "prompt": user_prompt
        }
    )