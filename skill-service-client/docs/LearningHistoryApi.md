# swagger_client.LearningHistoryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**learning_history_controller_get_learned_skills**](LearningHistoryApi.md#learning_history_controller_get_learned_skills) | **GET** /{learning-history/history_id}/learned-skills | 
[**learning_history_controller_get_personalized_path**](LearningHistoryApi.md#learning_history_controller_get_personalized_path) | **GET** /personalized-paths/{path_id} | 
[**learning_history_controller_get_personalized_paths**](LearningHistoryApi.md#learning_history_controller_get_personalized_paths) | **GET** /learning-history/{history_id}/personalized-paths | 

# **learning_history_controller_get_learned_skills**
> list[str] learning_history_controller_get_learned_skills(history_id)



Returns the learned skills of a user (sorted descending by creation date)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningHistoryApi()
history_id = 'history_id_example' # str | 

try:
    api_response = api_instance.learning_history_controller_get_learned_skills(history_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningHistoryApi->learning_history_controller_get_learned_skills: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_id** | **str**|  | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_history_controller_get_personalized_path**
> PersonalizedPathDto learning_history_controller_get_personalized_path(history_id, path_id)



Returns a personalized learning path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningHistoryApi()
history_id = 'history_id_example' # str | 
path_id = 'path_id_example' # str | 

try:
    api_response = api_instance.learning_history_controller_get_personalized_path(history_id, path_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningHistoryApi->learning_history_controller_get_personalized_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_id** | **str**|  | 
 **path_id** | **str**|  | 

### Return type

[**PersonalizedPathDto**](PersonalizedPathDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_history_controller_get_personalized_paths**
> PersonalizedLearningPathsListDto learning_history_controller_get_personalized_paths(history_id)



Returns the personalized learning paths of a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningHistoryApi()
history_id = 'history_id_example' # str | 

try:
    api_response = api_instance.learning_history_controller_get_personalized_paths(history_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningHistoryApi->learning_history_controller_get_personalized_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_id** | **str**|  | 

### Return type

[**PersonalizedLearningPathsListDto**](PersonalizedLearningPathsListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

