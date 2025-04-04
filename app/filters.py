from PIL import ImageEnhance

def apply_filters(image, grayscale=False, contrast=1.0):
    if grayscale:
        image = image.convert("L").convert("RGB")
    if contrast != 1.0:
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast)
    return image
