# ApiExceptionDetailsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 

## Example

```python
from pdfless_api.models.api_exception_details_result import ApiExceptionDetailsResult

# TODO update the JSON string below
json = "{}"
# create an instance of ApiExceptionDetailsResult from a JSON string
api_exception_details_result_instance = ApiExceptionDetailsResult.from_json(json)
# print the JSON string representation of the object
print(ApiExceptionDetailsResult.to_json())

# convert the object into a dict
api_exception_details_result_dict = api_exception_details_result_instance.to_dict()
# create an instance of ApiExceptionDetailsResult from a dict
api_exception_details_result_from_dict = ApiExceptionDetailsResult.from_dict(api_exception_details_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


