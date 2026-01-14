# BalanceTransfers
(*balance_transfers*)

## Overview

### Available Operations

* [create](#create) - Create a Connect balance transfer
* [list](#list) - List all Connect balance transfers
* [get](#get) - Get a Connect balance transfer

## create

This API endpoint allows you to create a balance transfer from your organization's balance to a connected organization's balance, or vice versa.
You can also create a balance transfer between two connected organizations.
To create a balance transfer, you must be authenticated as the source organization, and the destination organization must be a connected organization
that has authorized the `balance-transfers.write` scope for your organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-connect-balance-transfer" method="post" path="/connect/balance-transfers" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.balance_transfers.create(idempotency_key="123e4567-e89b-12d3-a456-426", entity_balance_transfer=mollie.EntityBalanceTransfer(
        amount=mollie.Amount(
            currency="EUR",
            value="10.00",
        ),
        source=mollie.EntityBalanceTransferParty(
            type=mollie.BalanceTransferPartyType.ORGANIZATION,
            id="org_1234567",
            description="Invoice fee",
        ),
        destination=mollie.EntityBalanceTransferParty(
            type=mollie.BalanceTransferPartyType.ORGANIZATION,
            id="org_1234567",
            description="Invoice fee",
        ),
        description="Invoice fee",
        category=mollie.BalanceTransferCategory.INVOICE_COLLECTION,
        metadata={
            "order_id": 12345,
            "customer_id": 9876,
        },
        testmode=False,
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `entity_balance_transfer`                                                        | [Optional[models.EntityBalanceTransfer]](../../models/entitybalancetransfer.md)  | :heavy_minus_sign:                                                               | N/A                                                                              |                                                                                  |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.EntityBalanceTransferResponse](../../models/entitybalancetransferresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 422                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list

Returns a paginated list of balance transfers associated with your organization. These may be a balance transfer that was received or sent from your balance, or a balance transfer that you initiated on behalf of your clients. If no balance transfers are available, the resulting array will be empty. This request should never throw an error.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-connect-balance-transfers" method="get" path="/connect/balance-transfers" -->
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

    res = client_sdk.balance_transfers.list(limit=50, sort=mollie.Sorting.DESC, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             | Example                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                      |                                                                                                                                                                         |
| `limit`                                                                                                                                                                 | *OptionalNullable[int]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | The maximum number of items to return. Defaults to 50 items.                                                                                                            | 50                                                                                                                                                                      |
| `sort`                                                                                                                                                                  | [Optional[models.Sorting]](../../models/sorting.md)                                                                                                                     | :heavy_minus_sign:                                                                                                                                                      | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from<br/>newest to oldest.                              | desc                                                                                                                                                                    |
| `testmode`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | You can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                         |
| `idempotency_key`                                                                                                                                                       | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                        | 123e4567-e89b-12d3-a456-426                                                                                                                                             |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |                                                                                                                                                                         |

### Response

**[models.ListConnectBalanceTransfersResponse](../../models/listconnectbalancetransfersresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

Retrieve a single Connect balance transfer object by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-connect-balance-transfer" method="get" path="/connect/balance-transfers/{balanceTransferId}" -->
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

    res = client_sdk.balance_transfers.get(balance_transfer_id="cbtr_j8NvRAM2WNZtsykpLEX8J", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             | Example                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `balance_transfer_id`                                                                                                                                                   | *str*                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                      | Provide the ID of the related balance transfer.                                                                                                                         | cbtr_j8NvRAM2WNZtsykpLEX8J                                                                                                                                              |
| `testmode`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | You can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                         |
| `idempotency_key`                                                                                                                                                       | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                        | 123e4567-e89b-12d3-a456-426                                                                                                                                             |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |                                                                                                                                                                         |

### Response

**[models.EntityBalanceTransferResponse](../../models/entitybalancetransferresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |