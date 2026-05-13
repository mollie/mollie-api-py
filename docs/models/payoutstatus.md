# PayoutStatus

The status of the payout.

## Example Usage

```python
from mollie.models import PayoutStatus

value = PayoutStatus.REQUESTED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `REQUESTED`          | requested            |
| `INITIATED`          | initiated            |
| `PROCESSING_AT_BANK` | processing-at-bank   |
| `COMPLETED`          | completed            |
| `FAILED`             | failed               |
| `CANCELED`           | canceled             |