# coding: utf-8

"""
    Pdfless API

    Pdfless allows you to quickly and easily generate PDF documents using templates designed with HTML/CSS and conditional formatting.

    The version of the OpenAPI document: v1
    Contact: contact@pdfless.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ApiExceptionDetailsResult(BaseModel):
    """
    ApiExceptionDetailsResult
    """ # noqa: E501
    message: Optional[StrictStr] = None
    error_code: Optional[StrictStr] = None
    documentation_url: Optional[StrictStr] = None
    correlation_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["message", "error_code", "documentation_url", "correlation_id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiExceptionDetailsResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if error_code (nullable) is None
        # and model_fields_set contains the field
        if self.error_code is None and "error_code" in self.model_fields_set:
            _dict['error_code'] = None

        # set to None if documentation_url (nullable) is None
        # and model_fields_set contains the field
        if self.documentation_url is None and "documentation_url" in self.model_fields_set:
            _dict['documentation_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiExceptionDetailsResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message": obj.get("message"),
            "error_code": obj.get("error_code"),
            "documentation_url": obj.get("documentation_url"),
            "correlation_id": obj.get("correlation_id")
        })
        return _obj

