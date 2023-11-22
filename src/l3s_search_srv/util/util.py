from flask import request, url_for
import urllib

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