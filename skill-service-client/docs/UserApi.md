# swagger_client.UserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_mgmt_controller_get_user_profiles**](UserApi.md#user_mgmt_controller_get_user_profiles) | **GET** /user-profiles/{user_profile_id} | 

# **user_mgmt_controller_get_user_profiles**
> UserWithoutChildrenDto user_mgmt_controller_get_user_profiles(user_profile_id)



Returns a list with all users-profiles. Returns the specified user-profile. Used in MLS.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
user_profile_id = 'user_profile_id_example' # str | 

try:
    api_response = api_instance.user_mgmt_controller_get_user_profiles(user_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_mgmt_controller_get_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_profile_id** | **str**|  | 

### Return type

[**UserWithoutChildrenDto**](UserWithoutChildrenDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

