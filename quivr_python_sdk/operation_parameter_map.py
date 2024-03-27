operation_parameter_map = {
    '/api-key-POST': {
        'parameters': [
        ]
    },
    '/api-key/{key_id}-DELETE': {
        'parameters': [
            {
                'name': 'key_id'
            },
        ]
    },
    '/api-keys-GET': {
        'parameters': [
        ]
    },
    '/brains/{brain_id}/subscription/accept-POST': {
        'parameters': [
            {
                'name': 'brain_id'
            },
        ]
    },
    '/brains-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'model'
            },
            {
                'name': 'temperature'
            },
            {
                'name': 'max_tokens'
            },
            {
                'name': 'prompt_id'
            },
            {
                'name': 'brain_type'
            },
            {
                'name': 'brain_definition'
            },
            {
                'name': 'brain_secrets_values'
            },
            {
                'name': 'connected_brains_ids'
            },
            {
                'name': 'integration'
            },
        ]
    },
    '/brains/{brain_id}/subscription/decline-POST': {
        'parameters': [
            {
                'name': 'brain_id'
            },
        ]
    },
    '/brains-GET': {
        'parameters': [
        ]
    },
    '/brains/public-GET': {
        'parameters': [
        ]
    },
    '/brains/{brain_id}-GET': {
        'parameters': [
            {
                'name': 'brain_id'
            },
        ]
    },
    '/brains/default-GET': {
        'parameters': [
        ]
    },
    '/brains/integrations-GET': {
        'parameters': [
        ]
    },
    '/brains/{brain_id}/documents-POST': {
        'parameters': [
            {
                'name': 'question'
            },
            {
                'name': 'brain_id'
            },
        ]
    },
    '/brains/{brain_id}/users-GET': {
        'parameters': [
            {
                'name': 'brain_id'
            },
        ]
    },
    '/brains/{brain_id}/subscription-DELETE': {
        'parameters': [
            {
                'name': 'brain_id'
            },
        ]
    },
    '/brains/{brain_id}/default-POST': {
        'parameters': [
            {
                'name': 'brain_id'
            },
        ]
    },
    '/brains/{brain_id}-PUT': {
        'parameters': [
            {
                'name': 'brain_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'temperature'
            },
            {
                'name': 'model'
            },
            {
                'name': 'max_tokens'
            },
            {
                'name': 'status'
            },
            {
                'name': 'prompt_id'
            },
            {
                'name': 'brain_definition'
            },
            {
                'name': 'connected_brains_ids'
            },
            {
                'name': 'integration'
            },
        ]
    },
    '/brains/{brain_id}/secrets-values-PUT': {
        'parameters': [
            {
                'name': 'brain_id'
            },
        ]
    },
    '/brains/{brain_id}/subscription-PUT': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'brain_id'
            },
            {
                'name': 'rights'
            },
        ]
    },
    '/brains/{brain_id}/subscription-GET': {
        'parameters': [
            {
                'name': 'brain_id'
            },
        ]
    },
    '/brains/{brain_id}/subscription-POST': {
        'parameters': [
            {
                'name': 'brain_id'
            },
            {
                'name': 'origin'
            },
        ]
    },
    '/chat/{chat_id}/question/answer-POST': {
        'parameters': [
            {
                'name': 'question'
            },
            {
                'name': 'answer'
            },
            {
                'name': 'chat_id'
            },
        ]
    },
    '/chat-POST': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/chat/{chat_id}/question/stream-POST': {
        'parameters': [
            {
                'name': 'question'
            },
            {
                'name': 'chat_id'
            },
            {
                'name': 'model'
            },
            {
                'name': 'temperature'
            },
            {
                'name': 'max_tokens'
            },
            {
                'name': 'brain_id'
            },
            {
                'name': 'prompt_id'
            },
            {
                'name': 'brain_id'
            },
        ]
    },
    '/chat/{chat_id}-DELETE': {
        'parameters': [
            {
                'name': 'chat_id'
            },
        ]
    },
    '/chat-GET': {
        'parameters': [
        ]
    },
    '/chat/{chat_id}/history-GET': {
        'parameters': [
            {
                'name': 'chat_id'
            },
        ]
    },
    '/chat/{chat_id}/question-POST': {
        'parameters': [
            {
                'name': 'question'
            },
            {
                'name': 'chat_id'
            },
            {
                'name': 'model'
            },
            {
                'name': 'temperature'
            },
            {
                'name': 'max_tokens'
            },
            {
                'name': 'brain_id'
            },
            {
                'name': 'prompt_id'
            },
            {
                'name': 'brain_id'
            },
        ]
    },
    '/chat/{chat_id}/{message_id}-PUT': {
        'parameters': [
            {
                'name': 'thumbs'
            },
            {
                'name': 'chat_id'
            },
            {
                'name': 'message_id'
            },
        ]
    },
    '/chat/{chat_id}/metadata-PUT': {
        'parameters': [
            {
                'name': 'chat_id'
            },
            {
                'name': 'chat_name'
            },
        ]
    },
    '/contact-POST': {
        'parameters': [
            {
                'name': 'customer_email'
            },
            {
                'name': 'content'
            },
        ]
    },
    '/crawl-POST': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'brain_id'
            },
            {
                'name': 'js'
            },
            {
                'name': 'depth'
            },
            {
                'name': 'max_pages'
            },
            {
                'name': 'max_time'
            },
            {
                'name': 'chat_id'
            },
        ]
    },
    '/chat/healthz-GET': {
        'parameters': [
        ]
    },
    '/crawl/healthz-GET': {
        'parameters': [
        ]
    },
    '/healthz-GET': {
        'parameters': [
        ]
    },
    '/upload/healthz-GET': {
        'parameters': [
        ]
    },
    '/knowledge/{knowledge_id}-DELETE': {
        'parameters': [
            {
                'name': 'knowledge_id'
            },
            {
                'name': 'brain_id'
            },
        ]
    },
    '/knowledge/{knowledge_id}/signed_download_url-GET': {
        'parameters': [
            {
                'name': 'knowledge_id'
            },
        ]
    },
    '/knowledge-GET': {
        'parameters': [
            {
                'name': 'brain_id'
            },
        ]
    },
    '/notifications/{chat_id}-GET': {
        'parameters': [
            {
                'name': 'chat_id'
            },
        ]
    },
    '/onboarding-GET': {
        'parameters': [
        ]
    },
    '/onboarding-PUT': {
        'parameters': [
            {
                'name': 'onboarding_a'
            },
            {
                'name': 'onboarding_b1'
            },
            {
                'name': 'onboarding_b2'
            },
            {
                'name': 'onboarding_b3'
            },
        ]
    },
    '/prompts-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'content'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/prompts-GET': {
        'parameters': [
        ]
    },
    '/prompts/{prompt_id}-GET': {
        'parameters': [
            {
                'name': 'prompt_id'
            },
        ]
    },
    '/prompts/{prompt_id}-PUT': {
        'parameters': [
            {
                'name': 'prompt_id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'content'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/-GET': {
        'parameters': [
        ]
    },
    '/brains/{brain_id}/subscribe-POST': {
        'parameters': [
            {
                'name': 'brain_id'
            },
        ]
    },
    '/brains/{brain_id}/unsubscribe-POST': {
        'parameters': [
            {
                'name': 'brain_id'
            },
        ]
    },
    '/upload-POST': {
        'parameters': [
            {
                'name': 'brain_id'
            },
            {
                'name': 'uploadFile'
            },
            {
                'name': 'chat_id'
            },
        ]
    },
    '/user/identity-GET': {
        'parameters': [
        ]
    },
    '/user-GET': {
        'parameters': [
        ]
    },
    '/user/identity-PUT': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'company'
            },
            {
                'name': 'onboarded'
            },
            {
                'name': 'company_size'
            },
            {
                'name': 'usage_purpose'
            },
        ]
    },
};