# coding: utf-8

"""
    Pdfless API

    Pdfless allows you to quickly and easily generate PDF documents using templates designed with HTML/CSS and conditional formatting.

    The version of the OpenAPI document: v1
    Contact: contact@pdfless.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pdfless_api.models.generate_pdf_command import GeneratePDFCommand

class TestGeneratePDFCommand(unittest.TestCase):
    """GeneratePDFCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeneratePDFCommand:
        """Test GeneratePDFCommand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeneratePDFCommand`
        """
        model = GeneratePDFCommand()
        if include_optional:
            return GeneratePDFCommand(
                template_id = '',
                payload = None,
                reference_id = ''
            )
        else:
            return GeneratePDFCommand(
        )
        """

    def testGeneratePDFCommand(self):
        """Test GeneratePDFCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
