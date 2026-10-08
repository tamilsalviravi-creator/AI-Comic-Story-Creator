import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def generate_outline(prompt_text: str):
    """
    Generates a 4-panel comic outline using Gemini Flash.
    Returns a list of dictionaries with panel details.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        system_prompt = f"""
        You are a comic book scriptwriter. Based on the following user request, 
        generate a 4-panel comic outline. 
        
        Request: {prompt_text}
        
        Return strictly a JSON array containing exactly 4 items. Each item must have:
        1. "panel_number": integer (1 to 4)
        2. "description": short description of the scene
        3. "dialogue": text spoken by characters or narrator
        4. "image_prompt": detailed prompt to generate an image for this panel
        
        Do not include markdown formatting like ```json, just pure raw JSON text.
        """
        
        response = model.generate_content(system_prompt)
        text_response = response.text.strip()
        
        # Clean up code blocks if present
        if text_response.startswith("```json"):
            text_response = text_response[7:]
        if text_response.startswith("```"):
            text_response = text_response[3:]
        if text_response.endswith("```"):
            text_response = text_response[:-3]
            
        text_response = text_response.strip()
        
        return json.loads(text_response)

    except Exception as e:
        # Fallback dummy outline if API fails or fails to parse
        return [
            {
                "panel_number": 1,
                "description": "Introduction scene",
                "dialogue": "Welcome to ComicCraft!",
                "image_prompt": f"Panel 1 concept art, {prompt_text}"
            },
            {
                "panel_number": 2,
                "description": "Rising action",
                "dialogue": "Something exciting begins...",
                "image_prompt": f"Panel 2 concept art, {prompt_text}"
            },
            {
                "panel_number": 3,
                "description": "Climax scene",
                "dialogue": "The turning point!",
                "image_prompt": f"Panel 3 concept art, {prompt_text}"
            },
            {
                "panel_number": 4,
                "description": "Resolution",
                "dialogue": "To be continued...",
                "image_prompt": f"Panel 4 concept art, {prompt_text}"
            }
        ]