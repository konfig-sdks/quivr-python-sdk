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

from quivr_python_sdk.type.api_brain_definition_schema_property_enum import ApiBrainDefinitionSchemaPropertyEnum

class RequiredApiBrainDefinitionSchemaProperty(TypedDict):
    description: str

    type: str

    name: str

class OptionalApiBrainDefinitionSchemaProperty(TypedDict, total=False):
    enum: typing.Optional[ApiBrainDefinitionSchemaPropertyEnum]

class ApiBrainDefinitionSchemaProperty(RequiredApiBrainDefinitionSchemaProperty, OptionalApiBrainDefinitionSchemaProperty):
    pass