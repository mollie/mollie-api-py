# Profiles
(*profiles*)

## Overview

### Available Operations

* [create](#create) - Create profile
* [list](#list) - List profiles
* [get](#get) - Get profile
* [update](#update) - Update profile
* [delete](#delete) - Delete profile
* [get_current](#get_current) - Get current profile

## create

Create a profile to process payments on.

Profiles are required for payment processing. Normally they are created via the Mollie dashboard. Alternatively, you
can use this endpoint to automate profile creation.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-profile" method="post" path="/profiles" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.profiles.create(profile_request={
        "name": "My website name",
        "website": "https://example.com",
        "email": "test@mollie.com",
        "phone": "+31208202070",
        "description": "My website description",
        "countries_of_activity": [
            "NL",
            "GB",
        ],
        "business_category": "OTHER_MERCHANDISE",
    }, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `profile_request`                                                                | [models.ProfileRequest](../../models/profilerequest.md)                          | :heavy_check_mark:                                                               | N/A                                                                              |                                                                                  |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.ProfileResponse](../../models/profileresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 422                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list

Retrieve a list of all of your profiles.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-profiles" method="get" path="/profiles" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.profiles.list(from_="pfl_QkEhN94Ba", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `from_`                                                                                                                        | *OptionalNullable[str]*                                                                                                        | :heavy_minus_sign:                                                                                                             | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set. |                                                                                                                                |
| `limit`                                                                                                                        | *OptionalNullable[int]*                                                                                                        | :heavy_minus_sign:                                                                                                             | The maximum number of items to return. Defaults to 50 items.                                                                   | 50                                                                                                                             |
| `idempotency_key`                                                                                                              | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                               | 123e4567-e89b-12d3-a456-426                                                                                                    |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.ListProfilesResponse](../../models/listprofilesresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

Retrieve a single profile by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-profile" method="get" path="/profiles/{profileId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    testmode=False,
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.profiles.get(profile_id="pfl_5B8cwPMGnU", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             | Example                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `profile_id`                                                                                                                                                            | *str*                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                      | Provide the ID of the related profile.                                                                                                                                  | pfl_5B8cwPMGnU                                                                                                                                                          |
| `testmode`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | You can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                         |
| `idempotency_key`                                                                                                                                                       | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                        | 123e4567-e89b-12d3-a456-426                                                                                                                                             |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |                                                                                                                                                                         |

### Response

**[models.ProfileResponse](../../models/profileresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 410             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## update

Update an existing profile.

Profiles are required for payment processing. Normally they are created and updated via the Mollie dashboard.
Alternatively, you can use this endpoint to automate profile management.

### Example Usage

<!-- UsageSnippet language="python" operationID="update-profile" method="patch" path="/profiles/{profileId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.profiles.update(profile_id="pfl_5B8cwPMGnU", request_body={
        "name": "My new website name",
        "website": "https://example.com",
        "email": "test@mollie.com",
        "phone": "+31208202071",
        "description": "My website description",
        "countries_of_activity": [
            "NL",
            "GB",
        ],
        "business_category": "OTHER_MERCHANDISE",
    }, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `profile_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related profile.                                           | pfl_5B8cwPMGnU                                                                   |
| `request_body`                                                                   | [models.UpdateProfileRequestBody](../../models/updateprofilerequestbody.md)      | :heavy_check_mark:                                                               | N/A                                                                              |                                                                                  |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.ProfileResponse](../../models/profileresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 410, 422        | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## delete

Delete a profile. A deleted profile and its related credentials can no longer be used for accepting payments.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-profile" method="delete" path="/profiles/{profileId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    client_sdk.profiles.delete(profile_id="pfl_5B8cwPMGnU", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `profile_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related profile.                                           | pfl_5B8cwPMGnU                                                                   |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 410             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get_current

Retrieve the currently authenticated profile. A convenient alias of the [Get profile](get-profile)
endpoint.

For a complete reference of the profile object, refer to the [Get profile](get-profile) endpoint
documentation.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-current-profile" method="get" path="/profiles/me" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.profiles.get_current(idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.ProfileResponse](../../models/profileresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |