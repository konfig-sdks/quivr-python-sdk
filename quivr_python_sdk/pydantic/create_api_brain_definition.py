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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from quivr_python_sdk.pydantic.api_brain_allowed_methods import ApiBrainAllowedMethods
from quivr_python_sdk.pydantic.api_brain_definition_schema import ApiBrainDefinitionSchema
from quivr_python_sdk.pydantic.api_brain_definition_schema_nullable import ApiBrainDefinitionSchemaNullable
from quivr_python_sdk.pydantic.api_brain_definition_secret import ApiBrainDefinitionSecret

class CreateApiBrainDefinition(BaseModel):
    method: ApiBrainAllowedMethods = Field(alias='method')

    url: str = Field(alias='url')

    params: typing.Optional[ApiBrainDefinitionSchemaNullable] = Field(None, alias='params')

    search_params: typing.Optional[ApiBrainDefinitionSchema] = Field(None, alias='search_params')

    secrets: typing.Optional[typing.Optional[typing.List[ApiBrainDefinitionSecret]]] = Field(None, alias='secrets')

    raw: typing.Optional[typing.Optional[bool]] = Field(None, alias='raw')

    jq_instructions: typing.Optional[typing.Optional[str]] = Field(None, alias='jq_instructions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
