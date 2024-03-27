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


class BrainGetDescriptionResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['IntegrationDescriptionEntity']:
            return IntegrationDescriptionEntity

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['IntegrationDescriptionEntity'], typing.List['IntegrationDescriptionEntity']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'BrainGetDescriptionResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'IntegrationDescriptionEntity':
        return super().__getitem__(i)

from quivr_python_sdk.model.integration_description_entity import IntegrationDescriptionEntity
