# coding: utf-8

"""
    FastAPI

    Open-source RAG Framework

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from quivr_python_sdk.paths.chat_chat_id_question_answer.post import AddQuestionAndAnswer
from quivr_python_sdk.paths.chat.post import CreateHandler
from quivr_python_sdk.paths.chat_chat_id_question_stream.post import CreateStreamQuestionHandler
from quivr_python_sdk.paths.chat_chat_id.delete import DeleteChatById
from quivr_python_sdk.paths.chat.get import GetAllChats
from quivr_python_sdk.paths.chat_chat_id_history.get import GetHistory
from quivr_python_sdk.paths.chat_chat_id_question.post import HandleQuestion
from quivr_python_sdk.paths.chat_chat_id_message_id.put import UpdateMessage
from quivr_python_sdk.paths.chat_chat_id_metadata.put import UpdateMetadataHandler
from quivr_python_sdk.apis.tags.chat_api_raw import ChatApiRaw


class ChatApi(
    AddQuestionAndAnswer,
    CreateHandler,
    CreateStreamQuestionHandler,
    DeleteChatById,
    GetAllChats,
    GetHistory,
    HandleQuestion,
    UpdateMessage,
    UpdateMetadataHandler,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ChatApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ChatApiRaw(api_client)
