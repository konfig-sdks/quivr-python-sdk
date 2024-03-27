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


class ApiKey(BaseModel):
    api_key: str = Field(alias='api_key')

    key_id: str = Field(alias='key_id')

    days: int = Field(alias='days')

    only_chat: bool = Field(alias='only_chat')

    name: str = Field(alias='name')

    creation_time: str = Field(alias='creation_time')

    is_active: bool = Field(alias='is_active')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )