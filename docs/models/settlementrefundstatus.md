# SettlementRefundStatus

The refund's status. Settlement refunds always have a status of `refunded`.

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