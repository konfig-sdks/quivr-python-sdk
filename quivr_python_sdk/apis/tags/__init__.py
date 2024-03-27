# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from quivr_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    BRAIN = "Brain"
    CHAT = "Chat"
    HEALTH = "Health"
    PROMPT = "Prompt"
    USER = "User"
    API_KEY = "API Key"
    KNOWLEDGE = "Knowledge"
    ONBOARDING = "Onboarding"
    BRAIN_SUBSCRIPTION = "BrainSubscription"
    SUBSCRIPTION = "Subscription"
    CRAWL = "Crawl"
    UPLOAD = "Upload"
    NOTIFICATION = "Notification"
    ROOT = "Root"
    CONTACT = "Contact"
