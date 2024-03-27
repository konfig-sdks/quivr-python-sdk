# coding: utf-8

"""
    FastAPI

    Open-source RAG Framework

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from quivr_python_sdk.paths.knowledge_knowledge_id.delete import DeleteSpecificBrainKnowledgeRaw
from quivr_python_sdk.paths.knowledge_knowledge_id_signed_download_url.get import GenerateSignedUrlRaw
from quivr_python_sdk.paths.knowledge.get import GetAllKnowledgeRaw


class KnowledgeApiRaw(
    DeleteSpecificBrainKnowledgeRaw,
    GenerateSignedUrlRaw,
    GetAllKnowledgeRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
