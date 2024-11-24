# GeneratePDFCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | [optional] 
**payload** | **object** |  | [optional] 
**reference_id** | **str** |  | [optional] 

## Example

```python
from pdfless_api.models.generate_pdf_command import GeneratePDFCommand

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratePDFCommand from a JSON string
generate_pdf_command_instance = GeneratePDFCommand.from_json(json)
# print the JSON string representation of the object
print(GeneratePDFCommand.to_json())

# convert the object into a dict
generate_pdf_command_dict = generate_pdf_command_instance.to_dict()
# create an instance of GeneratePDFCommand from a dict
generate_pdf_command_from_dict = GeneratePDFCommand.from_dict(generate_pdf_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


