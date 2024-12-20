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

from pdfless_api.models.pdf_dto import PDFDto

class TestPDFDto(unittest.TestCase):
    """PDFDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PDFDto:
        """Test PDFDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PDFDto`
        """
        model = PDFDto()
        if include_optional:
            return PDFDto(
                reference_id = '',
                template_id = '',
                download_url = '',
                expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PDFDto(
        )
        """

    def testPDFDto(self):
        """Test PDFDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
