# Invoices
(*invoices*)

## Overview

### Available Operations

* [list](#list) - List invoices
* [get](#get) - Get invoice

## list

Retrieve a list of all your invoices, optionally filtered by year or by
invoice reference.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-invoices" method="get" path="/invoices" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.invoices.list(reference="2024.10000", year="2024", from_="inv_xBEbP9rvAq", limit=50, sort=mollie.Sorting.DESC, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            | Example                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `reference`                                                                                                                            | *OptionalNullable[str]*                                                                                                                | :heavy_minus_sign:                                                                                                                     | Filter for an invoice with a specific invoice reference, for example<br/>`2024.10000`.                                                 | 2024.10000                                                                                                                             |
| `year`                                                                                                                                 | *OptionalNullable[str]*                                                                                                                | :heavy_minus_sign:                                                                                                                     | Filter for invoices of a specific year, for example `2024`.                                                                            | 2024                                                                                                                                   |
| `from_`                                                                                                                                | *OptionalNullable[str]*                                                                                                                | :heavy_minus_sign:                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.     |                                                                                                                                        |
| `limit`                                                                                                                                | *OptionalNullable[int]*                                                                                                                | :heavy_minus_sign:                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                           | 50                                                                                                                                     |
| `sort`                                                                                                                                 | [Optional[models.Sorting]](../../models/sorting.md)                                                                                    | :heavy_minus_sign:                                                                                                                     | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from<br/>newest to oldest. | desc                                                                                                                                   |
| `idempotency_key`                                                                                                                      | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                       | 123e4567-e89b-12d3-a456-426                                                                                                            |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |                                                                                                                                        |

### Response

**[models.ListInvoicesResponse](../../models/listinvoicesresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 404             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

Retrieve a single invoice by its ID.

If you want to retrieve the details of an invoice by its invoice number,
call the [List invoices](list-invoices) endpoint with the `reference` parameter.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-invoice" method="get" path="/invoices/{invoiceId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.invoices.get(invoice_id="inv_aHbjjdrUdm", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `invoice_id`                                                                     | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related invoice.                                           | inv_aHbjjdrUdm                                                                   |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.EntityInvoice](../../models/entityinvoice.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |