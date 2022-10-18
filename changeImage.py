#!/usr/bin/env python3

from PIL import Image
import os

image_dir = "~/supplier-data/images"
for file in os.listdir(image_dir):
    if not file.startswith("."):
        file_path = image_dir + file
        saved_path = image_dir + file.split(".")[0]
        im = Image.open(file_path)
        im.convert("RBG").resize((600,400)).save(saved_path, 'jpeg')
        im.close()