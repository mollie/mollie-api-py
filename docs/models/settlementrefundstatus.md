# SettlementRefundStatus

The refund's status. Settlement refunds are normally `refunded`, but can be `failed` if the refund
could not be processed.

## Example Usage

```python
from mollie.models import SettlementRefundStatus

value = SettlementRefundStatus.REFUNDED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `REFUNDED` | refunded   |
| `FAILED`   | failed     |