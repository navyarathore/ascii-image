from PIL import Image
from io import BytesIO
import requests

async def load_image(file, url):
    try:
        if file:
            return Image.open(BytesIO(await file.read()))
        elif url:
            response = requests.get(url)
            return Image.open(BytesIO(response.content))
    except Exception:
        return None
