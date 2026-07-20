# DraftTransfers

## Overview

### Available Operations

* [create](#create) - Create draft transfer
* [list](#list) - List draft transfers
* [get](#get) - Get draft transfer
* [cancel](#cancel) - Cancel draft transfer

## create

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Creates a draft transfer. The draft transfer immediately enters `awaiting-initiation` and appears in the
initiator's queue in Mollie Apps. It carries no legal weight and moves no funds until a human initiator
approves it there.

### Test mode

| Action | Test-mode behavior |
|---|---|
| Create | Always returns a synthetic draft in `awaiting-initiation`, regardless of most input values |
| Get / List | Always returns synthetic `awaiting-initiation` draft(s), not your real data |
| Cancel | Always returns a synthetic `declined` draft |

There is currently no way to synthesize an `initiated` draft via test mode alone. Initiation only happens when
a real initiator approves in Mollie Apps, which test mode doesn't touch.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-draft-transfer" method="post" path="/v2/business-accounts/draft-transfers" example="create-draft-transfer-201" -->
```python
from datetime import date
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        advanced_access_token=os.getenv("CLIENT_ADVANCED_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.draft_transfers.create(idempotency_key="123e4567-e89b-12d3-a456-426", create_draft_transfer_request={
        "debtor_iban": "NL55MLLE0123456789",
        "creditor": {
            "full_name": "Jan Jansen",
            "account": {
                "iban": "NL02ABNA0123456789",
            },
        },
        "amount": {
            "currency": "EUR",
            "value": "10.00",
        },
        "description": "Invoice 12345",
        "scheduled_for": date.fromisoformat("2025-03-01"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `idempotency_key`                                                                         | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | A unique key to ensure idempotent requests. This key should be a UUID v4 string.          | 123e4567-e89b-12d3-a456-426                                                               |
| `create_draft_transfer_request`                                                           | [Optional[models.CreateDraftTransferRequest]](../../models/createdrafttransferrequest.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |                                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[models.DraftTransferResponse](../../models/drafttransferresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 422, 429             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Retrieves a list of draft transfers for the organization including ones created in Mollie Apps, not just
ones created via this API.

The results are paginated.

In test mode, this always returns a synthetic `awaiting-initiation` list. See [Create draft
transfer](create-draft-transfer) for full test-mode behavior.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-draft-transfers" method="get" path="/v2/business-accounts/draft-transfers" example="list-draft-transfers-200" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        advanced_access_token=os.getenv("CLIENT_ADVANCED_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.draft_transfers.list(limit=50, status=mollie.DraftTransferStatus.AWAITING_INITIATION, source=mollie.DraftTransferSource.API, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              | Example                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `from_`                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                       | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                       |                                                                                                                                                                          |
| `limit`                                                                                                                                                                  | *OptionalNullable[int]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                       | The maximum number of items to return. Defaults to 50 items.                                                                                                             | 50                                                                                                                                                                       |
| `status`                                                                                                                                                                 | [Optional[models.DraftTransferStatus]](../../models/drafttransferstatus.md)                                                                                              | :heavy_minus_sign:                                                                                                                                                       | Filter the list by draft transfer status. Omit to return draft transfers in any status.                                                                                  | awaiting-initiation                                                                                                                                                      |
| `source`                                                                                                                                                                 | [Optional[models.DraftTransferSource]](../../models/drafttransfersource.md)                                                                                              | :heavy_minus_sign:                                                                                                                                                       | Filter the list by origin: `api` for draft transfers created via this API, `mollie-app` for ones created<br/>in Mollie Apps. Omit to return draft transfers from any source. | api                                                                                                                                                                      |
| `idempotency_key`                                                                                                                                                        | *Optional[str]*                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                       | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                         | 123e4567-e89b-12d3-a456-426                                                                                                                                              |
| `retries`                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                         | :heavy_minus_sign:                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                      |                                                                                                                                                                          |

### Response

**[models.ListDraftTransfersResponse](../../models/listdrafttransfersresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 429             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Retrieves a single draft transfer by its identifier.

Only draft transfers created via this API are visible via this endpoint. Draft transfers created in Mollie
Apps return a `404`, even though they appear in the [list endpoint](list-draft-transfers).

In test mode, this always returns a synthetic `awaiting-initiation` draft. See [Create draft
transfer](create-draft-transfer) for full test-mode behavior.

### Example Usage: get-draft-transfer-200

<!-- UsageSnippet language="python" operationID="get-draft-transfer" method="get" path="/v2/business-accounts/draft-transfers/{draftTransferId}" example="get-draft-transfer-200" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        advanced_access_token=os.getenv("CLIENT_ADVANCED_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.draft_transfers.get(draft_transfer_id="badrt_87GByBuj4UCcUTEbs6aGJ", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```
### Example Usage: initiated-draft-transfer

<!-- UsageSnippet language="python" operationID="get-draft-transfer" method="get" path="/v2/business-accounts/draft-transfers/{draftTransferId}" example="initiated-draft-transfer" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        advanced_access_token=os.getenv("CLIENT_ADVANCED_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.draft_transfers.get(draft_transfer_id="badrt_87GByBuj4UCcUTEbs6aGJ", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `draft_transfer_id`                                                              | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related draft transfer.                                    | badrt_87GByBuj4UCcUTEbs6aGJ                                                      |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.DraftTransferResponse](../../models/drafttransferresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 429             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## cancel

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Cancels a draft transfer created via this API. Transitions the draft transfer to `declined` with
`statusReason` set to `"Declined by creator"`.

Only draft transfers created via this API, and still in `awaiting-initiation`, can be cancelled this way. A
`422` is returned if the initiator has already started approving it.

In test mode, this always returns a synthetic `declined` draft. See [Create draft
transfer](create-draft-transfer) for full test-mode behavior.

### Example Usage

<!-- UsageSnippet language="python" operationID="cancel-draft-transfer" method="delete" path="/v2/business-accounts/draft-transfers/{draftTransferId}" example="cancel-draft-transfer-200" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        advanced_access_token=os.getenv("CLIENT_ADVANCED_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.draft_transfers.cancel(draft_transfer_id="badrt_87GByBuj4UCcUTEbs6aGJ", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `draft_transfer_id`                                                              | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related draft transfer.                                    | badrt_87GByBuj4UCcUTEbs6aGJ                                                      |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.DraftTransferResponse](../../models/drafttransferresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 422, 429        | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |