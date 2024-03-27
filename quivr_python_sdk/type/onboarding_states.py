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


class RequiredOnboardingStates(TypedDict):
    onboarding_a: bool

    onboarding_b1: bool

    onboarding_b2: bool

    onboarding_b3: bool

class OptionalOnboardingStates(TypedDict, total=False):
    pass

class OnboardingStates(RequiredOnboardingStates, OptionalOnboardingStates):
    pass
