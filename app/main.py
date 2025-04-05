from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import PlainTextResponse
from typing import Optional
from app.ascii_converter import image_to_ascii
from app.filters import apply_filters
from app.utils import load_image

app = FastAPI()

@app.post("/convert", response_class=PlainTextResponse)
async def convert_image(
    file: Optional[UploadFile] = File(None),
    url: Optional[str] = Form(None),
    width: int = Form(80),
    grayscale: bool = Form(False),
    contrast: float = Form(1.0)
):
    return "Test working!"
    # if not file and not url:
    #     return "Either a file or a URL must be provided."

    # image = await load_image(file, url)
    # if image is None:
    #     return "Failed to load image."

    # image = apply_filters(image, grayscale=grayscale, contrast=contrast)
    # ascii_art = image_to_ascii(image, width=width)
    # return ascii_art
