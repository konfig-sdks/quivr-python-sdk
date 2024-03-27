# coding: utf-8
"""
    FastAPI

    Open-source RAG Framework

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from quivr_python_sdk.client_custom import ClientCustom
from quivr_python_sdk.configuration import Configuration
from quivr_python_sdk.api_client import ApiClient
from quivr_python_sdk.type_util import copy_signature
from quivr_python_sdk.apis.tags.api_key_api import APIKeyApi
from quivr_python_sdk.apis.tags.brain_api import BrainApi
from quivr_python_sdk.apis.tags.brain_subscription_api import BrainSubscriptionApi
from quivr_python_sdk.apis.tags.chat_api import ChatApi
from quivr_python_sdk.apis.tags.contact_api import ContactApi
from quivr_python_sdk.apis.tags.crawl_api import CrawlApi
from quivr_python_sdk.apis.tags.health_api import HealthApi
from quivr_python_sdk.apis.tags.knowledge_api import KnowledgeApi
from quivr_python_sdk.apis.tags.notification_api import NotificationApi
from quivr_python_sdk.apis.tags.onboarding_api import OnboardingApi
from quivr_python_sdk.apis.tags.prompt_api import PromptApi
from quivr_python_sdk.apis.tags.root_api import RootApi
from quivr_python_sdk.apis.tags.subscription_api import SubscriptionApi
from quivr_python_sdk.apis.tags.upload_api import UploadApi
from quivr_python_sdk.apis.tags.user_api import UserApi



class Quivr(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.api_key: APIKeyApi = APIKeyApi(api_client)
        self.brain: BrainApi = BrainApi(api_client)
        self.brain_subscription: BrainSubscriptionApi = BrainSubscriptionApi(api_client)
        self.chat: ChatApi = ChatApi(api_client)
        self.contact: ContactApi = ContactApi(api_client)
        self.crawl: CrawlApi = CrawlApi(api_client)
        self.health: HealthApi = HealthApi(api_client)
        self.knowledge: KnowledgeApi = KnowledgeApi(api_client)
        self.notification: NotificationApi = NotificationApi(api_client)
        self.onboarding: OnboardingApi = OnboardingApi(api_client)
        self.prompt: PromptApi = PromptApi(api_client)
        self.root: RootApi = RootApi(api_client)
        self.subscription: SubscriptionApi = SubscriptionApi(api_client)
        self.upload: UploadApi = UploadApi(api_client)
        self.user: UserApi = UserApi(api_client)