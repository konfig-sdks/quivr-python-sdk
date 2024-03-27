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

from quivr_python_sdk.type.api_brain_allowed_methods import ApiBrainAllowedMethods
from quivr_python_sdk.type.api_brain_definition_schema import ApiBrainDefinitionSchema
from quivr_python_sdk.type.api_brain_definition_schema_nullable import ApiBrainDefinitionSchemaNullable
from quivr_python_sdk.type.api_brain_definition_secret import ApiBrainDefinitionSecret

class RequiredCreateApiBrainDefinition(TypedDict):
    method: ApiBrainAllowedMethods

    url: str

class OptionalCreateApiBrainDefinition(TypedDict, total=False):
    params: typing.Optional[ApiBrainDefinitionSchemaNullable]

    search_params: ApiBrainDefinitionSchema

    secrets: typing.Optional[typing.List[ApiBrainDefinitionSecret]]

    raw: typing.Optional[bool]

    jq_instructions: typing.Optional[str]

class CreateApiBrainDefinition(RequiredCreateApiBrainDefinition, OptionalCreateApiBrainDefinition):
    pass