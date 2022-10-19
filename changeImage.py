#!/usr/bin/env python3

from PIL import Image
import os

image_dir = "supplier-data/images/"
for file in os.listdir(image_dir):
    if file.endswith(".tiff"):
        file_path = image_dir + file
        saved_path = image_dir + file.split(".")[0]
        im = Image.open(file_path)
        im.load()
        new_im = Image.new("RGB", im.size, (255, 255, 255))
        new_im.paste(im, mask = im.split()[3])
        new_im.resize((600,400)).save(saved_path + ".jpeg", "jpeg")
        im.close()