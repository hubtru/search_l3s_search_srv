# swagger_client.SkillApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**skill_mgmt_controller_adapt_repo**](SkillApi.md#skill_mgmt_controller_adapt_repo) | **PATCH** /skill-repositories/{repositoryId} | 
[**skill_mgmt_controller_add_skill**](SkillApi.md#skill_mgmt_controller_add_skill) | **POST** /skill-repositories/{repositoryId}/skill/add_skill | 
[**skill_mgmt_controller_create_repository**](SkillApi.md#skill_mgmt_controller_create_repository) | **POST** /skill-repositories/create | 
[**skill_mgmt_controller_delete_repo**](SkillApi.md#skill_mgmt_controller_delete_repo) | **DELETE** /skill-repositories/{repositoryId} | 
[**skill_mgmt_controller_delete_skill_with_check**](SkillApi.md#skill_mgmt_controller_delete_skill_with_check) | **DELETE** /skill-repositories/skill/deleteWithCheck/{skillId} | 
[**skill_mgmt_controller_delete_skill_without_check**](SkillApi.md#skill_mgmt_controller_delete_skill_without_check) | **DELETE** /skill-repositories/skill/deleteWithoutCheck/{skillId} | 
[**skill_mgmt_controller_find_skills**](SkillApi.md#skill_mgmt_controller_find_skills) | **POST** /skill-repositories/findSkills | 
[**skill_mgmt_controller_find_skills_resolved**](SkillApi.md#skill_mgmt_controller_find_skills_resolved) | **POST** /skill-repositories/resolve/findSkills | 
[**skill_mgmt_controller_get_all_skills**](SkillApi.md#skill_mgmt_controller_get_all_skills) | **GET** /skill-repositories/getAllSkills | 
[**skill_mgmt_controller_get_resolved_skill**](SkillApi.md#skill_mgmt_controller_get_resolved_skill) | **GET** /skill-repositories/resolve/skill/{skillId} | 
[**skill_mgmt_controller_get_skill**](SkillApi.md#skill_mgmt_controller_get_skill) | **GET** /skill-repositories/skill/{skillId} | 
[**skill_mgmt_controller_list_repositories**](SkillApi.md#skill_mgmt_controller_list_repositories) | **GET** /skill-repositories/byOwner/{ownerId} | 
[**skill_mgmt_controller_load_repository**](SkillApi.md#skill_mgmt_controller_load_repository) | **GET** /skill-repositories/byId/{repositoryId} | 
[**skill_mgmt_controller_search_for_repositories**](SkillApi.md#skill_mgmt_controller_search_for_repositories) | **POST** /skill-repositories | 
[**skill_mgmt_controller_update_skill**](SkillApi.md#skill_mgmt_controller_update_skill) | **PATCH** /skill-repositories/skill/{skillId} | 

# **skill_mgmt_controller_adapt_repo**
> UnresolvedSkillRepositoryDto skill_mgmt_controller_adapt_repo(body, repository_id)



Adapts a repository and returns the adapted it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
body = swagger_client.SkillRepositoryUpdateDto() # SkillRepositoryUpdateDto | 
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.skill_mgmt_controller_adapt_repo(body, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_adapt_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SkillRepositoryUpdateDto**](SkillRepositoryUpdateDto.md)|  | 
 **repository_id** | **str**|  | 

### Return type

[**UnresolvedSkillRepositoryDto**](UnresolvedSkillRepositoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_add_skill**
> SkillDto skill_mgmt_controller_add_skill(body, repository_id)



Creates a new skill at the specified repository and returns the created skill.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
body = swagger_client.SkillCreationDto() # SkillCreationDto | 
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.skill_mgmt_controller_add_skill(body, repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_add_skill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SkillCreationDto**](SkillCreationDto.md)|  | 
 **repository_id** | **str**|  | 

### Return type

[**SkillDto**](SkillDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_create_repository**
> SkillRepositoryDto skill_mgmt_controller_create_repository(body)



Creates a new skill repository for the specified user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
body = swagger_client.SkillRepositoryCreationDto() # SkillRepositoryCreationDto | 

try:
    api_response = api_instance.skill_mgmt_controller_create_repository(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_create_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SkillRepositoryCreationDto**](SkillRepositoryCreationDto.md)|  | 

### Return type

[**SkillRepositoryDto**](SkillRepositoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_delete_repo**
> skill_mgmt_controller_delete_repo(repository_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
repository_id = 'repository_id_example' # str | 

try:
    api_instance.skill_mgmt_controller_delete_repo(repository_id)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_delete_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_delete_skill_with_check**
> skill_mgmt_controller_delete_skill_with_check(skill_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
skill_id = 'skill_id_example' # str | 

try:
    api_instance.skill_mgmt_controller_delete_skill_with_check(skill_id)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_delete_skill_with_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_delete_skill_without_check**
> skill_mgmt_controller_delete_skill_without_check(skill_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
skill_id = 'skill_id_example' # str | 

try:
    api_instance.skill_mgmt_controller_delete_skill_without_check(skill_id)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_delete_skill_without_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_find_skills**
> SkillListDto skill_mgmt_controller_find_skills(body)



Lists all skills matching given attributes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
body = swagger_client.SkillSearchDto() # SkillSearchDto | 

try:
    api_response = api_instance.skill_mgmt_controller_find_skills(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_find_skills: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SkillSearchDto**](SkillSearchDto.md)|  | 

### Return type

[**SkillListDto**](SkillListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_find_skills_resolved**
> ResolvedSkillListDto skill_mgmt_controller_find_skills_resolved(body)



Lists all skills.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
body = swagger_client.SkillSearchDto() # SkillSearchDto | 

try:
    api_response = api_instance.skill_mgmt_controller_find_skills_resolved(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_find_skills_resolved: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SkillSearchDto**](SkillSearchDto.md)|  | 

### Return type

[**ResolvedSkillListDto**](ResolvedSkillListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_get_all_skills**
> SkillListDto skill_mgmt_controller_get_all_skills()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()

try:
    api_response = api_instance.skill_mgmt_controller_get_all_skills()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_get_all_skills: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SkillListDto**](SkillListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_get_resolved_skill**
> ResolvedSkillDto skill_mgmt_controller_get_resolved_skill(skill_id)



Returns the specified skill.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
skill_id = 'skill_id_example' # str | 

try:
    api_response = api_instance.skill_mgmt_controller_get_resolved_skill(skill_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_get_resolved_skill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | **str**|  | 

### Return type

[**ResolvedSkillDto**](ResolvedSkillDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_get_skill**
> SkillDto skill_mgmt_controller_get_skill(skill_id)



Returns the specified skill.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
skill_id = 'skill_id_example' # str | 

try:
    api_response = api_instance.skill_mgmt_controller_get_skill(skill_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_get_skill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | **str**|  | 

### Return type

[**SkillDto**](SkillDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_list_repositories**
> SkillRepositoryListDto skill_mgmt_controller_list_repositories(owner_id)



Lists all repositories of the specified user, without showing its content.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
owner_id = 'owner_id_example' # str | 

try:
    api_response = api_instance.skill_mgmt_controller_list_repositories(owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_list_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id** | **str**|  | 

### Return type

[**SkillRepositoryListDto**](SkillRepositoryListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_load_repository**
> UnresolvedSkillRepositoryDto skill_mgmt_controller_load_repository(repository_id)



Returns one repository and its unresolved elements. Skills and their relations are handled as IDs and need to be resolved on the client-side.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
repository_id = 'repository_id_example' # str | 

try:
    api_response = api_instance.skill_mgmt_controller_load_repository(repository_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_load_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**|  | 

### Return type

[**UnresolvedSkillRepositoryDto**](UnresolvedSkillRepositoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_search_for_repositories**
> SkillRepositoryListDto skill_mgmt_controller_search_for_repositories(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
body = swagger_client.SkillRepositorySearchDto() # SkillRepositorySearchDto | 

try:
    api_response = api_instance.skill_mgmt_controller_search_for_repositories(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_search_for_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SkillRepositorySearchDto**](SkillRepositorySearchDto.md)|  | 

### Return type

[**SkillRepositoryListDto**](SkillRepositoryListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skill_mgmt_controller_update_skill**
> object skill_mgmt_controller_update_skill(body, skill_id)



Updates a skill as follows: - First: It will update all values of the skill (name, level, description, nestedSkills, parentSkills) - Second: It will move the skill to another repository, if a new repositoryId is specified <br> - In this case, all nested skills will be moved to the new repository as well <br> - None of the skills may be used in a learning unit <br> - None of the skills may have an additional parent, which is not moved to the new repository  For the update the following rules apply: - If a value is undefined, it will not be changed - If a value is null, it will be cleared / set to default - If a value is specified, it will be set to the specified value

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SkillApi()
body = swagger_client.SkillUpdateDto() # SkillUpdateDto | 
skill_id = 'skill_id_example' # str | 

try:
    api_response = api_instance.skill_mgmt_controller_update_skill(body, skill_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SkillApi->skill_mgmt_controller_update_skill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SkillUpdateDto**](SkillUpdateDto.md)|  | 
 **skill_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

