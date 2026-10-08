import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router

app = FastAPI(title="ComicCraft AI")

# Ensure static and panels directories exist
os.makedirs(os.path.join("static", "panels"), exist_ok=True)
os.makedirs(os.path.join("static", "exports"), exist_ok=True)

# Mount the static directory so browser can view generated images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include application routes
app.include_router(router)