import shutil
import psutil
import socket
import emails
import os

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80

def check_memory():
    avail_mem = (psutil.virtual_memory()[1])/1000000  #Or [4] in megabytes
    return avail_mem > 500

def check_hostname():
    data = socket.gethostbyname("localhost")
    ip = repr(data)
    return ip

sender = "automation@example.com"
recipient = "{}@example.com".format(os.environ.get('USER'))
subject = ""
body = "Please check your system and resolve the issue as soon as possible."

if not check_disk_usage("/"):
    subject = "Error - Available disk space is less than 20%"
    
if not check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    
if not check_memory():
    subject = "Error - Available memory is less than 500MB"
    
if check_hostname() != "127.0.0.1":
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    
message = emails.generate_error_report(sender, recipient, subject, body)
emails.send_email(message)