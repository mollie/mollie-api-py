# GetOpenSettlementStatus

The status of the settlement.

## Example Usage

```python
from mollie.models import GetOpenSettlementStatus

value = GetOpenSettlementStatus.OPEN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `OPEN`               | open                 |
| `PENDING`            | pending              |
| `PROCESSING_AT_BANK` | processing-at-bank   |
| `PAIDOUT`            | paidout              |
| `FAILED`             | failed               |