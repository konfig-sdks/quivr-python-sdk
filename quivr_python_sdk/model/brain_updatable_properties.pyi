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


class BrainUpdatableProperties(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
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
            
            
            class status(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'status':
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
        
            @staticmethod
            def brain_definition() -> typing.Type['ApiBrainDefinitionEntityInputNullable']:
                return ApiBrainDefinitionEntityInputNullable
        
            @staticmethod
            def connected_brains_ids() -> typing.Type['BrainUpdatablePropertiesConnectedBrainsIds']:
                return BrainUpdatablePropertiesConnectedBrainsIds
        
            @staticmethod
            def integration() -> typing.Type['BrainIntegrationUpdateSettingsNullable']:
                return BrainIntegrationUpdateSettingsNullable
            __annotations__ = {
                "description": description,
                "name": name,
                "temperature": temperature,
                "model": model,
                "max_tokens": max_tokens,
                "status": status,
                "prompt_id": prompt_id,
                "brain_definition": brain_definition,
                "connected_brains_ids": connected_brains_ids,
                "integration": integration,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temperature"]) -> MetaOapg.properties.temperature: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_tokens"]) -> MetaOapg.properties.max_tokens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompt_id"]) -> MetaOapg.properties.prompt_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brain_definition"]) -> 'ApiBrainDefinitionEntityInputNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connected_brains_ids"]) -> 'BrainUpdatablePropertiesConnectedBrainsIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["integration"]) -> 'BrainIntegrationUpdateSettingsNullable': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "name", "temperature", "model", "max_tokens", "status", "prompt_id", "brain_definition", "connected_brains_ids", "integration", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temperature"]) -> typing.Union[MetaOapg.properties.temperature, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> typing.Union[MetaOapg.properties.model, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_tokens"]) -> typing.Union[MetaOapg.properties.max_tokens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompt_id"]) -> typing.Union[MetaOapg.properties.prompt_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brain_definition"]) -> typing.Union['ApiBrainDefinitionEntityInputNullable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connected_brains_ids"]) -> typing.Union['BrainUpdatablePropertiesConnectedBrainsIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["integration"]) -> typing.Union['BrainIntegrationUpdateSettingsNullable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "name", "temperature", "model", "max_tokens", "status", "prompt_id", "brain_definition", "connected_brains_ids", "integration", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        temperature: typing.Union[MetaOapg.properties.temperature, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        model: typing.Union[MetaOapg.properties.model, None, str, schemas.Unset] = schemas.unset,
        max_tokens: typing.Union[MetaOapg.properties.max_tokens, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, None, str, schemas.Unset] = schemas.unset,
        prompt_id: typing.Union[MetaOapg.properties.prompt_id, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        brain_definition: typing.Union['ApiBrainDefinitionEntityInputNullable', schemas.Unset] = schemas.unset,
        connected_brains_ids: typing.Union['BrainUpdatablePropertiesConnectedBrainsIds', schemas.Unset] = schemas.unset,
        integration: typing.Union['BrainIntegrationUpdateSettingsNullable', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BrainUpdatableProperties':
        return super().__new__(
            cls,
            *args,
            description=description,
            name=name,
            temperature=temperature,
            model=model,
            max_tokens=max_tokens,
            status=status,
            prompt_id=prompt_id,
            brain_definition=brain_definition,
            connected_brains_ids=connected_brains_ids,
            integration=integration,
            _configuration=_configuration,
            **kwargs,
        )

from quivr_python_sdk.model.api_brain_definition_entity_input_nullable import ApiBrainDefinitionEntityInputNullable
from quivr_python_sdk.model.brain_integration_update_settings_nullable import BrainIntegrationUpdateSettingsNullable
from quivr_python_sdk.model.brain_updatable_properties_connected_brains_ids import BrainUpdatablePropertiesConnectedBrainsIds