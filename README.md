# pdfless-api
Pdfless allows you to quickly and easily generate PDF documents using templates designed with HTML/CSS and conditional formatting.

- API version: v1
- Package version: 1.0.x

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install pdfless-api
```
(you may need to run `pip` with root permission: `sudo pip install pdfless-api`)

Then import the package:
```python
import pdfless_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import pdfless_api
from pdfless_api.rest import ApiException
from pprint import pprint

configuration = pdfless_api.Configuration(
    host = "https://api.pdfless.com",
    api_key= {'PdflessApiKey': 'ak_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx'}
)

# Enter a context with an instance of the API client
with pdfless_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdfless_api.PDFsApi(api_client)
    version = '1' # str | 

    try:

        command = pdfless_api.GeneratePDFCommand(
            template_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx",
            payload= {
                "string_variable": "value1", 
                "int_variable": 1, 
                "bool_variable": True, 
                "object": {
                    "child_variable": "child_value", 
                    "string_list": [
                        "item1",
                        "item2",
                        "item3"
                    ]
                }
            }
        )

        # Generate PDF
        api_response = api_instance.generate(version, command)
        print("The response of PDFsApi->generate:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PDFsApi->generate: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.pdfless.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DocumentTemplatesApi* | [**list_document_templates**](docs/DocumentTemplatesApi.md#list_document_templates) | **GET** /v{version}/document-templates | List document templates
*PDFsApi* | [**generate**](docs/PDFsApi.md#generate) | **POST** /v{version}/pdfs | Create PDF
*WorkspacesApi* | [**get_workspace**](docs/WorkspacesApi.md#get_workspace) | **GET** /v{version}/workspaces | Get workspace


## Documentation For Models

 - [ApiExceptionDetailsResult](docs/ApiExceptionDetailsResult.md)
 - [DocumentTemplateDto](docs/DocumentTemplateDto.md)
 - [GeneratePDFCommand](docs/GeneratePDFCommand.md)
 - [PDFDto](docs/PDFDto.md)
 - [PDFDtoApiResult](docs/PDFDtoApiResult.md)
 - [WorkspaceDto](docs/WorkspaceDto.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="PdflessAPIKeyAuth"></a>
### PdflessAPIKeyAuth

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: HTTP header


## Author

contact@pdfless.com


