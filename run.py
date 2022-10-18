#!/usr/bin/env python3

import os
import json
import  socket
import requests

desc_dir = "~/supplier-data/descriptions"
image_dir = "~/supplier-data/images"
hostname = socket.gethostname()    
ip = socket.gethostbyname(hostname)    
url = "http://ip/fruits"
for item in os.listdir(desc_dir):
    file_path = desc_dir + item
    lines_arr = []
    item_dict = {}
    image_path = ""
    mod_item = item.split(".")[0]
    with open(file_path) as fp:
        f = fp.read()
        for line in f:
            lines_arr.append(line)
    for image in os.listdir(image_dir):
        if image.endswith(".jpeg"):
            mod_image = image.split(".")[0]
            if mod_item == mod_image:
                image_path = image
    mod_weight = lines_arr[1].split(" ")[0]
    item_dict["name"] = lines_arr[0]
    item_dict["weight"] = int(mod_weight)
    item_dict["description"] = lines_arr[2]
    item_dict["image_name"] = image_path
    
    r = requests.post(url, json=item_dict)