# coding: utf-8

"""
    FastAPI

    Open-source RAG Framework

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredCrawlWebsite(TypedDict):
    url: str

class OptionalCrawlWebsite(TypedDict, total=False):
    js: bool

    depth: int

    max_pages: int

    max_time: int

class CrawlWebsite(RequiredCrawlWebsite, OptionalCrawlWebsite):
    pass
