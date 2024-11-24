# PDFDtoApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PDFDto**](PDFDto.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pdfless_api.models.pdf_dto_api_result import PDFDtoApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of PDFDtoApiResult from a JSON string
pdf_dto_api_result_instance = PDFDtoApiResult.from_json(json)
# print the JSON string representation of the object
print(PDFDtoApiResult.to_json())

# convert the object into a dict
pdf_dto_api_result_dict = pdf_dto_api_result_instance.to_dict()
# create an instance of PDFDtoApiResult from a dict
pdf_dto_api_result_from_dict = PDFDtoApiResult.from_dict(pdf_dto_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


