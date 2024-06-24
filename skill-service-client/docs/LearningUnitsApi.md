# swagger_client.LearningUnitsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_learning_unit_controller_add_learning_unit_search**](LearningUnitsApi.md#search_learning_unit_controller_add_learning_unit_search) | **POST** /learning-units | 
[**search_learning_unit_controller_check_learning_unit**](LearningUnitsApi.md#search_learning_unit_controller_check_learning_unit) | **PUT** /learning-units/{learningUnitId}/checks | 
[**search_learning_unit_controller_delete_learning_unit**](LearningUnitsApi.md#search_learning_unit_controller_delete_learning_unit) | **DELETE** /learning-units/{learningUnitId} | 
[**search_learning_unit_controller_get_learning_unit**](LearningUnitsApi.md#search_learning_unit_controller_get_learning_unit) | **GET** /learning-units/{learningUnitId} | 
[**search_learning_unit_controller_get_learning_unit_search_with_filter**](LearningUnitsApi.md#search_learning_unit_controller_get_learning_unit_search_with_filter) | **GET** /learning-units | 
[**search_learning_unit_controller_list_learning_units**](LearningUnitsApi.md#search_learning_unit_controller_list_learning_units) | **GET** /learning-units/showAllLearningUnits | 
[**search_learning_unit_controller_patch_learning_unit**](LearningUnitsApi.md#search_learning_unit_controller_patch_learning_unit) | **PATCH** /learning-units/{learningUnitId} | 

# **search_learning_unit_controller_add_learning_unit_search**
> SearchLearningUnitDto search_learning_unit_controller_add_learning_unit_search(body)



Creates a new learningUnit at the specified repository and returns the created learningUnit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningUnitsApi()
body = swagger_client.SearchLearningUnitCreationDto() # SearchLearningUnitCreationDto | 

try:
    api_response = api_instance.search_learning_unit_controller_add_learning_unit_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningUnitsApi->search_learning_unit_controller_add_learning_unit_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchLearningUnitCreationDto**](SearchLearningUnitCreationDto.md)|  | 

### Return type

[**SearchLearningUnitDto**](SearchLearningUnitDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_learning_unit_controller_check_learning_unit**
> search_learning_unit_controller_check_learning_unit(learning_unit_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningUnitsApi()
learning_unit_id = 'learning_unit_id_example' # str | 

try:
    api_instance.search_learning_unit_controller_check_learning_unit(learning_unit_id)
except ApiException as e:
    print("Exception when calling LearningUnitsApi->search_learning_unit_controller_check_learning_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learning_unit_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_learning_unit_controller_delete_learning_unit**
> search_learning_unit_controller_delete_learning_unit(learning_unit_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningUnitsApi()
learning_unit_id = 'learning_unit_id_example' # str | 

try:
    api_instance.search_learning_unit_controller_delete_learning_unit(learning_unit_id)
except ApiException as e:
    print("Exception when calling LearningUnitsApi->search_learning_unit_controller_delete_learning_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learning_unit_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_learning_unit_controller_get_learning_unit**
> SearchLearningUnitDto search_learning_unit_controller_get_learning_unit(learning_unit_id)



Returns the specified learningUnit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningUnitsApi()
learning_unit_id = 'learning_unit_id_example' # str | 

try:
    api_response = api_instance.search_learning_unit_controller_get_learning_unit(learning_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningUnitsApi->search_learning_unit_controller_get_learning_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learning_unit_id** | **str**|  | 

### Return type

[**SearchLearningUnitDto**](SearchLearningUnitDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_learning_unit_controller_get_learning_unit_search_with_filter**
> SearchLearningUnitListDto search_learning_unit_controller_get_learning_unit_search_with_filter(required_skills=required_skills, teaching_goals=teaching_goals, owners=owners)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningUnitsApi()
required_skills = ['required_skills_example'] # list[str] | Filter by required skills (optional)
teaching_goals = ['teaching_goals_example'] # list[str] | Filter by required teachingGoals (optional)
owners = ['owners_example'] # list[str] | Filter by owners (optional)

try:
    api_response = api_instance.search_learning_unit_controller_get_learning_unit_search_with_filter(required_skills=required_skills, teaching_goals=teaching_goals, owners=owners)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningUnitsApi->search_learning_unit_controller_get_learning_unit_search_with_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **required_skills** | [**list[str]**](str.md)| Filter by required skills | [optional] 
 **teaching_goals** | [**list[str]**](str.md)| Filter by required teachingGoals | [optional] 
 **owners** | [**list[str]**](str.md)| Filter by owners | [optional] 

### Return type

[**SearchLearningUnitListDto**](SearchLearningUnitListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_learning_unit_controller_list_learning_units**
> SearchLearningUnitListDto search_learning_unit_controller_list_learning_units()



Lists all learningUnits.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningUnitsApi()

try:
    api_response = api_instance.search_learning_unit_controller_list_learning_units()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningUnitsApi->search_learning_unit_controller_list_learning_units: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SearchLearningUnitListDto**](SearchLearningUnitListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_learning_unit_controller_patch_learning_unit**
> SearchLearningUnitDto search_learning_unit_controller_patch_learning_unit(body, learning_unit_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LearningUnitsApi()
body = swagger_client.SearchLearningUnitCreationDto() # SearchLearningUnitCreationDto | 
learning_unit_id = 'learning_unit_id_example' # str | 

try:
    api_response = api_instance.search_learning_unit_controller_patch_learning_unit(body, learning_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LearningUnitsApi->search_learning_unit_controller_patch_learning_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchLearningUnitCreationDto**](SearchLearningUnitCreationDto.md)|  | 
 **learning_unit_id** | **str**|  | 

### Return type

[**SearchLearningUnitDto**](SearchLearningUnitDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

