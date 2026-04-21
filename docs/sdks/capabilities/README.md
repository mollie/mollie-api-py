# Capabilities

## Overview

### Available Operations

* [list](#list) - List capabilities

## list

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Retrieve a list of capabilities for an organization.

This API provides detailed insights into the specific requirements and status of each client's onboarding journey.

Capabilities are at the organization level, indicating if the organization can perform a given capability.
Capabilities may have requirements, which provide more information on what is needed to use this capability. 
Requirements may have a due date, which indicates the date by which the requirement should be fulfilled. 
If a requirement is past due, the capability is disabled until the requirement is fulfilled.

For payments, regardless them being at the profile level, the capability is listed at the organization level.
This means that if at least one of the clients's profiles can receive payments,
the payments capability is enabled, communicating that the organization can indeed receive payments.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-capabilities" method="get" path="/v2/capabilities" example="successful-response-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.capabilities.list(idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.ListCapabilitiesResponse](../../models/listcapabilitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |