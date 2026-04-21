# Settlements

## Overview

### Available Operations

* [list](#list) - List settlements
* [get](#get) - Get settlement
* [get_open](#get_open) - Get open settlement
* [get_next](#get_next) - Get next settlement
* [list_payments](#list_payments) - List settlement payments
* [list_captures](#list_captures) - List settlement captures
* [list_refunds](#list_refunds) - List settlement refunds
* [list_chargebacks](#list_chargebacks) - List settlement chargebacks

## list

Retrieve a list of all your settlements.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-settlements" method="get" path="/v2/settlements" example="list-settlements-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list(limit=50, balance_id="bal_gVMhHKqSSRYJyPsuoPNFH", year="2025", month="1", currencies=mollie.Currencies.EUR, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `from_`                                                                                                                        | *OptionalNullable[str]*                                                                                                        | :heavy_minus_sign:                                                                                                             | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set. |                                                                                                                                |
| `limit`                                                                                                                        | *OptionalNullable[int]*                                                                                                        | :heavy_minus_sign:                                                                                                             | The maximum number of items to return. Defaults to 50 items.                                                                   | 50                                                                                                                             |
| `balance_id`                                                                                                                   | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Provide the token of the balance to filter the settlements by. This is<br/>the balance token that the settlement was settled to. | bal_gVMhHKqSSRYJyPsuoPNFH                                                                                                      |
| `year`                                                                                                                         | *OptionalNullable[str]*                                                                                                        | :heavy_minus_sign:                                                                                                             | Provide the year to query the settlements. Must be used combined with `month` parameter                                        | 2025                                                                                                                           |
| `month`                                                                                                                        | *OptionalNullable[str]*                                                                                                        | :heavy_minus_sign:                                                                                                             | Provide the month to query the settlements. Must be used combined with `year` parameter                                        | 1                                                                                                                              |
| `currencies`                                                                                                                   | [Optional[models.Currencies]](../../models/currencies.md)                                                                      | :heavy_minus_sign:                                                                                                             | Provides the currencies to retrieve the settlements. It accepts multiple currencies in a comma-separated format.               | EUR                                                                                                                            |
| `idempotency_key`                                                                                                              | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                               | 123e4567-e89b-12d3-a456-426                                                                                                    |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.ListSettlementsResponse](../../models/listsettlementsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 404             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

Retrieve a single settlement by its ID.

To lookup settlements by their bank reference, replace the ID in the URL by
a reference. For example: `1234567.2404.03`.

A settlement represents a transfer of your balance funds to your external bank account.

Settlements will typically include a report that details what balance transactions have taken place between this
settlement and the previous one.

For more accurate bookkeeping, refer to the [balance report](get-balance-report) endpoint or the
[balance transactions](list-balance-transactions) endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-settlement" method="get" path="/v2/settlements/{settlementId}" example="get-settlement-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.get(settlement_id="stl_5B8cwPMGnU", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `settlement_id`                                                                  | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related settlement.                                        | stl_5B8cwPMGnU                                                                   |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.EntitySettlement](../../models/entitysettlement.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get_open

Retrieve the details of the open balance of the organization. This will return a settlement object representing your
organization's balance.

For a complete reference of the settlement object, refer to the [Get settlement endpoint](get-settlement)
documentation.

For more accurate bookkeeping, refer to the [balance report](get-balance-report) endpoint or the
[balance transactions](list-balance-transactions) endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-open-settlement" method="get" path="/v2/settlements/open" example="get-settlement-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.get_open(idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.EntitySettlement](../../models/entitysettlement.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_next

Retrieve the details of the current settlement, that has not yet been paid out.

For a complete reference of the settlement object, refer to the [Get settlement endpoint](get-settlement)
documentation.

For more accurate bookkeeping, refer to the [balance report](get-balance-report) endpoint or the
[balance transactions](list-balance-transactions) endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-next-settlement" method="get" path="/v2/settlements/next" example="get-settlement-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.get_next(idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.EntitySettlement](../../models/entitysettlement.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## list_payments

Retrieve all payments included in the given settlement.

The response is in the same format as the response of the [List payments endpoint](list-payments).

For capture-based payment methods such as Klarna, the payments are not listed here. Refer to the
[List captures endpoint](list-captures) endpoint instead.

### Example Usage: list-payments-200-1

<!-- UsageSnippet language="python" operationID="list-settlement-payments" method="get" path="/v2/settlements/{settlementId}/payments" example="list-payments-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    profile_id="<id>",
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list_payments(settlement_id="stl_5B8cwPMGnU", from_="tr_5B8cwPMGnU", limit=50, sort=mollie.Sorting.DESC, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: list-payments-200-2

<!-- UsageSnippet language="python" operationID="list-settlement-payments" method="get" path="/v2/settlements/{settlementId}/payments" example="list-payments-200-2" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    profile_id="<id>",
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list_payments(settlement_id="stl_5B8cwPMGnU", from_="tr_5B8cwPMGnU", limit=50, sort=mollie.Sorting.DESC, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: list-payments-200-3

<!-- UsageSnippet language="python" operationID="list-settlement-payments" method="get" path="/v2/settlements/{settlementId}/payments" example="list-payments-200-3" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    profile_id="<id>",
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list_payments(settlement_id="stl_5B8cwPMGnU", from_="tr_5B8cwPMGnU", limit=50, sort=mollie.Sorting.DESC, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: list-settlement-payments-200-1

<!-- UsageSnippet language="python" operationID="list-settlement-payments" method="get" path="/v2/settlements/{settlementId}/payments" example="list-settlement-payments-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    profile_id="<id>",
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list_payments(settlement_id="stl_5B8cwPMGnU", from_="tr_5B8cwPMGnU", limit=50, sort=mollie.Sorting.DESC, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `settlement_id`                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                   | Provide the ID of the related settlement.                                                                                                                                                                                                                                                                            | stl_5B8cwPMGnU                                                                                                                                                                                                                                                                                                       |
| `from_`                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                   | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate<br/>the result set.                                                                                                                                                                                   | tr_5B8cwPMGnU                                                                                                                                                                                                                                                                                                        |
| `limit`                                                                                                                                                                                                                                                                                                              | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                   | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                         | 50                                                                                                                                                                                                                                                                                                                   |
| `sort`                                                                                                                                                                                                                                                                                                               | [Optional[models.Sorting]](../../models/sorting.md)                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                   | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from<br/>newest to oldest.                                                                                                                                                                           | desc                                                                                                                                                                                                                                                                                                                 |
| `profile_id`                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                   | The identifier referring to the [profile](get-profile) you wish to<br/>retrieve the resources for.<br/><br/>Most API credentials are linked to a single profile. In these cases the `profileId` must not be sent. For<br/>organization-level credentials such as OAuth access tokens however, the `profileId` parameter is required. |                                                                                                                                                                                                                                                                                                                      |
| `idempotency_key`                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                   | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                                                                                                                                                                     | 123e4567-e89b-12d3-a456-426                                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                      |

### Response

**[models.ListSettlementPaymentsResponse](../../models/listsettlementpaymentsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list_captures

Retrieve all captures included in the given settlement.

The response is in the same format as the response of the [List captures endpoint](list-captures).

### Example Usage: list-captures-200-1

<!-- UsageSnippet language="python" operationID="list-settlement-captures" method="get" path="/v2/settlements/{settlementId}/captures" example="list-captures-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list_captures(settlement_id="stl_5B8cwPMGnU", from_="cpt_vytxeTZskVKR7C7WgdSP3d", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: list-captures-200-2

<!-- UsageSnippet language="python" operationID="list-settlement-captures" method="get" path="/v2/settlements/{settlementId}/captures" example="list-captures-200-2" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list_captures(settlement_id="stl_5B8cwPMGnU", from_="cpt_vytxeTZskVKR7C7WgdSP3d", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: list-settlement-captures-200-1

<!-- UsageSnippet language="python" operationID="list-settlement-captures" method="get" path="/v2/settlements/{settlementId}/captures" example="list-settlement-captures-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list_captures(settlement_id="stl_5B8cwPMGnU", from_="cpt_vytxeTZskVKR7C7WgdSP3d", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `settlement_id`                                                                                                                | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | Provide the ID of the related settlement.                                                                                      | stl_5B8cwPMGnU                                                                                                                 |
| `from_`                                                                                                                        | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate<br/>the result set. | cpt_vytxeTZskVKR7C7WgdSP3d                                                                                                     |
| `limit`                                                                                                                        | *OptionalNullable[int]*                                                                                                        | :heavy_minus_sign:                                                                                                             | The maximum number of items to return. Defaults to 50 items.                                                                   | 50                                                                                                                             |
| `embed`                                                                                                                        | *OptionalNullable[str]*                                                                                                        | :heavy_minus_sign:                                                                                                             | This endpoint allows you to embed additional resources via the<br/>`embed` query string parameter.                             |                                                                                                                                |
| `idempotency_key`                                                                                                              | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                               | 123e4567-e89b-12d3-a456-426                                                                                                    |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.ListSettlementCapturesResponse](../../models/listsettlementcapturesresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 404             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list_refunds

Retrieve all refunds 'deducted' from the given settlement.

The response is in the same format as the response of the [List refunds endpoint](list-refunds).

### Example Usage: list-refunds-200-1

<!-- UsageSnippet language="python" operationID="list-settlement-refunds" method="get" path="/v2/settlements/{settlementId}/refunds" example="list-refunds-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list_refunds(settlement_id="stl_5B8cwPMGnU", from_="re_5B8cwPMGnU", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: list-settlement-refunds-200-1

<!-- UsageSnippet language="python" operationID="list-settlement-refunds" method="get" path="/v2/settlements/{settlementId}/refunds" example="list-settlement-refunds-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list_refunds(settlement_id="stl_5B8cwPMGnU", from_="re_5B8cwPMGnU", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `settlement_id`                                                                                                                | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | Provide the ID of the related settlement.                                                                                      | stl_5B8cwPMGnU                                                                                                                 |
| `from_`                                                                                                                        | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate<br/>the result set. | re_5B8cwPMGnU                                                                                                                  |
| `limit`                                                                                                                        | *OptionalNullable[int]*                                                                                                        | :heavy_minus_sign:                                                                                                             | The maximum number of items to return. Defaults to 50 items.                                                                   | 50                                                                                                                             |
| `embed`                                                                                                                        | *OptionalNullable[str]*                                                                                                        | :heavy_minus_sign:                                                                                                             | This endpoint allows embedding related API items by appending the following values via the `embed` query string<br/>parameter. |                                                                                                                                |
| `idempotency_key`                                                                                                              | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                               | 123e4567-e89b-12d3-a456-426                                                                                                    |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.ListSettlementRefundsResponse](../../models/listsettlementrefundsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 404             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list_chargebacks

Retrieve all chargebacks 'deducted' from the given settlement.

The response is in the same format as the response of the [List chargebacks endpoint](list-chargebacks).

### Example Usage: list-chargeback-200-1

<!-- UsageSnippet language="python" operationID="list-settlement-chargebacks" method="get" path="/v2/settlements/{settlementId}/chargebacks" example="list-chargeback-200-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    testmode=False,
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list_chargebacks(settlement_id="stl_5B8cwPMGnU", from_="chb_xFzwUN4ci8HAmSGUACS4J", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: list-chargeback-200-2

<!-- UsageSnippet language="python" operationID="list-settlement-chargebacks" method="get" path="/v2/settlements/{settlementId}/chargebacks" example="list-chargeback-200-2" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    testmode=False,
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list_chargebacks(settlement_id="stl_5B8cwPMGnU", from_="chb_xFzwUN4ci8HAmSGUACS4J", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```
### Example Usage: list-chargeback-200-3

<!-- UsageSnippet language="python" operationID="list-settlement-chargebacks" method="get" path="/v2/settlements/{settlementId}/chargebacks" example="list-chargeback-200-3" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    testmode=True,
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.settlements.list_chargebacks(settlement_id="stl_5B8cwPMGnU", from_="chb_xFzwUN4ci8HAmSGUACS4J", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `settlement_id`                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                       | Provide the ID of the related settlement.                                                                                                                                                                                                                                                                                                                                                | stl_5B8cwPMGnU                                                                                                                                                                                                                                                                                                                                                                           |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                                                                                                                                                                                                                                       | chb_xFzwUN4ci8HAmSGUACS4J                                                                                                                                                                                                                                                                                                                                                                |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                  | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                             | 50                                                                                                                                                                                                                                                                                                                                                                                       |
| `embed`                                                                                                                                                                                                                                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | This endpoint allows you to embed additional information via the `embed` query string parameter.                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                          |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter must not be sent. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                                                                                                          |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                                                                                                                                                                                                                                         | 123e4567-e89b-12d3-a456-426                                                                                                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                          |

### Response

**[models.ListSettlementChargebacksResponse](../../models/listsettlementchargebacksresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 404             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |