# coding: utf-8

"""
    FastAPI

    Open-source RAG Framework

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from quivr_python_sdk import schemas  # noqa: F401


class ValidationError(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "msg",
            "loc",
            "type",
        }
        
        class properties:
        
            @staticmethod
            def loc() -> typing.Type['ValidationErrorLoc']:
                return ValidationErrorLoc
            msg = schemas.StrSchema
            type = schemas.StrSchema
            __annotations__ = {
                "loc": loc,
                "msg": msg,
                "type": type,
            }
    
    msg: MetaOapg.properties.msg
    loc: 'ValidationErrorLoc'
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loc"]) -> 'ValidationErrorLoc': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["msg"]) -> MetaOapg.properties.msg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["loc", "msg", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loc"]) -> 'ValidationErrorLoc': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["msg"]) -> MetaOapg.properties.msg: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["loc", "msg", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        msg: typing.Union[MetaOapg.properties.msg, str, ],
        loc: 'ValidationErrorLoc',
        type: typing.Union[MetaOapg.properties.type, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ValidationError':
        return super().__new__(
            cls,
            *args,
            msg=msg,
            loc=loc,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from quivr_python_sdk.model.validation_error_loc import ValidationErrorLoc
