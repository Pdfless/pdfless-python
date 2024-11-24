# PDFDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **str** | Internal reference identifier | [optional] 
**template_id** | **str** | Targeting template identifier | [optional] 
**download_url** | **str** | URL of generated document | [optional] 
**expires** | **datetime** | Expiration date | [optional] 
**created_at** | **datetime** | Creation date | [optional] 

## Example

```python
from pdfless_api.models.pdf_dto import PDFDto

# TODO update the JSON string below
json = "{}"
# create an instance of PDFDto from a JSON string
pdf_dto_instance = PDFDto.from_json(json)
# print the JSON string representation of the object
print(PDFDto.to_json())

# convert the object into a dict
pdf_dto_dict = pdf_dto_instance.to_dict()
# create an instance of PDFDto from a dict
pdf_dto_from_dict = PDFDto.from_dict(pdf_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


