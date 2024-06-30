# swagger_client.PathFinderApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**path_finder_controller_compute_path**](PathFinderApi.md#path_finder_controller_compute_path) | **POST** /PathFinder/computePath | 
[**path_finder_controller_enrollment**](PathFinderApi.md#path_finder_controller_enrollment) | **POST** /PathFinder/adapted-path | 
[**path_finder_controller_enrollment_by_goal**](PathFinderApi.md#path_finder_controller_enrollment_by_goal) | **POST** /PathFinder/calculated-path | 
[**path_finder_controller_simulate_enrollment**](PathFinderApi.md#path_finder_controller_simulate_enrollment) | **GET** /PathFinder/adapted-path | 
[**path_finder_controller_simulate_enrollment_by_goal**](PathFinderApi.md#path_finder_controller_simulate_enrollment_by_goal) | **GET** /PathFinder/calculated-path | 
[**path_finder_controller_skill_analysis**](PathFinderApi.md#path_finder_controller_skill_analysis) | **POST** /PathFinder/skillAnalysis | 
[**path_finder_controller_store_personalized_path**](PathFinderApi.md#path_finder_controller_store_personalized_path) | **POST** /PathFinder/{userId} | Experimental (WIP)

# **path_finder_controller_compute_path**
> PathDto path_finder_controller_compute_path(body)



Computes the optimal learning path to learn the specified skill(s).  Parameters: - goal (mandatory): The list of skills to be learned. - userId (optional): If specified, path will be computed and optimized for the specified user, e.g., considering learned skills and learning behavior. - optimalSolution (optional): If unspecified, algorithm will use a fast, greedy approach to find a path. If true, the algorithm will try to find an optimal path, at cost of performance.     Default path for learning Java (skill 1009) ```json {   \"goal\": [\"1009\"] } ```  Path for learning DigiMedia (skills 2501 - 2512) for user 2001, ensure performant computation ```json {   \"goal\": [\"2501\", \"2502\", \"2503\", \"2504\", \"2505\", \"2506\", \"2507\", \"2508\", \"2509\", \"2510\", \"2511\", \"2512\"],   \"userId\": \"2001\",   \"optimalSolution\": false } ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PathFinderApi()
body = swagger_client.PathRequestDto() # PathRequestDto | 

try:
    api_response = api_instance.path_finder_controller_compute_path(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathFinderApi->path_finder_controller_compute_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PathRequestDto**](PathRequestDto.md)|  | 

### Return type

[**PathDto**](PathDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_finder_controller_enrollment**
> path_finder_controller_enrollment(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PathFinderApi()
body = swagger_client.EnrollmentRequestDto() # EnrollmentRequestDto | 

try:
    api_instance.path_finder_controller_enrollment(body)
except ApiException as e:
    print("Exception when calling PathFinderApi->path_finder_controller_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrollmentRequestDto**](EnrollmentRequestDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_finder_controller_enrollment_by_goal**
> CustomCoursePreviewResponseDto path_finder_controller_enrollment_by_goal(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PathFinderApi()
body = swagger_client.CustomCourseRequestDto() # CustomCourseRequestDto | 

try:
    api_response = api_instance.path_finder_controller_enrollment_by_goal(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathFinderApi->path_finder_controller_enrollment_by_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomCourseRequestDto**](CustomCourseRequestDto.md)|  | 

### Return type

[**CustomCoursePreviewResponseDto**](CustomCoursePreviewResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_finder_controller_simulate_enrollment**
> EnrollmentPreviewResponseDto path_finder_controller_simulate_enrollment(user_id, learning_path_id, optimal_solution)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PathFinderApi()
user_id = 'user_id_example' # str | 
learning_path_id = 'learning_path_id_example' # str | 
optimal_solution = true # bool | 

try:
    api_response = api_instance.path_finder_controller_simulate_enrollment(user_id, learning_path_id, optimal_solution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathFinderApi->path_finder_controller_simulate_enrollment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **learning_path_id** | **str**|  | 
 **optimal_solution** | **bool**|  | 

### Return type

[**EnrollmentPreviewResponseDto**](EnrollmentPreviewResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_finder_controller_simulate_enrollment_by_goal**
> EnrollmentPreviewResponseDto path_finder_controller_simulate_enrollment_by_goal(user_id, goals, optimal_solution)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PathFinderApi()
user_id = 'user_id_example' # str | 
goals = ['goals_example'] # list[str] | 
optimal_solution = true # bool | 

try:
    api_response = api_instance.path_finder_controller_simulate_enrollment_by_goal(user_id, goals, optimal_solution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathFinderApi->path_finder_controller_simulate_enrollment_by_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **goals** | [**list[str]**](str.md)|  | 
 **optimal_solution** | **bool**|  | 

### Return type

[**EnrollmentPreviewResponseDto**](EnrollmentPreviewResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_finder_controller_skill_analysis**
> SubPathListDto path_finder_controller_skill_analysis(body)



Analysis a skill (goal) to find the missing skills in the learning path.  Parameters: - goal (mandatory): The list of skills to be learned.  Returns: - If the return path is empty, then there are no learning units for the skill.      Default path for learning Java (skill 1009) ```json { \"goal\": [\"1009\"] } ```

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PathFinderApi()
body = swagger_client.SkillsToAnalyze() # SkillsToAnalyze | 

try:
    api_response = api_instance.path_finder_controller_skill_analysis(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathFinderApi->path_finder_controller_skill_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SkillsToAnalyze**](SkillsToAnalyze.md)|  | 

### Return type

[**SubPathListDto**](SubPathListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_finder_controller_store_personalized_path**
> PathStorageResponseDto path_finder_controller_store_personalized_path(body, user_id)

Experimental (WIP)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PathFinderApi()
body = swagger_client.PathStorageRequestDto() # PathStorageRequestDto | 
user_id = 'user_id_example' # str | 

try:
    # Experimental (WIP)
    api_response = api_instance.path_finder_controller_store_personalized_path(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PathFinderApi->path_finder_controller_store_personalized_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PathStorageRequestDto**](PathStorageRequestDto.md)|  | 
 **user_id** | **str**|  | 

### Return type

[**PathStorageResponseDto**](PathStorageResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

