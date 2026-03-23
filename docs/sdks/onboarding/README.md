# Onboarding

## Overview

### Available Operations

* [get](#get) - Get onboarding status
* [submit](#submit) - Submit onboarding data

## get

Retrieve the onboarding status of the currently authenticated organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-onboarding-status" method="get" path="/onboarding/me" example="get-onboarding-status-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        o_auth=os.getenv("CLIENT_O_AUTH", ""),
    ),
) as client_sdk:

    res = client_sdk.onboarding.get(idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.EntityOnboardingStatus](../../models/entityonboardingstatus.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## submit

**⚠️ We no longer recommend implementing this endpoint. Please refer to the Client Links API instead to kick off the
onboarding process for your merchants.**

Submit data that will be prefilled in the merchant's onboarding. The data you submit will only be processed when the
onboarding status is `needs-data`.  
Information that the merchant has entered in their dashboard will not be overwritten.

### Example Usage

<!-- UsageSnippet language="python" operationID="submit-onboarding-data" method="post" path="/onboarding/me" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        o_auth=os.getenv("CLIENT_O_AUTH", ""),
    ),
) as client_sdk:

    client_sdk.onboarding.submit(idempotency_key="123e4567-e89b-12d3-a456-426", request_body={
        "organization": {
            "name": "Mollie B.V.",
            "address": {
                "street_and_number": "Keizersgracht 126",
                "postal_code": "1015 CW",
                "city": "Amsterdam",
                "country": "NL",
            },
            "registration_number": "30204462",
            "vat_number": "NL815839091B01",
            "vat_regulation": mollie.OnboardingVatRegulation.DUTCH,
        },
        "profile": {
            "name": "Mollie",
            "url": "https://www.mollie.com",
            "email": "info@mollie.com",
            "phone": "+31208202070",
            "description": "Payment service provider",
            "business_category": "MONEY_SERVICES",
        },
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         | Example                                                                                             |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `idempotency_key`                                                                                   | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                    | 123e4567-e89b-12d3-a456-426                                                                         |
| `request_body`                                                                                      | [Optional[models.SubmitOnboardingDataRequestBody]](../../models/submitonboardingdatarequestbody.md) | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |                                                                                                     |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |                                                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |