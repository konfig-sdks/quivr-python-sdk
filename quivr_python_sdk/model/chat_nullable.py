# coding: utf-8

"""
    FastAPI

    Open-source RAG Framework

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from quivr_python_sdk import schemas  # noqa: F401


class ChatNullable(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "creation_time",
            "user_id",
            "chat_id",
            "chat_name",
        }
        
        class properties:
            chat_id = schemas.StrSchema
            user_id = schemas.StrSchema
            creation_time = schemas.StrSchema
            chat_name = schemas.StrSchema
            __annotations__ = {
                "chat_id": chat_id,
                "user_id": user_id,
                "creation_time": creation_time,
                "chat_name": chat_name,
            }

    
    creation_time: MetaOapg.properties.creation_time
    user_id: MetaOapg.properties.user_id
    chat_id: MetaOapg.properties.chat_id
    chat_name: MetaOapg.properties.chat_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chat_id"]) -> MetaOapg.properties.chat_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creation_time"]) -> MetaOapg.properties.creation_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chat_name"]) -> MetaOapg.properties.chat_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["chat_id", "user_id", "creation_time", "chat_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chat_id"]) -> MetaOapg.properties.chat_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creation_time"]) -> MetaOapg.properties.creation_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chat_name"]) -> MetaOapg.properties.chat_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["chat_id", "user_id", "creation_time", "chat_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChatNullable':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
