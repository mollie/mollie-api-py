# SalesInvoices
(*sales_invoices*)

## Overview

### Available Operations

* [create](#create) - Create sales invoice
* [list](#list) - List sales invoices
* [get](#get) - Get sales invoice
* [update](#update) - Update sales invoice
* [delete](#delete) - Delete sales invoice

## create

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

With the Sales Invoice API you can generate sales invoices to send to your customers.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-sales-invoice" method="post" path="/sales-invoices" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.sales_invoices.create(idempotency_key="123e4567-e89b-12d3-a456-426", sales_invoice_request={
        "testmode": False,
        "profile_id": "pfl_QkEhN94Ba",
        "status": mollie.SalesInvoiceStatus.DRAFT,
        "vat_scheme": mollie.SalesInvoiceVatScheme.STANDARD,
        "vat_mode": mollie.SalesInvoiceVatMode.EXCLUSIVE,
        "memo": "This is a memo!",
        "payment_term": mollie.SalesInvoicePaymentTerm.THIRTYDAYS,
        "payment_details": {
            "source": mollie.SalesInvoicePaymentDetailsSource.PAYMENT_LINK,
            "source_reference": "pl_d9fQur83kFdhH8hIhaZfq",
        },
        "email_details": {
            "subject": "Your invoice is available",
            "body": "Please find your invoice enclosed.",
        },
        "customer_id": "cst_8wmqcHMN4U",
        "mandate_id": "mdt_pWUnw6pkBN",
        "recipient_identifier": "customer-xyz-0123",
        "recipient": {
            "type": mollie.SalesInvoiceRecipientType.CONSUMER,
            "title": "Mrs.",
            "given_name": "Jane",
            "family_name": "Doe",
            "organization_name": "Organization Corp.",
            "organization_number": "12345678",
            "vat_number": "NL123456789B01",
            "email": "example@email.com",
            "phone": "+0123456789",
            "street_and_number": "Keizersgracht 126",
            "street_additional": "4th floor",
            "postal_code": "5678AB",
            "city": "Amsterdam",
            "region": "Noord-Holland",
            "country": "NL",
            "locale": mollie.SalesInvoiceRecipientLocale.NL_NL,
        },
        "lines": [],
        "discount": {
            "type": mollie.SalesInvoiceDiscountType.AMOUNT,
            "value": "10.00",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `sales_invoice_request`                                                          | [Optional[models.SalesInvoiceRequest]](../../models/salesinvoicerequest.md)      | :heavy_minus_sign:                                                               | N/A                                                                              |                                                                                  |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.SalesInvoiceResponse](../../models/salesinvoiceresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 422             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Retrieve a list of all sales invoices created through the API.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-sales-invoices" method="get" path="/sales-invoices" -->
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

    res = client_sdk.sales_invoices.list(from_="invoice_4Y0eZitmBnQ6IDoMqZQKh", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                        |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                           | 50                                                                                                                                                                                                                                                                                                                                                                                     |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                                                                                                        |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                                                                                                                                                                                                                                       | 123e4567-e89b-12d3-a456-426                                                                                                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ListSalesInvoicesResponse](../../models/listsalesinvoicesresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Retrieve a single sales invoice by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-sales-invoice" method="get" path="/sales-invoices/{salesInvoiceId}" -->
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

    res = client_sdk.sales_invoices.get(sales_invoice_id="invoice_4Y0eZitmBnQ6IDoMqZQKh", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sales_invoice_id`                                                                                                                                                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the related sales invoice.                                                                                                                                                                                                                                                                                                                                           | invoice_4Y0eZitmBnQ6IDoMqZQKh                                                                                                                                                                                                                                                                                                                                                          |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                                                                                                        |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                                                                                                                                                                                                                                       | 123e4567-e89b-12d3-a456-426                                                                                                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.SalesInvoiceResponse](../../models/salesinvoiceresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## update

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Certain details of an existing sales invoice can be updated. For `draft` it is all values listed below, but for
statuses `paid` and `issued` there are certain additional requirements (`paymentDetails` and `emailDetails`,
respectively).

### Example Usage

<!-- UsageSnippet language="python" operationID="update-sales-invoice" method="patch" path="/sales-invoices/{salesInvoiceId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.sales_invoices.update(sales_invoice_id="invoice_4Y0eZitmBnQ6IDoMqZQKh", idempotency_key="123e4567-e89b-12d3-a456-426", update_values_sales_invoice={
        "testmode": False,
        "status": mollie.SalesInvoiceStatus.DRAFT,
        "memo": "An updated memo!",
        "payment_term": mollie.SalesInvoicePaymentTerm.THIRTYDAYS,
        "payment_details": {
            "source": mollie.SalesInvoicePaymentDetailsSource.PAYMENT_LINK,
            "source_reference": "pl_d9fQur83kFdhH8hIhaZfq",
        },
        "email_details": {
            "subject": "Your invoice is available",
            "body": "Please find your invoice enclosed.",
        },
        "recipient_identifier": "customer-xyz-0123",
        "recipient": {
            "type": mollie.SalesInvoiceRecipientType.CONSUMER,
            "title": "Mrs.",
            "given_name": "Jane",
            "family_name": "Doe",
            "organization_name": "Organization Corp.",
            "organization_number": "12345678",
            "vat_number": "NL123456789B01",
            "email": "example@email.com",
            "phone": "+0123456789",
            "street_and_number": "Keizersgracht 126",
            "street_additional": "4th floor",
            "postal_code": "5678AB",
            "city": "Amsterdam",
            "region": "Noord-Holland",
            "country": "NL",
            "locale": mollie.SalesInvoiceRecipientLocale.NL_NL,
        },
        "lines": [
            {
                "description": "LEGO 4440 Forest Police Station",
                "quantity": 1,
                "vat_rate": "21.00",
                "unit_price": {
                    "currency": "EUR",
                    "value": "10.00",
                },
                "discount": {
                    "type": mollie.SalesInvoiceDiscountType.AMOUNT,
                    "value": "10.00",
                },
            },
        ],
        "discount": {
            "type": mollie.SalesInvoiceDiscountType.AMOUNT,
            "value": "10.00",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `sales_invoice_id`                                                                    | *str*                                                                                 | :heavy_check_mark:                                                                    | Provide the ID of the related sales invoice.                                          | invoice_4Y0eZitmBnQ6IDoMqZQKh                                                         |
| `idempotency_key`                                                                     | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | A unique key to ensure idempotent requests. This key should be a UUID v4 string.      | 123e4567-e89b-12d3-a456-426                                                           |
| `update_values_sales_invoice`                                                         | [Optional[models.UpdateValuesSalesInvoice]](../../models/updatevaluessalesinvoice.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |                                                                                       |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |

### Response

**[models.SalesInvoiceResponse](../../models/salesinvoiceresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 422             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## delete

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Sales invoices which are in status `draft` can be deleted. For all other statuses, please use the
[Update sales invoice](update-sales-invoice) endpoint instead.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-sales-invoice" method="delete" path="/sales-invoices/{salesInvoiceId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    client_sdk.sales_invoices.delete(sales_invoice_id="invoice_4Y0eZitmBnQ6IDoMqZQKh", idempotency_key="123e4567-e89b-12d3-a456-426", delete_values_sales_invoice={
        "testmode": False,
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `sales_invoice_id`                                                                    | *str*                                                                                 | :heavy_check_mark:                                                                    | Provide the ID of the related sales invoice.                                          | invoice_4Y0eZitmBnQ6IDoMqZQKh                                                         |
| `idempotency_key`                                                                     | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | A unique key to ensure idempotent requests. This key should be a UUID v4 string.      | 123e4567-e89b-12d3-a456-426                                                           |
| `delete_values_sales_invoice`                                                         | [Optional[models.DeleteValuesSalesInvoice]](../../models/deletevaluessalesinvoice.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |                                                                                       |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 422             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |