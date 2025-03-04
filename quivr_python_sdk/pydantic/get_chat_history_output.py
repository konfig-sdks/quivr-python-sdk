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


class GetChatHistoryOutput(BaseModel):
    chat_id: str = Field(alias='chat_id')

    message_id: typing.Union[str, str] = Field(alias='message_id')

    user_message: str = Field(alias='user_message')

    assistant: str = Field(alias='assistant')

    message_time: typing.Optional[typing.Optional[str]] = Field(None, alias='message_time')

    prompt_title: typing.Optional[typing.Optional[str]] = Field(None, alias='prompt_title')

    brain_name: typing.Optional[typing.Optional[str]] = Field(None, alias='brain_name')

    brain_id: typing.Optional[typing.Optional[str]] = Field(None, alias='brain_id')

    metadata: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='metadata')

    thumbs: typing.Optional[typing.Optional[bool]] = Field(None, alias='thumbs')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
