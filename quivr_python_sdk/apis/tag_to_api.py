import typing_extensions

from quivr_python_sdk.apis.tags import TagValues
from quivr_python_sdk.apis.tags.brain_api import BrainApi
from quivr_python_sdk.apis.tags.chat_api import ChatApi
from quivr_python_sdk.apis.tags.health_api import HealthApi
from quivr_python_sdk.apis.tags.prompt_api import PromptApi
from quivr_python_sdk.apis.tags.user_api import UserApi
from quivr_python_sdk.apis.tags.api_key_api import APIKeyApi
from quivr_python_sdk.apis.tags.knowledge_api import KnowledgeApi
from quivr_python_sdk.apis.tags.onboarding_api import OnboardingApi
from quivr_python_sdk.apis.tags.brain_subscription_api import BrainSubscriptionApi
from quivr_python_sdk.apis.tags.subscription_api import SubscriptionApi
from quivr_python_sdk.apis.tags.crawl_api import CrawlApi
from quivr_python_sdk.apis.tags.upload_api import UploadApi
from quivr_python_sdk.apis.tags.notification_api import NotificationApi
from quivr_python_sdk.apis.tags.root_api import RootApi
from quivr_python_sdk.apis.tags.contact_api import ContactApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BRAIN: BrainApi,
        TagValues.CHAT: ChatApi,
        TagValues.HEALTH: HealthApi,
        TagValues.PROMPT: PromptApi,
        TagValues.USER: UserApi,
        TagValues.API_KEY: APIKeyApi,
        TagValues.KNOWLEDGE: KnowledgeApi,
        TagValues.ONBOARDING: OnboardingApi,
        TagValues.BRAIN_SUBSCRIPTION: BrainSubscriptionApi,
        TagValues.SUBSCRIPTION: SubscriptionApi,
        TagValues.CRAWL: CrawlApi,
        TagValues.UPLOAD: UploadApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.ROOT: RootApi,
        TagValues.CONTACT: ContactApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BRAIN: BrainApi,
        TagValues.CHAT: ChatApi,
        TagValues.HEALTH: HealthApi,
        TagValues.PROMPT: PromptApi,
        TagValues.USER: UserApi,
        TagValues.API_KEY: APIKeyApi,
        TagValues.KNOWLEDGE: KnowledgeApi,
        TagValues.ONBOARDING: OnboardingApi,
        TagValues.BRAIN_SUBSCRIPTION: BrainSubscriptionApi,
        TagValues.SUBSCRIPTION: SubscriptionApi,
        TagValues.CRAWL: CrawlApi,
        TagValues.UPLOAD: UploadApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.ROOT: RootApi,
        TagValues.CONTACT: ContactApi,
    }
)
