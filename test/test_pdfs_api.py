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

from pdfless_api.api.pdfs_api import PDFsApi


class TestPDFsApi(unittest.TestCase):
    """PDFsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PDFsApi()

    def tearDown(self) -> None:
        pass

    def test_generate(self) -> None:
        """Test case for generate

        Create PDF
        """
        pass


if __name__ == '__main__':
    unittest.main()
