# Sessions
(*sessions*)

## Overview

### Available Operations

* [create](#create) - Create session [BETA]
* [get](#get) - Get session

## create

> 🚧 Beta feature
>
> This feature is currently in private beta, and the final specification may still change.

Create a session to start a checkout process with Mollie Components.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-session" method="post" path="/sessions" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.sessions.create(idempotency_key="123e4567-e89b-12d3-a456-426", session_request=mollie.SessionRequest(
        amount=mollie.Amount(
            currency="EUR",
            value="10.00",
        ),
        description="Order #12345",
        redirect_url="https://example.org/redirect",
        billing_address=mollie.PaymentAddress(
            title="Mr.",
            given_name="Piet",
            family_name="Mondriaan",
            organization_name="Mollie B.V.",
            street_and_number="Keizersgracht 126",
            street_additional="Apt. 1",
            postal_code="1234AB",
            email="piet@example.org",
            phone="31208202070",
            city="Amsterdam",
            region="Noord-Holland",
            country="NL",
        ),
        shipping_address=mollie.PaymentAddress(
            title="Mr.",
            given_name="Piet",
            family_name="Mondriaan",
            organization_name="Mollie B.V.",
            street_and_number="Keizersgracht 126",
            street_additional="Apt. 1",
            postal_code="1234AB",
            email="piet@example.org",
            phone="31208202070",
            city="Amsterdam",
            region="Noord-Holland",
            country="NL",
        ),
        customer_id="cst_5B8cwPMGnU",
        sequence_type=mollie.SessionSequenceType.ONEOFF,
        payment=mollie.SessionRequestPayment(
            webhook_url="https://example.org/webhook",
        ),
        lines=[],
        profile_id="pfl_5B8cwPMGnU",
        testmode=False,
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `session_request`                                                                | [Optional[models.SessionRequest]](../../models/sessionrequest.md)                | :heavy_minus_sign:                                                               | N/A                                                                              |                                                                                  |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.SessionResponse](../../models/sessionresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 422                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

> 🚧 Beta feature
>
> This feature is currently in private beta, and the final specification may still change.

Retrieve a session to view its details and status to inform your customers about the checkout process.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-session" method="get" path="/sessions/{sessionId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.sessions.get(session_id="sess_82jFYDTrLcCQV68NLDvMJ", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `session_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related session.                                           | sess_82jFYDTrLcCQV68NLDvMJ                                                       |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.SessionResponse](../../models/sessionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |