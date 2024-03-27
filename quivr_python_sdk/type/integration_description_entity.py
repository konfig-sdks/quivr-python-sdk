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

from quivr_python_sdk.type.integration_brain_tag import IntegrationBrainTag
from quivr_python_sdk.type.integration_type import IntegrationType

class RequiredIntegrationDescriptionEntity(TypedDict):
    description: str

    id: str

    integration_name: str

    integration_type: IntegrationType

    max_files: int

    allow_model_change: bool

    integration_display_name: str

class OptionalIntegrationDescriptionEntity(TypedDict, total=False):
    tags: typing.Optional[typing.List[IntegrationBrainTag]]

    integration_logo_url: typing.Optional[str]

    connection_settings: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    information: typing.Optional[str]

class IntegrationDescriptionEntity(RequiredIntegrationDescriptionEntity, OptionalIntegrationDescriptionEntity):
    pass