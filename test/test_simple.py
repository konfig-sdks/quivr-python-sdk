# coding: utf-8

"""
    FastAPI

    Open-source RAG Framework

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from quivr_python_sdk import Quivr

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        quivr = Quivr(
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(quivr)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
