# coding: utf-8

"""
    FastAPI

    Open-source RAG Framework

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from quivr_python_sdk.paths.knowledge_knowledge_id.delete import DeleteSpecificBrainKnowledge
from quivr_python_sdk.paths.knowledge_knowledge_id_signed_download_url.get import GenerateSignedUrl
from quivr_python_sdk.paths.knowledge.get import GetAllKnowledge
from quivr_python_sdk.apis.tags.knowledge_api_raw import KnowledgeApiRaw


class KnowledgeApi(
    DeleteSpecificBrainKnowledge,
    GenerateSignedUrl,
    GetAllKnowledge,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: KnowledgeApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = KnowledgeApiRaw(api_client)
