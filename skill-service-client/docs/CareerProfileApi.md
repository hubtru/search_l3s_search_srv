# swagger_client.CareerProfileApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**career_profile_controller_add_job**](CareerProfileApi.md#career_profile_controller_add_job) | **POST** /career-profiles/{career_profile_id}/job_history | 
[**career_profile_controller_add_qualification_to_career_profile**](CareerProfileApi.md#career_profile_controller_add_qualification_to_career_profile) | **POST** /career-profiles/{career_profile_id}/qualifications | 
[**career_profile_controller_delete_job_history_at_career_profile_by_id**](CareerProfileApi.md#career_profile_controller_delete_job_history_at_career_profile_by_id) | **DELETE** /job_history/{job_id} | 
[**career_profile_controller_delete_qualification_to_career_profile**](CareerProfileApi.md#career_profile_controller_delete_qualification_to_career_profile) | **DELETE** /qualifications/{qualification_id} | 
[**career_profile_controller_get_all_career_profiles**](CareerProfileApi.md#career_profile_controller_get_all_career_profiles) | **GET** /career-profiles | 
[**career_profile_controller_get_career_profile_by_id**](CareerProfileApi.md#career_profile_controller_get_career_profile_by_id) | **GET** /career-profiles/{career_profile_id} | 
[**career_profile_controller_patch_career_profile_by_id**](CareerProfileApi.md#career_profile_controller_patch_career_profile_by_id) | **PATCH** /career-profiles/{career_profile_id} | 
[**career_profile_controller_patch_job_history_at_career_profile_by_id**](CareerProfileApi.md#career_profile_controller_patch_job_history_at_career_profile_by_id) | **PATCH** /job_history/{job_id} | 
[**career_profile_controller_patch_qualification_to_career_profile**](CareerProfileApi.md#career_profile_controller_patch_qualification_to_career_profile) | **PATCH** /qualifications/{qualification_id} | 

# **career_profile_controller_add_job**
> str career_profile_controller_add_job(body, career_profile_id)



Creates a new job object and adds it to the user's job history and their career profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CareerProfileApi()
body = swagger_client.JobDto() # JobDto | 
career_profile_id = 'career_profile_id_example' # str | 

try:
    api_response = api_instance.career_profile_controller_add_job(body, career_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CareerProfileApi->career_profile_controller_add_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobDto**](JobDto.md)|  | 
 **career_profile_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **career_profile_controller_add_qualification_to_career_profile**
> str career_profile_controller_add_qualification_to_career_profile(body, career_profile_id)



Adds a new qualification to the career profile of a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CareerProfileApi()
body = swagger_client.QualificationDto() # QualificationDto | 
career_profile_id = 'career_profile_id_example' # str | 

try:
    api_response = api_instance.career_profile_controller_add_qualification_to_career_profile(body, career_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CareerProfileApi->career_profile_controller_add_qualification_to_career_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualificationDto**](QualificationDto.md)|  | 
 **career_profile_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **career_profile_controller_delete_job_history_at_career_profile_by_id**
> career_profile_controller_delete_job_history_at_career_profile_by_id(job_id)



Deletes an existing job from the job history (and career profile) of a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CareerProfileApi()
job_id = 'job_id_example' # str | 

try:
    api_instance.career_profile_controller_delete_job_history_at_career_profile_by_id(job_id)
except ApiException as e:
    print("Exception when calling CareerProfileApi->career_profile_controller_delete_job_history_at_career_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **career_profile_controller_delete_qualification_to_career_profile**
> str career_profile_controller_delete_qualification_to_career_profile(qualification_id)



Deletes an existing qualification from the career profile of a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CareerProfileApi()
qualification_id = 'qualification_id_example' # str | 

try:
    api_response = api_instance.career_profile_controller_delete_qualification_to_career_profile(qualification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CareerProfileApi->career_profile_controller_delete_qualification_to_career_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qualification_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **career_profile_controller_get_all_career_profiles**
> list[CareerProfileDto] career_profile_controller_get_all_career_profiles()



Return all existing career profiles. Used for ai stuff.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CareerProfileApi()

try:
    api_response = api_instance.career_profile_controller_get_all_career_profiles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CareerProfileApi->career_profile_controller_get_all_career_profiles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CareerProfileDto]**](CareerProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **career_profile_controller_get_career_profile_by_id**
> CareerProfileDto career_profile_controller_get_career_profile_by_id(career_profile_id)



Returns the requested career profile including all child objects (sorted ascending by (start)date)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CareerProfileApi()
career_profile_id = 'career_profile_id_example' # str | 

try:
    api_response = api_instance.career_profile_controller_get_career_profile_by_id(career_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CareerProfileApi->career_profile_controller_get_career_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **career_profile_id** | **str**|  | 

### Return type

[**CareerProfileDto**](CareerProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **career_profile_controller_patch_career_profile_by_id**
> career_profile_controller_patch_career_profile_by_id(body, career_profile_id)



Allows a user to update their career profile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CareerProfileApi()
body = swagger_client.CareerProfileDto() # CareerProfileDto | 
career_profile_id = 'career_profile_id_example' # str | 

try:
    api_instance.career_profile_controller_patch_career_profile_by_id(body, career_profile_id)
except ApiException as e:
    print("Exception when calling CareerProfileApi->career_profile_controller_patch_career_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CareerProfileDto**](CareerProfileDto.md)|  | 
 **career_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **career_profile_controller_patch_job_history_at_career_profile_by_id**
> str career_profile_controller_patch_job_history_at_career_profile_by_id(body, job_id)



Updates the values of an existing job in the job history of a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CareerProfileApi()
body = swagger_client.JobDto() # JobDto | 
job_id = 'job_id_example' # str | 

try:
    api_response = api_instance.career_profile_controller_patch_job_history_at_career_profile_by_id(body, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CareerProfileApi->career_profile_controller_patch_job_history_at_career_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobDto**](JobDto.md)|  | 
 **job_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **career_profile_controller_patch_qualification_to_career_profile**
> str career_profile_controller_patch_qualification_to_career_profile(body, qualification_id)



Updates an existing qualification in the career profile of a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CareerProfileApi()
body = swagger_client.QualificationDto() # QualificationDto | 
qualification_id = 'qualification_id_example' # str | 

try:
    api_response = api_instance.career_profile_controller_patch_qualification_to_career_profile(body, qualification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CareerProfileApi->career_profile_controller_patch_qualification_to_career_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualificationDto**](QualificationDto.md)|  | 
 **qualification_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

