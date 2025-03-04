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


class QuestionAndAnswer(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "answer",
            "question",
        }
        
        class properties:
            question = schemas.StrSchema
            answer = schemas.StrSchema
            __annotations__ = {
                "question": question,
                "answer": answer,
            }
    
    answer: MetaOapg.properties.answer
    question: MetaOapg.properties.question
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["question"]) -> MetaOapg.properties.question: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer"]) -> MetaOapg.properties.answer: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["question", "answer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["question"]) -> MetaOapg.properties.question: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer"]) -> MetaOapg.properties.answer: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["question", "answer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        answer: typing.Union[MetaOapg.properties.answer, str, ],
        question: typing.Union[MetaOapg.properties.question, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'QuestionAndAnswer':
        return super().__new__(
            cls,
            *args,
            answer=answer,
            question=question,
            _configuration=_configuration,
            **kwargs,
        )
