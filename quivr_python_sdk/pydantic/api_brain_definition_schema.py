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

from quivr_python_sdk.pydantic.api_brain_definition_schema_property import ApiBrainDefinitionSchemaProperty
from quivr_python_sdk.pydantic.api_brain_definition_schema_required import ApiBrainDefinitionSchemaRequired

class ApiBrainDefinitionSchema(BaseModel):
    properties: typing.Optional[typing.List[ApiBrainDefinitionSchemaProperty]] = Field(None, alias='properties')

    required: typing.Optional[ApiBrainDefinitionSchemaRequired] = Field(None, alias='required')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )