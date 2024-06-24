# swagger_client.EventsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_controller_get_events**](EventsApi.md#events_controller_get_events) | **POST** /events | Experimental (WIP)

# **events_controller_get_events**
> object events_controller_get_events(body)

Experimental (WIP)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventsApi()
body = swagger_client.MLSEvent() # MLSEvent | 

try:
    # Experimental (WIP)
    api_response = api_instance.events_controller_get_events(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_controller_get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MLSEvent**](MLSEvent.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

