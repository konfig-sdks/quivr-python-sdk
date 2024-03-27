<div align="center">

[![Visit Quivr](./header.png)](https://quivr.app)

# Quivr<a id="quivr"></a>

Open-source RAG Framework


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`quivr.api_key.create_new_key`](#quivrapi_keycreate_new_key)
  * [`quivr.api_key.delete_key`](#quivrapi_keydelete_key)
  * [`quivr.api_key.get_list`](#quivrapi_keyget_list)
  * [`quivr.brain.accept_invitation`](#quivrbrainaccept_invitation)
  * [`quivr.brain.create_new_brain`](#quivrbraincreate_new_brain)
  * [`quivr.brain.decline_invitation`](#quivrbraindecline_invitation)
  * [`quivr.brain.get_all_for_user`](#quivrbrainget_all_for_user)
  * [`quivr.brain.get_all_public`](#quivrbrainget_all_public)
  * [`quivr.brain.get_by_id`](#quivrbrainget_by_id)
  * [`quivr.brain.get_default_brain`](#quivrbrainget_default_brain)
  * [`quivr.brain.get_description`](#quivrbrainget_description)
  * [`quivr.brain.get_question_context`](#quivrbrainget_question_context)
  * [`quivr.brain.get_users`](#quivrbrainget_users)
  * [`quivr.brain.remove_user_subscription`](#quivrbrainremove_user_subscription)
  * [`quivr.brain.set_default`](#quivrbrainset_default)
  * [`quivr.brain.update_configuration`](#quivrbrainupdate_configuration)
  * [`quivr.brain.update_secrets_values`](#quivrbrainupdate_secrets_values)
  * [`quivr.brain.update_subscription`](#quivrbrainupdate_subscription)
  * [`quivr.brain_subscription.get_user_invitation`](#quivrbrain_subscriptionget_user_invitation)
  * [`quivr.brain_subscription.invite_users_to_brain`](#quivrbrain_subscriptioninvite_users_to_brain)
  * [`quivr.chat.add_question_and_answer`](#quivrchatadd_question_and_answer)
  * [`quivr.chat.create_handler`](#quivrchatcreate_handler)
  * [`quivr.chat.create_stream_question_handler`](#quivrchatcreate_stream_question_handler)
  * [`quivr.chat.delete_chat_by_id`](#quivrchatdelete_chat_by_id)
  * [`quivr.chat.get_all_chats`](#quivrchatget_all_chats)
  * [`quivr.chat.get_history`](#quivrchatget_history)
  * [`quivr.chat.handle_question`](#quivrchathandle_question)
  * [`quivr.chat.update_message`](#quivrchatupdate_message)
  * [`quivr.chat.update_metadata_handler`](#quivrchatupdate_metadata_handler)
  * [`quivr.contact.create_new_contact`](#quivrcontactcreate_new_contact)
  * [`quivr.crawl.website_data_processor`](#quivrcrawlwebsite_data_processor)
  * [`quivr.health.check_status`](#quivrhealthcheck_status)
  * [`quivr.health.check_status_0`](#quivrhealthcheck_status_0)
  * [`quivr.health.check_status_1`](#quivrhealthcheck_status_1)
  * [`quivr.health.check_status_2`](#quivrhealthcheck_status_2)
  * [`quivr.knowledge.delete_specific_brain_knowledge`](#quivrknowledgedelete_specific_brain_knowledge)
  * [`quivr.knowledge.generate_signed_url`](#quivrknowledgegenerate_signed_url)
  * [`quivr.knowledge.get_all_knowledge`](#quivrknowledgeget_all_knowledge)
  * [`quivr.notification.get_by_chat_id`](#quivrnotificationget_by_chat_id)
  * [`quivr.onboarding.get_user_info`](#quivronboardingget_user_info)
  * [`quivr.onboarding.update_user_onboarding`](#quivronboardingupdate_user_onboarding)
  * [`quivr.prompt.create_prompt_by_id`](#quivrpromptcreate_prompt_by_id)
  * [`quivr.prompt.get_all_public_prompts`](#quivrpromptget_all_public_prompts)
  * [`quivr.prompt.get_by_id`](#quivrpromptget_by_id)
  * [`quivr.prompt.update_by_id`](#quivrpromptupdate_by_id)
  * [`quivr.root.status_check`](#quivrrootstatus_check)
  * [`quivr.subscription.brain_handler`](#quivrsubscriptionbrain_handler)
  * [`quivr.subscription.unregister_handler`](#quivrsubscriptionunregister_handler)
  * [`quivr.upload.file_post`](#quivruploadfile_post)
  * [`quivr.user.get_identity_route`](#quivruserget_identity_route)
  * [`quivr.user.get_user_information`](#quivruserget_user_information)
  * [`quivr.user.update_identity_route`](#quivruserupdate_identity_route)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Quivr&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from quivr_python_sdk import Quivr, ApiException

quivr = Quivr(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Create Api Key
    create_new_key_response = quivr.api_key.create_new_key()
    print(create_new_key_response)
except ApiException as e:
    print("Exception when calling APIKeyApi.create_new_key: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from quivr_python_sdk import Quivr, ApiException

quivr = Quivr(

    access_token = 'YOUR_BEARER_TOKEN'
)

async def main():
    try:
        # Create Api Key
        create_new_key_response = await quivr.api_key.acreate_new_key()
        print(create_new_key_response)
    except ApiException as e:
        print("Exception when calling APIKeyApi.create_new_key: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from quivr_python_sdk import Quivr, ApiException

quivr = Quivr(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Create Api Key
    create_new_key_response = quivr.api_key.raw.create_new_key()
    pprint(create_new_key_response.body)
    pprint(create_new_key_response.body["api_key"])
    pprint(create_new_key_response.body["key_id"])
    pprint(create_new_key_response.body["days"])
    pprint(create_new_key_response.body["only_chat"])
    pprint(create_new_key_response.body["name"])
    pprint(create_new_key_response.body["creation_time"])
    pprint(create_new_key_response.body["is_active"])
    pprint(create_new_key_response.headers)
    pprint(create_new_key_response.status)
    pprint(create_new_key_response.round_trip_time)
except ApiException as e:
    print("Exception when calling APIKeyApi.create_new_key: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `quivr.api_key.create_new_key`<a id="quivrapi_keycreate_new_key"></a>

Create new API key for the current user.

- `current_user`: The current authenticated user.
- Returns the newly created API key.

This endpoint generates a new API key for the current user. The API key is stored in the database and associated with
the user. It returns the newly created API key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_key_response = quivr.api_key.create_new_key()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ApiKey`](./quivr_python_sdk/pydantic/api_key.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api-key` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.api_key.delete_key`<a id="quivrapi_keydelete_key"></a>

Delete (deactivate) an API key for the current user.

- `key_id`: The ID of the API key to delete.

This endpoint deactivates and deletes the specified API key associated with the current user. The API key is marked
as inactive in the database.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_key_response = quivr.api_key.delete_key(
    key_id="key_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key_id: `str`<a id="key_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api-key/{key_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.api_key.get_list`<a id="quivrapi_keyget_list"></a>

Get all active API keys for the current user.

- `current_user`: The current authenticated user.
- Returns a list of active API keys with their IDs and creation times.

This endpoint retrieves all the active API keys associated with the current user. It returns a list of API key objects
containing the key ID and creation time for each API key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = quivr.api_key.get_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ApiKeyGetListResponse`](./quivr_python_sdk/pydantic/api_key_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api-keys` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.accept_invitation`<a id="quivrbrainaccept_invitation"></a>

Accept an invitation to a brain for a user. This function removes the
invitation from the subscription invitations and adds the user to the
brain users.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
accept_invitation_response = quivr.brain.accept_invitation(
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}/subscription/accept` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.create_new_brain`<a id="quivrbraincreate_new_brain"></a>

Create a new brain for the user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_brain_response = quivr.brain.create_new_brain(
    description="This is a description",
    name="Default brain",
    status="private",
    model="string_example",
    temperature=0,
    max_tokens=2000,
    prompt_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    brain_type="doc",
    brain_definition={
        "method": "GET",
        "url": "url_example",
        "secrets": [],
        "raw": False,
    },
    brain_secrets_values={},
    connected_brains_ids=[],
    integration={
        "integration_id": "integration_id_example",
        "settings": {},
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

##### name: `Optional[str]`<a id="name-optionalstr"></a>

##### status: `Optional[str]`<a id="status-optionalstr"></a>

##### model: `Optional[str]`<a id="model-optionalstr"></a>

##### temperature: `Optional[Union[int, float]]`<a id="temperature-optionalunionint-float"></a>

##### max_tokens: `Optional[int]`<a id="max_tokens-optionalint"></a>

##### prompt_id: `Optional[str]`<a id="prompt_id-optionalstr"></a>

##### brain_type: [`BrainTypeNullable`](./quivr_python_sdk/type/brain_type_nullable.py)<a id="brain_type-braintypenullablequivr_python_sdktypebrain_type_nullablepy"></a>

##### brain_definition: [`CreateApiBrainDefinitionNullable`](./quivr_python_sdk/type/create_api_brain_definition_nullable.py)<a id="brain_definition-createapibraindefinitionnullablequivr_python_sdktypecreate_api_brain_definition_nullablepy"></a>


##### brain_secrets_values: `Optional[Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`<a id="brain_secrets_values-optionaldictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### connected_brains_ids: [`CreateBrainPropertiesConnectedBrainsIds`](./quivr_python_sdk/type/create_brain_properties_connected_brains_ids.py)<a id="connected_brains_ids-createbrainpropertiesconnectedbrainsidsquivr_python_sdktypecreate_brain_properties_connected_brains_idspy"></a>

##### integration: [`BrainIntegrationSettingsNullable`](./quivr_python_sdk/type/brain_integration_settings_nullable.py)<a id="integration-brainintegrationsettingsnullablequivr_python_sdktypebrain_integration_settings_nullablepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateBrainProperties`](./quivr_python_sdk/type/create_brain_properties.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.decline_invitation`<a id="quivrbraindecline_invitation"></a>

Decline an invitation to a brain for a user. This function removes the
invitation from the subscription invitations.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
decline_invitation_response = quivr.brain.decline_invitation(
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}/subscription/decline` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.get_all_for_user`<a id="quivrbrainget_all_for_user"></a>

Retrieve all brains for the current user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_for_user_response = quivr.brain.get_all_for_user()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.get_all_public`<a id="quivrbrainget_all_public"></a>

Retrieve all Quivr public brains.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_public_response = quivr.brain.get_all_public()
```

#### 🔄 Return<a id="🔄-return"></a>

[`BrainGetAllPublicResponse`](./quivr_python_sdk/pydantic/brain_get_all_public_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/public` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.get_by_id`<a id="quivrbrainget_by_id"></a>

Retrieve details of a specific brain by its ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = quivr.brain.get_by_id(
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.get_default_brain`<a id="quivrbrainget_default_brain"></a>

Retrieve or create the default brain for the current user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_default_brain_response = quivr.brain.get_default_brain()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/default` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.get_description`<a id="quivrbrainget_description"></a>

Retrieve the integration brain description.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_description_response = quivr.brain.get_description()
```

#### 🔄 Return<a id="🔄-return"></a>

[`BrainGetDescriptionResponse`](./quivr_python_sdk/pydantic/brain_get_description_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/integrations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.get_question_context`<a id="quivrbrainget_question_context"></a>

Retrieve the question context from a specific brain.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_question_context_response = quivr.brain.get_question_context(
    question="string_example",
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### question: `str`<a id="question-str"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BrainQuestionRequest`](./quivr_python_sdk/type/brain_question_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}/documents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.get_users`<a id="quivrbrainget_users"></a>

Get all users for a brain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_users_response = quivr.brain.get_users(
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.remove_user_subscription`<a id="quivrbrainremove_user_subscription"></a>

Remove a user's subscription to a brain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_user_subscription_response = quivr.brain.remove_user_subscription(
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}/subscription` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.set_default`<a id="quivrbrainset_default"></a>

Set a brain as the default for the current user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_default_response = quivr.brain.set_default(
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}/default` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.update_configuration`<a id="quivrbrainupdate_configuration"></a>

Update an existing brain's configuration.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_configuration_response = quivr.brain.update_configuration(
    brain_id="brain_id_example",
    description="string_example",
    name="string_example",
    temperature=3.14,
    model="string_example",
    max_tokens=1,
    status="string_example",
    prompt_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    brain_definition={
        "brain_id": "brain_id_example",
        "method": "GET",
        "url": "url_example",
        "params": {
            "properties": [],
            "required": [],
        },
,
        "secrets": [
            {
                "name": "name_example",
                "type": "type_example",
            }
        ],
        "raw": False,
    },
    connected_brains_ids=[],
    integration={
        "settings": {},
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

##### description: `Optional[str]`<a id="description-optionalstr"></a>

##### name: `Optional[str]`<a id="name-optionalstr"></a>

##### temperature: `Optional[Union[int, float]]`<a id="temperature-optionalunionint-float"></a>

##### model: `Optional[str]`<a id="model-optionalstr"></a>

##### max_tokens: `Optional[int]`<a id="max_tokens-optionalint"></a>

##### status: `Optional[str]`<a id="status-optionalstr"></a>

##### prompt_id: `Optional[str]`<a id="prompt_id-optionalstr"></a>

##### brain_definition: [`ApiBrainDefinitionEntityInputNullable`](./quivr_python_sdk/type/api_brain_definition_entity_input_nullable.py)<a id="brain_definition-apibraindefinitionentityinputnullablequivr_python_sdktypeapi_brain_definition_entity_input_nullablepy"></a>


##### connected_brains_ids: [`BrainUpdatablePropertiesConnectedBrainsIds`](./quivr_python_sdk/type/brain_updatable_properties_connected_brains_ids.py)<a id="connected_brains_ids-brainupdatablepropertiesconnectedbrainsidsquivr_python_sdktypebrain_updatable_properties_connected_brains_idspy"></a>

##### integration: [`BrainIntegrationUpdateSettingsNullable`](./quivr_python_sdk/type/brain_integration_update_settings_nullable.py)<a id="integration-brainintegrationupdatesettingsnullablequivr_python_sdktypebrain_integration_update_settings_nullablepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BrainUpdatableProperties`](./quivr_python_sdk/type/brain_updatable_properties.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.update_secrets_values`<a id="quivrbrainupdate_secrets_values"></a>

Update an existing brain's secrets.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_secrets_values_response = quivr.brain.update_secrets_values(
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BrainUpdateSecretsValuesRequest`](./quivr_python_sdk/type/brain_update_secrets_values_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}/secrets-values` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain.update_subscription`<a id="quivrbrainupdate_subscription"></a>

Update Brain Subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_subscription_response = quivr.brain.update_subscription(
    email="string_example",
    brain_id="brain_id_example",
    rights="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

##### rights: `Optional[str]`<a id="rights-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BrainSubscriptionUpdatableProperties`](./quivr_python_sdk/type/brain_subscription_updatable_properties.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}/subscription` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain_subscription.get_user_invitation`<a id="quivrbrain_subscriptionget_user_invitation"></a>

Get an invitation to a brain for a user. This function checks if the user
has been invited to the brain and returns the invitation status.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_invitation_response = quivr.brain_subscription.get_user_invitation(
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}/subscription` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.brain_subscription.invite_users_to_brain`<a id="quivrbrain_subscriptioninvite_users_to_brain"></a>

Invite multiple users to a brain by their emails. This function creates
or updates a brain subscription invitation for each user and sends an
invitation email to each user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
invite_users_to_brain_response = quivr.brain_subscription.invite_users_to_brain(
    body=[
        {}
    ],
    brain_id="brain_id_example",
    origin="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

##### origin: `Optional[str]`<a id="origin-optionalstr"></a>

##### requestBody: [`BrainSubscriptionInviteUsersToBrainRequest`](./quivr_python_sdk/type/brain_subscription_invite_users_to_brain_request.py)<a id="requestbody-brainsubscriptioninviteuserstobrainrequestquivr_python_sdktypebrain_subscription_invite_users_to_brain_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}/subscription` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.chat.add_question_and_answer`<a id="quivrchatadd_question_and_answer"></a>

Add a new question and anwser to the chat.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_question_and_answer_response = quivr.chat.add_question_and_answer(
    question="string_example",
    answer="string_example",
    chat_id="chat_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### question: `str`<a id="question-str"></a>

##### answer: `str`<a id="answer-str"></a>

##### chat_id: `str`<a id="chat_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`QuestionAndAnswer`](./quivr_python_sdk/type/question_and_answer.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChatNullable`](./quivr_python_sdk/pydantic/chat_nullable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/chat/{chat_id}/question/answer` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.chat.create_handler`<a id="quivrchatcreate_handler"></a>

Create a new chat with initial chat messages.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_handler_response = quivr.chat.create_handler(
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateChatProperties`](./quivr_python_sdk/type/create_chat_properties.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/chat` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.chat.create_stream_question_handler`<a id="quivrchatcreate_stream_question_handler"></a>

Create Stream Question Handler

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_stream_question_handler_response = quivr.chat.create_stream_question_handler(
    question="string_example",
    chat_id="chat_id_example",
    model="string_example",
    temperature=3.14,
    max_tokens=1,
    brain_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    prompt_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    brain_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### chat_id: `str`<a id="chat_id-str"></a>

##### brain_id: `Optional[str]`<a id="brain_id-optionalstr"></a>

##### requestBody: [`ChatQuestion`](./quivr_python_sdk/type/chat_question.py)<a id="requestbody-chatquestionquivr_python_sdktypechat_questionpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/chat/{chat_id}/question/stream` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.chat.delete_chat_by_id`<a id="quivrchatdelete_chat_by_id"></a>

Delete a specific chat by chat ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_chat_by_id_response = quivr.chat.delete_chat_by_id(
    chat_id="chat_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### chat_id: `str`<a id="chat_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/chat/{chat_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.chat.get_all_chats`<a id="quivrchatget_all_chats"></a>

Retrieve all chats for the current user.

- `current_user`: The current authenticated user.
- Returns a list of all chats for the user.

This endpoint retrieves all the chats associated with the current authenticated user. It returns a list of chat objects
containing the chat ID and chat name for each chat.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_chats_response = quivr.chat.get_all_chats()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/chat` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.chat.get_history`<a id="quivrchatget_history"></a>

Get Chat History Handler

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_history_response = quivr.chat.get_history(
    chat_id="chat_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### chat_id: `str`<a id="chat_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ChatGetHistoryResponse`](./quivr_python_sdk/pydantic/chat_get_history_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/chat/{chat_id}/history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.chat.handle_question`<a id="quivrchathandle_question"></a>

Create Question Handler

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
handle_question_response = quivr.chat.handle_question(
    question="string_example",
    chat_id="chat_id_example",
    model="string_example",
    temperature=3.14,
    max_tokens=1,
    brain_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    prompt_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    brain_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### chat_id: `str`<a id="chat_id-str"></a>

##### brain_id: `Optional[str]`<a id="brain_id-optionalstr"></a>

##### requestBody: [`ChatQuestion`](./quivr_python_sdk/type/chat_question.py)<a id="requestbody-chatquestionquivr_python_sdktypechat_questionpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/chat/{chat_id}/question` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.chat.update_message`<a id="quivrchatupdate_message"></a>

Update Chat Message

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_message_response = quivr.chat.update_message(
    thumbs=True,
    chat_id="chat_id_example",
    message_id="message_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### thumbs: `Optional[bool]`<a id="thumbs-optionalbool"></a>

##### chat_id: `str`<a id="chat_id-str"></a>

##### message_id: `str`<a id="message_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChatMessageProperties`](./quivr_python_sdk/type/chat_message_properties.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/chat/{chat_id}/{message_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.chat.update_metadata_handler`<a id="quivrchatupdate_metadata_handler"></a>

Update chat attributes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_metadata_handler_response = quivr.chat.update_metadata_handler(
    chat_id="chat_id_example",
    chat_name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### chat_id: `str`<a id="chat_id-str"></a>

##### chat_name: `Optional[str]`<a id="chat_name-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChatUpdatableProperties`](./quivr_python_sdk/type/chat_updatable_properties.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/chat/{chat_id}/metadata` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.contact.create_new_contact`<a id="quivrcontactcreate_new_contact"></a>

Post Contact

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_contact_response = quivr.contact.create_new_contact(
    customer_email="string_example",
    content="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_email: `str`<a id="customer_email-str"></a>

##### content: `str`<a id="content-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContactMessage`](./quivr_python_sdk/type/contact_message.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/contact` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.crawl.website_data_processor`<a id="quivrcrawlwebsite_data_processor"></a>

Crawl a website and process the crawled data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
website_data_processor_response = quivr.crawl.website_data_processor(
    url="string_example",
    brain_id="brain_id_example",
    js=False,
    depth=1,
    max_pages=100,
    max_time=60,
    chat_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

The ID of the brain

##### js: `bool`<a id="js-bool"></a>

##### depth: `int`<a id="depth-int"></a>

##### max_pages: `int`<a id="max_pages-int"></a>

##### max_time: `int`<a id="max_time-int"></a>

##### chat_id: `Optional[str]`<a id="chat_id-optionalstr"></a>

The ID of the chat

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CrawlWebsite`](./quivr_python_sdk/type/crawl_website.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/crawl` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.health.check_status`<a id="quivrhealthcheck_status"></a>

Healthz

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_status_response = quivr.health.check_status()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/chat/healthz` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.health.check_status_0`<a id="quivrhealthcheck_status_0"></a>

Healthz

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_status_0_response = quivr.health.check_status_0()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/crawl/healthz` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.health.check_status_1`<a id="quivrhealthcheck_status_1"></a>

Healthz

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_status_1_response = quivr.health.check_status_1()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/healthz` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.health.check_status_2`<a id="quivrhealthcheck_status_2"></a>

Healthz

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_status_2_response = quivr.health.check_status_2()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/upload/healthz` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.knowledge.delete_specific_brain_knowledge`<a id="quivrknowledgedelete_specific_brain_knowledge"></a>

Delete a specific knowledge from a brain.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_specific_brain_knowledge_response = quivr.knowledge.delete_specific_brain_knowledge(
    knowledge_id="knowledge_id_example",
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### knowledge_id: `str`<a id="knowledge_id-str"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge/{knowledge_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.knowledge.generate_signed_url`<a id="quivrknowledgegenerate_signed_url"></a>

Generate a signed url to download the file from storage.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_signed_url_response = quivr.knowledge.generate_signed_url(
    knowledge_id="knowledge_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### knowledge_id: `str`<a id="knowledge_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge/{knowledge_id}/signed_download_url` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.knowledge.get_all_knowledge`<a id="quivrknowledgeget_all_knowledge"></a>

Retrieve and list all the knowledge in a brain.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_knowledge_response = quivr.knowledge.get_all_knowledge(
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

The ID of the brain

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/knowledge` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.notification.get_by_chat_id`<a id="quivrnotificationget_by_chat_id"></a>

Get notifications by chat_id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_chat_id_response = quivr.notification.get_by_chat_id(
    chat_id="chat_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### chat_id: `str`<a id="chat_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{chat_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.onboarding.get_user_info`<a id="quivronboardingget_user_info"></a>

Get user onboarding information for the current user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_info_response = quivr.onboarding.get_user_info()
```

#### 🔄 Return<a id="🔄-return"></a>

[`OnboardingStatesNullable`](./quivr_python_sdk/pydantic/onboarding_states_nullable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/onboarding` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.onboarding.update_user_onboarding`<a id="quivronboardingupdate_user_onboarding"></a>

Update user onboarding information for the current user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_onboarding_response = quivr.onboarding.update_user_onboarding(
    onboarding_a=True,
    onboarding_b1=True,
    onboarding_b2=True,
    onboarding_b3=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### onboarding_a: `Optional[bool]`<a id="onboarding_a-optionalbool"></a>

##### onboarding_b1: `Optional[bool]`<a id="onboarding_b1-optionalbool"></a>

##### onboarding_b2: `Optional[bool]`<a id="onboarding_b2-optionalbool"></a>

##### onboarding_b3: `Optional[bool]`<a id="onboarding_b3-optionalbool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OnboardingUpdatableProperties`](./quivr_python_sdk/type/onboarding_updatable_properties.py)
#### 🔄 Return<a id="🔄-return"></a>

[`OnboardingStates`](./quivr_python_sdk/pydantic/onboarding_states.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/onboarding` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.prompt.create_prompt_by_id`<a id="quivrpromptcreate_prompt_by_id"></a>

Create a prompt by its id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_prompt_by_id_response = quivr.prompt.create_prompt_by_id(
    title="string_example",
    content="string_example",
    status="private",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

##### content: `str`<a id="content-str"></a>

##### status: [`PromptStatusEnum`](./quivr_python_sdk/type/prompt_status_enum.py)<a id="status-promptstatusenumquivr_python_sdktypeprompt_status_enumpy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreatePromptProperties`](./quivr_python_sdk/type/create_prompt_properties.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PromptNullable`](./quivr_python_sdk/pydantic/prompt_nullable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/prompts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.prompt.get_all_public_prompts`<a id="quivrpromptget_all_public_prompts"></a>

Retrieve all public prompt

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_public_prompts_response = quivr.prompt.get_all_public_prompts()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PromptGetAllPublicPromptsResponse`](./quivr_python_sdk/pydantic/prompt_get_all_public_prompts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/prompts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.prompt.get_by_id`<a id="quivrpromptget_by_id"></a>

Retrieve a prompt by its id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = quivr.prompt.get_by_id(
    prompt_id="prompt_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### prompt_id: `str`<a id="prompt_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PromptNullable`](./quivr_python_sdk/pydantic/prompt_nullable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/prompts/{prompt_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.prompt.update_by_id`<a id="quivrpromptupdate_by_id"></a>

Update a prompt by its id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = quivr.prompt.update_by_id(
    prompt_id="prompt_id_example",
    title="string_example",
    content="string_example",
    status="private",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### prompt_id: `str`<a id="prompt_id-str"></a>

##### title: `Optional[str]`<a id="title-optionalstr"></a>

##### content: `Optional[str]`<a id="content-optionalstr"></a>

##### status: [`PromptStatusEnumNullable`](./quivr_python_sdk/type/prompt_status_enum_nullable.py)<a id="status-promptstatusenumnullablequivr_python_sdktypeprompt_status_enum_nullablepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PromptUpdatableProperties`](./quivr_python_sdk/type/prompt_updatable_properties.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PromptNullable`](./quivr_python_sdk/pydantic/prompt_nullable.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/prompts/{prompt_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.root.status_check`<a id="quivrrootstatus_check"></a>

Root endpoint to check the status of the API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
status_check_response = quivr.root.status_check()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.subscription.brain_handler`<a id="quivrsubscriptionbrain_handler"></a>

Subscribe to a public brain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
brain_handler_response = quivr.subscription.brain_handler(
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}/subscribe` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.subscription.unregister_handler`<a id="quivrsubscriptionunregister_handler"></a>

Unsubscribe from a brain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unregister_handler_response = quivr.subscription.unregister_handler(
    brain_id="brain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/brains/{brain_id}/unsubscribe` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.upload.file_post`<a id="quivruploadfile_post"></a>

Upload File

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
file_post_response = quivr.upload.file_post(
    brain_id="brain_id_example",
    upload_file=open('/path/to/file', 'rb'),
    chat_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brain_id: `str`<a id="brain_id-str"></a>

The ID of the brain

##### upload_file: `IO`<a id="upload_file-io"></a>

##### chat_id: `Optional[str]`<a id="chat_id-optionalstr"></a>

The ID of the chat

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BodyUploadFileUploadPost`](./quivr_python_sdk/type/body_upload_file_upload_post.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/upload` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.user.get_identity_route`<a id="quivruserget_identity_route"></a>

Get user identity.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_identity_route_response = quivr.user.get_identity_route()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UserIdentity`](./quivr_python_sdk/pydantic/user_identity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/identity` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.user.get_user_information`<a id="quivruserget_user_information"></a>

Get user information and statistics.

- `current_user`: The current authenticated user.
- Returns the user's email, maximum brain size, current brain size, maximum requests number, requests statistics, and the current date.

This endpoint retrieves information and statistics about the authenticated user. It includes the user's email, maximum brain size,
current brain size, maximum requests number, requests statistics, and the current date. The brain size is calculated based on the
user's uploaded vectors, and the maximum brain size is obtained from the environment variables. The requests statistics provide
information about the user's API usage.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_information_response = quivr.user.get_user_information()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `quivr.user.update_identity_route`<a id="quivruserupdate_identity_route"></a>

Update user identity.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_identity_route_response = quivr.user.update_identity_route(
    username="string_example",
    company="string_example",
    onboarded=True,
    company_size="string_example",
    usage_purpose="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `Optional[str]`<a id="username-optionalstr"></a>

##### company: `Optional[str]`<a id="company-optionalstr"></a>

##### onboarded: `Optional[bool]`<a id="onboarded-optionalbool"></a>

##### company_size: `Optional[str]`<a id="company_size-optionalstr"></a>

##### usage_purpose: `Optional[str]`<a id="usage_purpose-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UserUpdatableProperties`](./quivr_python_sdk/type/user_updatable_properties.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UserIdentity`](./quivr_python_sdk/pydantic/user_identity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user/identity` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
