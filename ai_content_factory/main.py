from fastapi import FastAPI, Request
from router import route_prompt
from notifier import send_telegram_message
from image_gen import generate_image

app = FastAPI()

@app.post("/generate-content")
async def generate_content(request: Request):
    data = await request.json()
    user_prompt = data.get("prompt")
    route = data.get("route")
    image_prompt = data.get("image_prompt")

    text_output = route_prompt(user_prompt, route)

    image_url = None
    if image_prompt:
        image_url = generate_image(image_prompt)

    send_telegram_message("Content Generated ✅", text_output)
    return {"content": text_output, "image": image_url}
