# PathRequestDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal** | **list[str]** | The list of skills to be learned. | 
**user_id** | **str** | If specified, path will be computed and optimized for the specified user. This includes: - taking into account the user&#x27;s current skills - taking into account the user&#x27;s learning behavior | [optional] 
**optimal_solution** | **bool** | If unspecified, algorithm will use a fast, greedy approach to find a path. If true, the algorithm will try to find an optimal path, at cost of performance. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

