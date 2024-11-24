# WorkspaceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of workspace | [optional] 
**active** | **bool** | Active status of workspace | [optional] 
**created** | **datetime** | Creation date | [optional] 
**modified** | **datetime** | Modification date | [optional] 
**quota** | **int** | Quota limit | [optional] 
**remaining_quota** | **int** | Remaining quota | [optional] 

## Example

```python
from pdfless_api.models.workspace_dto import WorkspaceDto

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceDto from a JSON string
workspace_dto_instance = WorkspaceDto.from_json(json)
# print the JSON string representation of the object
print(WorkspaceDto.to_json())

# convert the object into a dict
workspace_dto_dict = workspace_dto_instance.to_dict()
# create an instance of WorkspaceDto from a dict
workspace_dto_from_dict = WorkspaceDto.from_dict(workspace_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


