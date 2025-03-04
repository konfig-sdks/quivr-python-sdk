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


class RequiredBrainSubscriptionUpdatableProperties(TypedDict):
    email: str

class OptionalBrainSubscriptionUpdatableProperties(TypedDict, total=False):
    rights: typing.Optional[str]

class BrainSubscriptionUpdatableProperties(RequiredBrainSubscriptionUpdatableProperties, OptionalBrainSubscriptionUpdatableProperties):
    pass
