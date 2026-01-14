# Customers
(*customers*)

## Overview

### Available Operations

* [create](#create) - Create customer
* [list](#list) - List customers
* [get](#get) - Get customer
* [update](#update) - Update customer
* [delete](#delete) - Delete customer
* [create_payment](#create_payment) - Create customer payment
* [list_payments](#list_payments) - List customer payments

## create

Creates a simple minimal representation of a customer. Payments, recurring mandates, and subscriptions can be linked
to this customer object, which simplifies management of recurring payments.

Once registered, customers will also appear in your Mollie dashboard.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-customer" method="post" path="/customers" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.customers.create(idempotency_key="123e4567-e89b-12d3-a456-426", entity_customer={
        "name": "John Doe",
        "email": "example@email.com",
        "locale": mollie.LocaleResponse.EN_US,
        "testmode": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `entity_customer`                                                                | [Optional[models.EntityCustomer]](../../models/entitycustomer.md)                | :heavy_minus_sign:                                                               | N/A                                                                              |                                                                                  |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.CustomerResponse](../../models/customerresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list

Retrieve a list of all customers.

The results are paginated.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-customers" method="get" path="/customers" -->
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

    res = client_sdk.customers.list(from_="cst_5B8cwPMGnU", limit=50, sort=mollie.Sorting.DESC, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate the<br/>result set.                                                                                                                                                                                                                                                     | cst_5B8cwPMGnU                                                                                                                                                                                                                                                                                                                                                                         |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                           | 50                                                                                                                                                                                                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.Sorting]](../../models/sorting.md)                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from<br/>newest to oldest.                                                                                                                                                                                                                                             | desc                                                                                                                                                                                                                                                                                                                                                                                   |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                                                                                                        |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                                                                                                                                                                                                                                       | 123e4567-e89b-12d3-a456-426                                                                                                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ListCustomersResponse](../../models/listcustomersresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 404             | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

Retrieve a single customer by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-customer" method="get" path="/customers/{customerId}" -->
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

    res = client_sdk.customers.get(customer_id="cst_5B8cwPMGnU", include="events", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `customer_id`                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the related customer.                                                                                                                                                                                                                                                                                                                                                | cst_5B8cwPMGnU                                                                                                                                                                                                                                                                                                                                                                         |
| `include`                                                                                                                                                                                                                                                                                                                                                                              | *OptionalNullable[str]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | This endpoint allows you to include additional information via the `include` query string parameter.                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                        |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                                                                                                        |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                                                                                                                                                                                                                                       | 123e4567-e89b-12d3-a456-426                                                                                                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.GetCustomerResponse](../../models/getcustomerresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## update

Update an existing customer.

For an in-depth explanation of each parameter, refer to the [Create customer](create-customer) endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="update-customer" method="patch" path="/customers/{customerId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.customers.update(customer_id="cst_5B8cwPMGnU", idempotency_key="123e4567-e89b-12d3-a456-426", entity_customer={
        "name": "John Doe",
        "email": "example@email.com",
        "locale": mollie.LocaleResponse.EN_US,
        "testmode": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `customer_id`                                                                    | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related customer.                                          | cst_5B8cwPMGnU                                                                   |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `entity_customer`                                                                | [Optional[models.EntityCustomer]](../../models/entitycustomer.md)                | :heavy_minus_sign:                                                               | N/A                                                                              |                                                                                  |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.CustomerResponse](../../models/customerresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## delete

Delete a customer. All mandates and subscriptions created for this customer will be canceled as well.

### Example Usage

<!-- UsageSnippet language="python" operationID="delete-customer" method="delete" path="/customers/{customerId}" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    client_sdk.customers.delete(customer_id="cst_5B8cwPMGnU", idempotency_key="123e4567-e89b-12d3-a456-426", request_body={
        "testmode": False,
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             | Example                                                                                 |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `customer_id`                                                                           | *str*                                                                                   | :heavy_check_mark:                                                                      | Provide the ID of the related customer.                                                 | cst_5B8cwPMGnU                                                                          |
| `idempotency_key`                                                                       | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | A unique key to ensure idempotent requests. This key should be a UUID v4 string.        | 123e4567-e89b-12d3-a456-426                                                             |
| `request_body`                                                                          | [Optional[models.DeleteCustomerRequestBody]](../../models/deletecustomerrequestbody.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |                                                                                         |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |                                                                                         |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 404                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## create_payment

Creates a payment for the customer.

Linking customers to payments enables you to:

* Keep track of payment preferences for your customers
* Allow your customers to charge a previously used credit card with a single click in our hosted checkout
* Improve payment insights in the Mollie dashboard
* Use recurring payments

This endpoint is effectively an alias of the [Create payment endpoint](create-payment) with the `customerId`
parameter predefined.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-customer-payment" method="post" path="/customers/{customerId}/payments" -->
```python
from datetime import date
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.customers.create_payment(customer_id="cst_5B8cwPMGnU", idempotency_key="123e4567-e89b-12d3-a456-426", payment_request=mollie.PaymentRequest(
        description="Chess Board",
        amount=mollie.Amount(
            currency="EUR",
            value="10.00",
        ),
        redirect_url="https://example.org/redirect",
        cancel_url="https://example.org/cancel",
        webhook_url="https://example.org/webhooks",
        lines=[
            mollie.PaymentRequestLine(
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
                recurring=mollie.RecurringLineItem(
                    description="Gym subscription",
                    interval="... months",
                    amount=mollie.Amount(
                        currency="EUR",
                        value="10.00",
                    ),
                    times=1,
                    start_date="2024-12-12",
                ),
            ),
        ],
        billing_address=mollie.PaymentRequestBillingAddress(
            title="Mr.",
            given_name="Piet",
            family_name="Mondriaan",
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
        locale=mollie.Locale.EN_US,
        method=mollie.MethodEnum.IDEAL,
        issuer="ideal_INGBNL2A",
        restrict_payment_methods_to_country="NL",
        capture_mode=mollie.CaptureMode.MANUAL,
        capture_delay="8 hours",
        application_fee=mollie.PaymentRequestApplicationFee(
            amount=mollie.Amount(
                currency="EUR",
                value="10.00",
            ),
            description="10",
        ),
        routing=[
            mollie.EntityPaymentRoute(
                amount=mollie.Amount(
                    currency="EUR",
                    value="10.00",
                ),
                destination=mollie.EntityPaymentRouteDestination(
                    type=mollie.RouteDestinationType.ORGANIZATION,
                    organization_id="org_1234567",
                ),
                release_date="2024-12-12",
                links=mollie.EntityPaymentRouteLinks(
                    self_=mollie.URL(
                        href="https://...",
                        type="application/hal+json",
                    ),
                    payment=mollie.URL(
                        href="https://...",
                        type="application/hal+json",
                    ),
                ),
            ),
            mollie.EntityPaymentRoute(
                amount=mollie.Amount(
                    currency="EUR",
                    value="10.00",
                ),
                destination=mollie.EntityPaymentRouteDestination(
                    type=mollie.RouteDestinationType.ORGANIZATION,
                    organization_id="org_1234567",
                ),
                release_date="2024-12-12",
                links=mollie.EntityPaymentRouteLinks(
                    self_=mollie.URL(
                        href="https://...",
                        type="application/hal+json",
                    ),
                    payment=mollie.URL(
                        href="https://...",
                        type="application/hal+json",
                    ),
                ),
            ),
        ],
        sequence_type=mollie.SequenceType.ONEOFF,
        mandate_id="mdt_5B8cwPMGnU",
        customer_id="cst_5B8cwPMGnU",
        profile_id="pfl_5B8cwPMGnU",
        due_date="2025-01-01",
        testmode=False,
        apple_pay_payment_token="{\"paymentData\": {\"version\": \"EC_v1\", \"data\": \"vK3BbrCbI/....\"}}",
        company=mollie.Company(
            registration_number="12345678",
            vat_number="NL123456789B01",
        ),
        card_token="tkn_12345",
        voucher_number="1234567890",
        voucher_pin="1234",
        consumer_date_of_birth=date.fromisoformat("2000-01-01"),
        digital_goods=True,
        customer_reference="1234567890",
        terminal_id="term_1234567890",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `customer_id`                                                                    | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related customer.                                          | cst_5B8cwPMGnU                                                                   |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `payment_request`                                                                | [Optional[models.PaymentRequest]](../../models/paymentrequest.md)                | :heavy_minus_sign:                                                               | N/A                                                                              |                                                                                  |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.PaymentResponse](../../models/paymentresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 422                  | application/hal+json |
| models.ErrorResponse | 503                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## list_payments

Retrieve all payments linked to the customer.

### Example Usage

<!-- UsageSnippet language="python" operationID="list-customer-payments" method="get" path="/customers/{customerId}/payments" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    profile_id="pfl_5B8cwPMGnU",
    testmode=False,
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.customers.list_payments(customer_id="cst_5B8cwPMGnU", from_="tr_5B8cwPMGnU", limit=50, sort=mollie.Sorting.DESC, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `customer_id`                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                     | Provide the ID of the related customer.                                                                                                                                                                                                                                                                                                                                                | cst_5B8cwPMGnU                                                                                                                                                                                                                                                                                                                                                                         |
| `from_`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Provide an ID to start the result set from the item with the given ID and onwards. This allows you to paginate<br/>the result set.                                                                                                                                                                                                                                                     | tr_5B8cwPMGnU                                                                                                                                                                                                                                                                                                                                                                          |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[int]*                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The maximum number of items to return. Defaults to 50 items.                                                                                                                                                                                                                                                                                                                           | 50                                                                                                                                                                                                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.Sorting]](../../models/sorting.md)                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Used for setting the direction of the result set. Defaults to descending order, meaning the results are ordered from<br/>newest to oldest.                                                                                                                                                                                                                                             | desc                                                                                                                                                                                                                                                                                                                                                                                   |
| `profile_id`                                                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | The identifier referring to the [profile](get-profile) you wish to<br/>retrieve the resources for.<br/><br/>Most API credentials are linked to a single profile. In these cases the `profileId` can be omitted. For<br/>organization-level credentials such as OAuth access tokens however, the `profileId` parameter is required.                                                     |                                                                                                                                                                                                                                                                                                                                                                                        |
| `testmode`                                                                                                                                                                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. |                                                                                                                                                                                                                                                                                                                                                                                        |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                                                                                                                                                                                                                                                                                       | 123e4567-e89b-12d3-a456-426                                                                                                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.ListCustomerPaymentsResponse](../../models/listcustomerpaymentsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |