# swagger_client.BerufeNetApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**berufe_net_controller_get_all_jobs**](BerufeNetApi.md#berufe_net_controller_get_all_jobs) | **GET** /berufeNet/saveJobsToLocalDB | 
[**berufe_net_controller_get_all_jobs_start_with**](BerufeNetApi.md#berufe_net_controller_get_all_jobs_start_with) | **GET** /berufeNet/getJobsByPage | 
[**berufe_net_controller_get_competencies_by_job_id**](BerufeNetApi.md#berufe_net_controller_get_competencies_by_job_id) | **GET** /berufeNet/getCompetenciesByJobId | 
[**berufe_net_controller_get_digital_competencies_by_job_id**](BerufeNetApi.md#berufe_net_controller_get_digital_competencies_by_job_id) | **GET** /berufeNet/getDigitalCompetenciesByJobId | 
[**berufe_net_controller_get_jobs_by_id**](BerufeNetApi.md#berufe_net_controller_get_jobs_by_id) | **GET** /berufeNet/getJobById | 
[**berufe_net_controller_get_jobs_by_search_string**](BerufeNetApi.md#berufe_net_controller_get_jobs_by_search_string) | **GET** /berufeNet/getJobBySearchString | 

# **berufe_net_controller_get_all_jobs**
> list[object] berufe_net_controller_get_all_jobs()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BerufeNetApi()

try:
    api_response = api_instance.berufe_net_controller_get_all_jobs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BerufeNetApi->berufe_net_controller_get_all_jobs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **berufe_net_controller_get_all_jobs_start_with**
> object berufe_net_controller_get_all_jobs_start_with(page)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BerufeNetApi()
page = 'page_example' # str | 

try:
    api_response = api_instance.berufe_net_controller_get_all_jobs_start_with(page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BerufeNetApi->berufe_net_controller_get_all_jobs_start_with: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **berufe_net_controller_get_competencies_by_job_id**
> object berufe_net_controller_get_competencies_by_job_id(job_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BerufeNetApi()
job_id = 'job_id_example' # str | 

try:
    api_response = api_instance.berufe_net_controller_get_competencies_by_job_id(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BerufeNetApi->berufe_net_controller_get_competencies_by_job_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **berufe_net_controller_get_digital_competencies_by_job_id**
> object berufe_net_controller_get_digital_competencies_by_job_id(job_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BerufeNetApi()
job_id = 'job_id_example' # str | 

try:
    api_response = api_instance.berufe_net_controller_get_digital_competencies_by_job_id(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BerufeNetApi->berufe_net_controller_get_digital_competencies_by_job_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **berufe_net_controller_get_jobs_by_id**
> object berufe_net_controller_get_jobs_by_id(job_beruf_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BerufeNetApi()
job_beruf_id = 'job_beruf_id_example' # str | 

try:
    api_response = api_instance.berufe_net_controller_get_jobs_by_id(job_beruf_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BerufeNetApi->berufe_net_controller_get_jobs_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_beruf_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **berufe_net_controller_get_jobs_by_search_string**
> list[object] berufe_net_controller_get_jobs_by_search_string(search_string)



Getting Job Description by search string.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BerufeNetApi()
search_string = 'search_string_example' # str | 

try:
    api_response = api_instance.berufe_net_controller_get_jobs_by_search_string(search_string)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BerufeNetApi->berufe_net_controller_get_jobs_by_search_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**|  | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

