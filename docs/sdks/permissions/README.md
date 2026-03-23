# Permissions

## Overview

### Available Operations

* [list](#list) - List permissions
* [get](#get) - Get permission

## list

Retrieve a list of all permissions available to the current access token.

The results are **not** paginated.

### Example Usage: list-permissions-200-1

<!-- UsageSnippet language="python" operationID="list-permissions" method="get" path="/permissions" example="list-permissions-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        o_auth=os.getenv("CLIENT_O_AUTH", ""),
    ),
) as client_sdk:

    res = client_sdk.permissions.list(idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```
### Example Usage: list-permissions-200-2

<!-- UsageSnippet language="python" operationID="list-permissions" method="get" path="/permissions" example="list-permissions-200-2" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        o_auth=os.getenv("CLIENT_O_AUTH", ""),
    ),
) as client_sdk:

    res = client_sdk.permissions.list(idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.ListPermissionsResponse](../../models/listpermissionsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

Retrieve a single permission by its ID, and see if the permission is granted to the current access token.

### Example Usage: get-permission-200-1

<!-- UsageSnippet language="python" operationID="get-permission" method="get" path="/permissions/{permissionId}" example="get-permission-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    testmode=False,
    security=mollie.Security(
        o_auth=os.getenv("CLIENT_O_AUTH", ""),
    ),
) as client_sdk:

    res = client_sdk.permissions.get(permission_id="payments.read", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```
### Example Usage: get-permission-200-2

<!-- UsageSnippet language="python" operationID="get-permission" method="get" path="/permissions/{permissionId}" example="get-permission-200-2" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    testmode=False,
    security=mollie.Security(
        o_auth=os.getenv("CLIENT_O_AUTH", ""),
    ),
) as client_sdk:

    res = client_sdk.permissions.get(permission_id="payments.read", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             | Example                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `permission_id`                                                                                                                                                         | *str*                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                      | Provide the ID of the related permission.                                                                                                                               | payments.read                                                                                                                                                           |
| `testmode`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | You can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                         |
| `idempotency_key`                                                                                                                                                       | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                        | 123e4567-e89b-12d3-a456-426                                                                                                                                             |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |                                                                                                                                                                         |

### Response

**[models.EntityPermission](../../models/entitypermission.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |