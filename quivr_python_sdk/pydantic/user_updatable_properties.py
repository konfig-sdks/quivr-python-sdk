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


class UserUpdatableProperties(BaseModel):
    username: typing.Optional[typing.Optional[str]] = Field(None, alias='username')

    company: typing.Optional[typing.Optional[str]] = Field(None, alias='company')

    onboarded: typing.Optional[typing.Optional[bool]] = Field(None, alias='onboarded')

    company_size: typing.Optional[typing.Optional[str]] = Field(None, alias='company_size')

    usage_purpose: typing.Optional[typing.Optional[str]] = Field(None, alias='usage_purpose')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
