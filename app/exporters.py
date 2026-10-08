import os
import uuid

def save_pdf(layout_data):
    os.makedirs(os.path.join("static", "exports"), exist_ok=True)
    file_name = f"comic_{uuid.uuid4().hex[:8]}.pdf"
    file_path = os.path.join("static", "exports", file_name)
    
    # Simple empty PDF placeholder file creation
    with open(file_path, "w") as f:
        f.write("%PDF-1.4 header placeholder")
        
    return f"/static/exports/{file_name}"