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


class RequiredApiBrainDefinitionSecret(TypedDict):
    name: str

    type: str

class OptionalApiBrainDefinitionSecret(TypedDict, total=False):
    description: typing.Optional[str]

class ApiBrainDefinitionSecret(RequiredApiBrainDefinitionSecret, OptionalApiBrainDefinitionSecret):
    pass
