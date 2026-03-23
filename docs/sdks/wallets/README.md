# Wallets

## Overview

### Available Operations

* [request_apple_pay_session](#request_apple_pay_session) - Request Apple Pay payment session

## request_apple_pay_session

When integrating Apple Pay in your own checkout on the web, you need to
[provide merchant validation](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/providing_merchant_validation).
This is normally done using Apple's
[Requesting an Apple Pay Session](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/requesting_an_apple_pay_payment_session).
The merchant validation proves to Apple that a validated merchant is calling the Apple Pay Javascript APIs.

To integrate Apple Pay via Mollie, you will have to call the Mollie API instead of Apple's API. The response of this
API call can then be passed as-is to the completion method, `completeMerchantValidation`.

Before requesting an Apple Pay Payment Session, you must place the domain validation file on your server at:
`https://[domain]/.well-known/apple-developer-merchantid-domain-association`. Without this file, it will not be
possible to use Apple Pay on your domain.

Each new transaction requires a new payment session object. Merchant session objects are not reusable, and they
expire after five minutes.

Payment sessions cannot be requested directly from the browser. The request must be sent from your server. For the
full documentation, see the official
[Apple Pay JS API](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api) documentation.

### Example Usage

<!-- UsageSnippet language="python" operationID="request-apple-pay-payment-session" method="post" path="/wallets/applepay/sessions" example="request-apple-pay-payment-session-201-1" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.wallets.request_apple_pay_session(idempotency_key="123e4567-e89b-12d3-a456-426", request_body={
        "validation_url": "https://apple-pay-gateway-cert.apple.com/paymentservices/paymentSession",
        "domain": "pay.myshop.com",
        "profile_id": "pfl_5B8cwPMGnU",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           | Example                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `idempotency_key`                                                                                                     | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | A unique key to ensure idempotent requests. This key should be a UUID v4 string.                                      | 123e4567-e89b-12d3-a456-426                                                                                           |
| `request_body`                                                                                                        | [Optional[models.RequestApplePayPaymentSessionRequestBody]](../../models/requestapplepaypaymentsessionrequestbody.md) | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |                                                                                                                       |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |                                                                                                                       |

### Response

**[Dict[str, Any]](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 422                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |