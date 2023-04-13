
# import os
# import json, requests

# LOGIN_PAYLOAD = {
#   "client_id": os.getenv("MLS_CLIENT_ID"),
#   "client_secret": os.getenv("MLS_CLIENT_SECRET"),
#   "username": os.getenv("MLS_USERNAME"),
#   "password": os.getenv("MLS_PASSWORD"),
#   "grant_type": os.getenv("MLS_GRANT_TYPE"),
# }

# class MLSConnector(object):
#     CONTENT_TYPE = {
#         "DOCUMENTS": "documents",
#         "EXTERNAL_EUROPATHEK_BOOK": "external-europathek-books",
#         "FILE_RESOURCES": "file-resources",
#     }
    
#     def get_response(self, content_type):
#         # retrieve .env parameters
#         base_url = os.getenv("MLS_BASE_URL")
#         login_server_url = os.getenv("MLS_LOGIN_SERVER_URL")
#         realm = os.getenv("MLS_REALM")
#         # get login response
#         login_response = requests.post(login_server_url + "/realms/" + realm + "/protocol/openid-connect/token",
#                 data = LOGIN_PAYLOAD,
#                 headers =  {
#                 "Content-Type": "application/x-www-form-urlencoded",
#                 }
#             )
#         # get access token
#         access_token = login_response.json()["access_token"]
#         # create authenication header
#         auth_header = {
#             "Authorization": "Bearer " + access_token,
#             "Content-Type": "application/json"
#             }
        
#         url = base_url+"/mls-api/"+content_type        
#         results = requests.get(url, headers=auth_header)
#         return results
    
    
#     # def get_login_response(self, login_server_url, realm):
#     #     login_response = requests.post(login_server_url + "/realms/" + realm + "/protocol/openid-connect/token",
#     #             data = LOGIN_PAYLOAD,
#     #             headers =  {
#     #             "Content-Type": "application/x-www-form-urlencoded",
#     #             }
#     #         )
#     #     return login_response
    
#     # def get_access_token(self, login_response): 
#     #     return login_response.json()["access_token"]
    
    
#     # def get_auth_header(self, access_token):
#     #     auth_header =  {
#     #         "Authorization": "Bearer " + access_token,
#     #         "Content-Type": "application/json"
#     #         }
#     #     return auth_header
    
    
    