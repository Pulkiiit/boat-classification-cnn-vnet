from PIL import Image
import numpy as np

def preprocess_image(file):
    img = Image.open(file).convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    return img_array
