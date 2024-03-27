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


class ApiBrainDefinitionSchema(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class properties(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ApiBrainDefinitionSchemaProperty']:
                        return ApiBrainDefinitionSchemaProperty
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ApiBrainDefinitionSchemaProperty'], typing.List['ApiBrainDefinitionSchemaProperty']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'properties':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ApiBrainDefinitionSchemaProperty':
                    return super().__getitem__(i)
        
            @staticmethod
            def required() -> typing.Type['ApiBrainDefinitionSchemaRequired']:
                return ApiBrainDefinitionSchemaRequired
            __annotations__ = {
                "properties": properties,
                "required": required,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> MetaOapg.properties.properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> 'ApiBrainDefinitionSchemaRequired': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["properties", "required", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> typing.Union[MetaOapg.properties.properties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> typing.Union['ApiBrainDefinitionSchemaRequired', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["properties", "required", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        properties: typing.Union[MetaOapg.properties.properties, list, tuple, schemas.Unset] = schemas.unset,
        required: typing.Union['ApiBrainDefinitionSchemaRequired', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiBrainDefinitionSchema':
        return super().__new__(
            cls,
            *args,
            properties=properties,
            required=required,
            _configuration=_configuration,
            **kwargs,
        )

from quivr_python_sdk.model.api_brain_definition_schema_property import ApiBrainDefinitionSchemaProperty
from quivr_python_sdk.model.api_brain_definition_schema_required import ApiBrainDefinitionSchemaRequired