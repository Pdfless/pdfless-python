# pdfless_api.WorkspacesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /v{version}/workspaces | Get workspace


# **get_workspace**
> WorkspaceDto get_workspace(version)

Get workspace

Get workspace detail

### Example

* Api Key Authentication (PdflessApiKey):

```python
import pdfless_api
from pdfless_api.models.workspace_dto import WorkspaceDto
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
    api_instance = pdfless_api.WorkspacesApi(api_client)
    version = '1' # str | 

    try:
        # Get workspace
        api_response = api_instance.get_workspace(version)
        print("The response of WorkspacesApi->get_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 

### Return type

[**WorkspaceDto**](WorkspaceDto.md)

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

