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


class IntegrationBrainTag(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "new": "NEW",
            "recommended": "RECOMMENDED",
            "most_popular": "MOST_POPULAR",
            "premium": "PREMIUM",
            "coming_soon": "COMING_SOON",
            "community": "COMMUNITY",
            "deprecated": "DEPRECATED",
        }
    
    @schemas.classproperty
    def NEW(cls):
        return cls("new")
    
    @schemas.classproperty
    def RECOMMENDED(cls):
        return cls("recommended")
    
    @schemas.classproperty
    def MOST_POPULAR(cls):
        return cls("most_popular")
    
    @schemas.classproperty
    def PREMIUM(cls):
        return cls("premium")
    
    @schemas.classproperty
    def COMING_SOON(cls):
        return cls("coming_soon")
    
    @schemas.classproperty
    def COMMUNITY(cls):
        return cls("community")
    
    @schemas.classproperty
    def DEPRECATED(cls):
        return cls("deprecated")
