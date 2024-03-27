# coding: utf-8

"""
    FastAPI

    Open-source RAG Framework

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import quivr_python_sdk
from quivr_python_sdk.paths.healthz import get
from quivr_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestHealthz(ApiTestMixin, unittest.TestCase):
    """
    Healthz unit test stubs
        Healthz
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
