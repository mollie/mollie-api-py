# MandateMethod

Payment method of the mandate.

SEPA Direct Debit and PayPal mandates can be created directly.

## Example Usage

```python
from mollie.models import MandateMethod

value = MandateMethod.CREDITCARD
```


## Values

| Name          | Value         |
| ------------- | ------------- |
| `CREDITCARD`  | creditcard    |
| `DIRECTDEBIT` | directdebit   |
| `PAYPAL`      | paypal        |