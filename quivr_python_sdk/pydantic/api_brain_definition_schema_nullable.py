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

from quivr_python_sdk.pydantic.api_brain_definition_schema_nullable_required import ApiBrainDefinitionSchemaNullableRequired
from quivr_python_sdk.pydantic.api_brain_definition_schema_property import ApiBrainDefinitionSchemaProperty

class ApiBrainDefinitionSchemaNullable(BaseModel):
    properties: typing.Optional[typing.List[ApiBrainDefinitionSchemaProperty]] = Field(None, alias='properties')

    required: typing.Optional[ApiBrainDefinitionSchemaNullableRequired] = Field(None, alias='required')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
