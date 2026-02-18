# PaymentLinks
(*payment_links*)

## Overview

### Available Operations

* [create](#create) - Create payment link
* [list](#list) - List payment links
* [get](#get) - Get payment link
* [update](#update) - Update payment link
* [delete](#delete) - Delete payment link
* [list_payments](#list_payments) - Get payment link payments

## create

With the Payment links API you can generate payment links that by default, unlike regular payments, do not expire.
The payment link can be shared with your customers and will redirect them to them the payment page where they can
complete the payment. A [payment](get-payment) will only be created once the customer initiates the payment.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-payment-link" method="post" path="/payment-links" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payment_links.create(idempotency_key="123e4567-e89b-12d3-a456-426", request_body=mollie.CreatePaymentLinkRequestBody(
        description="Chess Board",
        amount=mollie.AmountNullable(
            currency="EUR",
            value="10.00",
        ),
        minimum_amount=mollie.AmountNullable(
            currency="EUR",
            value="10.00",
        ),
        redirect_url="https://webshop.example.org/payment-links/redirect/",
        webhook_url="https://webshop.example.org/payment-links/webhook/",
        lines=[
            mollie.PaymentLineItem(
                type=mollie.PaymentLineType.PHYSICAL,
                description="LEGO 4440 Forest Police Station",
                quantity=1,
                quantity_unit="pcs",
                unit_price=mollie.Amount(
                    currency="EUR",
                    value="10.00",
                ),
                discount_amount=mollie.Amount(
                    currency="EUR",
                    value="10.00",
                ),
                total_amount=mollie.Amount(
                    currency="EUR",
                    value="10.00",
                ),
                vat_rate="21.00",
                vat_amount=mollie.Amount(
                    currency="EUR",
                    value="10.00",
                ),
                sku="9780241661628",
                categories=[
                    mollie.LineCategories.MEAL,
                    mollie.LineCategories.ECO,
                ],
                image_url="https://...",
                product_url="https://...",
            ),
        ],
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
        profile_id="pfl_QkEhN94Ba",
        reusable=False,
        expires_at="2025-12-24T11:00:16+00:00",
        allowed_methods=[
            mollie.PaymentLinkMethod.IDEAL,
        ],
        application_fee=mollie.CreatePaymentLinkApplicationFee(
            amount=mollie.Amount(
                currency="EUR",
                value="10.00",
            ),
            description="Platform fee",
        ),
        sequence_type=mollie.PaymentLinkSequenceType.ONEOFF,
        customer_id="cst_XimFHuaEzd",
        testmode=False,
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `idempotency_key`                                                                             | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | A unique key to ensure idempotent requests. This key should be a UUID v4 string.              | 123e4567-e89b-12d3-a456-426                                                                   |
| `request_body`                                                                                | [Optional[models.CreatePaymentLinkRequestBody]](../../models/createpaymentlinkrequestbody.md) | :heavy_minus_sign:                                                                            | N/A                                                                                           |                                                                                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[models.PaymentLinkResponse](../../models/paymentlinkresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 422             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list

Retrieve a list of all payment links.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-payment-links" method="get" path="/payment-links" -->
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

    res = client_sdk.payment_links.list(from_="pl_d9fQur83kFdhH8hIhaZfq", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                                                                                                                                                                                                                                       | pl_d9fQur83kFdhH8hIhaZfq                                                                                                                                                                                                                                                                                                                                                                 |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                  | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                             | 50                                                                                                                                                                                                                                                                                                                                                                                       |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter must not be sent. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                                                                                                          |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                                                                                                                                                                                                                                         | 123e4567-e89b-12d3-a456-426                                                                                                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                          |

### Response

**[models.ListPaymentLinksResponse](../../models/listpaymentlinksresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

Retrieve a single payment link by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-payment-link" method="get" path="/payment-links/{paymentLinkId}" -->
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

    res = client_sdk.payment_links.get(payment_link_id="pl_d9fQur83kFdhH8hIhaZfq", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_link_id`                                                                                                                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                       | Provide the ID of the related payment link.                                                                                                                                                                                                                                                                                                                                              | pl_d9fQur83kFdhH8hIhaZfq                                                                                                                                                                                                                                                                                                                                                                 |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter must not be sent. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                                                                                                          |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                                                                                                                                                                                                                                         | 123e4567-e89b-12d3-a456-426                                                                                                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                          |

### Response

**[models.PaymentLinkResponse](../../models/paymentlinkresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## update

Certain details of an existing payment link can be updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="update-payment-link" method="patch" path="/payment-links/{paymentLinkId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.payment_links.update(payment_link_id="pl_d9fQur83kFdhH8hIhaZfq", idempotency_key="123e4567-e89b-12d3-a456-426", request_body=mollie.UpdatePaymentLinkRequestBody(
        description="Chess Board",
        minimum_amount=mollie.Amount(
            currency="EUR",
            value="10.00",
        ),
        archived=False,
        allowed_methods=[
            mollie.PaymentLinkMethod.IDEAL,
        ],
        lines=[
            mollie.PaymentLineItem(
                type=mollie.PaymentLineType.PHYSICAL,
                description="LEGO 4440 Forest Police Station",
                quantity=1,
                quantity_unit="pcs",
                unit_price=mollie.Amount(
                    currency="EUR",
                    value="10.00",
                ),
                discount_amount=mollie.Amount(
                    currency="EUR",
                    value="10.00",
                ),
                total_amount=mollie.Amount(
                    currency="EUR",
                    value="10.00",
                ),
                vat_rate="21.00",
                vat_amount=mollie.Amount(
                    currency="EUR",
                    value="10.00",
                ),
                sku="9780241661628",
                categories=[
                    mollie.LineCategories.MEAL,
                    mollie.LineCategories.ECO,
                ],
                image_url="https://...",
                product_url="https://...",
            ),
        ],
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
        testmode=False,
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `payment_link_id`                                                                             | *str*                                                                                         | :heavy_check_mark:                                                                            | Provide the ID of the related payment link.                                                   | pl_d9fQur83kFdhH8hIhaZfq                                                                      |
| `idempotency_key`                                                                             | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | A unique key to ensure idempotent requests. This key should be a UUID v4 string.              | 123e4567-e89b-12d3-a456-426                                                                   |
| `request_body`                                                                                | [Optional[models.UpdatePaymentLinkRequestBody]](../../models/updatepaymentlinkrequestbody.md) | :heavy_minus_sign:                                                                            | N/A                                                                                           |                                                                                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[models.PaymentLinkResponse](../../models/paymentlinkresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 422             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## delete

Payment links which have not been opened and no payments have been made yet can be deleted entirely.
This can be useful for removing payment links that have been incorrectly configured or that are no longer relevant.

Once deleted, the payment link will no longer show up in the API or Mollie dashboard.

To simply disable a payment link without fully deleting it, you can use the `archived` parameter on the
[Update payment link](update-payment-link) endpoint instead.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-payment-link" method="delete" path="/payment-links/{paymentLinkId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    client_sdk.payment_links.delete(payment_link_id="pl_d9fQur83kFdhH8hIhaZfq", idempotency_key="123e4567-e89b-12d3-a456-426", request_body={
        "testmode": False,
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `payment_link_id`                                                                             | *str*                                                                                         | :heavy_check_mark:                                                                            | Provide the ID of the related payment link.                                                   | pl_d9fQur83kFdhH8hIhaZfq                                                                      |
| `idempotency_key`                                                                             | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | A unique key to ensure idempotent requests. This key should be a UUID v4 string.              | 123e4567-e89b-12d3-a456-426                                                                   |
| `request_body`                                                                                | [Optional[models.DeletePaymentLinkRequestBody]](../../models/deletepaymentlinkrequestbody.md) | :heavy_minus_sign:                                                                            | N/A                                                                                           |                                                                                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404, 422             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list_payments

Retrieve the list of payments for a specific payment link.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-payment-link-payments" method="get" path="/payment-links/{paymentLinkId}/payments" -->
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

    res = client_sdk.payment_links.list_payments(payment_link_id="pl_d9fQur83kFdhH8hIhaZfq", from_="tr_5B8cwPMGnU", limit=50, sort=mollie.Sorting.DESC, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `payment_link_id`                                                                                                                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                       | Provide the ID of the related payment link.                                                                                                                                                                                                                                                                                                                                              | pl_d9fQur83kFdhH8hIhaZfq                                                                                                                                                                                                                                                                                                                                                                 |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                                                                                                                                                                                                                                       | tr_5B8cwPMGnU                                                                                                                                                                                                                                                                                                                                                                            |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                  | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                             | 50                                                                                                                                                                                                                                                                                                                                                                                       |
| `sort`                                                                                                                                                                                                                                                                                                                                                                                   | [Optional[models.Sorting]](../../models/sorting.md)                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from<br/>newest to oldest.                                                                                                                                                                                                                                               | desc                                                                                                                                                                                                                                                                                                                                                                                     |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter must not be sent. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                                                                                                          |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                                                                                                                                                                                                                                         | 123e4567-e89b-12d3-a456-426                                                                                                                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                          |

### Response

**[models.GetPaymentLinkPaymentsResponse](../../models/getpaymentlinkpaymentsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |