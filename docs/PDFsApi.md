# pdfless_api.PDFsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate**](PDFsApi.md#generate) | **POST** /v{version}/pdfs | Create PDF


# **generate**
> PDFDtoApiResult generate(version, generate_pdf_command=generate_pdf_command)

Create PDF

Generate document based on template ID and payload data

### Example

* Api Key Authentication (PdflessApiKey):

```python
import pdfless_api
from pdfless_api.models.generate_pdf_command import GeneratePDFCommand
from pdfless_api.models.pdf_dto_api_result import PDFDtoApiResult
from pdfless_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pdfless_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: PdflessApiKey
configuration.api_key['PdflessApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PdflessApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with pdfless_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdfless_api.PDFsApi(api_client)
    version = 'version_example' # str | 
    generate_pdf_command = pdfless_api.GeneratePDFCommand() # GeneratePDFCommand |  (optional)

    try:
        # Create PDF
        api_response = api_instance.generate(version, generate_pdf_command=generate_pdf_command)
        print("The response of PDFsApi->generate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFsApi->generate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **generate_pdf_command** | [**GeneratePDFCommand**](GeneratePDFCommand.md)|  | [optional] 

### Return type

[**PDFDtoApiResult**](PDFDtoApiResult.md)

### Authorization

[PdflessApiKey](../README.md#PdflessApiKey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

