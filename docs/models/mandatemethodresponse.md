# MandateMethodResponse

Payment method of the mandate.

SEPA Direct Debit and PayPal mandates can be created directly.

## Example Usage

```python
from mollie.models import MandateMethodResponse

value = MandateMethodResponse.CREDITCARD

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `CREDITCARD`  | creditcard    |
| `DIRECTDEBIT` | directdebit   |
| `PAYPAL`      | paypal        |