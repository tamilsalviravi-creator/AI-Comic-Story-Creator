import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def generate_story(outline: list) -> str:
    """
    Generates a full story narrative based on a 4-panel comic outline.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        prompt = f"""
        You are a creative writer. Based on the following comic panel outline, 
        write a cohesive, engaging short story narration that connects all 4 panels together:

        Outline:
        {outline}

        Keep the narration vivid, expressive, and concise.
        """
        
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        # Fallback story if generation fails
        story_lines = []
        for panel in outline:
            desc = panel.get("description", "A key event unfolds.")
            story_lines.append(desc)
        return " ".join(story_lines)