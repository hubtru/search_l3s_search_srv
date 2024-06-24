# PersonalizedPathDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personalized_path_id** | **str** | The id of the personalized path. | 
**learning_path_id** | **str** | The id of the learning path used as a template for the personalized path. Can be null when the path is created by the learner via goals. | 
**goals** | **list[str]** | The goals (taught skill ids) of the personalized path (created by a learner). Can be empty when the path is based on an existing learning path. | 
**status** | **object** | The status of the personalized path. Can be OPEN (newly enrolled), IN_PROGRESS (currently doing at least one contained learning unit), or FINISHED (all learning units are successfully finished) | 
**learning_unit_instances** | [**list[LearningUnitInstanceStatusDto]**](LearningUnitInstanceStatusDto.md) | The sequence of the contained learning unit instances (their unit&#x27;s id and status) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

