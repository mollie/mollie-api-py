# Migration Guide for Mollie API Python
Learn how to migrate to the latest version of the Python SDK

Mollie uses API specification to autogenerate the SDK and enhance its consistency, ensure frequent updates and provide a more streamlined integration experience for developers.

The new version of Python SDK introduces a number of changes that might affect the way your integration works and require adjustments in your current setup: new ways of defining specific arguments, changes to methods and parameter names etc. 

This guide takes you through all the changes specific to Python SDK to help you upgrade your integration.

*You can still use the legacy version of this SDK along with the new version but we advise to upgrade as soon as possible to ensure continuous compatibility.*

## Major Changes
Here are some things you need to know about the new Python SDK to ensure a consistent integration:
1. **Client Creation and Asynchronous Support**
    - The method to create the client changed, consolidating the `Api Key` and the `oAuth` methods.
    - We added support for asynchronous calls, improving performance and responsiveness.
2. **Explicit Arguments**
    - The request body must now be preceded by the `request_body=` argument.
3. **Method Names**
    - The method names have been updated for better clarity and consistency across all the SDKs.

## Client Creation
### Example - Api Key Client
**Old**
```py
from mollie.api.client import Mollie

client = Client()
client.set_api_key('API_KEY')
```

**New**
```py
from mollie import Mollie, Security

client = Mollie(
    security = Security(
        api_key = 'API_KEY,
    ),
)
```

### Example - oAuth Client
**Old**
```py
from mollie.api.client import Mollie

client = Client()
client.setup_oauth_authorization_response(authorization_response)
```

**New**
```py
from mollie import Mollie, Security

client = Mollie(
    security = Security(
        o_auth = 'OAUTH_KEY,
    ),
)
```

### Example - Async Client
```py
import asyncio
from mollie import Mollie, Security

async def main():
    async with Mollie(
        security=Security(
            api_key='API_KEY'
        ),
    ) as mollie:
        ...

asyncio.run(main())
```

### Explicit Arguments
**Old**
```py
payment = client.payments.create({
    'amount': {
        'currency': 'EUR',
        'value': '10.00' 
    },
    'description': 'My first API payment',
    'redirectUrl': 'https://webshop.example.org/order/12345/',
    'webhookUrl': 'https://webshop.example.org/mollie-webhook/',
})
```

**New**
```py
payment = client.payments.create(request_body={
	"amount": {
        "currency": "EUR",
        "value": "10.00",
    },
    "description": "My first API payment",
    "redirect_url": "https://webshop.example.org/order/12345/",
    "webhook_url": "https://webshop.example.org/mollie-webhook/",
})
```

## Method Names
To see code examples for each method refer to the [README](./README.md).

<table>
  <tr>
    <td>
      API
    </td>
    <td>
      Endpoint
    </td>
    <td>
      Old Method
    </td>
    <td>
      New Method
    </td>
  </tr>
  <tr>
    <td rowspan="6">
      Payments API
    </td>
    <td>
      Create payment
    </td>
    <td>
      client.payments.create
    </td>
    <td>
      client.payments.create
    </td>
  </tr>
  <tr>
    <td>
      List payments
    </td>
    <td>
      client.payments.list
    </td>
    <td>
      client.payments.list
    </td>
  </tr>
  <tr>
    <td>
      Get payment
    </td>
    <td>
      client.payments.get
    </td>
    <td>
      client.payments.get
    </td>
  </tr>
  <tr>
    <td>
      Update payment
    </td>
    <td>
      client.payments.update
    </td>
    <td>
      client.payments.update
    </td>
  </tr>
  <tr>
    <td>
      Cancel payment
    </td>
    <td>
      client.payments.delete
    </td>
    <td>
      client.payments.cancel
    </td>
  </tr>
  <tr>
    <td>
      Release payment authorization
    </td>
    <td>
      -
    </td>
    <td>
      client.payments.release_authorization
    </td>
  </tr>
  <tr>
    <td rowspan="7">
      Methods API
    </td>
    <td>
      List payment methods
    </td>
    <td>
      client.methods.list
    </td>
    <td>
      client.methods.list
    </td>
  </tr>
  <tr>
    <td>
      List all payment methods
    </td>
    <td>
      client.methods.all
    </td>
    <td>
      client.methods.all
    </td>
  </tr>
  <tr>
    <td>
      Get payment method
    </td>
    <td>
      client.methods.get
    </td>
    <td>
      client.methods.get
    </td>
  </tr>
  <tr>
    <td>
      Enable payment method
    </td>
    <td>
      profiles.methods.enable
    </td>
    <td>
      client.methods.enable
    </td>
  </tr>
  <tr>
    <td>
      Disable payment method
    </td>
    <td>
      profiles.methods.disable
    </td>
    <td>
      client.methods.disable
    </td>
  </tr>
  <tr>
    <td>
      Enable payment method issuer
    </td>
    <td>
      profiles.methods.enable_issuer
    </td>
    <td>
      client.methods.enable_issuer
    </td>
  </tr>
  <tr>
    <td>
      Disable payment method issuer
    </td>
    <td>
      profiles.methods.disable_issuer
    </td>
    <td>
      client.methods.disable_issuer
    </td>
  </tr>
  <tr>
    <td rowspan="7">
      Refunds API
    </td>
    <td>
      Create payment refund
    </td>
    <td>
      payment.refunds.create
    </td>
    <td>
      client.refunds.create
    </td>
  </tr>
  <tr>
    <td>
      List payment refunds
    </td>
    <td>
      payment.refunds.list
    </td>
    <td>
      client.refunds.list
    </td>
  </tr>
  <tr>
    <td>
      Get payment refund
    </td>
    <td>
      payment.refunds.get
    </td>
    <td>
      client.refunds.get
    </td>
  </tr>
  <tr>
    <td>
      Cancel payment refund
    </td>
    <td>
      payment.refunds.delete
    </td>
    <td>
      client.refunds.cancel
    </td>
  </tr>
  <tr>
    <td>
      Create order refund
    </td>
    <td>
      order.refunds.create
    </td>
    <td>
      client.refunds.create_order
    </td>
  </tr>
  <tr>
    <td>
      List order refunds
    </td>
    <td>
      -
    </td>
    <td>
      client.refunds.get_order
    </td>
  </tr>
  <tr>
    <td>
      List all refunds
    </td>
    <td>
      profile.refunds.list
    </td>
    <td>
      client.refunds.all
    </td>
  </tr>
  <tr>
    <td rowspan="3">
      Chargebacks API
    </td>
    <td>
      List payment chargebacks
    </td>
    <td>
      payment.chargebacks.list
    </td>
    <td>
      client.chargebacks.list
    </td>
  </tr>
  <tr>
    <td>
      Get payment chargeback
    </td>
    <td>
      payment.chargebacks.get
    </td>
    <td>
      client.chargebacks.get
    </td>
  </tr>
  <tr>
    <td>
      List all chargebacks
    </td>
    <td>
      client.chargebacks.list
    </td>
    <td>
      client.chargebacks.all
    </td>
  </tr>
  <tr>
    <td rowspan="3">
      Captures API
    </td>
    <td>
      Create capture
    </td>
    <td>
      payment.captures.create
    </td>
    <td>
      client.captures.create
    </td>
  </tr>
  <tr>
    <td>
      List captures
    </td>
    <td>
      payment.captures.list
    </td>
    <td>
      client.captures.list
    </td>
  </tr>
  <tr>
    <td>
      Get capture
    </td>
    <td>
      payment.captures.get
    </td>
    <td>
      client.captures.get
    </td>
  </tr>
  <tr>
    <td>
      Wallets API
    </td>
    <td>
      Request Apple Pay payment session
    </td>
    <td>
      -
    </td>
    <td>
      client.wallets.request_apple_pay_session
    </td>
  </tr>
  <tr>
    <td rowspan="6">
      Payment Links API
    </td>
    <td>
      Create payment link
    </td>
    <td>
      client.payment_links.create
    </td>
    <td>
      client.payment_links.create
    </td>
  </tr>
  <tr>
    <td>
      List payment links
    </td>
    <td>
      client.payment-links.list
    </td>
    <td>
      client.payment_links.list
    </td>
  </tr>
  <tr>
    <td>
      Get payment link
    </td>
    <td>
      client.payment-links.get
    </td>
    <td>
      client.payment_links.get
    </td>
  </tr>
  <tr>
    <td>
      Update payment link
    </td>
    <td>
      -
    </td>
    <td>
      client.payment_links.update
    </td>
  </tr>
  <tr>
    <td>
      Delete payment link
    </td>
    <td>
      -
    </td>
    <td>
      client.payment_links.delete
    </td>
  </tr>
  <tr>
    <td>
      Get payment link payments
    </td>
    <td>
      -
    </td>
    <td>
      client.payment_links.list_payments
    </td>
  </tr>
  <tr>
    <td rowspan="2">
      Terminals API
    </td>
    <td>
      List terminals
    </td>
    <td>
      client.terminals.list
    </td>
    <td>
      client.terminals.list
    </td>
  </tr>
  <tr>
    <td>
      Get terminal
    </td>
    <td>
      client.terminals.get
    </td>
    <td>
      client.terminals.get
    </td>
  </tr>
  <tr>
    <td rowspan="2">
      Delayed Routing API
    </td>
    <td>
      Create a delayed route
    </td>
    <td>
      -
    </td>
    <td>
      client.delayed_routing.create
    </td>
  </tr>
  <tr>
    <td>
      List payment routes
    </td>
    <td>
      -
    </td>
    <td>
      client.delayed_routing.list
    </td>
  </tr>
  <tr>
    <td rowspan="9">
      Orders API
    </td>
    <td>
      Create order
    </td>
    <td>
      client.orders.create
    </td>
    <td>
      client.orders.create
    </td>
  </tr>
  <tr>
    <td>
      List orders
    </td>
    <td>
      client.orders.list
    </td>
    <td>
      client.orders.list
    </td>
  </tr>
  <tr>
    <td>
      Get order
    </td>
    <td>
      client.orders.get
    </td>
    <td>
      client.orders.get
    </td>
  </tr>
  <tr>
    <td>
      Update order
    </td>
    <td>
      client.orders.update
    </td>
    <td>
      client.orders.update
    </td>
  </tr>
  <tr>
    <td>
      Cancel order
    </td>
    <td>
      client.orders.delete
    </td>
    <td>
      client.orders.cancel
    </td>
  </tr>
  <tr>
    <td>
      Manage order lines
    </td>
    <td>
      -
    </td>
    <td>
      client.orders.manage_lines
    </td>
  </tr>
  <tr>
    <td>
      Cancel order lines
    </td>
    <td>
      order.lines.delete
    </td>
    <td>
      client.orders.cancel_lines
    </td>
  </tr>
  <tr>
    <td>
      Update order line
    </td>
    <td>
      order.lines.update
    </td>
    <td>
      client.orders.update_line
    </td>
  </tr>
  <tr>
    <td>
      Create order payment
    </td>
    <td>
      order.payments.create
    </td>
    <td>
      client.orders.create_payment
    </td>
  </tr>
  <tr>
    <td rowspan="4">
      Shipments API
    </td>
    <td>
      Create shipment
    </td>
    <td>
      order.shipments.create
    </td>
    <td>
      client.shipments.create
    </td>
  </tr>
  <tr>
    <td>
      List shipments
    </td>
    <td>
      order.shipments.list
    </td>
    <td>
      client.shipments.list
    </td>
  </tr>
  <tr>
    <td>
      Get shipment
    </td>
    <td>
      order.shipments.get
    </td>
    <td>
      client.shipments.get
    </td>
  </tr>
  <tr>
    <td>
      Update shipment
    </td>
    <td>
      order.shipments.update
    </td>
    <td>
      client.shipments.update
    </td>
  </tr>
  <tr>
    <td rowspan="7">
      Customers API
    </td>
    <td>
      Create customer
    </td>
    <td>
      client.customers.create
    </td>
    <td>
      client.customers.create
    </td>
  </tr>
  <tr>
    <td>
      List customers
    </td>
    <td>
      client.customers.list
    </td>
    <td>
      client.customers.list
    </td>
  </tr>
  <tr>
    <td>
      Get customer
    </td>
    <td>
      client.customers.get
    </td>
    <td>
      client.customers.get
    </td>
  </tr>
  <tr>
    <td>
      Update customer
    </td>
    <td>
      client.customers.update
    </td>
    <td>
      client.customers.update
    </td>
  </tr>
  <tr>
    <td>
      Delete customer
    </td>
    <td>
      client.customers.delete
    </td>
    <td>
      client.customers.delete
    </td>
  </tr>
  <tr>
    <td>
      Create customer payment
    </td>
    <td>
      customer.payments.create
    </td>
    <td>
      client.customers.create_payment
    </td>
  </tr>
  <tr>
    <td>
      List customer payments
    </td>
    <td>
      customer.payments.list
    </td>
    <td>
      client.customers.list_payment
    </td>
  </tr>
  <tr>
    <td rowspan="4">
      Mandates API
    </td>
    <td>
      Create mandate
    </td>
    <td>
      customer.mandates.create
    </td>
    <td>
      client.mandates.create
    </td>
  </tr>
  <tr>
    <td>
      List mandates
    </td>
    <td>
      customer.mandates.list
    </td>
    <td>
      client.mandates.list
    </td>
  </tr>
  <tr>
    <td>
      Get mandate
    </td>
    <td>
      customer.mandates.get
    </td>
    <td>
      client.mandates.get
    </td>
  </tr>
  <tr>
    <td>
      Revoke mandate
    </td>
    <td>
      customer.mandates.delete
    </td>
    <td>
      client.mandates.revoke
    </td>
  </tr>
  <tr>
    <td rowspan="7">
      Subscriptions API
    </td>
    <td>
      Create subscription
    </td>
    <td>
      customer.subscriptions.create
    </td>
    <td>
      client.subscriptions.create
    </td>
  </tr>
  <tr>
    <td>
      List customer subscriptions
    </td>
    <td>
      customer.subscriptions.list
    </td>
    <td>
      client.subscriptions.list
    </td>
  </tr>
  <tr>
    <td>
      Get subscription
    </td>
    <td>
      customer.subscriptions.get
    </td>
    <td>
      client.subscriptions.get
    </td>
  </tr>
  <tr>
    <td>
      Update subscription
    </td>
    <td>
      customer.subscriptions.update
    </td>
    <td>
      client.subscriptions.update
    </td>
  </tr>
  <tr>
    <td>
      Cancel subscription
    </td>
    <td>
      customer.subscriptions.delete
    </td>
    <td>
      client.subscriptions.cancel
    </td>
  </tr>
  <tr>
    <td>
      List all subscriptions
    </td>
    <td>
      client.subscriptions.all
    </td>
    <td>
      client.subscriptions.all
    </td>
  </tr>
  <tr>
    <td>
      List subscription payments
    </td>
    <td>
      subscription.payments.list
    </td>
    <td>
      client.subscriptions.list_payments
    </td>
  </tr>
  <tr>
    <td rowspan="3">
      OAuth API
    </td>
    <td>
      Authorize
    </td>
    <td>
      client.setup_oauth
    </td>
    <td>
      client.oauth.authorize
    </td>
  </tr>
  <tr>
    <td>
      Generate tokens
    </td>
    <td>
      client.setup_oauth_authorization_response
    </td>
    <td>
      client.oauth.generate
    </td>
  </tr>
  <tr>
    <td>
      Revoke tokens
    </td>
    <td>
      -
    </td>
    <td>
      client.oauth.revoke
    </td>
  </tr>
  <tr>
    <td rowspan="2">
      Permissions API
    </td>
    <td>
      List permissions
    </td>
    <td>
      client.permissions.list
    </td>
    <td>
      client.permissions.list
    </td>
  </tr>
  <tr>
    <td>
      Get permission
    </td>
    <td>
      client.permissions.get
    </td>
    <td>
      client.permissions.get
    </td>
  </tr>
  <tr>
    <td rowspan="3">
      Organizations API
    </td>
    <td>
      Get organization
    </td>
    <td>
      client.organizations.get
    </td>
    <td>
      client.organizations.get
    </td>
  </tr>
  <tr>
    <td>
      Get current organization
    </td>
    <td>
      client.organizations.get
    </td>
    <td>
      client.organizations.current
    </td>
  </tr>
  <tr>
    <td>
      Get partner status
    </td>
    <td>
      -
    </td>
    <td>
      client.organizations.partner
    </td>
  </tr>
  <tr>
    <td rowspan="6">
      Profiles API
    </td>
    <td>
      Create profile
    </td>
    <td>
      client.profiles.create
    </td>
    <td>
      client.profiles.create
    </td>
  </tr>
  <tr>
    <td>
      List profiles
    </td>
    <td>
      client.profiles.list
    </td>
    <td>
      client.profiles.list
    </td>
  </tr>
  <tr>
    <td>
      Get profile
    </td>
    <td>
      client.profiles.get
    </td>
    <td>
      client.profiles.get
    </td>
  </tr>
  <tr>
    <td>
      Update profile
    </td>
    <td>
      client.profiles.update
    </td>
    <td>
      client.profiles.update
    </td>
  </tr>
  <tr>
    <td>
      Delete profile
    </td>
    <td>
      client.profiles.delete
    </td>
    <td>
      client.profiles.delete
    </td>
  </tr>
  <tr>
    <td>
      Get current profile
    </td>
    <td>
      client.profiles.get
    </td>
    <td>
      client.profiles.current
    </td>
  </tr>
  <tr>
    <td rowspan="2">
      Onboarding API
    </td>
    <td>
      Get onboarding status
    </td>
    <td>
      client.onboarding.get
    </td>
    <td>
      client.onboarding.get
    </td>
  </tr>
  <tr>
    <td>
      Submit onboarding data
    </td>
    <td>
      client.onboarding.create
    </td>
    <td>
      client.onboarding.submit
    </td>
  </tr>
  <tr>
    <td>
      Capabilities API
    </td>
    <td>
      List capabilities
    </td>
    <td>
      -
    </td>
    <td>
      client.capabilities.list
    </td>
  </tr>
  <tr>
    <td rowspan="2">
      Clients API
    </td>
    <td>
      List clients
    </td>
    <td>
      client.clients.list
    </td>
    <td>
      client.clients.list
    </td>
  </tr>
  <tr>
    <td>
      Get client
    </td>
    <td>
      client.clients.get
    </td>
    <td>
      client.clients.get
    </td>
  </tr>
  <tr>
    <td>
      Client Links API
    </td>
    <td>
      Create client link
    </td>
    <td>
      -
    </td>
    <td>
      client.client_links.create
    </td>
  </tr>
  <tr>
    <td rowspan="5">
      Balances API
    </td>
    <td>
      List balances
    </td>
    <td>
      -
    </td>
    <td>
      client.balances.list
    </td>
  </tr>
  <tr>
    <td>
      Get balance
    </td>
    <td>
      -
    </td>
    <td>
      client.balances.get
    </td>
  </tr>
  <tr>
    <td>
      Get primary balance
    </td>
    <td>
      -
    </td>
    <td>
      client.balances.primary
    </td>
  </tr>
  <tr>
    <td>
      Get balance report
    </td>
    <td>
      -
    </td>
    <td>
      client.balances.report
    </td>
  </tr>
  <tr>
    <td>
      List balance transactions
    </td>
    <td>
      -
    </td>
    <td>
      client.balances.transactions
    </td>
  </tr>
  <tr>
    <td rowspan="8">
      Settlements API
    </td>
    <td>
      List settlements
    </td>
    <td>
      client.settlements.list
    </td>
    <td>
      client.settlements.list
    </td>
  </tr>
  <tr>
    <td>
      Get settlement
    </td>
    <td>
      client.settlements.get
    </td>
    <td>
      client.settlements.get
    </td>
  </tr>
  <tr>
    <td>
      Get open settlement
    </td>
    <td>
      client.settlements.get
    </td>
    <td>
      client.settlements.open
    </td>
  </tr>
  <tr>
    <td>
      Get next settlement
    </td>
    <td>
      client.settlements.get
    </td>
    <td>
      client.settlements.next
    </td>
  </tr>
  <tr>
    <td>
      Get settlement payments
    </td>
    <td>
      settlements.payments.list
    </td>
    <td>
      client.settlements.payments
    </td>
  </tr>
  <tr>
    <td>
      Get settlement captures
    </td>
    <td>
      settlements.captures.list
    </td>
    <td>
      client.settlements.captures
    </td>
  </tr>
  <tr>
    <td>
      Get settlement refunds
    </td>
    <td>
      settlements.refunds.list
    </td>
    <td>
      client.settlements.refunds
    </td>
  </tr>
  <tr>
    <td>
      Get settlement chargebacks
    </td>
    <td>
      settlements.chargebacks.list
    </td>
    <td>
      client.settlements.chargebacks
    </td>
  </tr>
  <tr>
    <td rowspan="2">
      Invoices API
    </td>
    <td>
      List invoices
    </td>
    <td>
      client.invoices.list
    </td>
    <td>
      client.invoices.list
    </td>
  </tr>
  <tr>
    <td>
      Get invoice
    </td>
    <td>
      client.invoices.get
    </td>
    <td>
      client.invoices.get
    </td>
  </tr>
</table>
