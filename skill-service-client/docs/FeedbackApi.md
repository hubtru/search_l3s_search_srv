# swagger_client.FeedbackApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feedback_controller_add_feedback**](FeedbackApi.md#feedback_controller_add_feedback) | **POST** /feedbacks | 
[**feedback_controller_delete_feedback**](FeedbackApi.md#feedback_controller_delete_feedback) | **DELETE** /feedbacks/{feedbackId} | 
[**feedback_controller_get_feedback**](FeedbackApi.md#feedback_controller_get_feedback) | **GET** /feedbacks/{feedbackId} | 
[**feedback_controller_list_feedback**](FeedbackApi.md#feedback_controller_list_feedback) | **GET** /learning-units/{learningUnitId}/feedbacks | 

# **feedback_controller_add_feedback**
> FeedbackDto feedback_controller_add_feedback(body)



Creates a new feedback and returns it for the respective learning unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeedbackApi()
body = swagger_client.FeedbackCreationDto() # FeedbackCreationDto | 

try:
    api_response = api_instance.feedback_controller_add_feedback(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedbackApi->feedback_controller_add_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeedbackCreationDto**](FeedbackCreationDto.md)|  | 

### Return type

[**FeedbackDto**](FeedbackDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feedback_controller_delete_feedback**
> bool feedback_controller_delete_feedback(feedback_id)



Deletes the specified feedback from the database

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeedbackApi()
feedback_id = 'feedback_id_example' # str | 

try:
    api_response = api_instance.feedback_controller_delete_feedback(feedback_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedbackApi->feedback_controller_delete_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feedback_controller_get_feedback**
> feedback_controller_get_feedback(feedback_id)



Returns the specified feedback.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeedbackApi()
feedback_id = 'feedback_id_example' # str | 

try:
    api_instance.feedback_controller_get_feedback(feedback_id)
except ApiException as e:
    print("Exception when calling FeedbackApi->feedback_controller_get_feedback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feedback_controller_list_feedback**
> feedback_controller_list_feedback(learning_unit_id)



Lists all available feedback for the respective learning unit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeedbackApi()
learning_unit_id = 'learning_unit_id_example' # str | 

try:
    api_instance.feedback_controller_list_feedback(learning_unit_id)
except ApiException as e:
    print("Exception when calling FeedbackApi->feedback_controller_list_feedback: %s\n" % e)
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

