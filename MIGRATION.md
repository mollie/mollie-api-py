# Migrating from `mollie-api-python` to `mollie-api-py`

This guide covers migrating from the legacy community Python client (`mollie-api-python`, v4.x) to the official Speakeasy-generated Python SDK (`mollie-api-py`).

## Table of contents

- [Why migrate?](#why-migrate)
- [Installation](#installation)
- [Client initialization](#client-initialization)
- [Authentication](#authentication)
- [Resources and methods](#resources-and-methods)
- [Request parameters](#request-parameters)
- [Pagination and listing resources](#pagination-and-listing-resources)
- [Error handling](#error-handling)
- [New features](#new-features)
- [Full resource mapping](#full-resource-mapping)

---

## Why migrate?

Mollie is working towards fully migrating to the new, **automatically generated SDKs**. Unlike our legacy SDKs, which are updated manually, the new SDKs are generated directly from our API specification, making new features and API updates available within 24 hours of changes being released. This ensures that your integration stays up to date with minimal effort and allows you to benefit from the latest version of our product at all times.

Beyond staying up-to-date automatically, `mollie-api-py` also provides:

- Coverage for Accounts, Delayed Routing, Sales Invoices, Sessions, Transfers, Unmatched Credit Transfers and Verify Payee, which aren't available in the legacy SDK.
- Typed, Pydantic-backed request and response models (with IDE autocomplete), while still accepting plain `dict`s for request bodies if you prefer.
- Native `async`/`await` support alongside the synchronous client, using the same method names with an `_async` suffix.
- Automatic pagination through a `next()` method on the response, instead of manually calling `has_next()` / `get_next()` yourself.
- Built-in retry logic with configurable backoff strategies.
- First-class, framework-agnostic webhook signature validation.
- `profile_id` and `testmode` available as global client options regardless of auth type.
- HTTP-status-specific error classes are replaced by a single, richer `ErrorResponse` carrying the full error payload (`status`, `title`, `detail`, `field`, `links`).

---

## Installation

Remove the old package and add the new one.

```bash
pip uninstall mollie-api-python
pip install mollie-api-py
```

Or with `uv`/`poetry`:

```bash
uv remove mollie-api-python
uv add mollie-api-py

poetry remove mollie-api-python
poetry add mollie-api-py
```

Python 3.10+ is required for the new SDK. ~~(the old SDK also required 3.10+)~~

---

## Client initialization

The old SDK instantiated a bare `Client()` and configured it afterwards via setter methods. The new SDK configures everything through constructor arguments and is used as a context manager:

**Before:**

```py
from mollie.api.client import Client

mollie_client = Client()
mollie_client.set_api_key("test_...")
```

**After:**

```py
import mollie
from mollie import ClientSDK

with ClientSDK(
    security=mollie.Security(
        api_key="test_...",
    ),
) as client_sdk:
    ...
```

---

## Authentication

### API key

```
-mollie_client = Client()
-mollie_client.set_api_key("test_...")
+client_sdk = ClientSDK(security=mollie.Security(api_key="test_..."))
```

### Advanced Access Token

The old SDK reused `set_access_token()` on the same client to switch it into organization/OAuth-token mode (it just validated the `access_...` prefix). The new SDK introduces a distinct `advanced_access_token` scheme:

```
-mollie_client = Client()
-mollie_client.set_access_token("access_...")
+client_sdk = ClientSDK(security=mollie.Security(advanced_access_token="access_..."))
```

### OAuth token

The old SDK's OAuth flow was built directly into the client (`setup_oauth(...)`, `setup_oauth_authorization_response(...)`, `revoke_oauth_token(...)`) using `requests-oauthlib`, with your own callables to persist and refresh tokens. The new SDK exposes `o_auth` as a first-class client security scheme, and token exchange is a regular resource call — you own the authorize-redirect and token storage yourself, without a dedicated OAuth session object:

```py
import mollie
from mollie import ClientSDK

client_sdk = ClientSDK(security=mollie.Security(o_auth="Bearer eyJ..."))
```

```
-mollie_client = Client()
-is_authorized, authorization_url = mollie_client.setup_oauth(
-    client_id, client_secret, redirect_uri, scope, get_token(), set_token,
-)
-mollie_client.setup_oauth_authorization_response(authorization_response)
+with ClientSDK() as client_sdk:
+    res = client_sdk.oauth.generate(
+        security=mollie.OauthGenerateTokensSecurity(
+            username=client_id,
+            password=client_secret,
+        ),
+        request_body={
+            "grant_type": mollie.OauthGrantType.AUTHORIZATION_CODE,
+            "code": "auth_...",
+            "redirect_uri": redirect_uri,
+        },
+    )
```

### Global defaults (`profile_id`, `testmode`)

The old SDK only had `set_testmode(True)` (and it raised if you weren't using an access token or OAuth); there was no built-in concept of a global `profile_id`. The new SDK configures both once on the client:

```
-mollie_client = Client()
-mollie_client.set_access_token("access_...")
-mollie_client.set_testmode(True)
+client_sdk = ClientSDK(
+    security=mollie.Security(advanced_access_token="access_..."),
+    testmode=True,
+    profile_id="pfl_...",
+)
```

---

## Resources and methods

### Typed keyword arguments replace raw dicts, and responses are returned directly

The old SDK took request bodies as a plain `dict` passed positionally (or as `data=`), and query parameters as `**kwargs`. The new SDK accepts either a typed model or a plain `dict` (so migrating the payload itself needs no changes) as a named keyword argument, and returns the resource's response model directly — no wrapper object to unwrap.

```
-payment = mollie_client.payments.create({
-    "amount": {"currency": "EUR", "value": "10.00"},
-    "description": "Order #478",
-    "redirectUrl": "https://example.com/redirect",
-})
+payment = client_sdk.payments.create(payment_request={
+    "amount": {"currency": "EUR", "value": "10.00"},
+    "description": "Order #478",
+    "redirect_url": "https://example.com/redirect",
+})
```

Note that request body keys switch from `camelCase` to `snake_case` (`redirectUrl` → `redirect_url`) to match Python conventions — this applies whether you pass a `dict` or a typed model.

```
-payment = mollie_client.payments.get(payment_id)
+payment = client_sdk.payments.get(payment_id=payment_id)
```

### Update

```
-payment = mollie_client.payments.update(payment_id, {"description": "New description"})
+payment = client_sdk.payments.update(
+    payment_id=payment_id,
+    request_body={"description": "New description"},
+)
```

### Cancel / delete

```
-mollie_client.payments.delete(payment_id)
+client_sdk.payments.cancel(payment_id=payment_id)
```

### Nested resources are no longer accessed through the parent object

The old SDK exposed nested resources as *properties on the response object itself* — you had to fetch (or already hold) the parent object, then call a resource property on it.

**Before:**

```
-payment = mollie_client.payments.get(payment_id)
-refund = payment.refunds.create({"amount": {"currency": "EUR", "value": "2.00"}})
-
-customer = mollie_client.customers.get(customer_id)
-mandate = customer.mandates.create({"method": "directdebit", "consumerAccount": "NL55INGB0000000000"})
```

The new SDK drops the object-traversal step entirely: every nested operation lives directly on the top-level resource, taking the parent ID as a keyword argument.

**After:**

```
+refund = client_sdk.refunds.create(
+    payment_id=payment_id,
+    refund_request={"amount": {"currency": "EUR", "value": "2.00"}},
+)
+
+mandate = client_sdk.mandates.create(
+    customer_id=customer_id,
+    mandate_request={"method": mollie.MandateMethod.DIRECTDEBIT, "consumer_account": "NL55INGB0000000000"},
+)
```

| Old (via parent object) | New (`client_sdk.`) |
| --- | --- |
| `customer.payments.create(body)` | `client_sdk.customers.create_payment(customer_id=customer_id, payment_request=...)` |
| `customer.payments.list()` | `client_sdk.customers.list_payments(customer_id=customer_id)` |
| `customer.mandates.create(body)` | `client_sdk.mandates.create(customer_id=customer_id, mandate_request=...)` |
| `customer.mandates.list()` | `client_sdk.mandates.list(customer_id=customer_id)` |
| `mollie_client.customers.get(cid).mandates.revoke(mandate_id)`-style call | `client_sdk.mandates.revoke(customer_id=customer_id, mandate_id=mandate_id)` |
| `customer.subscriptions.create(body)` | `client_sdk.subscriptions.create(customer_id=customer_id, subscription_request=...)` |
| `payment.refunds.create(body)` | `client_sdk.refunds.create(payment_id=payment_id, refund_request=...)` |
| `payment.chargebacks.list()` | `client_sdk.chargebacks_sdk.list(payment_id=payment_id)` |
| `payment.captures.list()` | `client_sdk.captures.list(payment_id=payment_id)` |

---

## Request parameters

### Idempotency key

The old SDK auto-generated an idempotency key (`uuid.uuid4()`) for every mutating call if you didn't supply one via the `idempotency_key=` kwarg.   
The new SDK keeps the same `idempotency_key=` kwarg, but no longer generates one for you automatically:

```py
idempotency_key = "<some-idempotency-key>"

payment1 = client_sdk.payments.create(
    payment_request=payload,
    idempotency_key=idempotency_key,
)
payment2 = client_sdk.payments.create(
    payment_request=payload,
    idempotency_key=idempotency_key,
)
```

### `testmode` and `profile_id` per request

These can be overridden per request even when defaults are set on the client:

```py
payment = client_sdk.payments.create(
    payment_request={
        "testmode": False,
        "profile_id": "pfl_other",
        "description": "My first payment",
        "redirect_url": "https://example.org/redirect",
        "amount": {"currency": "EUR", "value": "10.00"},
    },
)
```

---

## Pagination and listing resources

### Old SDK — `has_next()` / `get_next()`

The old SDK's `list()` returned a `PaginationList` that you could iterate directly for the current page's items, but fetching subsequent pages required manually checking `has_next()` and calling `get_next()`:

```py
payments = mollie_client.payments.list()

while True:
    for payment in payments:
        ...  # handle item

    if not payments.has_next():
        break
    payments = payments.get_next()
```

### New SDK — `next()` auto-paginates

The response object itself exposes a `next()` method that fetches the next page, returning `None` once there are no more results:

```py
res = client_sdk.payments.list(limit=50)

while res is not None:
    for payment in res.result:
        ...  # handle item

    res = res.next()
```

An `async` equivalent is available via `list_async(...)` and `await res.next_async()`.

---

## Error handling

### Old SDK — HTTP-status-specific `ResponseError` subclasses

```py
from mollie.api.error import ResponseError

try:
    payment = mollie_client.payments.get("invalid")
except ResponseError as ex:
    print(ex.status)          # HTTP status
    print(ex.field)           # field that caused the error, if any
    print(ex.idempotency_key) # idempotency key used for the failed request
```

### New SDK — `ClientError` / `ErrorResponse`

```py
from mollie import ClientSDK, models

with ClientSDK() as client_sdk:
    try:
        payment = client_sdk.payments.get(payment_id="invalid")
    except models.ClientError as ex:  # all SDK exceptions inherit from ClientError
        print(ex.message)
        print(ex.status_code)
        print(ex.body)
        print(ex.headers)

        if isinstance(ex, models.ErrorResponse):
            print(ex.data.status)  # int
            print(ex.data.title)   # str
            print(ex.data.detail)  # str
            print(ex.data.field)   # Optional[str]
            print(ex.data.links)   # mollie.ErrorsLinks
```

---

## New features

### Webhook signature validation

```py
import os
from mollie.utils.webhooks import InvalidSignatureException, SignatureValidator


def handle_webhook(raw_body: str, signature_header: str | None) -> None:
    validator = SignatureValidator(os.getenv("MOLLIE_WEBHOOK_SECRET", ""))

    try:
        is_verified = validator.validate_payload(raw_body, signature_header)
    except InvalidSignatureException:
        print("Webhook signature is invalid")
        return

    if not is_verified:
        print("No signature header was provided; treating it as a legacy webhook")
        return

    print("Webhook signature is valid")
```

### Async support

The old SDK was synchronous only (built on `requests`). The new SDK is built on `httpx` and offers an `async`/`await` counterpart to every method, suffixed with `_async`:

```py
import asyncio
import mollie
from mollie import ClientSDK

async def main():
    async with ClientSDK(security=mollie.Security(api_key="test_...")) as client_sdk:
        payment = await client_sdk.payments.create_async(
            payment_request={
                "amount": {"currency": "EUR", "value": "10.00"},
                "description": "Order #478",
                "redirect_url": "https://example.com/redirect",
            },
        )
        print(payment)

asyncio.run(main())
```

### Retries

The old SDK only retried connection errors a fixed number of times (`Client(retry=3)`, via `urllib3.Retry`). The new SDK supports configurable backoff, settable on the client or per call:

```py
from mollie import ClientSDK
from mollie.utils import BackoffStrategy, RetryConfig

with ClientSDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(500, 60_000, 1.5, 300_000), True),
) as client_sdk:
    ...
```

### Custom HTTP client

The new SDK is built on `httpx` instead of `requests`. You can pass your own `httpx.Client`/`httpx.AsyncClient`, or wrap one to add custom logic:

```py
from mollie import ClientSDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
client_sdk = ClientSDK(client=http_client)
```

### Resource management

`ClientSDK` implements the context manager protocol and closes its underlying `httpx` clients on exit — prefer using `with ClientSDK(...) as client_sdk:` (or `async with`) over holding a bare instance for the lifetime of a long-running application.

### Debugging

```py
from mollie import ClientSDK
import logging

logging.basicConfig(level=logging.DEBUG)
client_sdk = ClientSDK(debug_logger=logging.getLogger("mollie"))
```

Or set the `CLIENT_DEBUG` environment variable to enable a default debug logger.

---

## Full resource mapping

### Resources available in both SDKs

| Old (`mollie_client.`) | New (`client_sdk.`) |
| --- | --- |
| `payments` | `payments` |
| `payment.refunds` (via parent object) | `refunds` (pass `payment_id`) |
| `payment.chargebacks` (via parent object) | `chargebacks_sdk` (pass `payment_id`) |
| `payment.captures` (via parent object) | `captures` (pass `payment_id`) |
| `methods` | `methods` |
| `customers` | `customers` |
| `customer.mandates` (via parent object) | `mandates` (pass `customer_id`) |
| `customer.subscriptions` (via parent object) | `subscriptions` (pass `customer_id`) |
| `customer.payments` (via parent object) | `customers.create_payment` / `customers.list_payments` (pass `customer_id`) |
| `settlements` | `settlements` |
| `profiles` | `profiles` |
| `organizations` | `organizations` |
| `permissions` | `permissions` |
| `onboarding` | `onboarding` |
| `terminals` | `terminals` |
| `payment_links` | `payment_links` |
| `clients` | `clients` |
| `client_links` | `client_links` |
| `invoices` | `invoices` |
| OAuth methods on `Client` | `oauth` |
| `balances` | `balances` |
| `orders` (deprecated) | not available — replaced by [Payment Links](https://docs.mollie.com/reference/v2/payment-links-api/create-payment-link) and standard Payments |

### Resources available only in the new SDK

| New (`client_sdk.`) | Description |
| --- | --- |
| `accounts` | Business account management |
| `balance_transfers` | Connect balance transfers |
| `capabilities` | List capabilities |
| `delayed_routing` | Delayed payment routing rules |
| `payouts` | Payout management |
| `sales_invoices` | Sales invoice management |
| `sessions` | Payment sessions |
| `transfers_sdk` | Transfer management |
| `unmatched_credit_transfers` | Unmatched credit transfer handling |
| `verify_payee` | Payee verification |
| `webhooks` | Webhook management |
| `webhook_events` | Webhook event retrieval |

For a complete list of all resources and operations with usage examples, see the [Available Resources and Operations](https://github.com/mollie/mollie-api-py#available-resources-and-operations) section in the SDK's README.
