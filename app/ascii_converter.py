from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, width=100):
    aspect_ratio = image.height / image.width
    height = int(aspect_ratio * width * 0.5)
    return image.resize((width, height))

def image_to_ascii(image, width=100):
    image = resize_image(image, width).convert("L")
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in pixels)

    ascii_lines = [ascii_str[i:i+width] for i in range(0, len(ascii_str), width)]
    return "\n".join(ascii_lines)
