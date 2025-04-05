from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import PlainTextResponse
from app.ascii_converter import image_to_ascii
from app.filters import apply_filters
from app.utils import load_image

app = FastAPI()

@app.post("/convert", response_class=PlainTextResponse)
async def convert_image(
    file: UploadFile = File(None),
    url: str = Form(None),
    width: int = Form(100),
    grayscale: bool = Form(False),
    contrast: float = Form(1.0)
):
    image = await load_image(file, url)
    if image is None:
        return "Failed to load image."

    image = apply_filters(image, grayscale=grayscale, contrast=contrast)
    ascii_art = image_to_ascii(image, width=width)
    return ascii_art


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)