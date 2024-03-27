import typing_extensions

from quivr_python_sdk.paths import PathValues
from quivr_python_sdk.apis.paths.brains_public import BrainsPublic
from quivr_python_sdk.apis.paths.brains_brain_id_secrets_values import BrainsBrainIdSecretsValues
from quivr_python_sdk.apis.paths.brains_brain_id_default import BrainsBrainIdDefault
from quivr_python_sdk.apis.paths.brains_brain_id_documents import BrainsBrainIdDocuments
from quivr_python_sdk.apis.paths.chat_healthz import ChatHealthz
from quivr_python_sdk.apis.paths.chat import Chat
from quivr_python_sdk.apis.paths.chat_chat_id import ChatChatId
from quivr_python_sdk.apis.paths.chat_chat_id_metadata import ChatChatIdMetadata
from quivr_python_sdk.apis.paths.chat_chat_id_message_id import ChatChatIdMessageId
from quivr_python_sdk.apis.paths.chat_chat_id_question import ChatChatIdQuestion
from quivr_python_sdk.apis.paths.chat_chat_id_question_stream import ChatChatIdQuestionStream
from quivr_python_sdk.apis.paths.chat_chat_id_history import ChatChatIdHistory
from quivr_python_sdk.apis.paths.chat_chat_id_question_answer import ChatChatIdQuestionAnswer
from quivr_python_sdk.apis.paths.crawl_healthz import CrawlHealthz
from quivr_python_sdk.apis.paths.crawl import Crawl
from quivr_python_sdk.apis.paths.onboarding import Onboarding
from quivr_python_sdk.apis.paths.root import Root
from quivr_python_sdk.apis.paths.healthz import Healthz
from quivr_python_sdk.apis.paths.upload_healthz import UploadHealthz
from quivr_python_sdk.apis.paths.upload import Upload
from quivr_python_sdk.apis.paths.user import User
from quivr_python_sdk.apis.paths.user_identity import UserIdentity
from quivr_python_sdk.apis.paths.api_key import ApiKey
from quivr_python_sdk.apis.paths.api_key_key_id import ApiKeyKeyId
from quivr_python_sdk.apis.paths.api_keys import ApiKeys
from quivr_python_sdk.apis.paths.brains_brain_id_subscription import BrainsBrainIdSubscription
from quivr_python_sdk.apis.paths.brains_brain_id_users import BrainsBrainIdUsers
from quivr_python_sdk.apis.paths.brains_brain_id_subscription_accept import BrainsBrainIdSubscriptionAccept
from quivr_python_sdk.apis.paths.brains_brain_id_subscription_decline import BrainsBrainIdSubscriptionDecline
from quivr_python_sdk.apis.paths.brains_brain_id_subscribe import BrainsBrainIdSubscribe
from quivr_python_sdk.apis.paths.brains_brain_id_unsubscribe import BrainsBrainIdUnsubscribe
from quivr_python_sdk.apis.paths.prompts import Prompts
from quivr_python_sdk.apis.paths.prompts_prompt_id import PromptsPromptId
from quivr_python_sdk.apis.paths.notifications_chat_id import NotificationsChatId
from quivr_python_sdk.apis.paths.knowledge import Knowledge
from quivr_python_sdk.apis.paths.knowledge_knowledge_id import KnowledgeKnowledgeId
from quivr_python_sdk.apis.paths.knowledge_knowledge_id_signed_download_url import KnowledgeKnowledgeIdSignedDownloadUrl
from quivr_python_sdk.apis.paths.contact import Contact
from quivr_python_sdk.apis.paths.brains_integrations import BrainsIntegrations
from quivr_python_sdk.apis.paths.brains import Brains
from quivr_python_sdk.apis.paths.brains_default import BrainsDefault
from quivr_python_sdk.apis.paths.brains_brain_id import BrainsBrainId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.BRAINS_PUBLIC: BrainsPublic,
        PathValues.BRAINS_BRAIN_ID_SECRETSVALUES: BrainsBrainIdSecretsValues,
        PathValues.BRAINS_BRAIN_ID_DEFAULT: BrainsBrainIdDefault,
        PathValues.BRAINS_BRAIN_ID_DOCUMENTS: BrainsBrainIdDocuments,
        PathValues.CHAT_HEALTHZ: ChatHealthz,
        PathValues.CHAT: Chat,
        PathValues.CHAT_CHAT_ID: ChatChatId,
        PathValues.CHAT_CHAT_ID_METADATA: ChatChatIdMetadata,
        PathValues.CHAT_CHAT_ID_MESSAGE_ID: ChatChatIdMessageId,
        PathValues.CHAT_CHAT_ID_QUESTION: ChatChatIdQuestion,
        PathValues.CHAT_CHAT_ID_QUESTION_STREAM: ChatChatIdQuestionStream,
        PathValues.CHAT_CHAT_ID_HISTORY: ChatChatIdHistory,
        PathValues.CHAT_CHAT_ID_QUESTION_ANSWER: ChatChatIdQuestionAnswer,
        PathValues.CRAWL_HEALTHZ: CrawlHealthz,
        PathValues.CRAWL: Crawl,
        PathValues.ONBOARDING: Onboarding,
        PathValues._: Root,
        PathValues.HEALTHZ: Healthz,
        PathValues.UPLOAD_HEALTHZ: UploadHealthz,
        PathValues.UPLOAD: Upload,
        PathValues.USER: User,
        PathValues.USER_IDENTITY: UserIdentity,
        PathValues.APIKEY: ApiKey,
        PathValues.APIKEY_KEY_ID: ApiKeyKeyId,
        PathValues.APIKEYS: ApiKeys,
        PathValues.BRAINS_BRAIN_ID_SUBSCRIPTION: BrainsBrainIdSubscription,
        PathValues.BRAINS_BRAIN_ID_USERS: BrainsBrainIdUsers,
        PathValues.BRAINS_BRAIN_ID_SUBSCRIPTION_ACCEPT: BrainsBrainIdSubscriptionAccept,
        PathValues.BRAINS_BRAIN_ID_SUBSCRIPTION_DECLINE: BrainsBrainIdSubscriptionDecline,
        PathValues.BRAINS_BRAIN_ID_SUBSCRIBE: BrainsBrainIdSubscribe,
        PathValues.BRAINS_BRAIN_ID_UNSUBSCRIBE: BrainsBrainIdUnsubscribe,
        PathValues.PROMPTS: Prompts,
        PathValues.PROMPTS_PROMPT_ID: PromptsPromptId,
        PathValues.NOTIFICATIONS_CHAT_ID: NotificationsChatId,
        PathValues.KNOWLEDGE: Knowledge,
        PathValues.KNOWLEDGE_KNOWLEDGE_ID: KnowledgeKnowledgeId,
        PathValues.KNOWLEDGE_KNOWLEDGE_ID_SIGNED_DOWNLOAD_URL: KnowledgeKnowledgeIdSignedDownloadUrl,
        PathValues.CONTACT: Contact,
        PathValues.BRAINS_INTEGRATIONS: BrainsIntegrations,
        PathValues.BRAINS: Brains,
        PathValues.BRAINS_DEFAULT: BrainsDefault,
        PathValues.BRAINS_BRAIN_ID: BrainsBrainId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.BRAINS_PUBLIC: BrainsPublic,
        PathValues.BRAINS_BRAIN_ID_SECRETSVALUES: BrainsBrainIdSecretsValues,
        PathValues.BRAINS_BRAIN_ID_DEFAULT: BrainsBrainIdDefault,
        PathValues.BRAINS_BRAIN_ID_DOCUMENTS: BrainsBrainIdDocuments,
        PathValues.CHAT_HEALTHZ: ChatHealthz,
        PathValues.CHAT: Chat,
        PathValues.CHAT_CHAT_ID: ChatChatId,
        PathValues.CHAT_CHAT_ID_METADATA: ChatChatIdMetadata,
        PathValues.CHAT_CHAT_ID_MESSAGE_ID: ChatChatIdMessageId,
        PathValues.CHAT_CHAT_ID_QUESTION: ChatChatIdQuestion,
        PathValues.CHAT_CHAT_ID_QUESTION_STREAM: ChatChatIdQuestionStream,
        PathValues.CHAT_CHAT_ID_HISTORY: ChatChatIdHistory,
        PathValues.CHAT_CHAT_ID_QUESTION_ANSWER: ChatChatIdQuestionAnswer,
        PathValues.CRAWL_HEALTHZ: CrawlHealthz,
        PathValues.CRAWL: Crawl,
        PathValues.ONBOARDING: Onboarding,
        PathValues._: Root,
        PathValues.HEALTHZ: Healthz,
        PathValues.UPLOAD_HEALTHZ: UploadHealthz,
        PathValues.UPLOAD: Upload,
        PathValues.USER: User,
        PathValues.USER_IDENTITY: UserIdentity,
        PathValues.APIKEY: ApiKey,
        PathValues.APIKEY_KEY_ID: ApiKeyKeyId,
        PathValues.APIKEYS: ApiKeys,
        PathValues.BRAINS_BRAIN_ID_SUBSCRIPTION: BrainsBrainIdSubscription,
        PathValues.BRAINS_BRAIN_ID_USERS: BrainsBrainIdUsers,
        PathValues.BRAINS_BRAIN_ID_SUBSCRIPTION_ACCEPT: BrainsBrainIdSubscriptionAccept,
        PathValues.BRAINS_BRAIN_ID_SUBSCRIPTION_DECLINE: BrainsBrainIdSubscriptionDecline,
        PathValues.BRAINS_BRAIN_ID_SUBSCRIBE: BrainsBrainIdSubscribe,
        PathValues.BRAINS_BRAIN_ID_UNSUBSCRIBE: BrainsBrainIdUnsubscribe,
        PathValues.PROMPTS: Prompts,
        PathValues.PROMPTS_PROMPT_ID: PromptsPromptId,
        PathValues.NOTIFICATIONS_CHAT_ID: NotificationsChatId,
        PathValues.KNOWLEDGE: Knowledge,
        PathValues.KNOWLEDGE_KNOWLEDGE_ID: KnowledgeKnowledgeId,
        PathValues.KNOWLEDGE_KNOWLEDGE_ID_SIGNED_DOWNLOAD_URL: KnowledgeKnowledgeIdSignedDownloadUrl,
        PathValues.CONTACT: Contact,
        PathValues.BRAINS_INTEGRATIONS: BrainsIntegrations,
        PathValues.BRAINS: Brains,
        PathValues.BRAINS_DEFAULT: BrainsDefault,
        PathValues.BRAINS_BRAIN_ID: BrainsBrainId,
    }
)
