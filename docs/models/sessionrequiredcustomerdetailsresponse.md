# SessionRequiredCustomerDetailsResponse

Customer details that should be collected during checkout.

## Example Usage

```python
from mollie.models import SessionRequiredCustomerDetailsResponse

value = SessionRequiredCustomerDetailsResponse.EMAIL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `EMAIL`            | email              |
| `BILLING_ADDRESS`  | billing-address    |
| `SHIPPING_ADDRESS` | shipping-address   |