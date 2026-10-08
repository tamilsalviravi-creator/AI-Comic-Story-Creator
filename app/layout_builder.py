def build_comic_layout(images, full_story, outline):
    layout = []
    for i, panel in enumerate(outline):
        img_path = images[i] if i < len(images) else ""
        layout.append({
            "panel_number": panel.get("panel_number", i + 1),
            "image_url": img_path,
            "dialogue": panel.get("dialogue", ""),
            "description": panel.get("description", "")
        })
    return {"panels": layout, "story": full_story}