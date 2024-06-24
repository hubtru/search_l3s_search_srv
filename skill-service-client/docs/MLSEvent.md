# MLSEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Which entity is concerned by the event? User/Task/TaskTodo/TaskTodoInfo | 
**method** | **str** | What kind is the event of? PUT/POST/DELETE | 
**id** | **str** | The unique id used in the MLS system for the entity. | 
**payload** | **object** | The complete entity (including its id and all other attributes existing in the MLS system) | 
**task_todo_payload** | **object** | A special payload to get the parent object of a taskTodoInfo object. Only existent for this kind of object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

