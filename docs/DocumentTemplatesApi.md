# pdfless_api.DocumentTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_document_templates**](DocumentTemplatesApi.md#list_document_templates) | **GET** /v{version}/document-templates | List document templates


# **list_document_templates**
> List[DocumentTemplateDto] list_document_templates(version, page=page, page_size=page_size)

List document templates

List document templates of current workspace

### Example

* Api Key Authentication (PdflessApiKey):

```python
import pdfless_api
from pdfless_api.models.document_template_dto import DocumentTemplateDto
from pdfless_api.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = pdfless_api.Configuration(
    host = "https://api.pdfless.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: PdflessApiKey
configuration.api_key['PdflessApiKey'] = os.environ["API_KEY"]

# Enter a context with an instance of the API client
with pdfless_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdfless_api.DocumentTemplatesApi(api_client)
    version = '1' # str | 
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)

    try:
        # List document templates
        api_response = api_instance.list_document_templates(version, page=page, page_size=page_size)
        print("The response of DocumentTemplatesApi->list_document_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentTemplatesApi->list_document_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**List[DocumentTemplateDto]**](DocumentTemplateDto.md)

### Authorization

[PdflessApiKey](../README.md#PdflessApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

