# coding: utf-8

"""
    FastAPI

    Open-source RAG Framework

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from quivr_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from quivr_python_sdk.api_response import AsyncGeneratorResponse
from quivr_python_sdk import api_client, exceptions
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

from quivr_python_sdk.model.create_api_brain_definition_nullable import CreateApiBrainDefinitionNullable as CreateApiBrainDefinitionNullableSchema
from quivr_python_sdk.model.brain_type_nullable import BrainTypeNullable as BrainTypeNullableSchema
from quivr_python_sdk.model.create_brain_properties_connected_brains_ids import CreateBrainPropertiesConnectedBrainsIds as CreateBrainPropertiesConnectedBrainsIdsSchema
from quivr_python_sdk.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from quivr_python_sdk.model.create_brain_properties import CreateBrainProperties as CreateBrainPropertiesSchema
from quivr_python_sdk.model.brain_integration_settings_nullable import BrainIntegrationSettingsNullable as BrainIntegrationSettingsNullableSchema

from quivr_python_sdk.type.create_api_brain_definition_nullable import CreateApiBrainDefinitionNullable
from quivr_python_sdk.type.brain_type_nullable import BrainTypeNullable
from quivr_python_sdk.type.brain_integration_settings_nullable import BrainIntegrationSettingsNullable
from quivr_python_sdk.type.http_validation_error import HTTPValidationError
from quivr_python_sdk.type.create_brain_properties_connected_brains_ids import CreateBrainPropertiesConnectedBrainsIds
from quivr_python_sdk.type.create_brain_properties import CreateBrainProperties

from ...api_client import Dictionary
from quivr_python_sdk.pydantic.create_brain_properties import CreateBrainProperties as CreateBrainPropertiesPydantic
from quivr_python_sdk.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic
from quivr_python_sdk.pydantic.brain_type_nullable import BrainTypeNullable as BrainTypeNullablePydantic
from quivr_python_sdk.pydantic.create_api_brain_definition_nullable import CreateApiBrainDefinitionNullable as CreateApiBrainDefinitionNullablePydantic
from quivr_python_sdk.pydantic.brain_integration_settings_nullable import BrainIntegrationSettingsNullable as BrainIntegrationSettingsNullablePydantic
from quivr_python_sdk.pydantic.create_brain_properties_connected_brains_ids import CreateBrainPropertiesConnectedBrainsIds as CreateBrainPropertiesConnectedBrainsIdsPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = CreateBrainPropertiesSchema


request_body_create_brain_properties = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'AuthBearer',
]
SchemaFor200ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationErrorSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: HTTPValidationError


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: HTTPValidationError


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_brain_mapped_args(
        self,
        description: typing.Optional[str] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[typing.Optional[str]] = None,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_type: typing.Optional[BrainTypeNullable] = None,
        brain_definition: typing.Optional[CreateApiBrainDefinitionNullable] = None,
        brain_secrets_values: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        connected_brains_ids: typing.Optional[CreateBrainPropertiesConnectedBrainsIds] = None,
        integration: typing.Optional[BrainIntegrationSettingsNullable] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if status is not None:
            _body["status"] = status
        if model is not None:
            _body["model"] = model
        if temperature is not None:
            _body["temperature"] = temperature
        if max_tokens is not None:
            _body["max_tokens"] = max_tokens
        if prompt_id is not None:
            _body["prompt_id"] = prompt_id
        if brain_type is not None:
            _body["brain_type"] = brain_type
        if brain_definition is not None:
            _body["brain_definition"] = brain_definition
        if brain_secrets_values is not None:
            _body["brain_secrets_values"] = brain_secrets_values
        if connected_brains_ids is not None:
            _body["connected_brains_ids"] = connected_brains_ids
        if integration is not None:
            _body["integration"] = integration
        args.body = _body
        return args

    async def _acreate_new_brain_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create New Brain
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/brains',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_brain_properties.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_new_brain_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create New Brain
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/brains',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_brain_properties.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateNewBrainRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_brain(
        self,
        description: typing.Optional[str] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[typing.Optional[str]] = None,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_type: typing.Optional[BrainTypeNullable] = None,
        brain_definition: typing.Optional[CreateApiBrainDefinitionNullable] = None,
        brain_secrets_values: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        connected_brains_ids: typing.Optional[CreateBrainPropertiesConnectedBrainsIds] = None,
        integration: typing.Optional[BrainIntegrationSettingsNullable] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_brain_mapped_args(
            description=description,
            name=name,
            status=status,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            prompt_id=prompt_id,
            brain_type=brain_type,
            brain_definition=brain_definition,
            brain_secrets_values=brain_secrets_values,
            connected_brains_ids=connected_brains_ids,
            integration=integration,
        )
        return await self._acreate_new_brain_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_brain(
        self,
        description: typing.Optional[str] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[typing.Optional[str]] = None,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_type: typing.Optional[BrainTypeNullable] = None,
        brain_definition: typing.Optional[CreateApiBrainDefinitionNullable] = None,
        brain_secrets_values: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        connected_brains_ids: typing.Optional[CreateBrainPropertiesConnectedBrainsIds] = None,
        integration: typing.Optional[BrainIntegrationSettingsNullable] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_brain_mapped_args(
            description=description,
            name=name,
            status=status,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            prompt_id=prompt_id,
            brain_type=brain_type,
            brain_definition=brain_definition,
            brain_secrets_values=brain_secrets_values,
            connected_brains_ids=connected_brains_ids,
            integration=integration,
        )
        return self._create_new_brain_oapg(
            body=args.body,
        )

class CreateNewBrain(BaseApi):

    async def acreate_new_brain(
        self,
        description: typing.Optional[str] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[typing.Optional[str]] = None,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_type: typing.Optional[BrainTypeNullable] = None,
        brain_definition: typing.Optional[CreateApiBrainDefinitionNullable] = None,
        brain_secrets_values: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        connected_brains_ids: typing.Optional[CreateBrainPropertiesConnectedBrainsIds] = None,
        integration: typing.Optional[BrainIntegrationSettingsNullable] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.acreate_new_brain(
            description=description,
            name=name,
            status=status,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            prompt_id=prompt_id,
            brain_type=brain_type,
            brain_definition=brain_definition,
            brain_secrets_values=brain_secrets_values,
            connected_brains_ids=connected_brains_ids,
            integration=integration,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def create_new_brain(
        self,
        description: typing.Optional[str] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[typing.Optional[str]] = None,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_type: typing.Optional[BrainTypeNullable] = None,
        brain_definition: typing.Optional[CreateApiBrainDefinitionNullable] = None,
        brain_secrets_values: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        connected_brains_ids: typing.Optional[CreateBrainPropertiesConnectedBrainsIds] = None,
        integration: typing.Optional[BrainIntegrationSettingsNullable] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.create_new_brain(
            description=description,
            name=name,
            status=status,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            prompt_id=prompt_id,
            brain_type=brain_type,
            brain_definition=brain_definition,
            brain_secrets_values=brain_secrets_values,
            connected_brains_ids=connected_brains_ids,
            integration=integration,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        description: typing.Optional[str] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[typing.Optional[str]] = None,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_type: typing.Optional[BrainTypeNullable] = None,
        brain_definition: typing.Optional[CreateApiBrainDefinitionNullable] = None,
        brain_secrets_values: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        connected_brains_ids: typing.Optional[CreateBrainPropertiesConnectedBrainsIds] = None,
        integration: typing.Optional[BrainIntegrationSettingsNullable] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_brain_mapped_args(
            description=description,
            name=name,
            status=status,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            prompt_id=prompt_id,
            brain_type=brain_type,
            brain_definition=brain_definition,
            brain_secrets_values=brain_secrets_values,
            connected_brains_ids=connected_brains_ids,
            integration=integration,
        )
        return await self._acreate_new_brain_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        description: typing.Optional[str] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        status: typing.Optional[typing.Optional[str]] = None,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_type: typing.Optional[BrainTypeNullable] = None,
        brain_definition: typing.Optional[CreateApiBrainDefinitionNullable] = None,
        brain_secrets_values: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        connected_brains_ids: typing.Optional[CreateBrainPropertiesConnectedBrainsIds] = None,
        integration: typing.Optional[BrainIntegrationSettingsNullable] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_brain_mapped_args(
            description=description,
            name=name,
            status=status,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            prompt_id=prompt_id,
            brain_type=brain_type,
            brain_definition=brain_definition,
            brain_secrets_values=brain_secrets_values,
            connected_brains_ids=connected_brains_ids,
            integration=integration,
        )
        return self._create_new_brain_oapg(
            body=args.body,
        )

