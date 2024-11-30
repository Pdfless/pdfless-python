# coding: utf-8

"""
    Pdfless API

    Pdfless allows you to quickly and easily generate PDF documents using templates designed with HTML/CSS and conditional formatting.

    The version of the OpenAPI document: v1
    Contact: contact@pdfless.com
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301
import sys

# Read README.md
with open("README_PY.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

####### get version from arguments start ##########
# version = None
# if '--version' in sys.argv:
#     index = sys.argv.index('--version')
#     sys.argv.pop(index)
#     version = sys.argv.pop(index)
# else:
#     version = "1.0.0"
####### get version from arguments end ##########

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "pdfless-api"
VERSION = "1.1.2"
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
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={"pdfless_api": ["py.typed"]},
)
