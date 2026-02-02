# mollie-api-py

Developer-friendly & type-safe Python SDK specifically catered to leverage *mollie-api-py* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=mollie-api-py&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

## Migration
This documentation is for the new Mollie's SDK. You can find more details on how to migrate from the old version to the new one [here](https://github.com/mollie/mollie-api-py/blob/master//MIGRATION.md).

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [mollie-api-py](https://github.com/mollie/mollie-api-py/blob/master/#mollie-api-py)
  * [Migration](https://github.com/mollie/mollie-api-py/blob/master/#migration)
  * [SDK Installation](https://github.com/mollie/mollie-api-py/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/mollie/mollie-api-py/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/mollie/mollie-api-py/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/mollie/mollie-api-py/blob/master/#authentication)
  * [Idempotency Key](https://github.com/mollie/mollie-api-py/blob/master/#idempotency-key)
  * [Add Custom User-Agent Header](https://github.com/mollie/mollie-api-py/blob/master/#add-custom-user-agent-header)
  * [Add Profile ID and Testmode to Client](https://github.com/mollie/mollie-api-py/blob/master/#add-profile-id-and-testmode-to-client)
  * [Available Resources and Operations](https://github.com/mollie/mollie-api-py/blob/master/#available-resources-and-operations)
  * [Global Parameters](https://github.com/mollie/mollie-api-py/blob/master/#global-parameters)
  * [Retries](https://github.com/mollie/mollie-api-py/blob/master/#retries)
  * [Error Handling](https://github.com/mollie/mollie-api-py/blob/master/#error-handling)
  * [Server Selection](https://github.com/mollie/mollie-api-py/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/mollie/mollie-api-py/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/mollie/mollie-api-py/blob/master/#resource-management)
  * [Debugging](https://github.com/mollie/mollie-api-py/blob/master/#debugging)
* [Development](https://github.com/mollie/mollie-api-py/blob/master/#development)
  * [Contributions](https://github.com/mollie/mollie-api-py/blob/master/#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add mollie-api-py
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install mollie-api-py
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add mollie-api-py
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from mollie-api-py python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "mollie-api-py",
# ]
# ///

from mollie import ClientSDK

sdk = ClientSDK(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import mollie
from mollie import ClientSDK
import os

async def main():

    async with ClientSDK(
        testmode=False,
        security=mollie.Security(
            api_key=os.getenv("CLIENT_API_KEY", ""),
        ),
    ) as client_sdk:

        res = await client_sdk.balances.list_async(currency="EUR", from_="bal_gVMhHKqSSRYJyPsuoPNFH", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name      | Type   | Scheme       | Environment Variable |
| --------- | ------ | ------------ | -------------------- |
| `api_key` | http   | HTTP Bearer  | `CLIENT_API_KEY`     |
| `o_auth`  | oauth2 | OAuth2 token | `CLIENT_O_AUTH`      |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
    testmode=False,
) as client_sdk:

    res = client_sdk.balances.list(currency="EUR", from_="bal_gVMhHKqSSRYJyPsuoPNFH", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Idempotency Key -->
## Idempotency Key

This SDK supports the usage of Idempotency Keys. See our [documentation](https://docs.mollie.com/reference/api-idempotency) on how to use it.

```python
import os
from mollie import ClientSDK, Security

client = ClientSDK(
    security = Security(
        api_key = os.getenv("CLIENT_API_KEY", "test_..."),
    )
)

payload = {
    "description": "Description",
    "amount": {
        "currency": "EUR",
        "value": "5.00",
    },
    "redirect_url": "https://example.org/redirect",
}

idempotency_key = "<some-idempotency-key>"
payment1 = client.payments.create(
    payment_request=payload,
    idempotency_key=idempotency_key
)

payment2 = client.payments.create(
    payment_request=payload,
    idempotency_key=idempotency_key
)
print(f"Payment created with ID: {payment1.id}")
print(f"Payment created with ID: {payment2.id}")
print("Payments are the same" if payment1.id == payment2.id else "Payments are different")
```
<!-- End Idempotency Key -->

<!-- Start Add Custom User-Agent Header -->

## Add Custom User-Agent Header
The SDK allows you to append a custom suffix to the `User-Agent` header for all requests. This can be used to identify
your application or integration when interacting with the API, making it easier to track usage or debug requests. The suffix is automatically added to the default User-Agent string generated by the SDK. You can add it when creating the
client:

```py
client = ClientSDK(
    security = Security(
        api_key = os.getenv("CLIENT_API_KEY", "test_..."),
    ),
    custom_user_agent = "insert something here"
)
```

<!-- End Add Custom User-Agent Header -->

<!-- Start Add Profile ID and Testmode to Client -->

## Add Profile ID and Testmode to Client
The SDK allows you to define the `profileId` and `testmode` in the client. This way, you don't need to add this
information to the payload every time when using OAuth. This will not override the details provided in the individual
requests.

```py
client = ClientSDK(
    security = Security(
        o_auth = os.getenv("CLIENT_OAUTH_KEY", "test_..."),
    ),
    testmode = False,
    profileId = "pfl_..."
)
```

<!-- End Add Profile ID and Testmode to Client -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [balance_transfers](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/balancetransfers/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/balancetransfers/README.md#create) - Create a Connect balance transfer
* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/balancetransfers/README.md#list) - List all Connect balance transfers
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/balancetransfers/README.md#get) - Get a Connect balance transfer

### [balances](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/balances/README.md)

* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/balances/README.md#list) - List balances
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/balances/README.md#get) - Get balance
* [get_primary](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/balances/README.md#get_primary) - Get primary balance
* [get_report](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/balances/README.md#get_report) - Get balance report
* [list_transactions](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/balances/README.md#list_transactions) - List balance transactions

### [capabilities](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/capabilities/README.md)

* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/capabilities/README.md#list) - List capabilities

### [captures](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/captures/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/captures/README.md#create) - Create capture
* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/captures/README.md#list) - List captures
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/captures/README.md#get) - Get capture

### [chargebacks](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/chargebackssdk/README.md)

* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/chargebackssdk/README.md#list) - List payment chargebacks
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/chargebackssdk/README.md#get) - Get payment chargeback
* [all](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/chargebackssdk/README.md#all) - List all chargebacks

### [client_links](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/clientlinks/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/clientlinks/README.md#create) - Create client link

### [clients](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/clients/README.md)

* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/clients/README.md#list) - List clients
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/clients/README.md#get) - Get client

### [customers](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/customers/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/customers/README.md#create) - Create customer
* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/customers/README.md#list) - List customers
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/customers/README.md#get) - Get customer
* [update](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/customers/README.md#update) - Update customer
* [delete](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/customers/README.md#delete) - Delete customer
* [create_payment](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/customers/README.md#create_payment) - Create customer payment
* [list_payments](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/customers/README.md#list_payments) - List customer payments

### [delayed_routing](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/delayedrouting/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/delayedrouting/README.md#create) - Create a delayed route
* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/delayedrouting/README.md#list) - List payment routes

### [invoices](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/invoices/README.md)

* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/invoices/README.md#list) - List invoices
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/invoices/README.md#get) - Get invoice

### [mandates](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/mandates/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/mandates/README.md#create) - Create mandate
* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/mandates/README.md#list) - List mandates
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/mandates/README.md#get) - Get mandate
* [revoke](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/mandates/README.md#revoke) - Revoke mandate

### [methods](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/methods/README.md)

* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/methods/README.md#list) - List payment methods
* [all](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/methods/README.md#all) - List all payment methods
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/methods/README.md#get) - Get payment method

### [onboarding](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/onboarding/README.md)

* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/onboarding/README.md#get) - Get onboarding status
* [submit](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/onboarding/README.md#submit) - Submit onboarding data

### [organizations](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/organizations/README.md)

* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/organizations/README.md#get) - Get organization
* [get_current](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/organizations/README.md#get_current) - Get current organization
* [get_partner](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/organizations/README.md#get_partner) - Get partner status

### [payment_links](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentlinks/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentlinks/README.md#create) - Create payment link
* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentlinks/README.md#list) - List payment links
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentlinks/README.md#get) - Get payment link
* [update](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentlinks/README.md#update) - Update payment link
* [delete](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentlinks/README.md#delete) - Delete payment link
* [list_payments](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentlinks/README.md#list_payments) - Get payment link payments

### [payments](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentssdk/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentssdk/README.md#create) - Create payment
* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentssdk/README.md#list) - List payments
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentssdk/README.md#get) - Get payment
* [update](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentssdk/README.md#update) - Update payment
* [cancel](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentssdk/README.md#cancel) - Cancel payment
* [release_authorization](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/paymentssdk/README.md#release_authorization) - Release payment authorization

### [permissions](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/permissions/README.md)

* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/permissions/README.md#list) - List permissions
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/permissions/README.md#get) - Get permission

### [profiles](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/profiles/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/profiles/README.md#create) - Create profile
* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/profiles/README.md#list) - List profiles
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/profiles/README.md#get) - Get profile
* [update](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/profiles/README.md#update) - Update profile
* [delete](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/profiles/README.md#delete) - Delete profile
* [get_current](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/profiles/README.md#get_current) - Get current profile

### [refunds](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/refundssdk/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/refundssdk/README.md#create) - Create payment refund
* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/refundssdk/README.md#list) - List payment refunds
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/refundssdk/README.md#get) - Get payment refund
* [cancel](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/refundssdk/README.md#cancel) - Cancel payment refund
* [all](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/refundssdk/README.md#all) - List all refunds

### [sales_invoices](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/salesinvoices/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/salesinvoices/README.md#create) - Create sales invoice
* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/salesinvoices/README.md#list) - List sales invoices
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/salesinvoices/README.md#get) - Get sales invoice
* [update](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/salesinvoices/README.md#update) - Update sales invoice
* [delete](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/salesinvoices/README.md#delete) - Delete sales invoice

### [settlements](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/settlements/README.md)

* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/settlements/README.md#list) - List settlements
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/settlements/README.md#get) - Get settlement
* [get_open](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/settlements/README.md#get_open) - Get open settlement
* [get_next](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/settlements/README.md#get_next) - Get next settlement
* [list_payments](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/settlements/README.md#list_payments) - List settlement payments
* [list_captures](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/settlements/README.md#list_captures) - List settlement captures
* [list_refunds](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/settlements/README.md#list_refunds) - List settlement refunds
* [list_chargebacks](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/settlements/README.md#list_chargebacks) - List settlement chargebacks

### [subscriptions](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/subscriptions/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/subscriptions/README.md#create) - Create subscription
* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/subscriptions/README.md#list) - List customer subscriptions
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/subscriptions/README.md#get) - Get subscription
* [update](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/subscriptions/README.md#update) - Update subscription
* [cancel](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/subscriptions/README.md#cancel) - Cancel subscription
* [all](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/subscriptions/README.md#all) - List all subscriptions
* [list_payments](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/subscriptions/README.md#list_payments) - List subscription payments

### [terminals](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/terminals/README.md)

* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/terminals/README.md#list) - List terminals
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/terminals/README.md#get) - Get terminal

### [wallets](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/wallets/README.md)

* [request_apple_pay_session](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/wallets/README.md#request_apple_pay_session) - Request Apple Pay payment session

### [webhook_events](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/webhookevents/README.md)

* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/webhookevents/README.md#get) - Get a Webhook Event

### [webhooks](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/webhooks/README.md)

* [create](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/webhooks/README.md#create) - Create a webhook
* [list](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/webhooks/README.md#list) - List all webhooks
* [update](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/webhooks/README.md#update) - Update a webhook
* [get](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/webhooks/README.md#get) - Get a webhook
* [delete](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/webhooks/README.md#delete) - Delete a webhook
* [test](https://github.com/mollie/mollie-api-py/blob/master/docs/sdks/webhooks/README.md#test) - Test a webhook

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Global Parameters [global-parameters] -->
## Global Parameters

Certain parameters are configured globally. These parameters may be set on the SDK client instance itself during initialization. When configured as an option during SDK initialization, These global values will be used as defaults on the operations that use them. When such operations are called, there is a place in each to override the global value, if needed.

For example, you can set `profileId` to `` at SDK initialization and then you do not have to pass the same value on calls to operations like `list`. But if you want to do so you may, which will locally override the global setting. See the example code below for a demonstration.


### Available Globals

The following global parameters are available.
Global parameters can also be set via environment variable.

| Name              | Type | Description                                                                                                                                                                                                                                                                                                                                                                                            | Environment              |
| ----------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| profile_id        | str  | The identifier referring to the [profile](https://github.com/mollie/mollie-api-py/blob/master/get-profile) you wish to<br/>retrieve the resources for.<br/><br/>Most API credentials are linked to a single profile. In these cases the `profileId` can be omitted. For<br/>organization-level credentials such as OAuth access tokens however, the `profileId` parameter is required.                                                                     | CLIENT_PROFILE_ID        |
| testmode          | bool | Most API credentials are specifically created for either live mode or test mode. In those cases the `testmode` query<br/>parameter can be omitted. For organization-level credentials such as OAuth access tokens, you can enable test mode by<br/>setting the `testmode` query parameter to `true`.<br/><br/>Test entities cannot be retrieved when the endpoint is set to live mode, and vice versa. | CLIENT_TESTMODE          |
| custom_user_agent | str  | Custom user agent string to be appended to the default Mollie SDK user agent.                                                                                                                                                                                                                                                                                                                          | CLIENT_CUSTOM_USER_AGENT |

### Example

```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    testmode=False,
    profile_id="<id>",
    custom_user_agent="<value>",
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.balances.list(currency="EUR", from_="bal_gVMhHKqSSRYJyPsuoPNFH", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```
<!-- End Global Parameters [global-parameters] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import mollie
from mollie import ClientSDK
from mollie.utils import BackoffStrategy, RetryConfig
import os


with ClientSDK(
    testmode=False,
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.balances.list(currency="EUR", from_="bal_gVMhHKqSSRYJyPsuoPNFH", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import mollie
from mollie import ClientSDK
from mollie.utils import BackoffStrategy, RetryConfig
import os


with ClientSDK(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    testmode=False,
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.balances.list(currency="EUR", from_="bal_gVMhHKqSSRYJyPsuoPNFH", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`ClientError`](https://github.com/mollie/mollie-api-py/blob/master/./src/mollie/models/clienterror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/mollie/mollie-api-py/blob/master/#error-classes). |

### Example
```python
import mollie
from mollie import ClientSDK, models
import os


with ClientSDK(
    testmode=False,
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:
    res = None
    try:

        res = client_sdk.balances.list(currency="EUR", from_="bal_gVMhHKqSSRYJyPsuoPNFH", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

        # Handle response
        print(res)


    except models.ClientError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.ErrorResponse):
            print(e.data.status)  # int
            print(e.data.title)  # str
            print(e.data.detail)  # str
            print(e.data.field)  # Optional[str]
            print(e.data.links)  # mollie.ErrorsLinks
```

### Error Classes
**Primary errors:**
* [`ClientError`](https://github.com/mollie/mollie-api-py/blob/master/./src/mollie/models/clienterror.py): The base class for HTTP error responses.
  * [`ErrorResponse`](https://github.com/mollie/mollie-api-py/blob/master/./src/mollie/models/errorresponse.py): An error response object. *

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`ClientError`](https://github.com/mollie/mollie-api-py/blob/master/./src/mollie/models/clienterror.py)**:
* [`ResponseValidationError`](https://github.com/mollie/mollie-api-py/blob/master/./src/mollie/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](https://github.com/mollie/mollie-api-py/blob/master/#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    server_url="https://api.mollie.com/v2",
    testmode=False,
    security=mollie.Security(
        api_key=os.getenv("CLIENT_API_KEY", ""),
    ),
) as client_sdk:

    res = client_sdk.balances.list(currency="EUR", from_="bal_gVMhHKqSSRYJyPsuoPNFH", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from mollie import ClientSDK
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = ClientSDK(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from mollie import ClientSDK
from mollie.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = ClientSDK(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `ClientSDK` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
import mollie
from mollie import ClientSDK
import os
def main():

    with ClientSDK(
        testmode=False,
        security=mollie.Security(
            api_key=os.getenv("CLIENT_API_KEY", ""),
        ),
    ) as client_sdk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with ClientSDK(
        testmode=False,
        security=mollie.Security(
            api_key=os.getenv("CLIENT_API_KEY", ""),
        ),
    ) as client_sdk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from mollie import ClientSDK
import logging

logging.basicConfig(level=logging.DEBUG)
s = ClientSDK(debug_logger=logging.getLogger("mollie"))
```

You can also enable a default debug logger by setting an environment variable `CLIENT_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=mollie-api-py&utm_campaign=python)
