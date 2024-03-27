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

from quivr_python_sdk.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from quivr_python_sdk.model.chat_question import ChatQuestion as ChatQuestionSchema

from quivr_python_sdk.type.chat_question import ChatQuestion
from quivr_python_sdk.type.http_validation_error import HTTPValidationError

from ...api_client import Dictionary
from quivr_python_sdk.pydantic.chat_question import ChatQuestion as ChatQuestionPydantic
from quivr_python_sdk.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic

from . import path

# Query params


class BrainIdSchema(
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
    ) -> 'BrainIdSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'brain_id': typing.Union[BrainIdSchema, None, str, uuid.UUID, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_brain_id = api_client.QueryParameter(
    name="brain_id",
    style=api_client.ParameterStyle.FORM,
    schema=BrainIdSchema,
    explode=True,
)
# Path params
ChatIdSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'chat_id': typing.Union[ChatIdSchema, str, uuid.UUID, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_chat_id = api_client.PathParameter(
    name="chat_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ChatIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ChatQuestionSchema


request_body_chat_question = api_client.RequestBody(
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

    def _handle_question_mapped_args(
        self,
        question: str,
        chat_id: str,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if question is not None:
            _body["question"] = question
        if model is not None:
            _body["model"] = model
        if temperature is not None:
            _body["temperature"] = temperature
        if max_tokens is not None:
            _body["max_tokens"] = max_tokens
        if brain_id is not None:
            _body["brain_id"] = brain_id
        if prompt_id is not None:
            _body["prompt_id"] = prompt_id
        args.body = _body
        if brain_id is not None:
            _query_params["brain_id"] = brain_id
        if chat_id is not None:
            _path_params["chat_id"] = chat_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _ahandle_question_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Create Question Handler
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_chat_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_brain_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/chat/{chat_id}/question',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_chat_question.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _handle_question_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Create Question Handler
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_chat_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_brain_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/chat/{chat_id}/question',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_chat_question.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


class HandleQuestionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ahandle_question(
        self,
        question: str,
        chat_id: str,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._handle_question_mapped_args(
            question=question,
            chat_id=chat_id,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            brain_id=brain_id,
            prompt_id=prompt_id,
            brain_id=brain_id,
        )
        return await self._ahandle_question_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def handle_question(
        self,
        question: str,
        chat_id: str,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._handle_question_mapped_args(
            question=question,
            chat_id=chat_id,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            brain_id=brain_id,
            prompt_id=prompt_id,
            brain_id=brain_id,
        )
        return self._handle_question_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class HandleQuestion(BaseApi):

    async def ahandle_question(
        self,
        question: str,
        chat_id: str,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.ahandle_question(
            question=question,
            chat_id=chat_id,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            brain_id=brain_id,
            prompt_id=prompt_id,
            brain_id=brain_id,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def handle_question(
        self,
        question: str,
        chat_id: str,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.handle_question(
            question=question,
            chat_id=chat_id,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            brain_id=brain_id,
            prompt_id=prompt_id,
            brain_id=brain_id,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        question: str,
        chat_id: str,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._handle_question_mapped_args(
            question=question,
            chat_id=chat_id,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            brain_id=brain_id,
            prompt_id=prompt_id,
            brain_id=brain_id,
        )
        return await self._ahandle_question_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        question: str,
        chat_id: str,
        model: typing.Optional[typing.Optional[str]] = None,
        temperature: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        max_tokens: typing.Optional[typing.Optional[int]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
        prompt_id: typing.Optional[typing.Optional[str]] = None,
        brain_id: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._handle_question_mapped_args(
            question=question,
            chat_id=chat_id,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            brain_id=brain_id,
            prompt_id=prompt_id,
            brain_id=brain_id,
        )
        return self._handle_question_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )
