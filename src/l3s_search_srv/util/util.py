from flask import request, url_for
import urllib
import os, shutil
from datetime import datetime

# aaa = urllib.parse.urlparse('http://127.0.0.1:9040/l3s-gateway/l3s-search/init/learning-units')

# import requests

def get_request_url(endpoint):
    # r1 = request.base_url.rsplit('/', 3)[0]
    parse_base_url = urllib.parse.urlparse(request.base_url)
    # print(f"parse_base_url: {parse_base_url}")
    endpoint_url = url_for(endpoint=endpoint)
    # print(f"endpoint_url: {endpoint_url}")
    # print(f"fisrt of endpoint_url: {endpoint_url[0]}")
    if endpoint_url[0] == "/":
        endpoint_url = endpoint_url[1:]
        # print(endpoint_url)
    request_url = f"{parse_base_url.scheme}://{parse_base_url.netloc}/{endpoint_url}"
    # print(f"request_url: {request_url}")
    return request_url



# def get_subdirs(target_dir):
#     subdirs = [d for d in os.listdir(target_dir) if os.path.isdir(os.path.join(target_dir, d))]
#     return subdirs

def dirs_pruning(target_dir):
    num_to_keep = 1
    subdirs = [d for d in os.listdir(target_dir) if os.path.isdir(os.path.join(target_dir, d))]
    if len(subdirs) <= num_to_keep:
        return
    
    if len(subdirs) > num_to_keep:
        subdirs.sort(key=lambda x: os.path.getmtime(os.path.join(target_dir, x)))
        subdirs_to_remove = subdirs[:-num_to_keep]
        
        for subdir in subdirs_to_remove:
            shutil.rmtree(os.path.join(target_dir, subdir))
            print(f"************ Removed: {os.path.abspath(subdir)} *************")
    return