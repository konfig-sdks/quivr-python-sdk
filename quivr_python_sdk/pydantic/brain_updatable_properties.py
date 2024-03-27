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

from quivr_python_sdk.pydantic.api_brain_definition_entity_input_nullable import ApiBrainDefinitionEntityInputNullable
from quivr_python_sdk.pydantic.brain_integration_update_settings_nullable import BrainIntegrationUpdateSettingsNullable
from quivr_python_sdk.pydantic.brain_updatable_properties_connected_brains_ids import BrainUpdatablePropertiesConnectedBrainsIds

class BrainUpdatableProperties(BaseModel):
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='temperature')

    model: typing.Optional[typing.Optional[str]] = Field(None, alias='model')

    max_tokens: typing.Optional[typing.Optional[int]] = Field(None, alias='max_tokens')

    status: typing.Optional[typing.Optional[str]] = Field(None, alias='status')

    prompt_id: typing.Optional[typing.Optional[str]] = Field(None, alias='prompt_id')

    brain_definition: typing.Optional[ApiBrainDefinitionEntityInputNullable] = Field(None, alias='brain_definition')

    connected_brains_ids: typing.Optional[BrainUpdatablePropertiesConnectedBrainsIds] = Field(None, alias='connected_brains_ids')

    integration: typing.Optional[BrainIntegrationUpdateSettingsNullable] = Field(None, alias='integration')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )