# app/image_generator.py
import os

# Read from environment or fallback to empty string
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN", "your_token_here")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}