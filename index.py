from PIL import Image

import os

filename = 'sample.jpeg'

image = Image.open(filename)

if image.mode == "RGBA":
    image = image.convert("RGB")

output = "sample.pdf"

if not os.path.exists(output):
    image.save(output,"PDF",resolution=100.00)