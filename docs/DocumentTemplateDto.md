# DocumentTemplateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Template identifier | [optional] 
**name** | **str** | Template name | [optional] 
**image_preview_url** | **str** | Image preview of document template | [optional] 
**pdf_preview_url** | **str** | PDF preview of document template | [optional] 
**created** | **datetime** | Creation date | [optional] 
**modified** | **datetime** | Modification date | [optional] 

## Example

```python
from pdfless_api.models.document_template_dto import DocumentTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTemplateDto from a JSON string
document_template_dto_instance = DocumentTemplateDto.from_json(json)
# print the JSON string representation of the object
print(DocumentTemplateDto.to_json())

# convert the object into a dict
document_template_dto_dict = document_template_dto_instance.to_dict()
# create an instance of DocumentTemplateDto from a dict
document_template_dto_from_dict = DocumentTemplateDto.from_dict(document_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


