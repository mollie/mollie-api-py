# PaymentResponseStatus

The payment's status. Refer to the [documentation regarding statuses](https://docs.mollie.com/docs/handling-payment-status) for more info about which
statuses occur at what point.

## Example Usage

```python
from mollie.models import PaymentResponseStatus

value = PaymentResponseStatus.OPEN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `OPEN`       | open         |
| `PENDING`    | pending      |
| `AUTHORIZED` | authorized   |
| `PAID`       | paid         |
| `CANCELED`   | canceled     |
| `EXPIRED`    | expired      |
| `FAILED`     | failed       |