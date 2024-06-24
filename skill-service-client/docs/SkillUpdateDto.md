# SkillUpdateDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nested_skills** | **list[str]** | Specifies nested child skills: - If undefined: No change - If null: Remove all nested skills - If specified: Replace all nested skills with the specified ones | [optional] 
**parent_skills** | **list[str]** | Specifies parent skills: - If undefined: No change - If null: Remove all parent skills -&gt; Make this a top level skill - If specified: Replace all parent skills with the specified ones | [optional] 
**repository_id** | **str** | Moves this and all nested skills to the specified repository. | [optional] 
**name** | **str** | Renames the skill. | [optional] 
**level** | **float** | Changes the level of the skill. | [optional] 
**description** | **str** | Changes the description of the skill: - If undefined: No change - If null: Remove the description - If specified: Replace the description with the specified one | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

