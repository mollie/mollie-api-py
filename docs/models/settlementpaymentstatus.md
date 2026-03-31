# SettlementPaymentStatus

The payment's status. Settlement payments always have a status of `paid`.

## Example Usage

```python
from mollie.models import SettlementPaymentStatus

value = SettlementPaymentStatus.PAID

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `PAID` | paid   |