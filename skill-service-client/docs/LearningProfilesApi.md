# swagger_client.LearningProfilesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**learning_profile_controller_get_learning_profile_by_id**](LearningProfilesApi.md#learning_profile_controller_get_learning_profile_by_id) | **GET** /learning-profiles/{learning_profile_id} | 
[**learning_profile_controller_patch_learning_profile_by_id**](LearningProfilesApi.md#learning_profile_controller_patch_learning_profile_by_id) | **PATCH** /learning-profiles/{learning_profile_id} | 

# **learning_profile_controller_get_learning_profile_by_id**
> LearningProfileDto learning_profile_controller_get_learning_profile_by_id(learning_profile_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningProfilesApi()
learning_profile_id = 'learning_profile_id_example' # str | 

try:
    api_response = api_instance.learning_profile_controller_get_learning_profile_by_id(learning_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningProfilesApi->learning_profile_controller_get_learning_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learning_profile_id** | **str**|  | 

### Return type

[**LearningProfileDto**](LearningProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_profile_controller_patch_learning_profile_by_id**
> str learning_profile_controller_patch_learning_profile_by_id(body, learning_profile_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningProfilesApi()
body = swagger_client.LearningProfileUpdateDto() # LearningProfileUpdateDto | 
learning_profile_id = 'learning_profile_id_example' # str | 

try:
    api_response = api_instance.learning_profile_controller_patch_learning_profile_by_id(body, learning_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningProfilesApi->learning_profile_controller_patch_learning_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LearningProfileUpdateDto**](LearningProfileUpdateDto.md)|  | 
 **learning_profile_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

