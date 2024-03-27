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


class IntegrationType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "custom": "CUSTOM",
            "sync": "SYNC",
            "doc": "DOC",
        }
    
    @schemas.classproperty
    def CUSTOM(cls):
        return cls("custom")
    
    @schemas.classproperty
    def SYNC(cls):
        return cls("sync")
    
    @schemas.classproperty
    def DOC(cls):
        return cls("doc")
