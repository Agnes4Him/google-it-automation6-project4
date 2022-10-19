#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

def get_info(url):
    fruit_info = ""
    for txt in os.listdir(url):
        txt_path = url + txt
        txt_list = []
        with open(txt_path) as tp:
            for line in tp:
                txt_list.append(line)
        fruit_info += "name" + ": " + txt_list[0] + "<br/>" + "weight" + ": " + txt_list[1] + "<br/><br/>"
    return fruit_info

if __name__ == "__main__":
    additional_info = get_info("supplier-data/descriptions/")
    today = str(date.today())
    title = "Processed Update on " + today
    filename = "/tmp/processed.pdf"
    
    report = reports.generate_report(filename, title, additional_info)
    message = emails.generate_email("automation@example.com", "{}@example.com".format(os.environ.get('USER')), "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", os.path.abspath(filename))
    emails.send_email(message)