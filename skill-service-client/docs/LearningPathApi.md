# swagger_client.LearningPathApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**learning_path_mgmt_controller_create_empty_learning_path**](LearningPathApi.md#learning_path_mgmt_controller_create_empty_learning_path) | **POST** /learning-paths | 
[**learning_path_mgmt_controller_delete_learning_path**](LearningPathApi.md#learning_path_mgmt_controller_delete_learning_path) | **DELETE** /learning-paths/{pathId} | 
[**learning_path_mgmt_controller_get_learning_path**](LearningPathApi.md#learning_path_mgmt_controller_get_learning_path) | **GET** /learning-paths/{pathId} | 
[**learning_path_mgmt_controller_get_learning_paths_of_owner**](LearningPathApi.md#learning_path_mgmt_controller_get_learning_paths_of_owner) | **GET** /learning-paths | 
[**learning_path_mgmt_controller_update_learning_path**](LearningPathApi.md#learning_path_mgmt_controller_update_learning_path) | **PATCH** /learning-paths/{pathId} | 
[**learning_path_mgmt_controller_validate_learning_path**](LearningPathApi.md#learning_path_mgmt_controller_validate_learning_path) | **GET** /learning-paths/{pathId}/validate | 

# **learning_path_mgmt_controller_create_empty_learning_path**
> LearningPathDto learning_path_mgmt_controller_create_empty_learning_path(body)



Creates a new empty learning path for the specified owner (orga-id).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningPathApi()
body = swagger_client.CreateEmptyPathRequestDto() # CreateEmptyPathRequestDto | 

try:
    api_response = api_instance.learning_path_mgmt_controller_create_empty_learning_path(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningPathApi->learning_path_mgmt_controller_create_empty_learning_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEmptyPathRequestDto**](CreateEmptyPathRequestDto.md)|  | 

### Return type

[**LearningPathDto**](LearningPathDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_path_mgmt_controller_delete_learning_path**
> learning_path_mgmt_controller_delete_learning_path(path_id)



Deletes a drafted Learning-Path or returns a 403 error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningPathApi()
path_id = 'path_id_example' # str | 

try:
    api_instance.learning_path_mgmt_controller_delete_learning_path(path_id)
except ApiException as e:
    print("Exception when calling LearningPathApi->learning_path_mgmt_controller_delete_learning_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_path_mgmt_controller_get_learning_path**
> LearningPathDto learning_path_mgmt_controller_get_learning_path(path_id)



Returns the specified learningpath.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningPathApi()
path_id = 'path_id_example' # str | 

try:
    api_response = api_instance.learning_path_mgmt_controller_get_learning_path(path_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningPathApi->learning_path_mgmt_controller_get_learning_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_id** | **str**|  | 

### Return type

[**LearningPathDto**](LearningPathDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_path_mgmt_controller_get_learning_paths_of_owner**
> LearningPathListDto learning_path_mgmt_controller_get_learning_paths_of_owner(owner=owner, page=page, page_size=page_size)



Returns all LearningPaths of the specified owner (orga-id).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningPathApi()
owner = 'owner_example' # str | Filter by owner if value is given, otherwise return all (optional)
page = 'page_example' # str | Page number - set up value if pagination is needed (optional)
page_size = 1.2 # float | Number of items per page - set up value if pagination is needed (optional)

try:
    api_response = api_instance.learning_path_mgmt_controller_get_learning_paths_of_owner(owner=owner, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningPathApi->learning_path_mgmt_controller_get_learning_paths_of_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Filter by owner if value is given, otherwise return all | [optional] 
 **page** | **str**| Page number - set up value if pagination is needed | [optional] 
 **page_size** | **float**| Number of items per page - set up value if pagination is needed | [optional] 

### Return type

[**LearningPathListDto**](LearningPathListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_path_mgmt_controller_update_learning_path**
> LearningPathDto learning_path_mgmt_controller_update_learning_path(body, path_id)



Partially updates a LearningPath. This function considers a tristate logic: - null: The field shall be deleted (reset to default), this is supported only by optional fields - undefined: The field shall not be changed - value: The field shall be updated to the given value  To specify a suggested ordering you need to pass the affected learning unit IDs in the array \"recommendedUnitSequence\" in the desired order. The old order will always be completely overwritten if a \"recommendedUnitSequence\" is defined, i.e., the recommendation of unspecified units will be deleted for this LearningPath. The old order will be kept if \"recommendedUnitSequence\" is undefined/not passed as parameter.  Default ordering of first 5 units of the first DigiMedia chapter: ```json {   \"recommendedUnitSequence\": [\"2001\", \"2002\", \"2005\", \"2003\", \"2004\"] } ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningPathApi()
body = swagger_client.UpdatePathRequestDto() # UpdatePathRequestDto | 
path_id = 'path_id_example' # str | 

try:
    api_response = api_instance.learning_path_mgmt_controller_update_learning_path(body, path_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningPathApi->learning_path_mgmt_controller_update_learning_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePathRequestDto**](UpdatePathRequestDto.md)|  | 
 **path_id** | **str**|  | 

### Return type

[**LearningPathDto**](LearningPathDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learning_path_mgmt_controller_validate_learning_path**
> learning_path_mgmt_controller_validate_learning_path(path_id)



Re-validates an existing learning path. Checks: - The path contains cycles - The goal can be reached (if actually a path exists)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningPathApi()
path_id = 'path_id_example' # str | 

try:
    api_instance.learning_path_mgmt_controller_validate_learning_path(path_id)
except ApiException as e:
    print("Exception when calling LearningPathApi->learning_path_mgmt_controller_validate_learning_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

