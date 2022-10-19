#!/usr/bin/env python3

import os
import requests

url = "http://localhost/upload/"
image_dir = "supplier-data/images/"
for item in os.listdir(image_dir):
    if item.endswith(".jpeg"):
        file_path = image_dir + item
        with open(file_path, 'rb') as fp:
            r = requests.post(url, files={'file':fp})