# SubscriptionMethod

The payment method used for this subscription. If omitted, any of the customer's valid mandates may be used.

## Example Usage

```python
from mollie.models import SubscriptionMethod

value = SubscriptionMethod.CREDITCARD
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `CREDITCARD`  | creditcard    |
| `DIRECTDEBIT` | directdebit   |
| `PAYPAL`      | paypal        |