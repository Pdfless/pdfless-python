# coding: utf-8

"""
    Pdfless API

    Pdfless allows you to quickly and easily generate PDF documents using templates designed with HTML/CSS and conditional formatting.

    The version of the OpenAPI document: v1
    Contact: contact@pdfless.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "pdfless-api"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Pdfless API",
    author="Pdfless support team",
    author_email="contact@pdfless.com",
    url="https://github.com/Pdfless/pdfless-python",
    keywords=["PDF Generator", "Pdfless API", "Pdfless"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    Pdfless allows you to quickly and easily generate PDF documents using templates designed with HTML/CSS and conditional formatting.
    """,  # noqa: E501
    package_data={"pdfless_api": ["py.typed"]},
)
