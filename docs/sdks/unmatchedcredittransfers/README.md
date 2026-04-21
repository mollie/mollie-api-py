# UnmatchedCreditTransfers

## Overview

### Available Operations

* [list](#list) - List unmatched credit transfers
* [get](#get) - Get unmatched credit transfer
* [match](#match) - Match unmatched credit transfer
* [return_](#return_) - Return unmatched credit transfer

## list

> 🚧 Beta feature
>
> This feature is currently in private beta, and the final specification may still change.

Retrieves a list of unmatched credit transfers for the profile.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-unmatched-credit-transfers" method="get" path="/v2/unmatched-credit-transfers" example="list-unmatched-credit-transfers-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.unmatched_credit_transfers.list(limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `from_`                                                                                                                        | *OptionalNullable[str]*                                                                                                        | :heavy_minus_sign:                                                                                                             | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set. |                                                                                                                                |
| `limit`                                                                                                                        | *OptionalNullable[int]*                                                                                                        | :heavy_minus_sign:                                                                                                             | The maximum number of items to return. Defaults to 50 items.                                                                   | 50                                                                                                                             |
| `idempotency_key`                                                                                                              | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                               | 123e4567-e89b-12d3-a456-426                                                                                                    |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.ListUnmatchedCreditTransfersResponse](../../models/listunmatchedcredittransfersresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

> 🚧 Beta feature
>
> This feature is currently in private beta, and the final specification may still change.

Retrieves a single unmatched credit transfer by its identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-unmatched-credit-transfer" method="get" path="/v2/unmatched-credit-transfers/{unmatchedCreditTransferId}" example="get-unmatched-credit-transfer-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.unmatched_credit_transfers.get(unmatched_credit_transfer_id="uct_abcDEFghij123456789", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `unmatched_credit_transfer_id`                                                   | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related unmatched credit transfer.                         | uct_abcDEFghij123456789                                                          |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.EntityUnmatchedCreditTransfer](../../models/entityunmatchedcredittransfer.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## match

> 🚧 Beta feature
>
> This feature is currently in private beta, and the final specification may still change.

Matches an unmatched credit transfer to one or more payments, settling the funds accordingly.

### Example Usage

<!-- UsageSnippet language="python" operationID="match-unmatched-credit-transfer" method="post" path="/v2/unmatched-credit-transfers/{unmatchedCreditTransferId}/match" example="match-unmatched-credit-transfer-201-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.unmatched_credit_transfers.match(unmatched_credit_transfer_id="uct_abcDEFghij123456789", idempotency_key="123e4567-e89b-12d3-a456-426", unmatched_credit_transfer_match_request={
        "payment_ids": [
            "tr_5B8cwPMGnU",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 | Example                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `unmatched_credit_transfer_id`                                                                              | *str*                                                                                                       | :heavy_check_mark:                                                                                          | Provide the ID of the related unmatched credit transfer.                                                    | uct_abcDEFghij123456789                                                                                     |
| `idempotency_key`                                                                                           | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                            | 123e4567-e89b-12d3-a456-426                                                                                 |
| `unmatched_credit_transfer_match_request`                                                                   | [Optional[models.UnmatchedCreditTransferMatchRequest]](../../models/unmatchedcredittransfermatchrequest.md) | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |                                                                                                             |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |                                                                                                             |

### Response

**[models.UnmatchedCreditTransferActionResponse](../../models/unmatchedcredittransferactionresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 422             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## return_

> 🚧 Beta feature
>
> This feature is currently in private beta, and the final specification may still change.

Returns an unmatched credit transfer, sending the funds back to the original sender.

### Example Usage

<!-- UsageSnippet language="python" operationID="return-unmatched-credit-transfer" method="post" path="/v2/unmatched-credit-transfers/{unmatchedCreditTransferId}/return" example="return-unmatched-credit-transfer-201-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.unmatched_credit_transfers.return_(unmatched_credit_transfer_id="uct_abcDEFghij123456789", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `unmatched_credit_transfer_id`                                                   | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related unmatched credit transfer.                         | uct_abcDEFghij123456789                                                          |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.UnmatchedCreditTransferActionResponse](../../models/unmatchedcredittransferactionresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |