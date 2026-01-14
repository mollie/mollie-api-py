# Balances
(*balances*)

## Overview

### Available Operations

* [list](#list) - List balances
* [get](#get) - Get balance
* [get_primary](#get_primary) - Get primary balance
* [get_report](#get_report) - Get balance report
* [list_transactions](#list_transactions) - List balance transactions

## list

Retrieve a list of the organization's balances, including the primary balance.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-balances" method="get" path="/balances" -->
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

    res = client_sdk.balances.list(currency="EUR", from_="bal_gVMhHKqSSRYJyPsuoPNFH", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             | Example                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `currency`                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Optionally only return balances with the given currency. For example: `EUR`.                                                                                            | EUR                                                                                                                                                                     |
| `from_`                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                      |                                                                                                                                                                         |
| `limit`                                                                                                                                                                 | *OptionalNullable[int]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | The maximum number of items to return. Defaults to 50 items.                                                                                                            | 50                                                                                                                                                                      |
| `testmode`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | You can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                         |
| `idempotency_key`                                                                                                                                                       | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                        | 123e4567-e89b-12d3-a456-426                                                                                                                                             |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |                                                                                                                                                                         |

### Response

**[models.ListBalancesResponse](../../models/listbalancesresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 404             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

When processing payments with Mollie, we put all pending funds — usually
minus Mollie fees — on a balance. Once you have linked a bank account to your Mollie account, we can pay out your
balance towards this bank account.

With the Balances API you can retrieve your current balance. The response
includes two amounts:

* The *pending amount*. These are payments that have been marked as `paid`,
but are not yet available on your balance.
* The *available amount*. This is the amount that you can get paid out to
your bank account, or use for refunds.

With instant payment methods like iDEAL, payments are moved to the available
balance instantly. With slower payment methods, like credit card for example, it can take a few days before the
funds are available on your balance. These funds will be shown under the *pending amount* in the meanwhile.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-balance" method="get" path="/balances/{balanceId}" -->
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

    res = client_sdk.balances.get(balance_id="bal_gVMhHKqSSRYJyPsuoPNFH", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             | Example                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `balance_id`                                                                                                                                                            | *str*                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                      | Provide the ID of the related balance.                                                                                                                                  | bal_gVMhHKqSSRYJyPsuoPNFH                                                                                                                                               |
| `testmode`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | You can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                         |
| `idempotency_key`                                                                                                                                                       | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                        | 123e4567-e89b-12d3-a456-426                                                                                                                                             |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |                                                                                                                                                                         |

### Response

**[models.EntityBalance](../../models/entitybalance.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get_primary

Retrieve the primary balance. This is the balance of your account's primary
currency, where all payments are settled to by default.

This endpoint is a convenient alias of the [Get balance](get-balance)
endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-primary-balance" method="get" path="/balances/primary" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.balances.get_primary(idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.EntityBalance](../../models/entitybalance.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_report

Retrieve a summarized report for all transactions on a given balance within a given timeframe.

The API also provides a detailed report on all 'prepayments' for Mollie fees that were deducted from your balance
during the reported period, ahead of your Mollie invoice.

The alias `primary` can be used instead of the balance ID to refer to the
organization's primary balance.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-balance-report" method="get" path="/balances/{balanceId}/report" -->
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

    res = client_sdk.balances.get_report(balance_id="bal_gVMhHKqSSRYJyPsuoPNFH", from_="2024-01-01", until="2024-02-01", grouping=mollie.BalanceReportGrouping.STATUS_BALANCES, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `balance_id`                                                                                                                                                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                       | Provide the ID of the related balance.                                                                                                                                                                                                                                                                                                                                                                                   | bal_gVMhHKqSSRYJyPsuoPNFH                                                                                                                                                                                                                                                                                                                                                                                                |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                       | The start date of the report, in `YYYY-MM-DD` format. The from date is<br/>'inclusive', and in Central European Time. This means a report with for example `from=2024-01-01` will<br/>include transactions from 2024-01-01 0:00:00 CET and onwards.                                                                                                                                                                      | 2024-01-01                                                                                                                                                                                                                                                                                                                                                                                                               |
| `until`                                                                                                                                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                       | The end date of the report, in `YYYY-MM-DD` format. The until date is 'exclusive', and in Central European Time.<br/>This means a report with for example `until=2024-02-01` will include transactions up until<br/>2024-01-31 23:59:59 CET.                                                                                                                                                                             | 2024-02-01                                                                                                                                                                                                                                                                                                                                                                                                               |
| `grouping`                                                                                                                                                                                                                                                                                                                                                                                                               | [Optional[models.BalanceReportGrouping]](../../models/balancereportgrouping.md)                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                       | You can retrieve reports in two different formats. With the `status-balances` format, transactions are grouped<br/>by status (e.g. `pending`, `available`), then by transaction type, and then by other sub-groupings where<br/>available (e.g. payment method).<br/><br/>With the `transaction-categories` format, transactions are grouped by<br/>transaction type, then by status, and then again by other sub-groupings where available. | status-balances                                                                                                                                                                                                                                                                                                                                                                                                          |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                       | You can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa.                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                       | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                                                                                                                                                                                                                                                                         | 123e4567-e89b-12d3-a456-426                                                                                                                                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                          |

### Response

**[models.EntityBalanceReport](../../models/entitybalancereport.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 422             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list_transactions

Retrieve a list of all balance transactions. Transactions include for
example payments, refunds, chargebacks, and settlements.

For an aggregated report of these balance transactions, refer to the [Get
balance report](get-balance-report) endpoint.

The alias `primary` can be used instead of the balance ID to refer to the
organization's primary balance.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-balance-transactions" method="get" path="/balances/{balanceId}/transactions" -->
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

    res = client_sdk.balances.list_transactions(balance_id="bal_gVMhHKqSSRYJyPsuoPNFH", from_="baltr_QM24QwzUWR4ev4Xfgyt29A", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             | Example                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `balance_id`                                                                                                                                                            | *str*                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                      | Provide the ID of the related balance.                                                                                                                                  | bal_gVMhHKqSSRYJyPsuoPNFH                                                                                                                                               |
| `from_`                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                      |                                                                                                                                                                         |
| `limit`                                                                                                                                                                 | *OptionalNullable[int]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | The maximum number of items to return. Defaults to 50 items.                                                                                                            | 50                                                                                                                                                                      |
| `testmode`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | You can enable test mode by setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                         |
| `idempotency_key`                                                                                                                                                       | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                        | 123e4567-e89b-12d3-a456-426                                                                                                                                             |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |                                                                                                                                                                         |

### Response

**[models.ListBalanceTransactionsResponse](../../models/listbalancetransactionsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 404, 429        | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |