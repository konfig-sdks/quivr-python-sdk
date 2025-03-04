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


class ChatQuestion(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "question",
        }
        
        class properties:
            question = schemas.StrSchema
            
            
            class model(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'model':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class temperature(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'temperature':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class max_tokens(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'max_tokens':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class brain_id(
                schemas.UUIDBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uuid'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, uuid.UUID, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'brain_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class prompt_id(
                schemas.UUIDBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uuid'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, uuid.UUID, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'prompt_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "question": question,
                "model": model,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "brain_id": brain_id,
                "prompt_id": prompt_id,
            }
    
    question: MetaOapg.properties.question
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["question"]) -> MetaOapg.properties.question: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temperature"]) -> MetaOapg.properties.temperature: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_tokens"]) -> MetaOapg.properties.max_tokens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brain_id"]) -> MetaOapg.properties.brain_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompt_id"]) -> MetaOapg.properties.prompt_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["question", "model", "temperature", "max_tokens", "brain_id", "prompt_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["question"]) -> MetaOapg.properties.question: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> typing.Union[MetaOapg.properties.model, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temperature"]) -> typing.Union[MetaOapg.properties.temperature, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_tokens"]) -> typing.Union[MetaOapg.properties.max_tokens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brain_id"]) -> typing.Union[MetaOapg.properties.brain_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompt_id"]) -> typing.Union[MetaOapg.properties.prompt_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["question", "model", "temperature", "max_tokens", "brain_id", "prompt_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        question: typing.Union[MetaOapg.properties.question, str, ],
        model: typing.Union[MetaOapg.properties.model, None, str, schemas.Unset] = schemas.unset,
        temperature: typing.Union[MetaOapg.properties.temperature, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        max_tokens: typing.Union[MetaOapg.properties.max_tokens, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        brain_id: typing.Union[MetaOapg.properties.brain_id, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        prompt_id: typing.Union[MetaOapg.properties.prompt_id, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChatQuestion':
        return super().__new__(
            cls,
            *args,
            question=question,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            brain_id=brain_id,
            prompt_id=prompt_id,
            _configuration=_configuration,
            **kwargs,
        )
