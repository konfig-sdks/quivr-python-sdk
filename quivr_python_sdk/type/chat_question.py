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


class RequiredChatQuestion(TypedDict):
    question: str

class OptionalChatQuestion(TypedDict, total=False):
    model: typing.Optional[str]

    temperature: typing.Optional[typing.Union[int, float]]

    max_tokens: typing.Optional[int]

    brain_id: typing.Optional[str]

    prompt_id: typing.Optional[str]

class ChatQuestion(RequiredChatQuestion, OptionalChatQuestion):
    pass
