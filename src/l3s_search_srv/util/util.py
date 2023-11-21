from flask import request, url_for
import urllib

aaa = urllib.parse.urlparse('http://127.0.0.1:9040/l3s-gateway/l3s-search/init/learning-units')

# import requests

def get_request_url(endpoint):
    # r1 = request.base_url.rsplit('/', 3)[0]
    parse_base_url = urllib.parse.urlparse(request.base_url)
    endpoint_url = url_for(endpoint=endpoint)
    request_url = f"{parse_base_url.scheme}://{parse_base_url.netloc}/{endpoint_url}"
    return request_url