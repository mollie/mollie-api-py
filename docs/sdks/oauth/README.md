# Oauth

## Overview

### Available Operations

* [generate](#generate) - Generate tokens
* [revoke](#revoke) - Revoke tokens

## generate

Exchange the authorization code you received from the [Authorize endpoint](oauth-authorize) for an 'access token'
API credential, with which you can communicate with the Mollie API on behalf of the consenting merchant.

This endpoint can only be accessed using **OAuth client credentials**.

### Example Usage

<!-- UsageSnippet language="python" operationID="oauth-generate-tokens" method="post" path="/oauth2/tokens" example="oauth-generate-tokens" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        o_auth=os.getenv("CLIENT_O_AUTH", ""),
    ),
) as client_sdk:

    res = client_sdk.oauth.generate(idempotency_key="123e4567-e89b-12d3-a456-426", request_body={
        "grant_type": mollie.OauthGrantType.AUTHORIZATION_CODE,
        "code": "auth_...",
        "refresh_token": "refresh_...",
        "redirect_uri": "https://example.com/redirect",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `idempotency_key`                                                                                 | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                  | 123e4567-e89b-12d3-a456-426                                                                       |
| `request_body`                                                                                    | [Optional[models.OauthGenerateTokensRequestBody]](../../models/oauthgeneratetokensrequestbody.md) | :heavy_minus_sign:                                                                                | N/A                                                                                               |                                                                                                   |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |
| `server_url`                                                                                      | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | An optional server URL to use.                                                                    | http://localhost:8080                                                                             |

### Response

**[models.OauthGenerateTokensResponse](../../models/oauthgeneratetokensresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## revoke

Revoke an access token or refresh token. Once revoked, the token can no longer be used.

Revoking a refresh token revokes all access tokens that were created using the same authorization.

This endpoint can only be accessed using **OAuth client credentials**.

### Example Usage

<!-- UsageSnippet language="python" operationID="oauth-revoke-tokens" method="delete" path="/oauth2/tokens" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        o_auth=os.getenv("CLIENT_O_AUTH", ""),
    ),
) as client_sdk:

    client_sdk.oauth.revoke(idempotency_key="123e4567-e89b-12d3-a456-426", request_body={
        "token_type_hint": mollie.OauthTokenTypeHint.ACCESS_TOKEN,
        "token": "access_...",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `idempotency_key`                                                                             | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | A unique key to ensure idempotent requests. This key should be a UUID v4 string.              | 123e4567-e89b-12d3-a456-426                                                                   |
| `request_body`                                                                                | [Optional[models.OauthRevokeTokensRequestBody]](../../models/oauthrevoketokensrequestbody.md) | :heavy_minus_sign:                                                                            | N/A                                                                                           |                                                                                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |
| `server_url`                                                                                  | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | An optional server URL to use.                                                                | http://localhost:8080                                                                         |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |