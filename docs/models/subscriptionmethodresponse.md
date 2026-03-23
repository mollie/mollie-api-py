# SubscriptionMethodResponse

The payment method used for this subscription. If omitted, any of the customer's valid mandates may be used.

## Example Usage

```python
from mollie.models import SubscriptionMethodResponse

value = SubscriptionMethodResponse.CREDITCARD

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `CREDITCARD`  | creditcard    |
| `DIRECTDEBIT` | directdebit   |
| `PAYPAL`      | paypal        |