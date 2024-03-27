# coding: utf-8

"""
    FastAPI

    Open-source RAG Framework

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from quivr_python_sdk.type.prompt_status_enum_nullable import PromptStatusEnumNullable

class RequiredPromptUpdatableProperties(TypedDict):
    pass

class OptionalPromptUpdatableProperties(TypedDict, total=False):
    title: typing.Optional[str]

    content: typing.Optional[str]

    status: typing.Optional[PromptStatusEnumNullable]

class PromptUpdatableProperties(RequiredPromptUpdatableProperties, OptionalPromptUpdatableProperties):
    pass
